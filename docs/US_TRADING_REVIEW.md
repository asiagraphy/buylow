# US trading implementation record

## Contract

Implement overseas-only short-horizon strategies for a one-week KIS demo experiment,
then add US trading support alongside the existing domestic workflow. After strategy
and execution validation, update README with beginner-friendly, one-line commands for
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
  prefix-conversion code; resolve the contract before implementing order submission.

## Strategy decisions

Two selectable rules share risk sizing and execution controls: intraday momentum and
opening-range breakout. Both are long-only US equities, use completed one-minute regular
session bars, require volume and liquidity, and cap holding time. Candidate stocks are a
starting scan list, not a forecast of the highest-returning stocks. Estimated costs are
explicit configurable assumptions. No weekly return has been measured or promised.

## Progress

Pure signal, sizing, and exit logic is written. Strategy tests, shared API pacing,
US account/order integration, replay validation, and the README guide are pending.
