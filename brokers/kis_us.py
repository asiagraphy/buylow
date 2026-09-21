"""KIS 미국주식 REST 연동. 모의·실전 키/서버를 분리하고 모든 HTTP 호출을 함께 제한한다."""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import threading
import time
from datetime import date, datetime, timedelta
from dataclasses import dataclass
from decimal import Decimal, ROUND_DOWN, ROUND_UP
from pathlib import Path

import requests

from orchestrator.us_strategy import Bar, NEW_YORK, Stock

HOSTS = {"demo": "https://openapivts.koreainvestment.com:29443",
         "real": "https://openapi.koreainvestment.com:9443"}
ORDER_IDS = {"demo": {"BUY": "VTTT1002U", "SELL": "VTTT1001U"},
             "real": {"BUY": "TTTT1002U", "SELL": "TTTT1006U"}}


@dataclass(frozen=True)
class Quote:
    time: datetime
    last: float
    bid: float
    ask: float

    def fresh(self, now: datetime, maximum_age: float = 120) -> bool:
        return 0 <= (now - self.time).total_seconds() <= maximum_age

    @property
    def spread(self) -> float:
        return (self.ask - self.bid) / ((self.ask + self.bid) / 2)


class BrokerError(RuntimeError):
    pass


class OrderUncertain(BrokerError):
    """증권사 접수 여부를 확인할 수 없어 재전송하면 안 되는 주문."""


class RequestPacer:
    def __init__(self, interval: float = 1.0, clock=time.monotonic, sleep=time.sleep):
        if interval < 1.0 or not math.isfinite(interval):
            raise ValueError("요청 간격은 최소 1초입니다")
        self.interval, self.clock, self.sleep = interval, clock, sleep
        self.next_at = 0.0
        self.lock = threading.Lock()

    def wait(self):
        with self.lock:
            remaining = self.next_at - self.clock()
            if remaining > 0:
                self.sleep(remaining)
            self.next_at = self.clock() + self.interval


def limit_price(price: float, side: str) -> str:
    if side not in ("BUY", "SELL") or not math.isfinite(price) or price <= 0:
        raise ValueError("유효한 지정가와 매매 방향이 필요합니다")
    rounding = ROUND_UP if side == "BUY" else ROUND_DOWN
    tick = Decimal("0.01") if price >= 1 else Decimal("0.0001")
    return str(Decimal(str(price)).quantize(tick, rounding=rounding))


