from datetime import datetime, timedelta
import json

import pytest

from brokers.kis_us import OrderUncertain, Quote
from orchestrator.us_runner import UsRunner
from orchestrator.us_strategy import Bar, NEW_YORK, Stock, STRATEGIES


class Broker:
    mode = "demo"
    profile = "synthetic-profile"

    def __init__(self):
        self.now = datetime(2026, 9, 21, 9, 55, tzinfo=NEW_YORK)
        self.price = 101.0
        self.records, self.placed, self.canceled = [], [], []
        self.positions = {}
        self.uncertain = False

    def holdings(self, exchanges):
        return [{"ovrs_pdno": symbol, "ovrs_cblc_qty": str(quantity)}
                for symbol, quantity in self.positions.items()]

    def orders(self, day):
        return self.records

    def bars(self, stock, since, now):
        opening = self.now.replace(hour=9, minute=30, second=0)
        rows = []
        for minute in range(1, 26):
            price = 101 if minute == 25 else 100 + minute * 0.02
            rows.append(Bar(opening + timedelta(minutes=minute), price - 0.03,
                            price + 0.05, price - 0.06, price,
                            20000 if minute == 25 else 10000))
        return rows

    def book(self, stock):
        return Quote(self.now, self.price, self.price - 0.01, self.price + 0.01)

    def buying_power(self, stock, price):
        return 10000

    def place(self, stock, side, quantity, price):
        self.placed.append((stock.symbol, side, quantity, price))
        if self.uncertain:
            raise OrderUncertain("synthetic lost response")
        number = str(len(self.placed))
        self.records.append({"odno": number, "pdno": stock.symbol, "ft_ccld_qty": "0",
                             "ft_ccld_amt3": "0", "nccs_qty": str(quantity), "rjct_rson": ""})
        return number

    def fill(self, number, quantity, price):
        row = next(row for row in self.records if row["odno"] == number)
        side = self.placed[int(number) - 1][1]
        row["ft_ccld_qty"] = str(int(row["ft_ccld_qty"]) + quantity)
        row["ft_ccld_amt3"] = str(float(row["ft_ccld_amt3"]) + quantity * price)
        row["nccs_qty"] = str(int(row["nccs_qty"]) - quantity)
        self.positions[row["pdno"]] = self.positions.get(row["pdno"], 0) + (quantity if side == "BUY" else -quantity)

    def cancel(self, stock, number, remaining):
        self.canceled.append((number, remaining))
        row = next(row for row in self.records if row["odno"] == number)
        row["nccs_qty"] = "0"
        row["rvse_cncl_dvsn"] = "02"


def runner(broker, path=None):
    return UsRunner(broker, STRATEGIES["momentum"], (Stock("AAPL"),), 10000,
                    path, now=lambda: broker.now)


def test_realistic_order_lifecycle_does_not_assume_submission_is_a_fill(tmp_path):
    broker = Broker()
    engine = runner(broker, tmp_path / "state.json")
    engine.tick()
    assert len(broker.placed) == 1
    assert not engine.state["positions"]
    assert engine.state["pending"]["AAPL"]["filled"] == 0
    quantity = broker.placed[0][2]
    broker.fill("1", quantity, 101.1)
    broker.now += timedelta(seconds=5)
    engine.tick()
    assert engine.state["positions"]["AAPL"]["quantity"] == quantity
    assert not engine.state["pending"]
    assert engine.summary()["estimated_profit_usd"] < 0
    broker.price = 105
    broker.now += timedelta(seconds=5)
    engine.tick()
    assert broker.placed[-1][1] == "SELL"
    broker.fill("2", quantity, 104.9)
    broker.now += timedelta(seconds=5)
    engine.tick()
    assert not engine.state["positions"]
    assert not engine.state["pending"]
    assert engine.summary()["estimated_profit_usd"] > 0
    assert len(engine.state["fills"]) == 2


def test_partial_entry_is_canceled_before_stop_exit_is_submitted():
    broker = Broker()
    engine = runner(broker)
    engine.tick()
    broker.fill("1", 2, 101.1)
    broker.price = 99
    broker.now += timedelta(seconds=5)
    engine.tick()
    assert broker.canceled and len(broker.placed) == 1
    broker.now += timedelta(seconds=5)
    engine.tick()
    assert broker.placed[-1][1:3] == ("SELL", 2)


def test_unknown_order_is_durable_and_cannot_be_restarted_blindly(tmp_path):
    broker = Broker()
    broker.uncertain = True
    path = tmp_path / "state.json"
    with pytest.raises(OrderUncertain):
        runner(broker, path).tick()
    persisted = json.loads(path.read_text())
    assert persisted["pending"]["AAPL"]["number"] is None
    assert persisted["halt"]
    with pytest.raises(OrderUncertain):
        runner(broker, path)
    assert len(broker.placed) == 1


def test_existing_manual_position_is_not_sold_or_added_to():
    broker = Broker()
    broker.positions["AAPL"] = 10
    engine = runner(broker)
    engine.tick()
    assert not broker.placed
    assert engine.state["excluded"] == ["AAPL"]


def test_resume_reconciles_account_before_more_orders(tmp_path):
    broker = Broker()
    path = tmp_path / "state.json"
    engine = runner(broker, path)
    engine.tick()
    broker.fill("1", broker.placed[0][2], 101.1)
    broker.now += timedelta(seconds=5)
    resumed = runner(broker, path)
    resumed.tick()
    assert len(broker.placed) == 1
    assert resumed.state["positions"]["AAPL"]["quantity"] == broker.positions["AAPL"]


def test_trial_loss_stays_latched_after_price_recovery():
    broker = Broker()
    engine = runner(broker)
    engine.start()
    engine.state["cash_flow"] = -600
    engine.tick()
    assert engine.state["halt"] == "실험 전체 손실 한도"
    engine.state["cash_flow"] = 0
    broker.now += timedelta(minutes=1)
    engine.tick()
    assert engine.state["halt"] == "실험 전체 손실 한도"
    assert not broker.placed
