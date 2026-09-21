#!/usr/bin/env bash
#
# run-backtest.sh — buylow LEAN 백테스트 실행/연동 검증 스크립트.
#
# 무수정 LEAN 엔진(NuGet) + 우리 thin 런처로 Python 전략 백테스트를 끝까지 돌린다.
# 토스/실거래 없이 "LEAN 연동이 살아있는지"를 한 방에 확인하는 용도(스모크 테스트).
#
# 사용법:
#   LEAN_DATA_DIR=/path/to/lean/Data scripts/run-backtest.sh            # 기본: SmokeTestAlgorithm
#   LEAN_DATA_DIR=/path/to/lean/Data \
#     STRATEGY=strategies/My.py ALGO_TYPE=My scripts/run-backtest.sh    # 다른 전략
#
# 환경변수:
#   LEAN_DATA_DIR  (필수) LEAN 포맷 데이터 루트. 예: QuantConnect/Lean 클론의 Data/ 디렉토리
#   STRATEGY       전략 .py 경로 (기본: strategies/SmokeTestAlgorithm.py)
#   ALGO_TYPE      알고리즘 클래스명 (기본: 파일명 stem)
#   DOTNET_ROOT    .NET SDK 위치 (기본: ~/.dotnet)
set -euo pipefail

# --- 경로 기준 ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

# --- .NET ---
export DOTNET_ROOT="${DOTNET_ROOT:-$HOME/.dotnet}"
export PATH="$DOTNET_ROOT:$PATH"
export DOTNET_CLI_TELEMETRY_OPTOUT=1
command -v dotnet >/dev/null || { echo "ERROR: dotnet 없음 ($DOTNET_ROOT). .NET 10 SDK 설치 필요"; exit 1; }

# --- 데이터 폴더 (머신마다 다름 → 반드시 지정) ---
DATA_FOLDER="${LEAN_DATA_DIR:-}"
[ -n "$DATA_FOLDER" ] || { echo "ERROR: LEAN_DATA_DIR을 LEAN 포맷 데이터 폴더로 지정하세요 (예: Lean 클론의 Data/)"; exit 1; }
[ -d "$DATA_FOLDER" ] || { echo "ERROR: LEAN_DATA_DIR 경로 없음: $DATA_FOLDER"; exit 1; }

# --- 전략 인자 ---
STRATEGY="${STRATEGY:-strategies/SmokeTestAlgorithm.py}"
STRATEGY_ABS="$(cd "$(dirname "$STRATEGY")" && pwd)/$(basename "$STRATEGY")"
[ -f "$STRATEGY_ABS" ] || { echo "ERROR: 전략 파일 없음: $STRATEGY_ABS"; exit 1; }
ALGO_TYPE="${ALGO_TYPE:-$(basename "$STRATEGY" .py)}"

# 대시보드와 같은 실행 경로를 사용해 Python·의존성·설정 해석을 일치시킨다.
command -v uv >/dev/null || { echo "ERROR: uv 설치 필요"; exit 1; }
exec uv run --locked python -m orchestrator.lean \
    --strategy "$STRATEGY_ABS" --algo-type "$ALGO_TYPE" --data-folder "$DATA_FOLDER" "$@"
