from orchestrator import us
from orchestrator.us_strategy import Stock


def test_setup_keeps_existing_secrets_and_unrelated_settings(tmp_path, monkeypatch, capsys):
    path = tmp_path / ".env.local"
    path.write_text("BUYLOW_KIS_DEMO_APP_KEY=synthetic-key\n"
                    "BUYLOW_KIS_DEMO_APP_SECRET=synthetic-secret\n"
                    "BUYLOW_BROKER=kis_demo\nUNRELATED=value\n")
    replies = iter(("", "", "50000000-01"))
    monkeypatch.setattr(us.getpass, "getpass", lambda prompt: next(replies))
    us.setup("demo", path)
    content = path.read_text()
    assert "BUYLOW_KIS_DEMO_APP_KEY=synthetic-key" in content
    assert "UNRELATED=value" in content
    assert "BUYLOW_KIS_DEMO_ACCOUNT_NO=50000000-01" in content
    assert path.stat().st_mode & 0o777 == 0o600
    output = capsys.readouterr().out
    assert "synthetic-key" not in output and "synthetic-secret" not in output


def test_doctor_local_does_not_connect(monkeypatch, capsys):
    monkeypatch.setattr(us, "credentials", lambda mode: {
        "app_key": "synthetic-key", "app_secret": "synthetic-secret", "account_no": "50000000-01"})
    monkeypatch.setattr(us, "client_for", lambda mode: (_ for _ in ()).throw(AssertionError("network")))
    assert us.main(["doctor", "--mode", "demo"]) == 0
    assert "로컬 설정만" in capsys.readouterr().out


def test_us_modes_and_strategy_selection_are_explicit(monkeypatch):
    captured = []
    monkeypatch.setattr(us, "run_live", lambda arguments: captured.append(arguments))
    assert us.main(["run", "--budget", "10000"]) == 0
    assert captured[-1].mode == "demo" and captured[-1].strategy == "momentum"
    assert us.main(["run", "--mode", "real", "--strategy", "opening-range", "--budget", "100"]) == 0
    assert captured[-1].mode == "real" and captured[-1].strategy == "opening-range"


def test_market_selection_rejects_domestic_tickers():
    assert us.stocks_from_text("AAPL,NYSE:IBM") == (Stock("AAPL"), Stock("IBM", "NYSE"))
    assert us.main(["run", "--budget", "nan"]) == 1


def test_two_runners_cannot_control_the_same_mode(tmp_path, monkeypatch):
    from brokers.kis_us import BrokerError
    import pytest

    monkeypatch.setattr(us, "STATE_ROOT", tmp_path)
    with us.account_lock("demo"):
        with pytest.raises(BrokerError, match="이미"):
            with us.account_lock("demo"):
                pass
        with us.account_lock("real"):
            pass


def test_trial_name_does_not_allow_path_escape(monkeypatch, tmp_path):
    import pytest

    monkeypatch.setattr(us, "STATE_ROOT", tmp_path)
    assert us.state_path("demo", "momentum", "week2").name == "momentum-week2.json"
    with pytest.raises(ValueError):
        us.state_path("demo", "momentum", "../../account")


def test_replay_command_runs_from_terminal_and_writes_a_complete_report(tmp_path):
    import csv
    import json
    import subprocess
    import sys
    from datetime import datetime, timedelta
    from orchestrator.us_strategy import NEW_YORK

    source = tmp_path / "minutes.csv"
    output = tmp_path / "result.json"
    opening = datetime(2026, 9, 21, 9, 30, tzinfo=NEW_YORK)
    with source.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(("symbol", "exchange", "time", "open", "high", "low", "close", "volume"))
        for minute in range(1, 71):
            price = 100 + minute * 0.02 if minute < 25 else 101 + (minute - 25) * 0.1
            writer.writerow(("AAPL", "NASD", (opening + timedelta(minutes=minute)).isoformat(),
                             price - 0.03, price + 0.05, price - 0.06, price,
                             20000 if minute == 25 else 10000))
    result = subprocess.run([sys.executable, "-m", "orchestrator.us", "replay", "--file", str(source),
                             "--strategy", "momentum", "--output", str(output)],
                            cwd=us.ROOT, capture_output=True, text=True, timeout=20)
    assert result.returncode == 0, result.stderr
    report = json.loads(output.read_text())
    assert report["mode"] == "replay" and report["fills"] >= 2
    assert report["finished_flat"]
    assert len(report["equity_curve"]) == 70
