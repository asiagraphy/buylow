# uv migration review

## Scope

Use one Python 3.11 project environment, declared dependencies in `pyproject.toml`,
and reproducible installs from `uv.lock` for native and Docker execution.
Review backtest and trading startup, shutdown, and broker integration; preserve
the existing Toss read-only commands. Actual account orders require separate
operator authorization. The paper trading provider is pending clarification.

## Resolved findings

- Native installation and Docker builds consume `uv.lock` through `uv sync --locked`.
- LEAN and the orchestrator share the Python 3.11 project environment and locked dependencies.
- Python shared-library discovery follows the interpreter running the application.
- Python metadata and `.python-version` both require 3.11. Development dependencies use a group.
- The shell backtest entry point uses the same runner as the dashboard.
- Trading restart checks the selected broker's adapter.
- Startup cancellation rejects and terminates a process from a stopped generation.
- Startup failures observe restart backoff even before a process exists.
- Concurrent jobs receive distinct configuration files with owner-only permissions.

## Remaining trading review

- Broker adapters return empty open-order lists on restart.
- KIS retries orders after ambiguous transport failures, risking duplicate submission.
- The current Toss API specification includes WebSocket support; existing documentation
  saying the API has no WebSocket is outdated. The adapter currently uses polling.

## Validation

The baseline passed 296 Python tests. After the runtime and process-control changes,
303 Python tests pass, with 10 integration tests deselected and two dependency
deprecation warnings. KIS and Toss adapter builds pass; their existing C# suites pass
11 and 13 tests respectively. A real LEAN backtest with generated prices produces
orders and fills under Python 3.11. Lockfile validation passes and `uv sync --locked
--dry-run` reports no changes.

Validation targets macOS. Docker configuration was migrated but no Docker image,
Linux runtime, Windows runtime, authenticated broker session, or account order was
tested. Passing current adapter tests does not resolve the trading findings above.
