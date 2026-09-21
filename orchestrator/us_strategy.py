"""미국 정규장 분봉 전략. 신호 판단과 주문 전송을 분리해 재생·모의·실전이 같은 규칙을 쓴다."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

NEW_YORK = ZoneInfo("America/New_York")
US_EXCHANGES = {"NASD": "NAS", "NYSE": "NYS", "AMEX": "AMS"}


@dataclass(frozen=True)
class Stock:
    symbol: str
    exchange: str = "NASD"

    def __post_init__(self):
        if self.exchange not in US_EXCHANGES:
            raise ValueError("미국 거래소 NASD, NYSE, AMEX만 지원합니다")
        if not re.fullmatch(r"[A-Z][A-Z0-9.\-]{0,9}", self.symbol):
            raise ValueError("미국 주식 티커를 입력하세요")

    @property
    def quote_exchange(self) -> str:
        return US_EXCHANGES[self.exchange]


# 고정 매수 목록이 아니라 신호·유동성·거래비용 조건을 평가할 시작 후보군이다.
DEFAULT_STOCKS = tuple(Stock(symbol) for symbol in (
    "AAPL", "MSFT", "NVDA", "AMD", "AMZN", "META", "GOOGL", "TSLA",
))


@dataclass(frozen=True)
class Bar:
    end: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

    def __post_init__(self):
        values = (self.open, self.high, self.low, self.close, self.volume)
        if self.end.tzinfo is None or any(not math.isfinite(value) for value in values):
            raise ValueError("봉에는 시간대와 유한한 가격·거래량이 필요합니다")
        if not 0 < self.low <= min(self.open, self.close) <= max(self.open, self.close) <= self.high:
            raise ValueError("OHLC 가격 범위가 올바르지 않습니다")
        if self.volume < 0:
            raise ValueError("거래량은 음수일 수 없습니다")


@dataclass(frozen=True)
class Strategy:
    name: str
    label: str
    relative_volume: float
    reward_multiple: float
    max_hold_minutes: int
    risk_fraction: float = 0.0035
    position_fraction: float = 0.25
    max_positions: int = 3
    max_entries_per_day: int = 6
    max_entries_per_stock: int = 2
    cooldown_minutes: int = 10
    daily_loss_fraction: float = 0.02
    trial_loss_fraction: float = 0.05
    min_price: float = 5.0
    min_minute_turnover: float = 250_000.0
    max_spread_fraction: float = 0.002
    limit_offset_fraction: float = 0.001
    entry_timeout_seconds: int = 45
    max_bar_age_seconds: int = 120
    max_sessions: int = 5
    # 계좌별 실제 수수료가 아닌 검증용 비용 가정이다. 운영 설정에서 별도로 지정한다.
    commission_bps: float = 25.0
    slippage_bps: float = 5.0


STRATEGIES = {
    "momentum": Strategy("momentum", "미국 장중 모멘텀", 1.25, 2.0, 60),
    "opening-range": Strategy("opening-range", "미국 개장 범위 돌파", 1.5, 2.0, 90,
                              max_entries_per_day=4, max_entries_per_stock=1),
}


@dataclass(frozen=True)
class Entry:
    stock: Stock
    time: datetime
    reference_price: float
    stop_distance: float
    target_distance: float
    relative_volume: float
    score: float
    reason: str


@dataclass
class Position:
    stock: Stock
    quantity: int
    entry_price: float
    opened_at: datetime
    stop_price: float
    target_price: float


def _ema(values: list[float], period: int) -> float:
    result = values[0]
    smoothing = 2 / (period + 1)
    for value in values[1:]:
        result += smoothing * (value - result)
    return result


def completed_bars(bars: list[Bar], now: datetime, session_open: datetime,
                   session_close: datetime) -> list[Bar]:
    """완성된 정규장 봉만 사용한다. 동일 시각 봉은 최신 응답으로 교체한다."""
    return sorted({bar.end: bar for bar in bars
                   if session_open < bar.end <= min(now, session_close)}.values(),
                  key=lambda bar: bar.end)


def entry_signal(strategy: Strategy, stock: Stock, bars: list[Bar], now: datetime,
                 session_open: datetime, session_close: datetime) -> Entry | None:
    bars = completed_bars(bars, now, session_open, session_close)
    if len(bars) < 22 or now >= session_close - timedelta(minutes=45):
        return None
    current, previous = bars[-1], bars[-2]
    if (now - current.end).total_seconds() > strategy.max_bar_age_seconds:
        return None
    if current.close < strategy.min_price:
        return None
    # 누락된 구간을 연속 봉으로 간주하면 돌파·거래량 비교가 왜곡된다.
    recent = bars[-22:]
    if any(right.end - left.end != timedelta(minutes=1)
           for left, right in zip(recent, recent[1:])):
        return None
    prior = bars[-21:-1]
    average_volume = sum(bar.volume for bar in prior) / len(prior)
    average_turnover = sum(bar.volume * bar.close for bar in prior) / len(prior)
    if average_volume <= 0 or average_turnover < strategy.min_minute_turnover:
        return None
    relative_volume = current.volume / average_volume
    if relative_volume < strategy.relative_volume:
        return None
    volume = sum(bar.volume for bar in bars)
    vwap = sum((bar.high + bar.low + bar.close) / 3 * bar.volume for bar in bars) / volume
    closes = [bar.close for bar in bars]
    if current.close <= vwap or _ema(closes, 8) <= _ema(closes, 21):
        return None

    if strategy.name == "momentum":
        resistance = max(bar.high for bar in bars[-6:-1])
        triggered = previous.close <= resistance < current.close
        reason = "5분 고점 돌파 + EMA8>EMA21 + VWAP 상회 + 거래량 증가"
    elif strategy.name == "opening-range":
        opening = [bar for bar in bars if bar.end <= session_open + timedelta(minutes=15)]
        if len(opening) != 15 or opening[0].end != session_open + timedelta(minutes=1):
            return None
        resistance = max(bar.high for bar in opening) * 1.0005
        triggered = previous.close <= resistance < current.close
        reason = "개장 15분 범위 돌파 + EMA8>EMA21 + VWAP 상회 + 거래량 증가"
    else:
        raise ValueError("등록되지 않은 전략입니다")
    if not triggered:
        return None

    ranges = [max(bar.high - bar.low, abs(bar.high - before.close), abs(bar.low - before.close))
              for before, bar in zip(bars[-15:-1], bars[-14:])]
    atr = sum(ranges) / len(ranges)
    stop_distance = max(1.25 * atr, current.close * 0.006)
    if stop_distance > current.close * 0.02:
        return None
    round_trip_cost = current.close * 2 * (strategy.commission_bps + strategy.slippage_bps) / 10_000
    # 가격 차이만 2배로 잡으면 수수료가 큰 계좌에서 순손익비가 역전된다.
    target_distance = strategy.reward_multiple * (stop_distance + round_trip_cost) + round_trip_cost
    score = min(relative_volume, 5) * (current.close / bars[0].open - 1) / (stop_distance / current.close)
    return Entry(stock, current.end, current.close, stop_distance, target_distance,
                 relative_volume, score, reason)


def size_entry(strategy: Strategy, entry: Entry, budget: float, available_cash: float,
               limit_price: float) -> int:
    values = (budget, available_cash, limit_price, entry.stop_distance)
    if any(not math.isfinite(value) or value <= 0 for value in values):
        return 0
    fee_factor = 1 + strategy.commission_bps / 10_000
    # 매매 비용도 손실 예산에 포함해 작은 손절폭이 과도한 수량으로 이어지지 않게 한다.
    risk_per_share = entry.stop_distance + 2 * limit_price * (strategy.commission_bps + strategy.slippage_bps) / 10_000
    return max(0, math.floor(min(
        budget * strategy.risk_fraction / risk_per_share,
        budget * strategy.position_fraction / (limit_price * fee_factor),
        available_cash / (limit_price * fee_factor),
    )))


def exit_reason(strategy: Strategy, position: Position, price: float, now: datetime,
                session_close: datetime) -> str | None:
    if not math.isfinite(price) or price <= 0:
        raise ValueError("유효한 현재가가 필요합니다")
    if now >= session_close - timedelta(minutes=10):
        return "장 마감 전 청산"
    if price <= position.stop_price:
        return "손절"
    if price >= position.target_price:
        return "목표수익 도달"
    if now - position.opened_at >= timedelta(minutes=strategy.max_hold_minutes):
        return "최대 보유시간 도달"
    return None


def loss_limit(strategy: Strategy, budget: float, trial_profit: float,
               day_profit: float) -> str | None:
    if trial_profit <= -budget * strategy.trial_loss_fraction:
        return "실험 전체 손실 한도"
    if day_profit <= -budget * strategy.daily_loss_fraction:
        return "일일 손실 한도"
    return None
