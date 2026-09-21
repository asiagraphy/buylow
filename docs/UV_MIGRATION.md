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

## Trading corrections

- KIS no longer resubmits orders after ambiguous transport failures.
- Unknown final order state disables trading and prevents automatic restart.
- Toss creation retries preserve a unique idempotency key; modifications and cancellations
  do not retry ambiguous transport failures. HTTP 429 uses the actual HTTP status and Retry-After.
- Toss restores domestic open orders with remaining quantities and prior fill totals.
- Toss tracks replacement order IDs, keeps cancellation pending until confirmed, and calculates
  partial-fill prices from incremental filled amounts.
- Toss dashboard history reads OPEN and paginated CLOSED orders, grouped by order creation date.
- Minute ingestion converts Toss end timestamps to LEAN start timestamps and includes the closing auction.

## Remaining scope

- KIS open-order synchronization remains unimplemented.
- Toss paper execution is not implemented. The current adapter sends real orders.
- Authentication renewal and actual broker fills, replacements, cancellations, and recovery
  have not been validated against an account.
- Existing minute data is preserved; files created with the previous timestamp conversion
  need an explicitly scoped refresh before using them to assess intraday timing.
- Snapshot the official Toss documentation into flat `docs/toss/*.md` using the requested
  aside-browser skill, then assess which KRX data fields Toss can replace.

## Validation

The baseline passed 296 Python tests. After the runtime and process-control changes,
307 Python tests pass, with 10 integration tests deselected and two dependency
deprecation warnings. KIS and Toss adapter builds pass; their C# suites pass
11 and 19 tests respectively. Two runtime integration checks pass, including a real
LEAN backtest with generated prices that produces
orders and fills under Python 3.11. Lockfile validation passes and `uv sync --locked
--dry-run` reports no changes.

Validation targets macOS. Docker configuration was migrated but no Docker image,
Linux runtime, Windows runtime, authenticated broker session, or account order was
tested. Passing current adapter tests does not resolve the trading findings above.