def private_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    os.fchmod(descriptor, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


class KisUsClient:
    def __init__(self, app_key: str, app_secret: str, account: str, mode: str = "demo",
                 *, session=None, pacer=None, token_path: Path | None = None):
        if mode not in HOSTS:
            raise ValueError("투자 환경은 demo 또는 real이어야 합니다")
        if not app_key or not app_secret:
            raise BrokerError("선택한 투자 환경의 App Key와 App Secret을 설정하세요")
        match = re.fullmatch(r"(\d{8})-?(\d{2})", account or "")
        if not match:
            raise BrokerError("계좌번호를 8자리-2자리 형식으로 설정하세요")
        self.mode, self.host = mode, HOSTS[mode]
        self.app_key, self.app_secret = app_key, app_secret
        self.cano, self.product = match.groups()
        self.profile = hashlib.sha256(f"{mode}:{app_key}:{account}".encode()).hexdigest()
        self.session = session or requests.Session()
        self.pacer = pacer or RequestPacer()
        self.token_path = token_path
        self.token, self.expires = "", 0.0

    def _send(self, method: str, path: str, **kwargs):
        self.pacer.wait()
        return self.session.request(method, self.host + path, timeout=10, **kwargs)

    def _access_token(self) -> str:
        if self.token and self.expires > time.time() + 60:
            return self.token
        if self.token_path and self.token_path.exists():
            try:
                cached = json.loads(self.token_path.read_text())
                if cached.get("profile") == self.profile and cached.get("expires", 0) > time.time() + 60:
                    self.token, self.expires = cached["token"], cached["expires"]
                    return self.token
            except (ValueError, KeyError, OSError):
                pass
        try:
            response = self._send("POST", "/oauth2/tokenP", json={
                "grant_type": "client_credentials", "appkey": self.app_key, "appsecret": self.app_secret,
            })
            payload = response.json()
        except (requests.RequestException, ValueError) as error:
            raise BrokerError("KIS 토큰 발급 응답을 확인할 수 없습니다") from error
        if response.status_code != 200 or not payload.get("access_token"):
            raise BrokerError(f"KIS 인증 실패 (HTTP {response.status_code}). 투자 환경과 키를 확인하세요")
        self.token = payload["access_token"]
        self.expires = time.time() + float(payload.get("expires_in", 86400)) - 600
        if self.token_path:
            private_json(self.token_path, {"profile": self.profile, "token": self.token, "expires": self.expires})
        return self.token

    def request(self, method: str, path: str, transaction: str, parameters: dict,
                continuation: str = "") -> tuple[dict, str]:
        for attempt in range(3):
            # 인증 요청 이후에도 실제 API 전송 직전에 같은 제한기를 통과한다.
            headers = {"authorization": "Bearer " + self._access_token(), "appkey": self.app_key,
                       "appsecret": self.app_secret, "tr_id": transaction, "custtype": "P",
                       "tr_cont": continuation, "content-type": "application/json"}
            try:
                response = self._send(method, path, headers=headers,
                                      **({"params": parameters} if method == "GET" else {"json": parameters}))
                payload = response.json()
            except (requests.RequestException, ValueError) as error:
                if method == "POST":
                    raise OrderUncertain("주문 응답이 불명확합니다. 주문내역 확인 전 재전송하지 마세요") from error
                raise BrokerError("KIS 조회 응답을 확인할 수 없습니다") from error
            if response.status_code == 200 and str(payload.get("rt_cd")) == "0":
                return payload, response.headers.get("tr_cont", "")
            code = str(payload.get("msg_cd", "UNKNOWN"))
            if code == "EGW00201" and attempt < 2:
                self.pacer.sleep(2 ** attempt)
                continue
            if method == "POST" and (response.status_code >= 500 or "rt_cd" not in payload):
                raise OrderUncertain("주문 처리 결과가 불명확합니다. 증권사 주문내역을 확인하세요")
            raise BrokerError(f"KIS 요청 거부: {code} (HTTP {response.status_code})")
        raise BrokerError("KIS 호출 한도를 초과했습니다")

    def _account_parameters(self) -> dict:
        return {"CANO": self.cano, "ACNT_PRDT_CD": self.product}

    def _pages(self, path: str, transaction: str, parameters: dict, output: str) -> list[dict]:
        parameters = {**parameters, "CTX_AREA_FK200": "", "CTX_AREA_NK200": ""}
        rows, cursors, continuation = [], set(), ""
        while True:
            payload, more = self.request("GET", path, transaction, parameters, continuation)
            if output not in payload or not isinstance(payload[output], list):
                raise BrokerError("KIS 목록 응답 형식이 올바르지 않습니다")
            rows.extend(payload[output])
            if more not in ("F", "M"):
                return rows
            cursor = (str(payload.get("ctx_area_fk200", "")).strip(),
                      str(payload.get("ctx_area_nk200", "")).strip())
            if not any(cursor) or cursor in cursors:
                raise BrokerError("KIS 연속조회가 완료되지 않았습니다")
            cursors.add(cursor)
            parameters.update(CTX_AREA_FK200=cursor[0], CTX_AREA_NK200=cursor[1])
            continuation = "N"

    def bars(self, stock: Stock, since: datetime, now: datetime) -> list[Bar]:
        parameters = {"AUTH": "", "EXCD": stock.quote_exchange, "SYMB": stock.symbol,
                      "NMIN": "1", "PINC": "1", "NEXT": "", "NREC": "120", "FILL": "", "KEYB": ""}
        found, previous_cursor = {}, None
        while True:
            payload, _ = self.request("GET", "/uapi/overseas-price/v1/quotations/inquire-time-itemchartprice",
                                      "HHDFS76950200", parameters)
            rows = payload.get("output2")
            if not isinstance(rows, list):
                raise BrokerError("해외 분봉 응답을 확인할 수 없습니다")
            if not rows:
                break
            starts = []
            for row in rows:
                start = datetime.strptime(row["xymd"] + row["xhms"].zfill(6), "%Y%m%d%H%M%S").replace(tzinfo=NEW_YORK)
                starts.append(start)
                # 현재 진행 중인 봉을 신호에 사용하지 않도록 한 분이 지난 데이터만 넘긴다.
                end = start + timedelta(minutes=1)
                if since < end <= now:
                    found[end] = Bar(end, float(row["open"]), float(row["high"]), float(row["low"]),
                                     float(row["last"]), float(row["evol"]))
            earliest = min(starts)
            if earliest <= since or len(rows) < 120:
                break
            cursor = (earliest - timedelta(minutes=1)).strftime("%Y%m%d%H%M%S")
            if cursor == previous_cursor:
                raise BrokerError("분봉 조회 커서가 진행되지 않습니다")
            previous_cursor = cursor
            parameters.update(NEXT="1", KEYB=cursor)
        return [found[key] for key in sorted(found)]

    def quote(self, stock: Stock) -> float:
        payload, _ = self.request("GET", "/uapi/overseas-price/v1/quotations/price", "HHDFS00000300",
                                  {"AUTH": "", "EXCD": stock.quote_exchange, "SYMB": stock.symbol})
        price = float(payload["output"]["last"])
        if not math.isfinite(price) or price <= 0:
            raise BrokerError("유효한 미국 주식 현재가가 없습니다")
        return price

    def book(self, stock: Stock) -> Quote:
        payload, _ = self.request("GET", "/uapi/overseas-price/v1/quotations/inquire-asking-price", "HHDFS76200100",
                                  {"AUTH": "", "EXCD": stock.quote_exchange, "SYMB": stock.symbol})
        fields = {}
        for key in ("output1", "output2", "output3"):
            block = payload.get(key) or {}
            if isinstance(block, list):
                block = block[0] if block else {}
            fields.update(block)
        timestamp = datetime.strptime(fields["dymd"] + fields["dhms"].zfill(6), "%Y%m%d%H%M%S").replace(tzinfo=NEW_YORK)
        quote = Quote(timestamp, float(fields["last"]), float(fields["pbid1"]), float(fields["pask1"]))
        if not all(math.isfinite(value) and value > 0 for value in (quote.last, quote.bid, quote.ask)) or quote.ask < quote.bid:
            raise BrokerError("미국 주식 호가를 확인할 수 없습니다")
        return quote

    def buying_power(self, stock: Stock, price: float) -> float:
        transaction = "VTTS3007R" if self.mode == "demo" else "TTTS3007R"
        payload, _ = self.request("GET", "/uapi/overseas-stock/v1/trading/inquire-psamount", transaction,
            {**self._account_parameters(), "OVRS_EXCG_CD": stock.exchange,
             "OVRS_ORD_UNPR": limit_price(price, "BUY"), "ITEM_CD": stock.symbol})
        # 자동환전 가능액을 투자 현금으로 취급하지 않는다.
        return max(0.0, float(payload["output"]["ord_psbl_frcr_amt"]))

    def holdings(self, exchanges: set[str]) -> list[dict]:
        transaction = "VTTS3012R" if self.mode == "demo" else "TTTS3012R"
        rows = []
        for exchange in sorted(exchanges if self.mode == "demo" else {"NASD"}):
            rows.extend(self._pages("/uapi/overseas-stock/v1/trading/inquire-balance", transaction,
                {**self._account_parameters(), "OVRS_EXCG_CD": exchange, "TR_CRCY_CD": "USD"}, "output1"))
        return rows

    def orders(self, day: date) -> list[dict]:
        transaction = "VTTS3035R" if self.mode == "demo" else "TTTS3035R"
        return self._pages("/uapi/overseas-stock/v1/trading/inquire-ccnl", transaction,
            {**self._account_parameters(), "PDNO": "" if self.mode == "demo" else "%",
             "ORD_STRT_DT": day.strftime("%Y%m%d"), "ORD_END_DT": day.strftime("%Y%m%d"),
             "SLL_BUY_DVSN": "00", "CCLD_NCCS_DVSN": "00", "SORT_SQN": "DS",
             "OVRS_EXCG_CD": "" if self.mode == "demo" else "NASD",
             "ORD_DT": "", "ORD_GNO_BRNO": "", "ODNO": ""}, "output")

    def place(self, stock: Stock, side: str, quantity: int, price: float) -> str:
        if side not in ("BUY", "SELL") or quantity <= 0 or type(quantity) is not int:
            raise ValueError("양의 정수 수량과 매매 방향이 필요합니다")
        payload, _ = self.request("POST", "/uapi/overseas-stock/v1/trading/order", ORDER_IDS[self.mode][side],
            {**self._account_parameters(), "OVRS_EXCG_CD": stock.exchange, "PDNO": stock.symbol,
             "ORD_QTY": str(quantity), "OVRS_ORD_UNPR": limit_price(price, side), "ORD_DVSN": "00",
             "CTAC_TLNO": "", "MGCO_APTM_ODNO": "", "SLL_TYPE": "00" if side == "SELL" else "",
             "ORD_SVR_DVSN_CD": "0"})
        number = payload.get("output", {}).get("ODNO")
        if not number:
            raise OrderUncertain("주문 접수 응답에 주문번호가 없습니다")
        return str(number)

    def cancel(self, stock: Stock, number: str, remaining: int) -> None:
        if not number or type(remaining) is not int or remaining <= 0:
            raise ValueError("취소할 주문번호와 양의 정수 잔량이 필요합니다")
        transaction = "VTTT1004U" if self.mode == "demo" else "TTTT1004U"
        self.request("POST", "/uapi/overseas-stock/v1/trading/order-rvsecncl", transaction,
            {**self._account_parameters(), "OVRS_EXCG_CD": stock.exchange, "PDNO": stock.symbol,
             "ORGN_ODNO": number, "RVSE_CNCL_DVSN_CD": "02", "ORD_QTY": str(remaining),
             "OVRS_ORD_UNPR": "0", "MGCO_APTM_ODNO": "", "ORD_SVR_DVSN_CD": "0"})
