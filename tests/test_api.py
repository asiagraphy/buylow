"""Control API 테스트 — 가짜 runner를 주입해 LEAN/.NET 없이 빠르게 검증."""

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from orchestrator.api import create_app
from orchestrator.lean import RunRequest, RunResult
from orchestrator.persistence import RunStore


class FakeRunner:
    """LeanRunner를 흉내내는 가짜 — 실제 백테스트 대신 정해진 결과를 돌려줌."""

    def __init__(self):
        self.calls: list[RunRequest] = []

    def run_backtest(self, request: RunRequest, on_start=None) -> RunResult:
        self.calls.append(request)
        return RunResult(
            run_id="fake-run-1",
            exit_code=0,
            statistics={"Total Orders": "1", "Net Profit": "1.694%"},
            run_dir=Path("/runs/fake-run-1"),
            log_path=Path("/runs/fake-run-1/run.log"),
            result_json=Path("/runs/fake-run-1/fake-run-1-summary.json"),
        )


@pytest.fixture
def client(tmp_path):
    runner = FakeRunner()
    app = create_app(runner=runner, store=RunStore(tmp_path / "api.db"))
    return TestClient(app), runner


def test_healthz(client):
    c, _ = client
    assert c.get("/healthz").json() == {"status": "ok"}


def test_create_run_persists_and_returns_record(client):
    c, runner = client
    resp = c.post("/runs", json={"strategy": "strategies/SmokeTestAlgorithm.py", "data_folder": "/data"})
    assert resp.status_code == 200
    body = resp.json()
    assert body["run_id"] == "fake-run-1"
    assert body["success"] is True
    assert body["statistics"]["Net Profit"] == "1.694%"
    # runner가 올바른 요청으로 호출됐는지
    assert runner.calls[0].data_folder == "/data"


def test_create_run_defaults_data_folder_from_config(client, tmp_path, monkeypatch):
    # data_folder 미지정 시 config(env > config.local.yaml > 기본)에서 해석돼야 함
    c, runner = client
    from orchestrator import config
    cfg = tmp_path / "config.local.yaml"
    cfg.write_text("data_folder: /cfg/data\n")
    monkeypatch.setattr(config, "CONFIG_LOCAL", cfg)
    monkeypatch.delenv("LEAN_DATA_DIR", raising=False)
    resp = c.post("/runs", json={"strategy": "strategies/SmokeTestAlgorithm.py"})
    assert resp.status_code == 200
    assert runner.calls[-1].data_folder == "/cfg/data"


def test_list_and_get_run(client):
    c, _ = client
    c.post("/runs", json={"strategy": "strategies/x.py", "data_folder": "/data"})
    assert len(c.get("/runs").json()) == 1
    assert c.get("/runs/fake-run-1").json()["run_id"] == "fake-run-1"
    assert c.get("/runs/missing").status_code == 404


@pytest.mark.parametrize("broker,adapter", [("kis_demo", "MyTrading.Kis.dll"),
                                          ("toss", "MyTrading.Toss.dll")])
def test_restart_uses_selected_broker_adapter(tmp_path, monkeypatch, broker, adapter):
    from orchestrator import config
    from orchestrator.lean import environment
    from unittest.mock import Mock

    config.set_broker(broker)
    monkeypatch.setattr(config, "live_start_ok", lambda: (True, "ok"))
    monkeypatch.setattr(config, "get_strategy", lambda: {"signals": {}})
    monkeypatch.setattr(config, "get_live_universe", lambda: ["005930"])
    monkeypatch.setattr(environment, "LAUNCHER_OUT", tmp_path)
    (tmp_path / adapter).touch()
    manager = Mock()
    runner = FakeRunner()
    app = create_app(runner=runner, broker_cache=Mock(), live_manager=manager)
    with TestClient(app) as client:
        assert client.get("/healthz").status_code == 200
        manager.enable.assert_called_once()
        assert manager.enable.call_args.args[0] is runner
    manager.shutdown.assert_called_once()
