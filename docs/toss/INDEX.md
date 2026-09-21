# 토스증권 Open API 문서 색인

원본 URL: https://developers.tossinvest.com/docs

REST 문서 버전: 1.2.17 (OpenAPI 3.1.0)

웹소켓 문서 버전: 1.2.2 (AsyncAPI 3.0.0)

## 범위

- 공식 Markdown: 개요, FAQ, API 참조 색인, API 그룹 13개, 모델 문서 124개.
- REST: 33개 경로, 36개 연산, 90개 컴포넌트 스키마.
- 웹소켓: 4개 채널, 10개 연산과 모든 메시지·인라인 스키마.
- 원본 JSON 전문은 OPENAPI_SPEC.md와 ASYNCAPI_SPEC.md에 보존됩니다. JSON 내부의 `$ref`는 각 명세의 JSON Pointer이며, 모든 390개 참조 대상이 해당 원본 안에 존재합니다.
- 개요와 FAQ는 원문에 별도 버전이 없습니다.

## 원문 링크 오류

공식 `Models/AnyType.md`는 HTTP 404입니다. 해당 링크를 사용하는 ApiError.data의 실제 인라인 정의를 [MODEL_ANY_TYPE.md](MODEL_ANY_TYPE.md)에 보존했습니다. 공식 Markdown에 별도 모델 파일이 없는 OAuth2TokenRequest도 원본 명세에서 보존했습니다.

## 브라우저 문서 대응

| 문서 URL | 로컬 파일 |
|---|---|
| https://developers.tossinvest.com/docs | [OVERVIEW.md](OVERVIEW.md) |
| https://developers.tossinvest.com/docs/auth | [AUTH.md](AUTH.md) |
| https://developers.tossinvest.com/docs/market-data | [MARKET_DATA.md](MARKET_DATA.md) |
| https://developers.tossinvest.com/docs/stock-info | [STOCK_INFO.md](STOCK_INFO.md) |
| https://developers.tossinvest.com/docs/market-info | [MARKET_INFO.md](MARKET_INFO.md) |
| https://developers.tossinvest.com/docs/ranking | [RANKING.md](RANKING.md) |
| https://developers.tossinvest.com/docs/market-indicators | [MARKET_INDICATORS.md](MARKET_INDICATORS.md) |
| https://developers.tossinvest.com/docs/account | [ACCOUNT.md](ACCOUNT.md) |
| https://developers.tossinvest.com/docs/asset | [ASSET.md](ASSET.md) |
| https://developers.tossinvest.com/docs/order | [ORDER.md](ORDER.md) |
| https://developers.tossinvest.com/docs/order-history | [ORDER_HISTORY.md](ORDER_HISTORY.md) |
| https://developers.tossinvest.com/docs/order-info | [ORDER_INFO.md](ORDER_INFO.md) |
| https://developers.tossinvest.com/docs/conditional-order | [CONDITIONAL_ORDER.md](CONDITIONAL_ORDER.md) |
| https://developers.tossinvest.com/docs/conditional-order-history | [CONDITIONAL_ORDER_HISTORY.md](CONDITIONAL_ORDER_HISTORY.md) |
| https://developers.tossinvest.com/docs/connection | [CONNECTION.md](CONNECTION.md) |
| https://developers.tossinvest.com/docs/trade | [TRADE.md](TRADE.md) |
| https://developers.tossinvest.com/docs/orderbook | [ORDERBOOK.md](ORDERBOOK.md) |
| https://developers.tossinvest.com/docs/order-event | [ORDER_EVENT.md](ORDER_EVENT.md) |
| https://developers.tossinvest.com/docs/faq | [FAQ.md](FAQ.md) |

## 전체 파일 및 원본 URL

