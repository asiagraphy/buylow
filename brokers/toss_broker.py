"""토스증권(Toss) 매매 조회 어댑터 — 매매 탭 읽기 계층.

TossClient(REST)를 감싸 계좌/잔고/장상태를 대시보드용 dict로 돌려준다. 실주문은 LEAN 라이브 +
C# 어댑터(adapter/MyTrading.Toss)가 집행하고, 이 클래스는 '조회'만 한다(읽기/쓰기 분리 — KisBroker와 동일).

KisBroker와의 차이:
- 모의투자 env가 없다(실전 단일).
- 체결은 OPEN·CLOSED 주문의 누적 체결량을 사용한다. REST 조회는 개별 체결 이벤트가 아니라
  주문별 합계이며, 날짜 필터는 주문 생성일 기준이다.
"""

from __future__ import annotations

from datetime import date, datetime, time
from zoneinfo import ZoneInfo

from .base import mask_account
from .toss import TossClient

_SEOUL = ZoneInfo("Asia/Seoul")
# KRX 정규장 09:00~15:30 (market/krx.py와 동일).
_OPEN = time(9, 0)
_CLOSE = time(15, 30)


class TossBroker:
    def __init__(self, client_id: str, client_secret: str,
                 client: TossClient | None = None, now_fn=None,
                 name: str = "toss", label: str = "토스증권"):
        self.name = name
        self.label = label
        # 주입형 client(테스트) 우선, 없으면 자격증명으로 생성.
        self._client = client or TossClient(client_id, client_secret)
        self._now = now_fn or (lambda: datetime.now(_SEOUL))

    def account_info(self) -> dict:
        # 계좌번호는 getAccounts로 해석(없으면 빈 문자열 → 마스킹이 '(미설정)').
        try:
            acct = self._client.account_no()
        except Exception:
            acct = ""
        return {
            "broker": self.name,
            "broker_label": self.label,
            "account_no": mask_account(acct),
            "account_type": "종합매매",
            "env": "real",  # Toss는 실전 단일
        }

    def balance(self) -> dict:
        b = self._client.fetch_balance()
        total_purchase = sum(h["avg_price"] * h["qty"] for h in b["holdings"])
        total_pnl = sum(h["pnl"] for h in b["holdings"])
        total_pnl_pct = (total_pnl / total_purchase * 100) if total_purchase else 0.0
        return {
            "deposit": b["deposit"],
            "buying_power": b["buying_power"],
            "total_eval": b["total_eval"],
            "total_purchase": total_purchase,
            "total_pnl": total_pnl,
            "total_pnl_pct": total_pnl_pct,
            "net_asset": b["net_asset"],
            "items": b["holdings"],
        }

    def market_status(self) -> dict:
        now = self._now()
        today = now.date()
        try:
            open_day = self._client.check_market_open(today)
        except Exception:
            # 휴장일 조회 실패 시 주말만이라도 판정(보수적; KisBroker와 동일 폴백).
            open_day = today.weekday() < 5
        if not open_day:
            session = "closed"
        elif now.time() < _OPEN:
            session = "pre"      # 장 시작 전
        elif now.time() <= _CLOSE:
            session = "regular"  # 장중
        else:
            session = "closed"   # 장 마감
        return {
            "open": session == "regular",
            "session": session,
            "is_holiday": not open_day,
            "env": "real",
            "as_of": now.strftime("%Y-%m-%d %H:%M"),
        }

    def trades(self, date_iso: str) -> list[dict]:
        day = date.fromisoformat(date_iso)
        orders = {}
        for status in ("OPEN", "CLOSED"):
            for order in self._client.orders(status, day):
                orders[order["orderId"]] = order
        rows = []
        for order in orders.values():
            if order.get("currency") != "KRW":
                continue
            execution = order.get("execution") or {}
            quantity = int(float(execution.get("filledQuantity") or 0))
            if quantity <= 0:
                continue
            price = float(execution.get("averageFilledPrice") or 0)
            rows.append({
                "ts": execution.get("filledAt") or order["orderedAt"],
                "ticker": order["symbol"], "name": "", "side": order["side"],
                "qty": quantity, "price": price,
                "amount": float(execution.get("filledAmount") or quantity * price),
                "realized_pnl": None, "reason": "주문별 누적체결 (주문일 기준)",
            })
        return sorted(rows, key=lambda row: row["ts"])
