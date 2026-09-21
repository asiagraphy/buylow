# Development

> How to set up, build, and run buylow locally. For the system design see
> [ARCHITECTURE.md](./ARCHITECTURE.md).

## Prerequisites

- **.NET 10 SDK** (LEAN targets `net10.0`)
- **Python 3.11**, installed with `uv python install 3.11`. LEAN embeds this interpreter.
- **[uv](https://github.com/astral-sh/uv)** — Python env/dependency manager
- **git**
- For the backtest smoke test: a folder of **LEAN-format market data** (see below)

### Installing .NET 10 without sudo

The official script installs into `~/.dotnet` without touching the system:

```bash
curl -fsSL https://dot.net/v1/dotnet-install.sh | bash -s -- --channel 10.0 --install-dir "$HOME/.dotnet"
export DOTNET_ROOT="$HOME/.dotnet"
export PATH="$HOME/.dotnet:$PATH"
```

(`scripts/run-backtest.sh` sets these automatically if `~/.dotnet` is used.)

## Running in Docker (the easy path)

The two runtimes (Python 3.11 + .NET 10) make a native setup fiddly, so the recommended way to
run buylow — and the **only path we suggest for Windows** — is Docker. The `Dockerfile` is based on
`python:3.11-slim` (LEAN's pythonnet needs *exactly* 3.11) with the .NET 10 SDK layered on; the image
build prepares the launcher, both broker adapters, and NuGet content. `uv sync --locked --no-dev`
installs the orchestrator and strategy dependencies in one Python 3.11 project environment.

```bash
docker compose up -d --build   # → http://127.0.0.1:8420  (BUYLOW_PORT=9000 to change)
```

- **No prep step**: every bind mount is a *directory* (`data/`, `runs/`, `state/`), which Docker auto-creates
  if missing — works the same on every OS. (Bind-mounting individual *files* that don't exist is the footgun:
  Docker would create them as directories and the app would crash; we avoid it by mounting dirs only.)
- **Relocatable state paths**: the three runtime files default to the repo root but honor env overrides so the
  image can funnel them into one mounted dir — `BUYLOW_CONFIG_LOCAL` (`config.py`), `BUYLOW_DB_PATH`
  (`store.default_db_path`), `BUYLOW_KIS_TOKEN_CACHE` (`brokers/kis.py`), and `BUYLOW_TOSS_TOKEN_CACHE`
  (`brokers/toss.py`). The Dockerfile sets these under
  `/app/state`, and `docker-compose.yml` bind-mounts `./state` there. Native runs leave them at the root.
- **Host binding**: the server defaults to `127.0.0.1` (local-only — it holds trading control). In the
  container that would be unreachable through the port map, so the image sets
  `BUYLOW_DASHBOARD_HOST=0.0.0.0` (`get_dashboard_host()`). The local-only guarantee is preserved by
  `docker-compose.yml` mapping the host side to `127.0.0.1:<port>` only — no external exposure.
- **Persistence**: `data/`, `runs/`, and `state/` (config + DB + token) survive `docker compose down` +
  rebuilds. **`.dockerignore`** keeps the build context lean and never bakes host secrets/state into the image.
- API keys are entered in the dashboard's Settings tab after launch (written into `state/config.local.yaml`).

## LEAN NuGet version trap (important)

QuantConnect publishes **two lineages** on NuGet, and the higher semver is the **old** one:

| Lineage | Example | Target | Use? |
|---|---|---|---|
| `2.5.x` (current) | **`2.5.17757`** | `net10.0` | ✅ use this |
| `10730.0.0` (legacy) | `10730.0.0` | `net462` | ❌ incompatible with net10 |

`versions[-1]` resolves to the legacy `10730.x` — do **not** use it. All core packages
(`QuantConnect.Lean.Engine`, `Common`, `Brokerages`, `Indicators`, `Algorithm`,
`Compression`, `Configuration`, `Messaging`, `Queues`, `Api`, `Research`) are at
`2.5.17757`. Note: the `Holding` type lives in the root `QuantConnect` namespace.

## Building the launcher

```bash
dotnet build launcher/BuylowLauncher.csproj -c Release
```

`launcher/` is a net10 console app that vendors LEAN's `Program.cs` and references the
LEAN Engine NuGet (no fork). LEAN's `Composer` loads handler/plugin assemblies by name
from the output folder; `launcher/config.json` selects them.

## Running the backtest smoke test

A health check that the LEAN integration works end-to-end (no Toss/live needed):

```bash
# Point at a folder of LEAN-format data (e.g. the Data/ dir of a local QuantConnect/Lean clone).
export LEAN_DATA_DIR=/path/to/lean/Data
./scripts/run-backtest.sh
```

- `uv run --locked` uses the Python 3.11 project environment, including locked pandas and NumPy.
- **Exit code 0 means the LEAN integration is healthy.**
- Run a different strategy:
  ```bash
  STRATEGY=strategies/MyStrategy.py ALGO_TYPE=MyStrategy ./scripts/run-backtest.sh
  ```

### How the run script wires Python

LEAN's Python strategies do `from AlgorithmImports import *`, which loads many
`QuantConnect.*` CLR assemblies. The script sets:

- `PYTHONNET_PYDLL` → the detected `libpython3.11` shared library
- `PYTHONPATH` → the uv project site-packages, the `AlgorithmImports.py` directory (shipped
  inside the `QuantConnect.Common` NuGet package's `content/`), and the strategy directory

### Platform support (env resolution)

`orchestrator/lean/environment.py` resolves these paths per-OS so the same engine path runs on
macOS, Linux, **and Windows**:

- **libpython** — file name differs (`libpython3.11.dylib` / `.so` / `python311.dll`) and so does
  its location (Unix = `sysconfig LIBDIR`; Windows = the interpreter's install root, not `LIBDIR`
  which is `None` there). See `_libpython_filename` / `_resolve_pythonnet_pydll`.
- **Python selection**: `.python-version` and `requires-python` select Python 3.11 through uv.
  LEAN uses the current interpreter's shared library and `sysconfig.get_path('purelib')`.
  A mismatched Python version or missing shared library stops preparation before launch.
- **NuGet content**: `NUGET_PACKAGES` is honored when locating `AlgorithmImports.py`.
- **dotnet** — `dotnet.exe` vs `dotnet`; otherwise found on PATH.

macOS/Linux are CI-validated. The per-OS branches (incl. Windows) remain in
`environment.py` and are unit-tested in `tests/test_environment.py`, but **a native Windows install is
no longer a documented path** — Windows users run buylow via Docker (see *Running in Docker* above), which
sidesteps the .NET/Python runtime juggling entirely. The documented native paths are Linux and macOS.

## Running via the orchestrator (LEAN Runner)

The orchestrator's `LeanRunner` (`orchestrator/lean/`) is the programmatic equivalent of
`run-backtest.sh`: it resolves the environment, builds the launcher, generates `config.json`,
spawns the LEAN process, and parses the results.

```bash
LEAN_DATA_DIR=/path/to/lean/Data uv run --locked python -m orchestrator.lean
# a different strategy + parameters:
LEAN_DATA_DIR=/path/to/lean/Data uv run --locked python -m orchestrator.lean \
    --strategy strategies/My.py --algo-type My --param threshold=0.12
```

Results land in `runs/<run-id>/` (the LEAN result JSON + `run.log`); summary statistics are
parsed from stdout. Exit code `0` = the backtest completed. This is the same machinery the
dashboard/API uses. `scripts/run-backtest.sh` delegates to this same runner.
Each process receives its own `--config` file. Live configuration files contain credentials
and are created with owner-only permissions. Keep the ignored `runs/` directory private.

## Control API (dashboard backend)

```bash
# Install the locked project environment, including the default dev dependency group.
uv python install 3.11
uv sync --locked

# Prepare Python and the .NET launcher without starting the server or placing orders.
uv run --locked python -m orchestrator.lean --prepare

# run the Control API on 127.0.0.1:8420 (port via BUYLOW_DASHBOARD_PORT)
LEAN_DATA_DIR=/path/to/lean/Data uv run --locked python -m orchestrator.api
```

This also serves the **browser dashboard** at `http://127.0.0.1:8420` (3 chapters: ① 전략 설정 →
② 백테스트 → ③ 설정; HTMX + Jinja, vendored — no Node build). The strategy is **singular and
persisted** (`config.local.yaml` `strategy:`): you save conditions+risk once, then each backtest
only supplies period/cash/universe. JSON endpoints: `GET /healthz`, `POST /runs` (trigger a
backtest), `GET /runs`, `GET /runs/{id}`; HTML routes: `GET /` (② backtest form + history),
`GET /` redirects to `/strategy` (landing); HTML routes: `GET /backtest` (backtest form +
history), `POST /backtest` (run saved strategy → background job), `GET /ui/runs/{id}` (result
detail), `GET|POST /strategy` (edit + save the rule conditions and global risk; hides internal
UP/DOWN/NONE), `GET /data` + `GET /data/{ticker}` (view loaded OHLCV & 수급),
`POST /data/update` (③ '데이터 최신화': incremental load from the last loaded date to today,
or a 5-year bootstrap if empty; background), `GET /universe/index/{name}` (KOSPI200/KOSDAQ150
constituents ∩ loaded), `GET /jobs` + `GET /jobs/{id}` (background job status + live log), `GET|POST /settings`
(③ API keys). Dashboard backtests run as background jobs (non-blocking) with a live log. State is
persisted in `buylow.db` (SQLite, gitignored). The server binds to `127.0.0.1` only.

## Configuration & secrets

Settings resolve in order **env var → `config.local.yaml` → default**. Copy `config.example.yaml`
to `config.local.yaml` (gitignored) and fill values, or enter secrets in the dashboard at
`/settings`. With `data_folder` set in config you no longer need to `export LEAN_DATA_DIR`.

```yaml
# config.local.yaml (gitignored — never committed)
data_folder: ./data
dashboard_port: 8420
scheduler:
  enabled: false
  interval_minutes: 30
  minute_universe: []
risk:               # global risk management (%, blank = off) — applies to all backtests + live
  stop_loss:        # per-security stop-loss %, e.g. 7
  take_profit:      # per-security take-profit %
  trailing:         # trailing-stop %
secrets:
  krx_id: ""      # https://data.krx.co.kr free account — for pykrx fundamentals (PER/PBR)
  krx_pw: ""
```

The dashboard's **Data** page can trigger a bulk universe load (e.g. 3 years) as a **background
job** (`/jobs` shows status) without blocking; daily incremental updates run via the scheduler
(above). Bulk/incremental writes merge into existing per-ticker files (no duplicate dates).

- **KRX login**: `pykrx` reads `KRX_ID`/`KRX_PW` env vars. The server injects them from config on
  startup (`apply_krx_credentials`), so fundamentals (PER/PBR) work once credentials are set.
  Price (OHLCV) data needs no login.
- Recommend `chmod 600 config.local.yaml`. OS keychain storage is possible future hardening.

## Loading Korean market data (ETL)

LEAN replays historical data from disk; the ETL fetches it and writes LEAN-format files into
`./data`. Sources are pluggable (pykrx default, FinanceDataReader fallback).

```bash
python -m etl.krx --ticker 005930 --from 2023-01-01 --to 2023-12-31          # OHLCV via pykrx
python -m etl.krx --ticker 005930 --from 2023-01-01 --source fdr             # alternative source

# Investor flows (수급) and fundamentals (PER/PBR/배당) — require KRX login
python -m etl.flow --ticker 005930 --from 2023-01-01 --to 2023-12-31
python -m etl.fundamental --ticker 005930 --from 2023-01-01 --to 2023-12-31

# Bulk: a whole universe at once (efficient — one cross-sectional call per trading day,
# not one per ticker). market: KOSPI200 (default) | KOSPI | KOSDAQ | ALL
python -m etl.universe --market KOSPI200 --from 2023-01-01 --to 2023-12-31
```

OHLCV needs no login; **flows (수급) and fundamentals require KRX credentials** (see Configuration).
The KRX market definition is injected automatically. Files land in
`data/equity/krx/daily/<ticker>.zip` and `data/krx/flow/<ticker>.csv` (gitignored). 수급 is
non-standard data, consumed in strategies via a custom data type (PythonData) — coming next.

## Minute seed bundle (maintainer)

Bulk minute history is slow to fetch from KIS (many calls per ticker × day), so we ship a
**seed bundle as a GitHub Release asset** instead of committing it — `data/` stays gitignored,
clones stay light, and there's no unbounded git-history growth. Minute zips are write-once, so
re-packaging and replacing the asset is safe.

```bash
# Maintainer: package the local data/equity/krx/minute and (create or --clobber) the release.
# Requires `gh` logged in. Run when you've filled more/recent minute data and want to publish it.
bash scripts/make_minute_seed.sh
#   env overrides: BUYLOW_REPO (default JeongSeongMok/buylow), BUYLOW_SEED_TAG (default minute-seed)

# User: pull the seed (no gh/token — curls the public release asset) and extract into data/.
bash scripts/fetch_minute_seed.sh
```

Workflow: fill minute data locally (dashboard 분봉 최신화, or `python -m etl.kis_minute`) →
`make_minute_seed.sh` to publish → users `fetch_minute_seed.sh` and top up gaps incrementally
(the 분봉 최신화 button skips days already on disk). The fixed `minute-seed` tag keeps the
download URL stable across re-uploads.

## Tests

```bash
uv run --locked pytest               # unit + API tests
# end-to-end backtest (needs .NET + Python 3.11 + LEAN_DATA_DIR):
LEAN_DATA_DIR=/path/to/lean/Data uv run --locked pytest -m integration -o addopts=""
```

Per project rule, every feature ships with tests. Integration tests (real LEAN runs) are
marked `@pytest.mark.integration` and deselected by default so the normal run stays fast.

The macOS runtime check uses generated prices and runs the actual CLI, LEAN engine,
Python strategy, and fill logging without broker credentials or market-data requests:

```bash
uv run --locked pytest tests/test_lean_runtime.py -m integration -o addopts=""
```

The `dev` dependency group is included by default. Use `uv sync --locked --no-dev` for
application-only installation. Use `uv run --locked --env-file .env ...` when loading local
environment variables. `uvx` is for standalone tools, not for project tests or the dashboard.

## Machine-specific notes / gotchas

- **`dotnet` not on PATH:** export `DOTNET_ROOT`/`PATH` as above (the run script does this for `~/.dotnet`).
- **git commit fails with `invalid value for 'gpg.format': ''`:** your global `~/.gitconfig`
  has an empty `format =` under `[gpg]`. Remove that line (reverts to git's default). Commit
  signing is unaffected if `commit.gpgsign = false`.
- **A local clone of [QuantConnect/Lean](https://github.com/QuantConnect/Lean)** is a useful
  read-only reference for interfaces and sample data; its path is machine-specific (set
  `LEAN_DATA_DIR` to its `Data/` for the smoke test).

## Validation log

**2026-05-30** — Verified end-to-end on net10:
- .NET 10 SDK + LEAN `2.5.17757` packages restore and build.
- A net10 class library references LEAN, derives from `Brokerage`, implements
  `IDataQueueHandler`, and builds (`MyTrading.Toss.dll`).
- A self-built net10 thin launcher runs a full backtest (C# and Python strategies, identical results).
- Python strategy execution works via pythonnet (Python 3.11 + pandas + `AlgorithmImports`).
- `Composer` loads assemblies by name from the output folder.
