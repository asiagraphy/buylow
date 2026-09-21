from datetime import datetime, timedelta

from orchestrator.us_replay import ReplayBroker, replay
from orchestrator.us_strategy import Bar, NEW_YORK, Stock, STRATEGIES


def test_replay_cannot_fill_on_signal_bar_and_limits_participation():
    start = datetime(2026, 9, 21, 10, 0, tzinfo=NEW_YORK)
    stock = Stock("AAPL")
    histories = {stock: [Bar(start, 100, 101, 99, 100, 100),
                         Bar(start + timedelta(minutes=1), 100, 101, 99, 100, 100)]}
    broker = ReplayBroker(histories, STRATEGIES["momentum"], 10000)
    number = broker.place(stock, "BUY", 10, 100.2)
    broker.advance(start)
    assert broker.orders(start.date())[0]["ft_ccld_qty"] == "0"
    broker.advance(start + timedelta(minutes=1))
    assert broker.orders(start.date())[0]["ft_ccld_qty"] == "1"
    assert broker.positions["AAPL"] == 1
    broker.cancel(stock, number, 9)
    assert broker.orders(start.date())[0]["nccs_qty"] == "0"


def test_replay_prices_beyond_limit_do_not_fill():
    start = datetime(2026, 9, 21, 10, 0, tzinfo=NEW_YORK)
    stock = Stock("AAPL")
    histories = {stock: [Bar(start, 100, 101, 99, 100, 10000),
                         Bar(start + timedelta(minutes=1), 105, 106, 104, 105, 10000)]}
    broker = ReplayBroker(histories, STRATEGIES["momentum"], 10000)
    broker.place(stock, "BUY", 2, 101)
    broker.advance(start + timedelta(minutes=1))
    assert not broker.positions


def test_replay_runs_shared_strategy_and_reports_costs_without_promising_profit():
    opening = datetime(2026, 9, 21, 9, 30, tzinfo=NEW_YORK)
    stock = Stock("AAPL")
    bars = []
    for minute in range(1, 71):
        price = 100 + minute * 0.02 if minute < 25 else 101 + (minute - 25) * 0.1
        bars.append(Bar(opening + timedelta(minutes=minute), price - 0.03,
                        price + 0.05, price - 0.06, price, 20000 if minute == 25 else 10000))
    result = replay({stock: bars}, STRATEGIES["momentum"], 10000)
    assert result["fills"] >= 2
    assert all(fill["estimated_fee"] > 0 for fill in result["fills_detail"])
    assert result["equity_curve"]
    assert result["source"] == "historical_csv"
