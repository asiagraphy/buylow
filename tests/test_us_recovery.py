import json
from contextlib import nullcontext
from datetime import timedelta

from brokers.kis_us import QueryUnavailable
from orchestrator import us
from test_us_runner import Broker


def test_real_runner_retries_read_and_keeps_order_identity(tmp_path, monkeypatch):
    broker = Broker()
    original_bars = broker.bars
    reads, waits = [], []

    def bars(*arguments):
        reads.append(True)
        if len(reads) == 1:
            raise QueryUnavailable("/quotes/bars", "Timeout")
        return original_bars(*arguments)

    def wait(seconds):
        waits.append(seconds)
        if len(waits) == 2:
            raise KeyboardInterrupt
        broker.now += timedelta(seconds=seconds)

    original_runner = us.UsRunner
    engines = []

    def create(*arguments, **options):
        options["now"] = lambda: broker.now
        engine = original_runner(*arguments, **options)
        engines.append(engine)
        return engine

    monkeypatch.setattr(us, "STATE_ROOT", tmp_path)
    monkeypatch.setattr(us, "account_lock", lambda mode: nullcontext())
    monkeypatch.setattr(us, "client_for", lambda mode: broker)
    monkeypatch.setattr(us, "UsRunner", create)
    monkeypatch.setattr(us.time, "sleep", wait)
    broker.bars = bars
    assert us.main(["run", "--mode", "demo", "--budget", "10000", "--stocks", "AAPL"]) == 130
    assert len(engines) == 1 and len(reads) == 2
    assert len(broker.placed) == 1 and waits[0] == 5
    state = json.loads(us.state_path("demo", "momentum").read_text())
    assert state["query_health"]["status"] == "recovered"
    assert state["pending"]["AAPL"]["number"] == "1"
    event_path = us.state_path("demo", "momentum").with_suffix(".errors.jsonl")
    assert json.loads(event_path.read_text())["endpoint"] == "/quotes/bars"
    assert event_path.stat().st_mode & 0o777 == 0o600


def test_uncertain_order_never_enters_read_recovery_loop(tmp_path, monkeypatch):
    broker = Broker()
    broker.uncertain = True
    original_runner = us.UsRunner
    monkeypatch.setattr(us, "STATE_ROOT", tmp_path)
    monkeypatch.setattr(us, "account_lock", lambda mode: nullcontext())
    monkeypatch.setattr(us, "client_for", lambda mode: broker)
    monkeypatch.setattr(us, "UsRunner", lambda *args, **kwargs:
                        original_runner(*args, **kwargs, now=lambda: broker.now))
    monkeypatch.setattr(us.time, "sleep", lambda seconds: (_ for _ in ()).throw(AssertionError("order retry")))
    assert us.main(["run", "--budget", "10000", "--stocks", "AAPL"]) == 1
    assert len(broker.placed) == 1
    state = json.loads(us.state_path("demo", "momentum").read_text())
    assert state["pending"]["AAPL"]["number"] is None
    assert state["query_health"]["status"] == "stopped"
