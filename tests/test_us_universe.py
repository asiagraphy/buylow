from datetime import datetime, timedelta
import json

from brokers.kis_us import BrokerError
from orchestrator.us_strategy import NEW_YORK, STRATEGIES
from orchestrator.us_universe import MAX_CANDIDATES, UniverseScanner, rank_candidates


def price_row(symbol="ALFA", **changes):
    return dict(symb=symbol, excd="NAS", enam=f"{symbol} INC", e_ordyn="○",
                last="50", rate="8", n_rate="2", tvol="2000000",
                pbid="49.99", pask="50.01", **changes)


def volume_row(symbol="ALFA"):
    return dict(symb=symbol, excd="NAS", n_diff="200000")


def test_percentile_score_and_filters():
    prices = [price_row("ALFA"), {**price_row("BETA"), "rate": "12", "n_rate": "3"}]
    volumes = [volume_row("ALFA"), volume_row("BETA")]
    rows, count = rank_candidates(prices, volumes, STRATEGIES["momentum"])
    assert count == 2 and rows[0]["symbol"] == "BETA"
    for changes in ({"enam": "ALFA 2X ETF"}, {"last": "4"}, {"pask": "55"},
                    {"rate": "nan"}, {"e_ordyn": ""}, {"n_rate": "0"}, {"tvol": "20"}):
        rows, _ = rank_candidates([{**price_row(), **changes}], [volume_row()], STRATEGIES["momentum"])
        assert not rows
    rows, _ = rank_candidates([price_row()], [], STRATEGIES["momentum"])
    assert not rows


def test_limit_and_incumbent_bonus_do_not_keep_ineligible_stocks():
    prices = [price_row(f"STOCK{number}") for number in range(14)]
    volumes = [volume_row(row["symb"]) for row in prices]
    selected, total = rank_candidates(prices, volumes, STRATEGIES["momentum"], {"STOCK9"}, {"STOCK0"})
    assert total == 13 and len(selected) == MAX_CANDIDATES
    assert selected[0]["symbol"] == "STOCK9"
    assert "STOCK0" not in {row["symbol"] for row in selected}


class RankingBroker:
    def __init__(self):
        self.calls = []
        self.fail = False

    def rankings(self, kind, exchange):
        self.calls.append((kind, exchange))
        if self.fail:
            raise BrokerError("순위 조회 실패")
        if exchange != "NASD":
            return []
        return [price_row()] if kind == "price" else [volume_row()]


def test_incremental_refresh_expiry_failure_and_history(tmp_path):
    broker = RankingBroker()
    state = {"candidates": []}
    history = tmp_path / "selection.jsonl"
    scanner = UniverseScanner(broker, STRATEGIES["momentum"], state, history)
    opening = datetime(2026, 9, 21, 9, 30, tzinfo=NEW_YORK)
    scanner.step(opening, opening)
    assert not broker.calls
    now = opening + timedelta(minutes=22)
    for index in range(6):
        scanner.step(now + timedelta(seconds=index * 5), opening)
        assert len(broker.calls) == index + 1
        assert scanner.ready(now + timedelta(seconds=index * 5), opening) == (index == 5)
    assert state["candidates"][0]["symbol"] == "ALFA"
    assert json.loads(history.read_text())["added"] == ["ALFA"]
    assert history.stat().st_mode & 0o777 == 0o600
    assert not scanner.ready(now + timedelta(minutes=11), opening)
    broker.fail = True
    scanner.step(now + timedelta(minutes=5), opening)
    assert state["error"] and not scanner.ready(now + timedelta(minutes=5), opening)
    assert state["candidates"]  # 실패했다고 기존 관측 기록을 지우지 않는다.
    scanner.step(now + timedelta(minutes=5, seconds=5), opening)
    assert len(broker.calls) == 7


def test_restart_requires_new_snapshot_before_entries():
    now = datetime(2026, 9, 21, 10, tzinfo=NEW_YORK)
    scanner = UniverseScanner(RankingBroker(), STRATEGIES["momentum"],
                              {"candidates": [], "updated_at": now.isoformat(), "error": ""})
    assert not scanner.ready(now, now.replace(hour=9, minute=30))
