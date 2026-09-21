"""자격증명·외부 시세 없이 실제 LEAN 프로세스에서 uv 런타임을 검증한다."""

import json
import os
import signal
import subprocess
import sys
from datetime import date, timedelta

import pytest

from etl.lean_format import write_equity_daily
from etl.sources import Bar
from market.krx import inject_krx_market
from orchestrator.lean.environment import REPO_ROOT
from orchestrator.lean.runner import _statistics_from_result


@pytest.mark.integration
def test_uv_runtime_executes_rule_strategy(tmp_path):
    data = tmp_path / "data"
    inject_krx_market(data)
    bars = []
    for offset in range(90):
        day = date(2024, 1, 1) + timedelta(days=offset)
        if day.weekday() < 5:
            price = 60000 + offset * 100
            bars.append(Bar(day, price, price + 100, price - 100, price, 100000))
    write_equity_daily(data, "krx", "005930", bars)
    spec = {
        "signals": {"EMA": {"type": "ema", "params": {"fast": 3, "slow": 5}}},
        "rule": "EMA", "universe": ["005930"], "resolution": "daily",
        "start": "2024-02-01", "end": "2024-02-16", "cash": 1000000,
        "data_folder": str(data),
    }
    process_env = dict(os.environ, BUYLOW_CONFIG_LOCAL=str(tmp_path / "config.local.yaml"))
    with (tmp_path / "run.log").open("w") as log:
        process = subprocess.Popen(
            [sys.executable, "-c",
             "import sys; from pathlib import Path; from orchestrator.lean import runner; "
             "runner.RUNS_DIR = Path(sys.argv.pop(1)); raise SystemExit(runner.main())",
             str(tmp_path / "runs"), "--strategy", "strategies/RuleStrategy.py",
             "--data-folder", str(data), "--param", "rule_spec=" + json.dumps(spec)],
            cwd=REPO_ROOT, env=process_env, start_new_session=True,
            stdout=log, stderr=subprocess.STDOUT,
        )
        try:
            process.wait(timeout=90)
        finally:
            if process.poll() is None:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    assert process.returncode == 0, (tmp_path / "run.log").read_text()[-6000:]
    run_dir, = (tmp_path / "runs").iterdir()
    statistics = _statistics_from_result(next(run_dir.glob("*-summary.json")))
    assert int(statistics["Total Orders"]) > 0
    fills = [json.loads(line) for line in (run_dir / "fills.jsonl").read_text().splitlines()]
    assert any(fill["quantity"] > 0 and fill["price"] > 0 for fill in fills)
