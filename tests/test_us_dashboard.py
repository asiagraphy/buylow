import json
import signal

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from fastapi.templating import Jinja2Templates

from orchestrator import us
from orchestrator.us_dashboard import UsDashboard, register_us_dashboard
from orchestrator.dashboard.routes import TEMPLATES_DIR


@pytest.fixture
def web(tmp_path, monkeypatch):
    monkeypatch.setattr(us, "STATE_ROOT", tmp_path)
    monkeypatch.setattr(us, "credentials", lambda mode: dict(app_key="", app_secret="", account_no=""))
    manager = UsDashboard()
    app = FastAPI()
    register_us_dashboard(app, Jinja2Templates(directory=str(TEMPLATES_DIR)), manager)
    return TestClient(app), manager


def test_page_and_selection_do_not_start_trading(web, monkeypatch):
    client, manager = web
    monkeypatch.setattr(us, "client_for", lambda mode: pytest.fail("GET/save must not connect"))
    response = client.get("/us")
    assert response.status_code == 200
    assert "미국주식 자동매매" in response.text
    assert "최대 보유 60분" in response.text and "최대 보유 90분" in response.text
    response = client.post("/us/select", data={**manager.selection, "token": manager.token,
                                              "strategy": "opening-range"})
    assert response.status_code == 200
    assert manager.selection["strategy"] == "opening-range"
    assert not manager.running()
    assert UsDashboard().selection == manager.selection


def test_mutations_require_token_and_real_requires_confirmation(web, monkeypatch):
    client, manager = web
    assert client.post("/us/start", data=manager.selection).status_code == 403
    monkeypatch.setattr(us, "client_for", lambda mode: pytest.fail("No real start without consent"))
    response = client.post("/us/start", data={**manager.selection, "token": manager.token, "mode": "real"})
    assert response.status_code == 400 and "실전 주문 동의" in response.text
    response = client.post("/us/select", data={**manager.selection, "token": manager.token, "budget": "nan"})
    assert response.status_code == 400


def test_start_stop_uses_existing_cli_and_no_credentials_in_command(web, monkeypatch):
    from orchestrator import us_dashboard
    client, manager = web
    calls, signals = [], []
    class Process:
        returncode = None
        def poll(self): return self.returncode
        def send_signal(self, value): signals.append(value)
    process = Process()
    monkeypatch.setattr(us, "client_for", lambda mode: object())
    monkeypatch.setattr(us_dashboard.subprocess, "Popen", lambda command, **kwargs: calls.append(command) or process)
    monkeypatch.setattr(manager, "_read", lambda process: None)
    payload = {**manager.selection, "token": manager.token}
    assert client.post("/us/start", data=payload).status_code == 200
    assert calls[0][3:6] == ["orchestrator.us", "run", "--mode"]
    assert "--budget" in calls[0] and "--commission-bps" in calls[0]
    assert client.post("/us/start", data=payload).status_code == 400
    assert len(calls) == 1
    assert client.post("/us/stop", data={"token": manager.token}).status_code == 200
    assert signals == [signal.SIGINT]
    assert client.post("/us/stop", data={"token": manager.token}).status_code == 200
    assert signals == [signal.SIGINT]
    assert "중지 처리 중" in client.get("/us/status").text


def test_process_output_and_shutdown_without_broker_requests(web, monkeypatch):
    import subprocess
    import sys
    import time
    from orchestrator import us_dashboard
    _, manager = web
    spawn = subprocess.Popen
    script = 'import time; print(\'{"phase":"closed","halt":""}\', flush=True); time.sleep(30)'
    monkeypatch.setattr(us, "client_for", lambda mode: object())
    monkeypatch.setattr(us_dashboard.subprocess, "Popen",
                        lambda command, **kwargs: spawn([sys.executable, "-u", "-c", script], **kwargs))
    try:
        manager.start(manager.selection)
        deadline = time.monotonic() + 3
        while not manager.phase and time.monotonic() < deadline:
            time.sleep(0.01)
        assert manager.view()["phase"] == "closed"
        assert manager.running()
    finally:
        manager.shutdown()
    assert not manager.running()


def test_saved_fills_and_profit_are_displayed_without_profile(web):
    client, manager = web
    path = us.state_path("demo", "momentum", "week1")
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(dict(profile="private-profile", cash_flow=12.5, marks={},
        positions={}, pending={}, fills=[dict(time="2026-09-21T10:00:00-04:00", symbol="AAPL",
        side="SELL", quantity=1, price=110, reason="목표 가격")], halt="", sessions=[],
        budget=10000, max_drawdown=0.01)))
    response = client.get("/us/status")
    assert response.status_code == 200
    assert "$12.50" in response.text and "AAPL" in response.text
    assert "private-profile" not in response.text
