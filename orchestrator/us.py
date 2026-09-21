"""미국주식 설정·연결 점검·전략 재생·KIS 모의/실전 실행 명령."""

from __future__ import annotations

import argparse
import csv
import fcntl
import getpass
import json
import math
import os
import re
import time
from contextlib import contextmanager
from dataclasses import replace
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from brokers.kis_us import BrokerError, KisUsClient, OrderUncertain, private_json
from market.us import session_for
from . import config
from .us_replay import load_bars, replay
from .us_runner import UsRunner
from .us_strategy import DEFAULT_STOCKS, NEW_YORK, STRATEGIES, Stock

ROOT = Path(__file__).resolve().parents[1]
STATE_ROOT = ROOT / "state" / "us-trading"


def stocks_from_text(text: str | None) -> tuple[Stock, ...]:
    if text is None:
        return DEFAULT_STOCKS
    stocks = []
    for item in text.split(","):
        parts = item.strip().upper().split(":")
        if len(parts) == 1:
            stocks.append(Stock(parts[0]))
        elif len(parts) == 2:
            stocks.append(Stock(parts[1], parts[0]))
        else:
            raise ValueError("종목은 AAPL 또는 NYSE:IBM 형식입니다")
    return tuple(stocks)


def state_path(mode: str, strategy: str, trial: str = "week") -> Path:
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9-]{0,39}", trial):
        raise ValueError("실험 이름은 영문·숫자·하이픈으로 입력하세요")
    return STATE_ROOT / mode / f"{strategy}-{trial}.json"


@contextmanager
def account_lock(mode: str):
    directory = STATE_ROOT / mode
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / "trading.lock").open("a") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise BrokerError("이 투자 환경에서 다른 미국주식 실행기가 이미 동작 중입니다") from error
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def credentials(mode: str) -> dict:
    return config.get_kis_credentials("kis_demo" if mode == "demo" else "kis")


def client_for(mode: str) -> KisUsClient:
    values = credentials(mode)
    return KisUsClient(values["app_key"], values["app_secret"], values["account_no"], mode,
                       token_path=STATE_ROOT / mode / "token.json")


