"""유동성 필터와 단면 순위로 미국주식 매수 후보를 주기적으로 갱신한다."""

from __future__ import annotations

import json
import math
import os
import re
from datetime import datetime, timedelta

from brokers.kis_us import BrokerError
from .us_strategy import Stock, US_EXCHANGES

REFRESH_SECONDS = 300
MAX_AGE_SECONDS = 600
MAX_CANDIDATES = 12


def rank_candidates(prices, volumes, strategy, incumbents=(), excluded=()):
    volume_by_symbol = {(row.get("excd"), row.get("symb")): row for row in volumes}
    candidates = {}
    exchanges = {value: key for key, value in US_EXCHANGES.items()}
    for row in prices:
        try:
            stock = Stock(row["symb"], exchanges[row["excd"]])
            volume = volume_by_symbol[(row["excd"], stock.symbol)]
            # 순위 API의 이름 기준 제외이며, 종목 마스터 분류를 대체하지 않는다.
            name = row["enam"].upper()
            if not name or re.search(r"\b(ETF|ETN|WARRANTS?|RIGHTS?|[23]X)\b", name):
                continue
            if row.get("e_ordyn") != "○" or stock.symbol in excluded:
                continue
            price, change, momentum, total_volume, bid, ask = (
                float(row[key]) for key in ("last", "rate", "n_rate", "tvol", "pbid", "pask"))
            recent_volume = float(volume["n_diff"])
            if not all(math.isfinite(value) for value in
                       (price, change, momentum, total_volume, bid, ask, recent_volume)):
                continue
            if price < strategy.min_price or change < 3 or momentum <= 0 or bid <= 0 or ask < bid:
                continue
            spread = (ask - bid) / ((ask + bid) / 2)
            turnover = price * recent_volume / 15
            if (total_volume < 100_000 or price * total_volume < 5_000_000
                    or turnover < strategy.min_minute_turnover or spread > strategy.max_spread_fraction):
                continue
            candidates[stock.symbol] = dict(symbol=stock.symbol, exchange=stock.exchange,
                day_change=change, momentum=momentum, minute_turnover=turnover,
                spread_pct=spread * 100)
        except (KeyError, ValueError, TypeError):
            continue
    rows = list(candidates.values())

    def percentile(key, value):
        if len(rows) == 1:
            return 0.5
        below = sum(other[key] < value for other in rows)
        tied = sum(other[key] == value for other in rows)
        return (below + (tied - 1) / 2) / (len(rows) - 1)

    for row in rows:
        # 백분위 점수로 단일 극단값의 지배를 막고, 호가 비용을 별도로 차감한다.
        row["score"] = round(100 * sum(weight * percentile(key, row[key]) for key, weight in
            (("day_change", 0.4), ("momentum", 0.35), ("minute_turnover", 0.25)))
            - 10 * row["spread_pct"] / (strategy.max_spread_fraction * 100), 3)
        row["retention_bonus"] = 3 if row["symbol"] in incumbents else 0
    rows.sort(key=lambda row: (-(row["score"] + row["retention_bonus"]), row["symbol"]))
    return rows[:MAX_CANDIDATES], len(rows)


class UniverseScanner:
    def __init__(self, broker, strategy, state, history_path=None):
        self.broker, self.strategy, self.state = broker, strategy, state
        self.history_path = history_path
        self.pending = []
        self.collected = {}
        self.attempted = False
        self.verified = False

    def ready(self, now, session_open):
        updated = self.state.get("updated_at")
        return bool(self.verified and updated and not self.state.get("error")
                    and session_open <= datetime.fromisoformat(updated) <= now
                    and (now - datetime.fromisoformat(updated)).total_seconds() <= MAX_AGE_SECONDS)

    def step(self, now, session_open, excluded=()):
        if now < session_open + timedelta(minutes=22):
            return
        if not self.pending:
            next_refresh = self.state.get("next_refresh")
            if self.attempted and next_refresh and now < datetime.fromisoformat(next_refresh):
                return
            self.attempted = True
            self.pending = [(kind, exchange) for exchange in US_EXCHANGES
                            for kind in ("price", "volume")]
            self.collected = {"price": [], "volume": []}
            self.state.update(last_attempt=now.isoformat(), progress=0,
                              next_refresh=(now + timedelta(seconds=REFRESH_SECONDS)).isoformat())
        try:
            if (now - datetime.fromisoformat(self.state["last_attempt"])).total_seconds() > 120:
                raise BrokerError("순위 수집이 2분을 넘어 신규 매수를 중단합니다")
            kind, exchange = self.pending.pop(0)
            # 매 사이클 청산·체결 처리 뒤 요청 하나만 실행한다.
            self.collected[kind].extend(self.broker.rankings(kind, exchange))
            self.state["progress"] += 1
        except BrokerError as error:
            self.state["error"] = str(error)
            self.pending.clear()
            self.verified = False
            return
        if self.pending:
            return
        previous = {row["symbol"] for row in self.state.get("candidates", [])}
        candidates, count = rank_candidates(self.collected["price"], self.collected["volume"],
                                            self.strategy, previous, excluded)
        selected = {row["symbol"] for row in candidates}
        snapshot = dict(updated_at=now.isoformat(), candidates=candidates,
                        source_count=len(self.collected["price"]), eligible_count=count,
                        added=sorted(selected - previous), removed=sorted(previous - selected))
        if self.history_path:
            self.history_path.parent.mkdir(parents=True, exist_ok=True)
            descriptor = os.open(self.history_path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                stream.write(json.dumps(snapshot, ensure_ascii=False, allow_nan=False) + "\n")
        self.state.update(snapshot, error="")
        self.verified = True
