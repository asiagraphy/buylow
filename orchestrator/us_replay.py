"""미국 분봉 CSV 재생. 신호 다음 봉부터 지정가·거래량 제한·비용을 적용한다."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from brokers.kis_us import Quote
from .us_runner import UsRunner
from .us_strategy import Bar, NEW_YORK, Stock, Strategy


def load_bars(path: Path) -> dict[Stock, list[Bar]]:
    histories = {}
    with path.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        required = {"symbol", "exchange", "time", "open", "high", "low", "close", "volume"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("CSV에 symbol, exchange, time, open, high, low, close, volume 열이 필요합니다")
        for row in reader:
            stock = Stock(row["symbol"], row["exchange"])
            bar = Bar(datetime.fromisoformat(row["time"]),
                      *(float(row[key]) for key in ("open", "high", "low", "close", "volume")))
            histories.setdefault(stock, {})[bar.end] = bar
    if not histories:
        raise ValueError("분봉 CSV가 비어 있습니다")
    return {stock: [bars[time] for time in sorted(bars)] for stock, bars in histories.items()}


class ReplayBroker:
    mode = "replay"
    profile = "csv-replay"

    def __init__(self, histories: dict[Stock, list[Bar]], strategy: Strategy, budget: float):
        self.histories, self.strategy, self.cash = histories, strategy, budget
        self.now = min(bar.end for bars in histories.values() for bar in bars)
        self.records = []
        self.positions = {}

    def advance(self, now: datetime):
        self.now = now
        capacities = {}
        for record in self.records:
            if not int(record["nccs_qty"]) or record["submitted_at"] >= now:
                continue
            stock = record["stock"]
            bar = next((bar for bar in self.histories[stock] if bar.end == now), None)
            if bar is None:
                continue
            capacities.setdefault(stock, int(bar.volume * 0.01))
            quantity = min(int(record["nccs_qty"]), capacities[stock])
            if quantity <= 0:
                continue
            limit = record["price"]
            buy = record["side"] == "BUY"
            slipped_open = bar.open * (1 + self.strategy.slippage_bps / 10000 * (1 if buy else -1))
            if buy and bar.low <= limit:
                price = min(limit, slipped_open)
            elif not buy and bar.high >= limit:
                price = max(limit, slipped_open)
            else:
                continue
            amount = quantity * price
            fee = amount * self.strategy.commission_bps / 10000
            if buy and amount + fee > self.cash:
                record["rjct_rson"] = "INSUFFICIENT_CASH"
                record["nccs_qty"] = "0"
                continue
            self.cash += (-amount if buy else amount) - fee
            self.positions[stock.symbol] = self.positions.get(stock.symbol, 0) + (quantity if buy else -quantity)
            record["ft_ccld_qty"] = str(int(record["ft_ccld_qty"]) + quantity)
            record["ft_ccld_amt3"] = str(float(record["ft_ccld_amt3"]) + amount)
            record["nccs_qty"] = str(int(record["nccs_qty"]) - quantity)
            capacities[stock] -= quantity

    def bars(self, stock: Stock, since: datetime, now: datetime) -> list[Bar]:
        return [bar for bar in self.histories[stock] if since < bar.end <= now]

    def book(self, stock: Stock) -> Quote:
        bars = [bar for bar in self.histories[stock] if bar.end <= self.now]
        if not bars:
            raise ValueError("현재 시각까지의 분봉이 없습니다")
        bar = bars[-1]
        return Quote(bar.end, bar.close, bar.close * 0.99975, bar.close * 1.00025)

    def holdings(self, exchanges: set[str]) -> list[dict]:
        return [{"ovrs_pdno": symbol, "ovrs_cblc_qty": str(quantity)}
                for symbol, quantity in self.positions.items() if quantity]

    def orders(self, day) -> list[dict]:
        return [row for row in self.records if row["submitted_at"].astimezone(NEW_YORK).date() == day]

    def buying_power(self, stock: Stock, price: float) -> float:
        return self.cash

    def place(self, stock: Stock, side: str, quantity: int, price: float) -> str:
        number = str(len(self.records) + 1)
        self.records.append({"odno": number, "pdno": stock.symbol, "stock": stock, "side": side,
                             "quantity": quantity, "price": price, "submitted_at": self.now,
                             "ft_ccld_qty": "0", "ft_ccld_amt3": "0", "nccs_qty": str(quantity),
                             "rjct_rson": "", "rvse_cncl_dvsn": ""})
        return number

    def cancel(self, stock: Stock, number: str, remaining: int):
        record = next(row for row in self.records if row["odno"] == number)
        record["nccs_qty"] = "0"
        record["rvse_cncl_dvsn"] = "02"


def replay(histories: dict[Stock, list[Bar]], strategy: Strategy, budget: float) -> dict:
    broker = ReplayBroker(histories, strategy, budget)
    runner = UsRunner(broker, strategy, tuple(histories), budget, now=lambda: broker.now)
    curve = []
    for timestamp in sorted({bar.end for bars in histories.values() for bar in bars}):
        broker.advance(timestamp)
        result = runner.tick()
        curve.append({"time": timestamp.isoformat(), "equity_usd": budget + runner.profit()})
        if result["halt"] in ("실험 전체 손실 한도", "일주일 실험 기간 종료") and not result["open_positions"] and not result["pending_orders"]:
            break
    return {**runner.summary(), "source": "historical_csv", "commission_bps_per_side": strategy.commission_bps,
            "slippage_bps": strategy.slippage_bps, "synthetic_spread_bps": 5,
            "bar_volume_participation_cap": 0.01, "fills_detail": runner.state["fills"], "equity_curve": curve,
            "finished_flat": not runner.state["positions"] and not runner.state["pending"]}