def setup(mode: str, path: Path | None = None):
    path = path or ROOT / ".env.local"
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    existing = {}
    for line in lines:
        match = re.match(r"^([A-Z_]+)=(.*)$", line)
        if match:
            existing[match[1]] = match[2]
    prefix = "BUYLOW_KIS_DEMO" if mode == "demo" else "BUYLOW_KIS"
    print("한투 모의투자 설정" if mode == "demo" else "한투 실전투자 설정")
    print("키와 계좌번호는 화면에 표시되지 않습니다. 기존 값은 Enter로 유지합니다.")
    values = {}
    for suffix, label in (("APP_KEY", "App Key"), ("APP_SECRET", "App Secret"),
                          ("ACCOUNT_NO", "계좌번호 (8자리-2자리)")):
        key = f"{prefix}_{suffix}"
        current = existing.get(key) or os.environ.get(key)
        value = getpass.getpass(f"{label}{' [기존 값 있음]' if current else ''}: ").strip()
        if not value:
            if current:
                continue
            raise ValueError(f"{label}이 필요합니다")
        if suffix == "ACCOUNT_NO" and not re.fullmatch(r"\d{8}-\d{2}", value):
            raise ValueError("계좌번호는 8자리-2자리 형식입니다")
        if any(character.isspace() for character in value) or any(character in value for character in "\"'#$"):
            raise ValueError("값에 공백·따옴표·환경변수 문자가 포함돼 있습니다. 복사한 값을 확인하세요")
        values[key] = value
    replaced = set()
    output = []
    for line in lines:
        key = line.split("=", 1)[0]
        if key in values:
            if key not in replaced:
                output.append(f"{key}={values[key]}")
                replaced.add(key)
        else:
            output.append(line)
    output.extend(f"{key}={value}" for key, value in values.items() if key not in replaced)
    temporary = path.with_name(path.name + ".tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    os.fchmod(descriptor, 0o600)
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        stream.write("\n".join(output) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)
    print(".env.local에 저장했습니다. API 호출과 주문은 실행하지 않았습니다.")


def doctor(mode: str, online: bool):
    values = credentials(mode)
    missing = [name for name in ("app_key", "app_secret", "account_no") if not values.get(name)]
    print("투자 환경:", "한투 모의투자" if mode == "demo" else "한투 실전투자")
    print("시장: 미국 NASDAQ / NYSE / AMEX, 통화: USD")
    if missing:
        raise BrokerError("설정이 부족합니다: " + ", ".join(missing) + ". setup 명령을 실행하세요")
    if not re.fullmatch(r"\d{8}-?\d{2}", values["account_no"]):
        raise BrokerError("계좌번호 형식을 확인하세요")
    print("키·계좌 설정: 준비됨 (값은 표시하지 않음)")
    print("호출 간격: 인증·시세·계좌·주문 전체에 최소 1초")
    if online:
        with account_lock(mode):
            client = client_for(mode)
            rows = client.holdings({stock.exchange for stock in DEFAULT_STOCKS})
            orders = client.orders(datetime.now(NEW_YORK).date())
            print(f"계좌 조회 성공: 보유 응답 {len(rows)}건, 당일 주문 응답 {len(orders)}건")
            quote = client.book(DEFAULT_STOCKS[0])
            age = (datetime.now(NEW_YORK) - quote.time).total_seconds()
            print(f"AAPL 호가 기준: {quote.time.isoformat()}, 경과 {age:.0f}초")
            if not quote.fresh(datetime.now(NEW_YORK)):
                print("호가가 지연되거나 장이 닫혀 있습니다. 정규장에도 지연되면 실시간 시세 권한을 확인하세요.")
            print("주문은 전송하지 않았습니다.")
    else:
        print("로컬 설정만 확인했습니다. 실제 연결 점검에는 --online을 붙이세요.")


def strategy_for(arguments):
    strategy = STRATEGIES[arguments.strategy]
    if arguments.commission_bps is not None:
        if not math.isfinite(arguments.commission_bps) or arguments.commission_bps < 0:
            raise ValueError("수수료 bps는 0 이상의 유한한 수여야 합니다")
        strategy = replace(strategy, commission_bps=arguments.commission_bps)
    return strategy


def report_saved(mode: str, name: str, trial: str = "week"):
    path = state_path(mode, name, trial)
    if not path.exists():
        print("저장된 실행 상태가 없습니다.")
        return
    saved = json.loads(path.read_text(encoding="utf-8"))
    # 계좌 식별용 내부 값과 토큰은 출력하지 않는다.
    report = {key: saved.get(key) for key in ("mode", "strategy", "budget", "started_at", "sessions", "halt")}
    report["positions"] = saved["positions"]
    report["pending_orders"] = saved["pending"]
    report["fills"] = saved["fills"]
    print(json.dumps(report, ensure_ascii=False, indent=2))


def run_live(arguments):
    strategy = strategy_for(arguments)
    stocks = stocks_from_text(arguments.stocks)
    with account_lock(arguments.mode):
        broker = client_for(arguments.mode)
        def event(value):
            print(json.dumps(value, ensure_ascii=False), flush=True)
        runner = UsRunner(broker, strategy, stocks, arguments.budget,
                          state_path(arguments.mode, strategy.name, arguments.trial), on_event=event)
        print(f"{strategy.label} / {'모의투자' if arguments.mode == 'demo' else '실전투자'} / 예산 ${arguments.budget:,.2f}")
        print("중지: Control+C. 중지해도 보유 주식과 증권사 미체결 주문은 남습니다.")
        last_display = None
        try:
            while True:
                before = time.monotonic()
                result = runner.tick()
                display = (datetime.now(NEW_YORK).strftime("%Y-%m-%d %H:%M"), result["phase"],
                           result["fills"], result["halt"])
                if display != last_display:
                    print(json.dumps(result, ensure_ascii=False), flush=True)
                    last_display = display
                if result["halt"] in ("실험 전체 손실 한도", "일주일 실험 기간 종료") and not result["open_positions"] and not result["pending_orders"]:
                    print("실험을 종료했습니다. status 명령으로 결과를 확인하세요.")
                    break
                time.sleep(max(0, (15 if result["phase"] == "closed" else 5) - (time.monotonic() - before)))
        finally:
            runner.save()
            result = runner.summary()
            print(f"실행 종료: 보유 {result['open_positions']}종목, 미체결 {result['pending_orders']}건. 증권사에서 확인하세요.")


def download(arguments):
    stocks = stocks_from_text(arguments.stocks)
    now = datetime.now(NEW_YORK)
    day, sessions = now.date(), []
    while len(sessions) < arguments.sessions:
        session = session_for(day)
        if session and session.open < now:
            sessions.append(session)
        day -= timedelta(days=1)
    since = sessions[-1].open
    destination = Path(arguments.output)
    if destination.exists():
        raise ValueError("출력 파일이 이미 있습니다. 다른 파일명을 사용하세요")
    with account_lock(arguments.mode):
        client = client_for(arguments.mode)
        collected = []
        for stock in stocks:
            bars = client.bars(stock, since, now)
            if not bars:
                raise BrokerError("요청한 종목의 분봉이 없습니다")
            print(f"{stock.symbol}: {len(bars)}개 봉, {bars[0].end.date()} ~ {bars[-1].end.date()}")
            collected.extend((stock, bar) for bar in bars)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("x", newline="", encoding="utf-8") as stream:
            writer = csv.writer(stream)
            writer.writerow(("symbol", "exchange", "time", "open", "high", "low", "close", "volume"))
            for stock, bar in collected:
                writer.writerow((stock.symbol, stock.exchange, bar.end.isoformat(),
                                 bar.open, bar.high, bar.low, bar.close, bar.volume))
    print("분봉을 저장했습니다. 반환된 실제 날짜 범위를 확인한 뒤 replay 명령을 사용하세요.")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="buylow 미국주식 전략과 한투 모의·실전 거래")
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("setup", "doctor", "status", "run", "download"):
        command = commands.add_parser(name)
        command.add_argument("--mode", choices=("demo", "real"), default="demo")
        if name in ("run", "status"):
            command.add_argument("--strategy", choices=STRATEGIES, default="momentum")
            command.add_argument("--trial", default="week", help="실험 이름. 같은 이름으로 실행하면 이어서 진행")
        if name == "doctor":
            command.add_argument("--online", action="store_true", help="토큰 발급과 계좌 조회, 주문 없음")
        if name == "run":
            command.add_argument("--budget", type=float, required=True, help="이 전략에 사용할 USD 예산")
            command.add_argument("--commission-bps", type=float)
            command.add_argument("--stocks", help="기본 후보군 대신 AAPL,NASD:NVDA,NYSE:IBM 형식")
        if name == "download":
            command.add_argument("--sessions", type=int, choices=range(1, 6), default=5)
            command.add_argument("--stocks")
            command.add_argument("--output", default="data/us/minutes.csv")
    command = commands.add_parser("replay", help="CSV로 전략을 재생, API 호출 없음")
    command.add_argument("--file", required=True)
    command.add_argument("--strategy", choices=STRATEGIES, default="momentum")
    command.add_argument("--budget", type=float, default=10000)
    command.add_argument("--commission-bps", type=float)
    command.add_argument("--output", default="runs/us-replay/result.json")
    commands.add_parser("strategies", help="선택 가능한 미국주식 전략")
    arguments = parser.parse_args(argv)
    try:
        if hasattr(arguments, "budget") and (not math.isfinite(arguments.budget) or arguments.budget <= 0):
            raise ValueError("USD 예산은 양수여야 합니다")
        if arguments.command == "setup":
            setup(arguments.mode)
        elif arguments.command == "doctor":
            doctor(arguments.mode, arguments.online)
        elif arguments.command == "status":
            report_saved(arguments.mode, arguments.strategy, arguments.trial)
        elif arguments.command == "run":
            run_live(arguments)
        elif arguments.command == "download":
            download(arguments)
        elif arguments.command == "replay":
            destination = Path(arguments.output)
            if destination.exists():
                raise ValueError("결과 파일이 이미 있습니다. --output에 다른 파일명을 지정하세요")
            result = replay(load_bars(Path(arguments.file)), strategy_for(arguments), arguments.budget)
            private_json(destination, result)
            print(json.dumps({key: value for key, value in result.items()
                              if key not in ("fills_detail", "equity_curve")}, ensure_ascii=False, indent=2))
        elif arguments.command == "strategies":
            for strategy in STRATEGIES.values():
                print(f"{strategy.name}: {strategy.label}, 최대 {strategy.max_entries_per_day}회 진입 시도/일, "
                      f"최대 보유 {strategy.max_hold_minutes}분")
    except KeyboardInterrupt:
        print("사용자가 실행을 중지했습니다.")
        return 130
    except (BrokerError, ValueError, OSError, KeyError) as error:
        print(f"중단: {error}" if isinstance(error, (BrokerError, ValueError)) else "중단: 로컬 파일 또는 응답 형식을 확인하세요.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
