"""미국주식 웹 화면이 CLI 실행기를 시작·중지하고 저장 상태를 조회한다."""

from __future__ import annotations

import json
import math
import secrets
import signal
import subprocess
import sys
import threading

from fastapi import HTTPException, Request
from fastapi.responses import RedirectResponse

from brokers.kis_us import BrokerError, private_json
from . import us
from .us_strategy import DEFAULT_STOCKS, STRATEGIES


class UsDashboard:
    def __init__(self):
        self.lock = threading.RLock()
        self.process = None
        self.stopping = False
        self.message = "아직 시작하지 않았습니다."
        self.phase = ""
        self.token = secrets.token_urlsafe(32)
        self.path = us.STATE_ROOT / "dashboard.json"
        self.selection = dict(mode="demo", strategy="momentum", budget=10000,
                              trial="week1", commission_bps=25, universe_mode="auto",
                              stocks=",".join(stock.symbol for stock in DEFAULT_STOCKS))
        if self.path.exists():
            self.selection = self.validate(json.loads(self.path.read_text()))

    @staticmethod
    def validate(values):
        mode, strategy = values.get("mode"), values.get("strategy")
        if mode not in ("demo", "real") or strategy not in STRATEGIES:
            raise ValueError("투자 환경과 전략을 선택하세요.")
        budget = float(values.get("budget", 0))
        commission = float(values.get("commission_bps", 25))
        if not math.isfinite(budget) or budget <= 0 or not math.isfinite(commission) or commission < 0:
            raise ValueError("예산은 양수, 수수료는 0 이상이어야 합니다.")
        trial = str(values.get("trial", "week1"))
        universe_mode = values.get("universe_mode", "manual")
        if universe_mode not in ("auto", "manual"):
            raise ValueError("자동 탐색 또는 수동 지정을 선택하세요.")
        us.state_path(mode, strategy, trial)
        stocks = us.stocks_from_text(str(values.get("stocks", ""))) if universe_mode == "manual" else ()
        if universe_mode == "manual" and (not stocks or len({stock.symbol for stock in stocks}) != len(stocks)):
            raise ValueError("중복 없는 미국주식 후보를 입력하세요.")
        return dict(mode=mode, strategy=strategy, budget=budget, trial=trial, universe_mode=universe_mode,
                    commission_bps=commission,
                    stocks=",".join(f"{stock.exchange}:{stock.symbol}" for stock in stocks))

    def running(self):
        return self.process is not None and self.process.poll() is None

    def select(self, values):
        with self.lock:
            if self.running():
                raise ValueError("실행 중에는 설정을 바꿀 수 없습니다. 먼저 중지하세요.")
            selection = self.validate(values)
            private_json(self.path, selection)
            self.selection = selection
            self.message = "설정을 저장했습니다. 주문은 실행하지 않았습니다."

    def start(self, values):
        with self.lock:
            selection = self.validate(values)
            if selection["mode"] == "real" and values.get("confirm_real") != "yes":
                raise ValueError("실전은 실제 돈으로 주문됩니다. 실전 주문 동의를 선택하세요.")
            us.client_for(selection["mode"])  # 인증 요청 없이 필수 키·계좌 형식만 확인한다.
            self.select(selection)
            command = [sys.executable, "-u", "-m", "orchestrator.us", "run"]
            for name, value in selection.items():
                command.extend(["--" + name.replace("_", "-"), str(value)])
            self.process = subprocess.Popen(command, cwd=us.ROOT, stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT, text=True,
                                            start_new_session=True)
            self.stopping, self.phase = False, ""
            self.message = "실행기 시작 중입니다. 계좌·저장 상태를 확인합니다."
            threading.Thread(target=self._read, args=(self.process,), daemon=True).start()

    def _read(self, process):
        try:
            for line in process.stdout:
                with self.lock:
                    if self.process is not process:
                        break
                    if line.startswith("중단:"):
                        self.message = line.strip()
                    elif line.startswith("{"):
                        value = json.loads(line)
                        if "phase" in value:
                            self.phase = value["phase"]
                            self.message = (f"{value.get('error', '조회 실패')} · {value.get('retry_seconds')}초 후 재시도"
                                            if self.phase == "retrying" else value.get("halt") or (
                                            "정규장 시작을 기다립니다." if self.phase == "closed" else "전략 실행 중입니다."))
        finally:
            process.stdout.close()
            process.wait()
            with self.lock:
                if self.process is process and not self.message.startswith("중단:"):
                    self.message = ("실행을 중지했습니다. 증권사 미체결·보유는 남을 수 있습니다."
                                    if self.stopping or process.returncode == 0 else
                                    "실행기가 종료됐습니다. 저장 상태와 증권사 주문내역을 확인하세요.")

    def stop(self):
        with self.lock:
            if self.running() and not self.stopping:
                self.stopping = True
                self.message = "중지 요청을 보냈습니다. 주문과 보유는 자동 청산되지 않습니다."
                try:
                    self.process.send_signal(signal.SIGINT)
                except ProcessLookupError:
                    pass

    def shutdown(self):
        self.stop()
        if self.process:
            try:
                self.process.wait(timeout=15)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=5)

    def view(self):
        with self.lock:
            selection = dict(self.selection)
            result = dict(selection=selection, running=self.running(), stopping=self.stopping,
                          message=self.message, phase=self.phase, saved=None, token=self.token)
        path = us.state_path(selection["mode"], selection["strategy"], selection["trial"])
        if path.exists():
            saved = json.loads(path.read_text())
            profit = saved["cash_flow"] + sum(
                value["quantity"] * saved["marks"].get(symbol, value["entry_price"])
                for symbol, value in saved["positions"].items())
            # 계좌 식별값과 토큰은 HTML 컨텍스트에도 넣지 않는다.
            result["saved"] = {key: saved[key] for key in
                               ("positions", "pending", "fills", "halt", "sessions", "budget")}
            result["saved"].update(profit=profit, returns=profit / saved["budget"] * 100,
                                   drawdown=saved["max_drawdown"] * 100,
                                   universe=saved.get("universe"), query_health=saved.get("query_health"))
        result["ready"] = all(us.credentials(selection["mode"]).values())
        return result


def register_us_dashboard(app, templates, manager):
    def render(request, error="", status=200, partial=False):
        return templates.TemplateResponse(request, "partials/us_status.html" if partial else "us.html",
                                          {**manager.view(), "strategies": STRATEGIES, "error": error},
                                          status_code=status)

    @app.get("/us")
    def page(request: Request):
        return render(request)

    @app.get("/us/status")
    def status(request: Request):
        return render(request, partial=True)

    async def perform(request, action):
        form = await request.form()
        if not secrets.compare_digest(str(form.get("token", "")), manager.token):
            raise HTTPException(403, "화면을 새로고침한 뒤 다시 시도하세요.")
        try:
            action(form)
        except (ValueError, BrokerError) as error:
            return render(request, str(error), 400)
        except OSError:
            return render(request, "실행기 또는 로컬 파일을 열 수 없습니다.", 400)
        return RedirectResponse("/us", status_code=303)

    @app.post("/us/select")
    async def select(request: Request):
        return await perform(request, manager.select)

    @app.post("/us/start")
    async def start(request: Request):
        return await perform(request, manager.start)

    @app.post("/us/stop")
    async def stop(request: Request):
        return await perform(request, lambda form: manager.stop())
