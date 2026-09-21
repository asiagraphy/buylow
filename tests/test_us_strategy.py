from datetime import datetime, timedelta

import pytest

from orchestrator.us_strategy import (
    Bar, Entry, NEW_YORK, Position, Stock, STRATEGIES,
    completed_bars, entry_signal, exit_reason, loss_limit, size_entry,
)


def session():
    opening = datetime(2026, 9, 21, 9, 30, tzinfo=NEW_YORK)
    return opening, opening.replace(hour=16, minute=0)


def breakout_bars():
    opening, _ = session()
    bars = []
    for minute in range(1, 26):
        price = 100 + minute * 0.02
        if minute == 25:
            price = 101
        bars.append(Bar(opening + timedelta(minutes=minute), price - 0.03,
                        price + 0.05, price - 0.06, price,
                        10000 if minute < 25 else 20000))
    return bars


def test_only_us_exchange_and_ticker_accepted():
    assert Stock("NVDA").quote_exchange == "NAS"
    assert Stock("IBM", "NYSE").quote_exchange == "NYS"
    with pytest.raises(ValueError):
        Stock("005930")
    with pytest.raises(ValueError):
        Stock("NVDA", "KRX")


def test_momentum_requires_completed_fresh_volume_confirmed_breakout():
    opening, closing = session()
    bars = breakout_bars()
    strategy = STRATEGIES["momentum"]
    assert entry_signal(strategy, Stock("NVDA"), bars, bars[-1].end, opening, closing)
    assert entry_signal(strategy, Stock("NVDA"), bars, bars[-1].end - timedelta(seconds=1), opening, closing) is None
    assert entry_signal(strategy, Stock("NVDA"), bars, bars[-1].end + timedelta(minutes=3), opening, closing) is None
    last = bars[-1]
    bars[-1] = Bar(last.end, last.open, last.high, last.low, last.close, 1000)
    assert entry_signal(strategy, Stock("NVDA"), bars, last.end, opening, closing) is None


def test_missing_minute_does_not_masquerade_as_contiguous_history():
    opening, closing = session()
    bars = breakout_bars()
    assert entry_signal(STRATEGIES["momentum"], Stock("NVDA"),
                        bars[:10] + bars[11:], bars[-1].end, opening, closing) is None


def test_future_and_duplicate_bars_are_not_extra_signal_inputs():
    opening, closing = session()
    bars = breakout_bars()
    actual = completed_bars(bars + [bars[-1]], bars[-2].end, opening, closing)
    assert actual == bars[:-1]


def test_opening_range_is_frozen_after_first_fifteen_minutes():
    opening, closing = session()
    bars = breakout_bars()
    # 앞선 돌파가 없도록 개장 범위 상단을 높여 마지막 봉에서 처음 돌파시킨다.
    first = bars[0]
    bars[0] = Bar(first.end, first.open, 100.8, first.low, first.close, first.volume)
    result = entry_signal(STRATEGIES["opening-range"], Stock("AAPL"), bars,
                          bars[-1].end, opening, closing)
    assert result and "15분" in result.reason


def test_size_respects_risk_cash_allocation_and_whole_shares():
    opening, _ = session()
    strategy = STRATEGIES["momentum"]
    entry = Entry(Stock("AAPL"), opening, 100, 1, 2, 2, 1, "test")
    quantity = size_entry(strategy, entry, 10000, 10000, 100)
    assert quantity * (1 + 2 * 100 * 0.0025) <= 10000 * strategy.risk_fraction
    assert quantity * 100 * 1.0025 <= 10000 * strategy.position_fraction
    assert size_entry(strategy, entry, 10000, 99, 100) == 0


def test_exits_respect_early_close_and_holding_deadline():
    opening, closing = session()
    position = Position(Stock("AAPL"), 5, 100, opening, 99, 102)
    strategy = STRATEGIES["momentum"]
    assert exit_reason(strategy, position, 98.9, opening + timedelta(minutes=1), closing) == "손절"
    assert exit_reason(strategy, position, 102, opening + timedelta(minutes=2), closing) == "목표수익 도달"
    assert exit_reason(strategy, position, 100, opening + timedelta(minutes=60), closing) == "최대 보유시간 도달"
    early_close = closing.replace(hour=13)
    assert exit_reason(strategy, position, 100, early_close - timedelta(minutes=10), early_close) == "장 마감 전 청산"


def test_daily_and_trial_loss_stop_new_risk():
    strategy = STRATEGIES["momentum"]
    assert loss_limit(strategy, 10000, -100, -200) == "일일 손실 한도"
    assert loss_limit(strategy, 10000, -500, 0) == "실험 전체 손실 한도"
    assert loss_limit(strategy, 10000, 0, 0) is None


def test_profit_target_accounts_for_round_trip_costs():
    opening, closing = session()
    bars = breakout_bars()
    strategy = STRATEGIES["momentum"]
    result = entry_signal(strategy, Stock("NVDA"), bars, bars[-1].end, opening, closing)
    cost = result.reference_price * 2 * (strategy.commission_bps + strategy.slippage_bps) / 10000
    assert result.target_distance - cost == pytest.approx(strategy.reward_multiple * (result.stop_distance + cost))
