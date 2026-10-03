# US trading implementation record

## Contract

Implement overseas-only short-horizon strategies for a one-week KIS demo experiment,
then add US trading support alongside the existing domestic workflow. Update README
with beginner-friendly, one-line commands for
configuration, strategy selection, demo trading, and explicit real-account operation.
Do not submit account orders during implementation. Existing credentials stay in ignored
local files and must never enter this record or test fixtures.

## Research

- [Alpaca concurrent scalping](https://github.com/alpacahq/example-scalping/tree/4d0962785e272a01fcb4c89f0e961264e9a91827):
  minute events, limit entries, pending-order state, and stale-entry cancellation are useful.
  The original one-cent exit and indefinite sell wait are unsuitable for uncertain KIS costs.
  No explicit repository license was identified; implementation uses the general ideas,
  not copied source or an Alpaca runtime dependency.
- [QuantConnect EMA alpha](https://github.com/QuantConnect/Lean/blob/985ef30ad3ac774218c5ac516b4cb0aa2655730f/Algorithm.Framework/Alphas/EmaCrossAlphaModel.py):
  ready indicators and transition-based signals inform the trend filter. This does not
  establish profitability for the chosen week or stock universe.
- [Community opening-range bot](https://github.com/afletch117/TradingBotAugustineFiveMinOpeningRangeBreakout/tree/c699d0cceb58098c578a71d07ba7981fd8529ab9):
  README explicitly calls the bot incomplete; it is not an execution implementation source.
- [KIS overseas order example](https://github.com/koreainvestment/open-trading-api/blob/b4e6249714418aa57833d1cbbbced39cbcc5b125/examples_llm/overseas_stock/order/order.py):
  US demo orders are limit-only. Its demo sell TR-ID comment conflicts with its generated
  prefix-conversion code. The official paper Postman sample and order documentation use
  `VTTT1001U` for US paper sells, not the generated `VTTT1006U`. The implementation uses
  explicit IDs: paper buy/sell `VTTT1002U` / `VTTT1001U`, real buy/sell `TTTT1002U` /
  `TTTT1006U`. Reference: `legacy/postman/모의계좌_POSTMAN_샘플코드_v1.6.json` in that same clone.

## Strategy decisions

### Automatic candidate discovery

Use KIS price-fluctuation and volume-surge first-page rankings for NASDAQ, NYSE, and
AMEX as a bounded candidate source, not an exhaustive whole-market feed. Refresh every
five minutes during regular hours after 22 completed minutes. Require positive momentum,
liquidity, and tradable spreads before cross-sectional percentile ranking. Preserve
positions and pending orders independently of changing candidates. A failed or expired
snapshot blocks new entries, not position management. Process one ranking request per
runner cycle after exits, and rotate minute-data checks to avoid a large synchronous scan.
Keep selection history and source scores for inspection; CSV replay remains fixed-universe
and must not be described as a historical test of this live discovery policy.

Two selectable rules share risk sizing and execution controls: intraday momentum and
opening-range breakout. Both are long-only US equities, use completed one-minute regular
session bars, require volume and liquidity, and cap holding time. Candidate stocks are a
starting scan list, not a forecast of the highest-returning stocks. Estimated costs are
explicit configurable assumptions. No weekly return has been measured or promised.

## Implemented scope

- `orchestrator/us_strategy.py`: completed-bar momentum and opening-range rules, cost-aware
  sizing and targets, position limits, timed exits, and daily/trial loss triggers.
- `market/us.py`: New York sessions, holidays, daylight saving time, and early closes.
- `brokers/kis_us.py`: separate demo/real hosts and credentials, USD account reads, minute
  bars and quotes, limit orders/cancellation, pagination, token caching, and shared pacing.
- `orchestrator/us_runner.py`: persistent order intents, cumulative partial fills, cancellation
  confirmation, restart reconciliation, ambiguous-order stops, and bounded experiments.
- `orchestrator/us_replay.py`: the same runner against CSV bars, subsequent-bar limit fills,
  volume participation limits, and estimated transaction costs.
- `orchestrator/us.py`: masked credential setup, local/online diagnostics, strategy selection,
  run/status, history download, and replay.
- `orchestrator/us_dashboard.py`: the `/us` web page selects presets, starts the existing
  CLI, requests interruption, and displays saved holdings, orders, fills, and estimated
  results. It defaults to demo, requires explicit real-order consent and a form token,
  and does not automatically restart trading. The root page redirects to `/us`.
- README in Korean, English, and Japanese: macOS setup, one-line commands, paper/real
  separation, strategy rules, stop/resume behavior, results, and troubleshooting.
- `.env.example`: supported credential and operational fields, with optional settings
  commented out and no actual credentials.

## Verification boundary

Transient query transport/HTTP failures are distinct from uncertain order outcomes.
The live loop keeps its runner and order identities, pauses new decisions, and retries
with backoff. Endpoint, exception class, attempt, and next retry time are persisted without
credentials or response bodies. Permanent account errors and ambiguous POST outcomes
still stop execution. A targeted run of 29 tests covered the broker, actual runner recovery,
dashboard, and order-uncertainty behavior; the recovery test observes a failed bar request,
a subsequent successful request, and exactly one order intent without reconstructing the
runner. Account-level order and fill validation remains separate.

Automatic discovery has 39 passing targeted tests across universe selection, the shared
runner, dashboard, CLI, broker, and CSV replay. They cover factor ordering, liquidity and
instrument-name filters, retention, incremental collection, expiry/failure, restart gating,
and exits for holdings removed from the candidate list. Six authenticated ranking reads
succeeded across the three US exchanges. An outside-session read produced no qualifying
candidates; filters were not relaxed to manufacture a selection. Full live order/fill
behavior and the automatic selection policy's profitability remain unverified.

The dashboard integration completed with 58 passing targeted dashboard tests. Coverage
includes preset selection, no trading on GET/save, form-token checks, explicit real-mode
consent, duplicate-start rejection, stop signals, saved result rendering, and a real local
child process stopping without broker requests. Browser rendering uses synthetic state;
no account order is submitted by the visual check.

The latest targeted offline run completed with 36 passing tests across US strategy,
broker, runner, replay, and CLI modules. The CLI replay test runs the actual command on
synthetic bars and reads its output. An earlier full suite completed with 341 passing and
10 deselected tests; that earlier run does not cover subsequent US changes. These checks
do not measure real-market performance or establish broker-account compatibility.

Authenticated demo market-data requests succeeded for price/volume rankings and quotes.
An initial balance request returned `OPSQ2000 / INPUT INVALID_CHECK_ACNO`; subsequent
account correction and authentication allowed demo balance/order reads and a waiting
runner to start. No paper or real orders were submitted in those checks. The live quote
response exposed a timestamp interpretation bug:
the one-level quote's `dymd/dhms` uses Korean time, unlike the minute bar's local date/time.
The quote parser now converts from Asia/Seoul to New York. Targeted broker tests cover
summer time and winter date rollover. History availability, order rejection, partial
fills, cancellation, and restart recovery remain unverified against an account.
Additional runtime verification is deferred. Limit-order exits do not guarantee flat
positions by the close or compliance with the numerical loss triggers. The README
distinguishes this boundary from the implemented execution path.

The existing Korean-equity LEAN workflow remains separate. Its account-level verification
and KIS restart open-order synchronization are not completed by the US implementation.