| 파일 | 원본 URL |
|---|---|
| [ACCOUNT.md](ACCOUNT.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/AccountApi.md |
| [API_REFERENCE.md](API_REFERENCE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/README.md |
| [ASSET.md](ASSET.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/AssetApi.md |
| [ASYNCAPI_SPEC.md](ASYNCAPI_SPEC.md) | https://openapi.tossinvest.com/openapi-docs/latest/asyncapi.json |
| [AUTH.md](AUTH.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/AuthApi.md |
| [CONDITIONAL_ORDER_HISTORY.md](CONDITIONAL_ORDER_HISTORY.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/ConditionalOrderHistoryApi.md |
| [CONDITIONAL_ORDER.md](CONDITIONAL_ORDER.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/ConditionalOrderApi.md |
| [CONNECTION.md](CONNECTION.md) | https://openapi.tossinvest.com/openapi-docs/latest/asyncapi.json#/channels/connection |
| [FAQ.md](FAQ.md) | https://openapi.tossinvest.com/openapi-docs/faq.md |
| [MARKET_DATA.md](MARKET_DATA.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/MarketDataApi.md |
| [MARKET_INDICATORS.md](MARKET_INDICATORS.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/MarketIndicatorsApi.md |
| [MARKET_INFO.md](MARKET_INFO.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/MarketInfoApi.md |
| [MODEL_ACCOUNT.md](MODEL_ACCOUNT.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Account.md |
| [MODEL_AFTER_MARKET_SESSION.md](MODEL_AFTER_MARKET_SESSION.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/AfterMarketSession.md |
| [MODEL_ANY_TYPE.md](MODEL_ANY_TYPE.md) | https://openapi.tossinvest.com/openapi-docs/latest/openapi.json#/components/schemas/ApiError/properties/data |
| [MODEL_API_ERROR.md](MODEL_API_ERROR.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ApiError.md |
| [MODEL_API_RESPONSE.md](MODEL_API_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ApiResponse.md |
| [MODEL_BUYING_POWER_RESPONSE.md](MODEL_BUYING_POWER_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/BuyingPowerResponse.md |
| [MODEL_CANDLE_PAGE_RESPONSE.md](MODEL_CANDLE_PAGE_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/CandlePageResponse.md |
| [MODEL_CANDLE.md](MODEL_CANDLE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Candle.md |
| [MODEL_CFD_BALANCE.md](MODEL_CFD_BALANCE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/CfdBalance.md |
| [MODEL_COMMISSION.md](MODEL_COMMISSION.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Commission.md |
| [MODEL_CONDITION_REQUEST.md](MODEL_CONDITION_REQUEST.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionRequest.md |
| [MODEL_CONDITIONAL_ORDER_CONDITION.md](MODEL_CONDITIONAL_ORDER_CONDITION.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderCondition.md |
| [MODEL_CONDITIONAL_ORDER_CREATE_REQUEST.md](MODEL_CONDITIONAL_ORDER_CREATE_REQUEST.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderCreateRequest.md |
| [MODEL_CONDITIONAL_ORDER_CREATE_RESPONSE.md](MODEL_CONDITIONAL_ORDER_CREATE_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderCreateResponse.md |
| [MODEL_CONDITIONAL_ORDER_DETAIL_RESPONSE.md](MODEL_CONDITIONAL_ORDER_DETAIL_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderDetailResponse.md |
| [MODEL_CONDITIONAL_ORDER_MODIFY_REQUEST.md](MODEL_CONDITIONAL_ORDER_MODIFY_REQUEST.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderModifyRequest.md |
| [MODEL_CONDITIONAL_ORDER_RESPONSE.md](MODEL_CONDITIONAL_ORDER_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderResponse.md |
| [MODEL_COST.md](MODEL_COST.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Cost.md |
| [MODEL_CREATE_CONDITIONAL_ORDER_200_RESPONSE.md](MODEL_CREATE_CONDITIONAL_ORDER_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/createConditionalOrder_200_response.md |
| [MODEL_CREATE_ORDER_200_RESPONSE.md](MODEL_CREATE_ORDER_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/createOrder_200_response.md |
| [MODEL_CREDIT_TRADE_DETAIL.md](MODEL_CREDIT_TRADE_DETAIL.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/CreditTradeDetail.md |
| [MODEL_CREDIT_TRADE_RECORD.md](MODEL_CREDIT_TRADE_RECORD.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/CreditTradeRecord.md |
| [MODEL_CREDIT_TRADES_RESPONSE.md](MODEL_CREDIT_TRADES_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/CreditTradesResponse.md |
| [MODEL_CURRENCY.md](MODEL_CURRENCY.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Currency.md |
| [MODEL_DAILY_PROFIT_LOSS.md](MODEL_DAILY_PROFIT_LOSS.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/DailyProfitLoss.md |
| [MODEL_ERROR_RESPONSE.md](MODEL_ERROR_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ErrorResponse.md |
| [MODEL_EXCHANGE_RATE_RESPONSE.md](MODEL_EXCHANGE_RATE_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ExchangeRateResponse.md |
| [MODEL_FOREIGNER_HOLDING.md](MODEL_FOREIGNER_HOLDING.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ForeignerHolding.md |
| [MODEL_GET_ACCOUNTS_200_RESPONSE.md](MODEL_GET_ACCOUNTS_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getAccounts_200_response.md |
| [MODEL_GET_BUYING_POWER_200_RESPONSE.md](MODEL_GET_BUYING_POWER_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getBuyingPower_200_response.md |
| [MODEL_GET_CANDLES_200_RESPONSE.md](MODEL_GET_CANDLES_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getCandles_200_response.md |
| [MODEL_GET_COMMISSIONS_200_RESPONSE.md](MODEL_GET_COMMISSIONS_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getCommissions_200_response.md |
| [MODEL_GET_CONDITIONAL_ORDER_200_RESPONSE.md](MODEL_GET_CONDITIONAL_ORDER_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getConditionalOrder_200_response.md |
| [MODEL_GET_CONDITIONAL_ORDERS_200_RESPONSE.md](MODEL_GET_CONDITIONAL_ORDERS_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getConditionalOrders_200_response.md |
| [MODEL_GET_EXCHANGE_RATE_200_RESPONSE.md](MODEL_GET_EXCHANGE_RATE_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getExchangeRate_200_response.md |
| [MODEL_GET_HOLDINGS_200_RESPONSE.md](MODEL_GET_HOLDINGS_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getHoldings_200_response.md |
| [MODEL_GET_KR_MARKET_CALENDAR_200_RESPONSE.md](MODEL_GET_KR_MARKET_CALENDAR_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getKrMarketCalendar_200_response.md |
| [MODEL_GET_MARKET_INDICATOR_CANDLES_200_RESPONSE.md](MODEL_GET_MARKET_INDICATOR_CANDLES_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getMarketIndicatorCandles_200_response.md |
| [MODEL_GET_MARKET_INDICATOR_INVESTOR_TRADING_200_RESPONSE.md](MODEL_GET_MARKET_INDICATOR_INVESTOR_TRADING_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getMarketIndicatorInvestorTrading_200_response.md |
| [MODEL_GET_MARKET_INDICATOR_PRICES_200_RESPONSE.md](MODEL_GET_MARKET_INDICATOR_PRICES_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getMarketIndicatorPrices_200_response.md |
| [MODEL_GET_ORDER_200_RESPONSE.md](MODEL_GET_ORDER_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getOrder_200_response.md |
| [MODEL_GET_ORDERBOOK_200_RESPONSE.md](MODEL_GET_ORDERBOOK_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getOrderbook_200_response.md |
| [MODEL_GET_ORDERS_200_RESPONSE.md](MODEL_GET_ORDERS_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getOrders_200_response.md |
| [MODEL_GET_PRICE_LIMIT_200_RESPONSE.md](MODEL_GET_PRICE_LIMIT_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getPriceLimit_200_response.md |
| [MODEL_GET_PRICES_200_RESPONSE.md](MODEL_GET_PRICES_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getPrices_200_response.md |
| [MODEL_GET_RANKINGS_200_RESPONSE.md](MODEL_GET_RANKINGS_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getRankings_200_response.md |
| [MODEL_GET_SELLABLE_QUANTITY_200_RESPONSE.md](MODEL_GET_SELLABLE_QUANTITY_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getSellableQuantity_200_response.md |
| [MODEL_GET_STOCK_CREDIT_TRADES_200_RESPONSE.md](MODEL_GET_STOCK_CREDIT_TRADES_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getStockCreditTrades_200_response.md |
| [MODEL_GET_STOCK_INVESTOR_TRADING_200_RESPONSE.md](MODEL_GET_STOCK_INVESTOR_TRADING_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getStockInvestorTrading_200_response.md |
| [MODEL_GET_STOCK_PROGRAM_TRADES_200_RESPONSE.md](MODEL_GET_STOCK_PROGRAM_TRADES_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getStockProgramTrades_200_response.md |
| [MODEL_GET_STOCK_SECURITIES_LENDING_200_RESPONSE.md](MODEL_GET_STOCK_SECURITIES_LENDING_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getStockSecuritiesLending_200_response.md |
| [MODEL_GET_STOCK_SHORT_SELLING_200_RESPONSE.md](MODEL_GET_STOCK_SHORT_SELLING_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getStockShortSelling_200_response.md |
| [MODEL_GET_STOCK_WARNINGS_200_RESPONSE.md](MODEL_GET_STOCK_WARNINGS_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getStockWarnings_200_response.md |
| [MODEL_GET_STOCKS_200_RESPONSE.md](MODEL_GET_STOCKS_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getStocks_200_response.md |
| [MODEL_GET_TRADES_200_RESPONSE.md](MODEL_GET_TRADES_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getTrades_200_response.md |
| [MODEL_GET_US_MARKET_CALENDAR_200_RESPONSE.md](MODEL_GET_US_MARKET_CALENDAR_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/getUsMarketCalendar_200_response.md |
| [MODEL_HOLDINGS_ITEM.md](MODEL_HOLDINGS_ITEM.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/HoldingsItem.md |
| [MODEL_HOLDINGS_OVERVIEW.md](MODEL_HOLDINGS_OVERVIEW.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/HoldingsOverview.md |
| [MODEL_INSTITUTION_TRADING_AMOUNT.md](MODEL_INSTITUTION_TRADING_AMOUNT.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InstitutionTradingAmount.md |
| [MODEL_INSTITUTION_TRADING_BREAKDOWN.md](MODEL_INSTITUTION_TRADING_BREAKDOWN.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InstitutionTradingBreakdown.md |
| [MODEL_INTEGRATED_HOUR.md](MODEL_INTEGRATED_HOUR.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/IntegratedHour.md |
| [MODEL_INVESTOR_TRADING_AMOUNT.md](MODEL_INVESTOR_TRADING_AMOUNT.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InvestorTradingAmount.md |
| [MODEL_INVESTOR_TRADING_RECORD.md](MODEL_INVESTOR_TRADING_RECORD.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InvestorTradingRecord.md |
| [MODEL_INVESTOR_TRADING_RESPONSE.md](MODEL_INVESTOR_TRADING_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InvestorTradingResponse.md |
| [MODEL_INVESTOR_TRADING_VOLUME.md](MODEL_INVESTOR_TRADING_VOLUME.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InvestorTradingVolume.md |
| [MODEL_KR_MARKET_CALENDAR_RESPONSE.md](MODEL_KR_MARKET_CALENDAR_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/KrMarketCalendarResponse.md |
| [MODEL_KR_MARKET_DAY.md](MODEL_KR_MARKET_DAY.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/KrMarketDay.md |
| [MODEL_KR_MARKET_DETAIL.md](MODEL_KR_MARKET_DETAIL.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/KrMarketDetail.md |
| [MODEL_LIST_STOCKS_200_RESPONSE.md](MODEL_LIST_STOCKS_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/listStocks_200_response.md |
| [MODEL_LISTED_STOCK.md](MODEL_LISTED_STOCK.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ListedStock.md |
| [MODEL_MARKET_COUNTRY.md](MODEL_MARKET_COUNTRY.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/MarketCountry.md |
| [MODEL_MARKET_INDICATOR_CANDLE_PAGE_RESPONSE.md](MODEL_MARKET_INDICATOR_CANDLE_PAGE_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/MarketIndicatorCandlePageResponse.md |
| [MODEL_MARKET_INDICATOR_CANDLE.md](MODEL_MARKET_INDICATOR_CANDLE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/MarketIndicatorCandle.md |
| [MODEL_MARKET_INDICATOR_PRICE_RESPONSE.md](MODEL_MARKET_INDICATOR_PRICE_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/MarketIndicatorPriceResponse.md |
| [MODEL_MARKET_VALUE.md](MODEL_MARKET_VALUE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/MarketValue.md |
| [MODEL_MODIFY_CONDITIONAL_ORDER_200_RESPONSE.md](MODEL_MODIFY_CONDITIONAL_ORDER_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/modifyConditionalOrder_200_response.md |
| [MODEL_MODIFY_ORDER_200_RESPONSE.md](MODEL_MODIFY_ORDER_200_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/modifyOrder_200_response.md |
| [MODEL_O_AUTH2_ERROR_RESPONSE.md](MODEL_O_AUTH2_ERROR_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OAuth2ErrorResponse.md |
| [MODEL_O_AUTH2_TOKEN_REQUEST.md](MODEL_O_AUTH2_TOKEN_REQUEST.md) | https://openapi.tossinvest.com/openapi-docs/latest/openapi.json#/components/schemas/OAuth2TokenRequest |
| [MODEL_O_AUTH2_TOKEN_RESPONSE.md](MODEL_O_AUTH2_TOKEN_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OAuth2TokenResponse.md |
| [MODEL_ORDER_CREATE_AMOUNT_BASED.md](MODEL_ORDER_CREATE_AMOUNT_BASED.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderCreateAmountBased.md |
| [MODEL_ORDER_CREATE_QUANTITY_BASED.md](MODEL_ORDER_CREATE_QUANTITY_BASED.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderCreateQuantityBased.md |
| [MODEL_ORDER_CREATE_REQUEST.md](MODEL_ORDER_CREATE_REQUEST.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderCreateRequest.md |
| [MODEL_ORDER_EXECUTION.md](MODEL_ORDER_EXECUTION.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderExecution.md |
| [MODEL_ORDER_MODIFY_REQUEST.md](MODEL_ORDER_MODIFY_REQUEST.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderModifyRequest.md |
| [MODEL_ORDER_OPERATION_RESPONSE.md](MODEL_ORDER_OPERATION_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderOperationResponse.md |
| [MODEL_ORDER_RESPONSE.md](MODEL_ORDER_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderResponse.md |
| [MODEL_ORDER_STATUS.md](MODEL_ORDER_STATUS.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderStatus.md |
| [MODEL_ORDER.md](MODEL_ORDER.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Order.md |
| [MODEL_ORDERBOOK_ENTRY.md](MODEL_ORDERBOOK_ENTRY.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderbookEntry.md |
| [MODEL_ORDERBOOK_RESPONSE.md](MODEL_ORDERBOOK_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderbookResponse.md |
| [MODEL_OVERVIEW_DAILY_PROFIT_LOSS.md](MODEL_OVERVIEW_DAILY_PROFIT_LOSS.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OverviewDailyProfitLoss.md |
| [MODEL_OVERVIEW_MARKET_VALUE.md](MODEL_OVERVIEW_MARKET_VALUE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OverviewMarketValue.md |
| [MODEL_OVERVIEW_PROFIT_LOSS.md](MODEL_OVERVIEW_PROFIT_LOSS.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OverviewProfitLoss.md |
| [MODEL_PAGINATED_CONDITIONAL_ORDER_RESPONSE.md](MODEL_PAGINATED_CONDITIONAL_ORDER_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/PaginatedConditionalOrderResponse.md |
| [MODEL_PAGINATED_ORDER_RESPONSE.md](MODEL_PAGINATED_ORDER_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/PaginatedOrderResponse.md |
| [MODEL_PRE_MARKET_SESSION.md](MODEL_PRE_MARKET_SESSION.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/PreMarketSession.md |
| [MODEL_PRICE_LIMIT_RESPONSE.md](MODEL_PRICE_LIMIT_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/PriceLimitResponse.md |
| [MODEL_PRICE_RESPONSE.md](MODEL_PRICE_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/PriceResponse.md |
| [MODEL_PRICE.md](MODEL_PRICE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Price.md |
| [MODEL_PROFIT_LOSS.md](MODEL_PROFIT_LOSS.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ProfitLoss.md |
| [MODEL_PROGRAM_TRADE_RECORD.md](MODEL_PROGRAM_TRADE_RECORD.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ProgramTradeRecord.md |
| [MODEL_PROGRAM_TRADES_RESPONSE.md](MODEL_PROGRAM_TRADES_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ProgramTradesResponse.md |
| [MODEL_PROGRAM_TRADING_VOLUME.md](MODEL_PROGRAM_TRADING_VOLUME.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ProgramTradingVolume.md |
| [MODEL_RANKING_ITEM.md](MODEL_RANKING_ITEM.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/RankingItem.md |
| [MODEL_RANKING_PRICE.md](MODEL_RANKING_PRICE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/RankingPrice.md |
| [MODEL_RANKING_RESPONSE.md](MODEL_RANKING_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/RankingResponse.md |
| [MODEL_REGULAR_MARKET_SESSION.md](MODEL_REGULAR_MARKET_SESSION.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/RegularMarketSession.md |
| [MODEL_SECURITIES_LENDING_RECORD.md](MODEL_SECURITIES_LENDING_RECORD.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/SecuritiesLendingRecord.md |
| [MODEL_SECURITIES_LENDING_RESPONSE.md](MODEL_SECURITIES_LENDING_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/SecuritiesLendingResponse.md |
| [MODEL_SELLABLE_QUANTITY_RESPONSE.md](MODEL_SELLABLE_QUANTITY_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/SellableQuantityResponse.md |
| [MODEL_SHORT_SELLING_RECORD.md](MODEL_SHORT_SELLING_RECORD.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ShortSellingRecord.md |
| [MODEL_SHORT_SELLING_RESPONSE.md](MODEL_SHORT_SELLING_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ShortSellingResponse.md |
| [MODEL_STOCK_INFO.md](MODEL_STOCK_INFO.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockInfo.md |
| [MODEL_STOCK_INSTITUTION_TRADING_BREAKDOWN.md](MODEL_STOCK_INSTITUTION_TRADING_BREAKDOWN.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockInstitutionTradingBreakdown.md |
| [MODEL_STOCK_INSTITUTION_TRADING_VOLUME.md](MODEL_STOCK_INSTITUTION_TRADING_VOLUME.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockInstitutionTradingVolume.md |
| [MODEL_STOCK_INVESTOR_TRADING_RECORD.md](MODEL_STOCK_INVESTOR_TRADING_RECORD.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockInvestorTradingRecord.md |
| [MODEL_STOCK_INVESTOR_TRADING_RESPONSE.md](MODEL_STOCK_INVESTOR_TRADING_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockInvestorTradingResponse.md |
| [MODEL_STOCK_WARNING.md](MODEL_STOCK_WARNING.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockWarning.md |
| [MODEL_TRADE.md](MODEL_TRADE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Trade.md |
| [MODEL_US_AFTER_MARKET_SESSION.md](MODEL_US_AFTER_MARKET_SESSION.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/UsAfterMarketSession.md |
| [MODEL_US_DAY_MARKET_SESSION.md](MODEL_US_DAY_MARKET_SESSION.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/UsDayMarketSession.md |
| [MODEL_US_MARKET_CALENDAR_RESPONSE.md](MODEL_US_MARKET_CALENDAR_RESPONSE.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/UsMarketCalendarResponse.md |
| [MODEL_US_MARKET_DAY.md](MODEL_US_MARKET_DAY.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/UsMarketDay.md |
| [MODEL_US_PRE_MARKET_SESSION.md](MODEL_US_PRE_MARKET_SESSION.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/UsPreMarketSession.md |
| [MODEL_US_REGULAR_MARKET_SESSION.md](MODEL_US_REGULAR_MARKET_SESSION.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/UsRegularMarketSession.md |
| [OPENAPI_SPEC.md](OPENAPI_SPEC.md) | https://openapi.tossinvest.com/openapi-docs/latest/openapi.json |
| [ORDER_EVENT.md](ORDER_EVENT.md) | https://openapi.tossinvest.com/openapi-docs/latest/asyncapi.json#/channels/realtime-order |
| [ORDER_HISTORY.md](ORDER_HISTORY.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/OrderHistoryApi.md |
| [ORDER_INFO.md](ORDER_INFO.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/OrderInfoApi.md |
| [ORDER.md](ORDER.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/OrderApi.md |
| [ORDERBOOK.md](ORDERBOOK.md) | https://openapi.tossinvest.com/openapi-docs/latest/asyncapi.json#/channels/realtime-orderbook |
| [OVERVIEW.md](OVERVIEW.md) | https://openapi.tossinvest.com/openapi-docs/overview.md |
| [RANKING.md](RANKING.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/RankingApi.md |
| [REST_DEFINITIONS.md](REST_DEFINITIONS.md) | https://openapi.tossinvest.com/openapi-docs/latest/openapi.json#/components |
| [STOCK_INFO.md](STOCK_INFO.md) | https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/StockInfoApi.md |
| [TRADE.md](TRADE.md) | https://openapi.tossinvest.com/openapi-docs/latest/asyncapi.json#/channels/realtime-trade |
| [INDEX.md](INDEX.md) | https://developers.tossinvest.com/docs |
