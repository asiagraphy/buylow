# Toss paper trading setup

## Scope

Prepare automated paper trading using Toss market data. Keep real-money trading disabled and stop before starting automated trading. Broker credentials remain in the ignored `.env` file.

## Progress

- Python 3.11 project dependencies installed with `uv`.
- Toss OAuth and a real current-price request succeeded.
- Read-only commands added for prices, stock information, holdings, and buying power; regression tests pending.
- .NET 10 SDK installed; LEAN runtime preparation is in progress.
- The existing Toss adapter sends real orders. Paper execution must use a simulated brokerage instead.
- No trading strategy or symbol universe is configured. Initial virtual capital and strategy settings await user input.
- No orders have been submitted. Automated trading remains disabled.

## References

- [Toss OpenAPI specification](https://openapi.tossinvest.com/openapi-docs/latest/openapi.json)
- [Toss integration guide](https://developers.tossinvest.com/)
