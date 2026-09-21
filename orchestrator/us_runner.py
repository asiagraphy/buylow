"""미국주식 전략 실행기. KIS 모의·실전 및 재생 브로커가 같은 주문 상태 관리를 사용한다."""

from __future__ import annotations

import math
from dataclasses import asdict
from datetime import datetime, timedelta
from pathlib import Path

from brokers.kis_us import BrokerError, OrderUncertain, limit_price, private_json
from market.us import session_for
from .us_strategy import (
    Bar, Entry, NEW_YORK, Position, Stock, Strategy,
    entry_signal, exit_reason, loss_limit, size_entry,
)


class UsRunner:
    def __init__(self, broker, strategy: Strategy, stocks: tuple[Stock, ...], budget: float,
                 state_path: Path | None = None, *, now=None, on_event=None):
        if not math.isfinite(budget) or budget <= 0 or not stocks:
            raise ValueError("양수인 USD 예산과 미국 주식 후보가 필요합니다")
        if len({stock.symbol for stock in stocks}) != len(stocks):
            raise ValueError("중복 종목은 사용할 수 없습니다")
        self.broker, self.strategy, self.stocks, self.budget = broker, strategy, stocks, budget
        self.path = state_path
        self.now = now or (lambda: datetime.now(NEW_YORK))
        self.on_event = on_event or (lambda event: None)
        self.bars: dict[str, list[Bar]] = {}
        self.last_scan = None
        self.last_sync = None
        self.started = False
        self.state = {
            "profile": broker.profile, "mode": broker.mode, "strategy": strategy.name, "budget": budget,
            "strategy_settings": asdict(strategy),
            "stocks": [asdict(stock) for stock in stocks], "started_at": self.now().isoformat(),
            "sessions": [], "day": "", "day_start_profit": 0.0, "cash_flow": 0.0,
            "positions": {}, "pending": {}, "fills": [], "entry_counts": {},
            "cooldown": {}, "marks": {}, "excluded": [], "halt": "", "peak_equity": budget,
            "exit_attempts": {},
            "max_drawdown": 0.0,
        }
        if state_path and state_path.exists():
            import json
            saved = json.loads(state_path.read_text(encoding="utf-8"))
            for key in ("profile", "mode", "strategy", "budget", "stocks", "strategy_settings"):
                if saved.get(key) != self.state[key]:
                    raise BrokerError("실행 상태의 계좌·환경·전략·예산·종목이 다릅니다. 기존 실행을 확인하세요")
            self.state = saved
        if any(not pending.get("number") for pending in self.state["pending"].values()):
            raise OrderUncertain("응답을 확인하지 못한 주문이 남아 있습니다. status와 증권사 주문내역을 대조하세요")

    def save(self):
        if self.path:
            private_json(self.path, self.state)

    def emit(self, kind: str, **fields):
        self.on_event({"time": self.now().isoformat(), "kind": kind, **fields})

    def profit(self) -> float:
        return self.state["cash_flow"] + sum(
            value["quantity"] * self.state["marks"].get(symbol, value["entry_price"])
            for symbol, value in self.state["positions"].items())

    def summary(self) -> dict:
        profit = self.profit()
        equity = self.budget + profit
        self.state["peak_equity"] = max(equity, self.state["peak_equity"])
        self.state["max_drawdown"] = max(self.state["max_drawdown"],
            (self.state["peak_equity"] - equity) / self.state["peak_equity"])
        return {"mode": self.broker.mode, "strategy": self.strategy.name, "budget_usd": self.budget,
                "estimated_profit_usd": round(profit, 2), "estimated_return_pct": round(profit / self.budget * 100, 3),
                "max_drawdown_pct": round(self.state["max_drawdown"] * 100, 3),
                "fills": len(self.state["fills"]), "open_positions": len(self.state["positions"]),
                "pending_orders": len(self.state["pending"]), "sessions": len(self.state["sessions"]),
                "halt": self.state["halt"]}

    def start(self):
        self.sync_orders(force=True)
        rows = self.broker.holdings({stock.exchange for stock in self.stocks})
        holdings = {str(row["ovrs_pdno"]): int(float(row["ovrs_cblc_qty"])) for row in rows}
        for symbol, position in self.state["positions"].items():
            if holdings.get(symbol, 0) != position["quantity"]:
                raise BrokerError("저장된 보유량과 증권사 잔고가 다릅니다. 자동매매를 시작하지 않습니다")
        # 시작 전부터 있던 수동 포지션과 주문은 전략의 소유로 편입하지 않는다.
        excluded = set(self.state["excluded"])
        excluded.update(symbol for symbol, quantity in holdings.items()
                        if quantity and symbol not in self.state["positions"])
        for order in self.broker.orders(self.now().astimezone(NEW_YORK).date()):
            if int(float(order.get("nccs_qty") or 0)) > 0:
                known = any(pending["number"] == str(order["odno"]) for pending in self.state["pending"].values())
                if not known:
                    excluded.add(str(order["pdno"]))
        self.state["excluded"] = sorted(excluded)
        self.started = True
        self.save()

    def _apply_fill(self, symbol: str, pending: dict, quantity: int, amount: float):
        difference = quantity - pending["filled"]
        if difference <= 0:
            return
        if quantity > pending["quantity"] or not math.isfinite(amount) or amount <= pending["amount"]:
            raise OrderUncertain("증권사 체결 수량·금액이 저장된 주문과 일치하지 않습니다")
        increment = amount - pending["amount"]
        price = increment / difference
        fee = increment * self.strategy.commission_bps / 10_000
        positions = self.state["positions"]
        if pending["side"] == "BUY":
            previous = positions.get(symbol)
            prior_quantity = previous["quantity"] if previous else 0
            prior_cost = prior_quantity * previous["entry_price"] if previous else 0
            average = (prior_cost + increment) / (prior_quantity + difference)
            positions[symbol] = {
                "exchange": pending["exchange"], "quantity": prior_quantity + difference,
                "entry_price": average, "opened_at": previous["opened_at"] if previous else self.now().isoformat(),
                "stop_price": average - pending["stop_distance"],
                "target_price": average + pending["target_distance"],
            }
            self.state["cash_flow"] -= increment + fee
        else:
            if symbol not in positions or difference > positions[symbol]["quantity"]:
                raise OrderUncertain("매도 체결 수량이 전략 보유량보다 큽니다")
            self.state["cash_flow"] += increment - fee
            positions[symbol]["quantity"] -= difference
            if not positions[symbol]["quantity"]:
                del positions[symbol]
                self.state["exit_attempts"].pop(symbol, None)
                self.state["cooldown"][symbol] = (self.now() + timedelta(minutes=self.strategy.cooldown_minutes)).isoformat()
        pending["filled"], pending["amount"] = quantity, amount
        self.state["marks"][symbol] = price
        fill = {"time": self.now().isoformat(), "symbol": symbol, "side": pending["side"],
                "quantity": difference, "price": price, "estimated_fee": fee, "reason": pending["reason"]}
        self.state["fills"].append(fill)
        self.emit("fill", **{key: value for key, value in fill.items() if key != "time"})

    def sync_orders(self, force=False):
        now = self.now()
        if not self.state["pending"]:
            return
        if not force and self.last_sync and (now - self.last_sync).total_seconds() < 5:
            return
        histories = {}
        for pending in self.state["pending"].values():
            day = datetime.fromisoformat(pending["submitted_at"]).astimezone(NEW_YORK).date()
            if day not in histories:
                histories[day] = self.broker.orders(day)
        for symbol, pending in list(self.state["pending"].items()):
            day = datetime.fromisoformat(pending["submitted_at"]).astimezone(NEW_YORK).date()
            record = next((row for row in histories[day] if str(row["odno"]) == pending["number"]), None)
            age = (now - datetime.fromisoformat(pending["submitted_at"])).total_seconds()
            if record is None:
                if age > 120:
                    raise OrderUncertain("접수된 주문을 체결조회에서 찾을 수 없습니다")
                continue
            quantity = int(float(record["ft_ccld_qty"]))
            amount = float(record["ft_ccld_amt3"] or 0)
            remaining = int(float(record["nccs_qty"]))
            if quantity < pending["filled"]:
                continue
            self._apply_fill(symbol, pending, quantity, amount)
            rejected = str(record.get("rjct_rson") or "").strip() not in ("", "0", "0000")
            canceled = (str(record.get("rvse_cncl_dvsn", "")) == "02"
                        or "취소" in str(record.get("prcs_stat_name", "")))
            finished = quantity >= pending["quantity"] or (
                remaining == 0 and (rejected or canceled or pending.get("cancel_requested")))
            if finished:
                del self.state["pending"][symbol]
                if quantity == 0:
                    self.state["cooldown"][symbol] = (now + timedelta(minutes=self.strategy.cooldown_minutes)).isoformat()
                self.emit("order_closed", symbol=symbol, filled=quantity, canceled=quantity < pending["quantity"])
            elif pending.get("cancel_requested"):
                if (now - datetime.fromisoformat(pending["cancel_requested"])).total_seconds() > 120:
                    raise OrderUncertain("취소 완료를 확인할 수 없습니다. 추가 주문을 중단합니다")
            elif remaining > 0 and age >= self.strategy.entry_timeout_seconds:
                pending["cancel_requested"] = now.isoformat()
                self.save()
                self.broker.cancel(Stock(symbol, pending["exchange"]), pending["number"], remaining)
                self.emit("cancel_requested", symbol=symbol, remaining=remaining)
            self.save()
        self.last_sync = now

    def submit(self, stock: Stock, side: str, quantity: int, price: float, reason: str,
               entry: Entry | None = None):
        if stock.symbol in self.state["pending"] or quantity <= 0:
            return
        if side == "SELL":
            attempts = self.state["exit_attempts"].get(stock.symbol, 0)
            if attempts >= 3:
                raise BrokerError("청산 주문이 반복해서 미체결됐습니다. 증권사에서 보유·미체결을 확인하세요")
            self.state["exit_attempts"][stock.symbol] = attempts + 1
        pending = {"side": side, "exchange": stock.exchange, "quantity": quantity,
                   "price": price, "reason": reason, "submitted_at": self.now().isoformat(),
                   "filled": 0, "amount": 0.0, "number": None,
                   "stop_distance": entry.stop_distance if entry else 0,
                   "target_distance": entry.target_distance if entry else 0}
        # 전송 전에 기록한다. 응답 직전 프로세스가 종료돼도 같은 주문을 새 주문으로 재전송하지 않는다.
        self.state["pending"][stock.symbol] = pending
        self.save()
        try:
            pending["number"] = self.broker.place(stock, side, quantity, price)
        except OrderUncertain:
            self.state["halt"] = "주문 접수 여부 확인 필요"
            self.save()
            raise
        except BrokerError as error:
            del self.state["pending"][stock.symbol]
            self.state["cooldown"][stock.symbol] = (
                self.now() + timedelta(minutes=self.strategy.cooldown_minutes)).isoformat()
            self.save()
            self.emit("order_rejected", symbol=stock.symbol, message=str(error))
            return
        self.save()
        self.emit("order_submitted", symbol=stock.symbol, side=side, quantity=quantity,
                  limit_price=price, reason=reason)

    def _position(self, symbol: str, value: dict) -> Position:
        return Position(Stock(symbol, value["exchange"]), value["quantity"], value["entry_price"],
                        datetime.fromisoformat(value["opened_at"]), value["stop_price"],
                        value["target_price"])

    def tick(self) -> dict:
        if not self.started:
            self.start()
        now = self.now().astimezone(NEW_YORK)
        session = session_for(now.date())
        self.sync_orders()
        if session is None or now < session.open or now >= session.close:
            if (len(self.state["sessions"]) >= self.strategy.max_sessions
                    or now - datetime.fromisoformat(self.state["started_at"]) >= timedelta(days=7)):
                self.state["halt"] = "일주일 실험 기간 종료"
                self.save()
            return {**self.summary(), "phase": "closed"}
        day = now.date().isoformat()
        if self.state["day"] != day:
            self.state["day_start_profit"] = self.profit()
            self.state["day"] = day
            self.state["entry_counts"] = {}
            self.bars.clear()
            if day not in self.state["sessions"]:
                self.state["sessions"].append(day)
            if self.state["halt"] == "일일 손실 한도":
                self.state["halt"] = ""
        elapsed = now - datetime.fromisoformat(self.state["started_at"])
        if len(self.state["sessions"]) > self.strategy.max_sessions or elapsed >= timedelta(days=7):
            self.state["halt"] = "일주일 실험 기간 종료"

        quotes = {}
        for symbol, value in list(self.state["positions"].items()):
            quote = self.broker.book(Stock(symbol, value["exchange"]))
            if not quote.fresh(self.now()):
                raise BrokerError("보유 종목의 호가가 지연됐습니다. 증권사에서 포지션을 확인하세요")
            quotes[symbol] = quote
            self.state["marks"][symbol] = quote.bid
        profit = self.profit()
        breached = loss_limit(self.strategy, self.budget, profit, profit - self.state["day_start_profit"])
        if breached and self.state["halt"] in ("", "일일 손실 한도"):
            self.state["halt"] = breached
        if self.state["halt"] or now >= session.close - timedelta(minutes=10):
            for symbol, pending in self.state["pending"].items():
                if pending["side"] == "BUY" and not pending.get("cancel_requested"):
                    pending["cancel_requested"] = now.isoformat()
                    self.save()
                    self.broker.cancel(Stock(symbol, pending["exchange"]), pending["number"],
                                       pending["quantity"] - pending["filled"])
        for symbol, value in list(self.state["positions"].items()):
            position = self._position(symbol, value)
            reason = self.state["halt"] or exit_reason(self.strategy, position, quotes[symbol].bid, now, session.close)
            if reason:
                if symbol in self.state["pending"]:
                    pending = self.state["pending"][symbol]
                    if pending["side"] == "BUY" and not pending.get("cancel_requested"):
                        pending["cancel_requested"] = now.isoformat()
                        self.save()
                        self.broker.cancel(position.stock, pending["number"], pending["quantity"] - pending["filled"])
                else:
                    price = float(limit_price(quotes[symbol].bid * (1 - self.strategy.limit_offset_fraction), "SELL"))
                    self.submit(position.stock, "SELL", position.quantity, price, reason)

        minute = now.replace(second=0, microsecond=0)
        if self.last_scan != minute and not self.state["halt"]:
            self.last_scan = minute
            signals = []
            for stock in self.stocks:
                if stock.symbol in self.state["excluded"]:
                    continue
                history = self.bars.get(stock.symbol, [])
                since = history[-2].end if len(history) >= 2 else session.open
                fetched = self.broker.bars(stock, since, self.now())
                combined = {bar.end: bar for bar in history + fetched}
                history = self.bars[stock.symbol] = [combined[key] for key in sorted(combined)]
                signal = entry_signal(self.strategy, stock, history, self.now(), session.open, session.close)
                if signal:
                    signals.append(signal)
            self.emit("scan", candidates=len(self.stocks), signals=len(signals))
            for signal in sorted(signals, key=lambda signal: signal.score, reverse=True):
                symbol = signal.stock.symbol
                counts = self.state["entry_counts"]
                if (symbol in self.state["positions"] or symbol in self.state["pending"]
                        or sum(counts.values()) >= self.strategy.max_entries_per_day
                        or counts.get(symbol, 0) >= self.strategy.max_entries_per_stock):
                    continue
                cooldown = self.state["cooldown"].get(symbol)
                if cooldown and self.now() < datetime.fromisoformat(cooldown):
                    continue
                occupied = set(self.state["positions"]) | set(self.state["pending"])
                if len(occupied) >= self.strategy.max_positions:
                    break
                quote = self.broker.book(signal.stock)
                if not quote.fresh(self.now()) or quote.spread > self.strategy.max_spread_fraction:
                    continue
                if abs(quote.ask / signal.reference_price - 1) > self.strategy.limit_offset_fraction * 2:
                    continue
                price = float(limit_price(quote.ask * (1 + self.strategy.limit_offset_fraction), "BUY"))
                reserved = sum((pending["quantity"] - pending["filled"]) * pending["price"]
                               for pending in self.state["pending"].values() if pending["side"] == "BUY")
                cash = min(self.budget + self.state["cash_flow"] - reserved,
                           self.broker.buying_power(signal.stock, price))
                quantity = size_entry(self.strategy, signal, self.budget, cash, price)
                if quantity:
                    counts[symbol] = counts.get(symbol, 0) + 1
                    self.submit(signal.stock, "BUY", quantity, price, signal.reason, signal)
        result = {**self.summary(), "phase": "running"}
        self.save()
        return result
