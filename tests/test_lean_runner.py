"""LeanRunner의 순수 로직 단위 테스트 (LEAN/.NET 없이 빠르게)."""

import os
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from orchestrator.lean.runner import (
    RunRequest, RunResult, _build_config, _STAT_RE, _statistics_from_result,
)


def test_request_defaults_algorithm_type_to_filename_stem():
    req = RunRequest(strategy_path="strategies/SmokeTestAlgorithm.py", data_folder="/tmp/data")
    assert req.resolved_algorithm_type() == "SmokeTestAlgorithm"


def test_request_explicit_algorithm_type_wins():
    req = RunRequest(strategy_path="strategies/x.py", data_folder="/tmp", algorithm_type="Custom")
    assert req.resolved_algorithm_type() == "Custom"


def test_build_config_core_fields(tmp_path):
    req = RunRequest(
        strategy_path="strategies/SmokeTestAlgorithm.py",
        data_folder=str(tmp_path),
        parameters={"threshold": 0.12, "n": 5},  # 비문자열도 받아 문자열로 강제돼야 함
    )
    cfg = _build_config(req, results_dir=tmp_path / "run1", algorithm_id="run1")

    assert cfg["environment"] == "backtesting"
    # 종료 시 'Press any key' 콘솔 대기로 멈추지 않도록 자동 종료 플래그가 켜져 있어야 함
    assert cfg["close-automatically"] is True
    assert cfg["algorithm-language"] == "Python"
    assert cfg["algorithm-type-name"] == "SmokeTestAlgorithm"
    assert cfg["algorithm-id"] == "run1"
    assert os.path.isabs(cfg["algorithm-location"])  # 절대경로로 해석
    assert cfg["results-destination-folder"] == str(tmp_path / "run1")
    # 파라미터는 전부 문자열이어야 함 (LEAN get_parameter는 문자열 반환)
    assert cfg["parameters"]["threshold"] == "0.12" and cfg["parameters"]["n"] == "5"
    # 체결 로그 경로가 run_dir/fills.jsonl 로 주입돼야 함(완전한 거래내역 확보용)
    assert cfg["parameters"]["trade_log"] == str(tmp_path / "run1" / "fills.jsonl")
    # 백테스트 환경 핸들러가 있어야 함
    assert "backtesting" in cfg["environments"]
    assert cfg["environments"]["backtesting"]["live-mode"] is False


def test_params_with_risk_injects_global_risk(tmp_path, monkeypatch):
    from orchestrator import config
    from orchestrator.lean.runner import _params_with_risk
    monkeypatch.setattr(config, "CONFIG_LOCAL", tmp_path / "config.local.yaml")
    config.save_risk({"stop_loss": "7"})
    params = _params_with_risk({"composition": "{}"})
    assert params["risk_stop_loss"] == "7.0"     # 전역 리스크가 주입됨
    assert params["composition"] == "{}"          # 기존 파라미터 보존
    assert "risk_take_profit" not in params       # 미설정은 주입 안 함


@pytest.mark.parametrize(
    "line,name,value",
    [
        ("STATISTICS:: Total Orders 1", "Total Orders", "1"),
        ("STATISTICS:: Net Profit 1.694%", "Net Profit", "1.694%"),
        ("STATISTICS:: Total Fees $3.45", "Total Fees", "$3.45"),
    ],
)
def test_stat_regex_parses_name_and_value(line, name, value):
    m = _STAT_RE.search(line)
    assert m is not None
    assert m.group(1).strip() == name
    assert m.group(2).strip() == value


def test_statistics_from_result_reads_summary_json(tmp_path):
    import json
    p = tmp_path / "x-summary.json"
    p.write_text(json.dumps({"statistics": {"Net Profit": "-4.926%", "Total Orders": "343"}}),
                 encoding="utf-8")
    stats = _statistics_from_result(p)
    assert stats["Net Profit"] == "-4.926%" and stats["Total Orders"] == "343"


def test_statistics_from_result_handles_missing_or_bad(tmp_path):
    assert _statistics_from_result(None) == {}
    assert _statistics_from_result(tmp_path / "nope.json") == {}
    bad = tmp_path / "bad.json"; bad.write_text("not json", encoding="utf-8")
    assert _statistics_from_result(bad) == {}
    empty = tmp_path / "e.json"; empty.write_text("{}", encoding="utf-8")
    assert _statistics_from_result(empty) == {}


def test_run_result_success_only_on_zero_exit(tmp_path):
    ok = RunResult("r", 0, {}, tmp_path, tmp_path / "run.log", None)
    bad = RunResult("r", 1, {}, tmp_path, tmp_path / "run.log", None)
    assert ok.success is True
    assert bad.success is False


def test_backtests_use_distinct_private_configs(tmp_path, monkeypatch):
    from orchestrator.lean import runner

    calls = []

    class Process:
        stdout = []
        returncode = 0

        def wait(self):
            return self.returncode

    def launch(command, **kwargs):
        configuration = Path(command[command.index("--config") + 1])
        calls.append((configuration, json.loads(configuration.read_text())))
        assert configuration.stat().st_mode & 0o777 == 0o600
        return Process()

    monkeypatch.setattr(runner, "RUNS_DIR", tmp_path / "runs")
    monkeypatch.setattr(runner.subprocess, "Popen", launch)
    environment = SimpleNamespace(
        venv_site_packages=tmp_path, algorithm_imports_dir=tmp_path,
        launcher_dll=tmp_path / "launcher" / "BuylowLauncher.dll",
        dotnet_exe=tmp_path / "dotnet", process_env=lambda parts: {},
    )
    instance = runner.LeanRunner(env=environment)
    request = RunRequest("strategies/RuleStrategy.py", str(tmp_path))
    first = instance.run_backtest(request)
    second = instance.run_backtest(request)
    assert first.run_id != second.run_id
    assert calls[0][0].parent == first.run_dir
    assert calls[1][0].parent == second.run_dir
    assert calls[0][1]["algorithm-id"] == first.run_id
    assert not (environment.launcher_dll.parent / "config.json").exists()


@pytest.mark.integration
def test_backtest_end_to_end():
    """실제 LEAN 백테스트 (LEAN_DATA_DIR + .NET + Python3.11 필요). 기본 실행에서 제외."""
    data_dir = os.environ.get("LEAN_DATA_DIR")
    if not data_dir:
        pytest.skip("LEAN_DATA_DIR 미설정")
    from orchestrator.lean import LeanRunner
    result = LeanRunner().run_backtest(
        RunRequest(strategy_path="strategies/SmokeTestAlgorithm.py", data_folder=data_dir)
    )
    assert result.success
    assert "Total Orders" in result.statistics
