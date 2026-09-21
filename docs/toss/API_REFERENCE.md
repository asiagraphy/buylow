> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/README.md
> 문서 버전: 1.2.17

# Documentation for 토스증권 Open API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://openapi.tossinvest.com*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *AccountApi* | [**getAccounts**](ACCOUNT.md#getAccounts) | **GET** /api/v1/accounts | 계좌 목록 조회 |
| *AssetApi* | [**getHoldings**](ASSET.md#getHoldings) | **GET** /api/v1/holdings | 보유 주식 조회 |
| *AuthApi* | [**issueOAuth2Token**](AUTH.md#issueOAuth2Token) | **POST** /oauth2/token | OAuth2 액세스 토큰 발급 |
| *ConditionalOrderApi* | [**cancelConditionalOrder**](CONDITIONAL_ORDER.md#cancelConditionalOrder) | **DELETE** /api/v1/conditional-orders/{conditionalOrderId} | 조건주문 취소 |
| *ConditionalOrderApi* | [**createConditionalOrder**](CONDITIONAL_ORDER.md#createConditionalOrder) | **POST** /api/v1/conditional-orders | 조건주문 생성 |
| *ConditionalOrderApi* | [**modifyConditionalOrder**](CONDITIONAL_ORDER.md#modifyConditionalOrder) | **POST** /api/v1/conditional-orders/{conditionalOrderId}/modify | 조건주문 수정 |
| *ConditionalOrderHistoryApi* | [**getConditionalOrder**](CONDITIONAL_ORDER_HISTORY.md#getConditionalOrder) | **GET** /api/v1/conditional-orders/{conditionalOrderId} | 조건주문 상세 조회 |
| *ConditionalOrderHistoryApi* | [**getConditionalOrders**](CONDITIONAL_ORDER_HISTORY.md#getConditionalOrders) | **GET** /api/v1/conditional-orders | 조건주문 목록 조회 |
| *MarketDataApi* | [**getCandles**](MARKET_DATA.md#getCandles) | **GET** /api/v1/candles | 캔들 차트 조회 |
| *MarketDataApi* | [**getOrderbook**](MARKET_DATA.md#getOrderbook) | **GET** /api/v1/orderbook | 호가 조회 |
| *MarketDataApi* | [**getPriceLimit**](MARKET_DATA.md#getPriceLimit) | **GET** /api/v1/price-limits | 상/하한가 조회 |
| *MarketDataApi* | [**getPrices**](MARKET_DATA.md#getPrices) | **GET** /api/v1/prices | 현재가 조회 |
| *MarketDataApi* | [**getTrades**](MARKET_DATA.md#getTrades) | **GET** /api/v1/trades | 최근 체결 내역 조회 |
| *MarketIndicatorsApi* | [**getMarketIndicatorCandles**](MARKET_INDICATORS.md#getMarketIndicatorCandles) | **GET** /api/v1/market-indicators/{symbol}/candles | 시장 지표 캔들 차트 조회 |
| *MarketIndicatorsApi* | [**getMarketIndicatorInvestorTrading**](MARKET_INDICATORS.md#getMarketIndicatorInvestorTrading) | **GET** /api/v1/market-indicators/{symbol}/investor-trading | 투자자별 매매대금 조회 |
| *MarketIndicatorsApi* | [**getMarketIndicatorPrices**](MARKET_INDICATORS.md#getMarketIndicatorPrices) | **GET** /api/v1/market-indicators/prices | 시장 지표 현재가 조회 |
| *MarketInfoApi* | [**getExchangeRate**](MARKET_INFO.md#getExchangeRate) | **GET** /api/v1/exchange-rate | 환율 조회 |
| *MarketInfoApi* | [**getKrMarketCalendar**](MARKET_INFO.md#getKrMarketCalendar) | **GET** /api/v1/market-calendar/KR | 국내 장 운영 정보 조회 |
| *MarketInfoApi* | [**getUsMarketCalendar**](MARKET_INFO.md#getUsMarketCalendar) | **GET** /api/v1/market-calendar/US | 해외 장 운영 정보 조회 |
| *OrderApi* | [**cancelOrder**](ORDER.md#cancelOrder) | **POST** /api/v1/orders/{orderId}/cancel | 주문 취소 |
| *OrderApi* | [**createOrder**](ORDER.md#createOrder) | **POST** /api/v1/orders | 주문 생성 |
| *OrderApi* | [**modifyOrder**](ORDER.md#modifyOrder) | **POST** /api/v1/orders/{orderId}/modify | 주문 정정 |
| *OrderHistoryApi* | [**getOrder**](ORDER_HISTORY.md#getOrder) | **GET** /api/v1/orders/{orderId} | 주문 상세 조회 |
| *OrderHistoryApi* | [**getOrders**](ORDER_HISTORY.md#getOrders) | **GET** /api/v1/orders | 주문 목록 조회 |
| *OrderInfoApi* | [**getBuyingPower**](ORDER_INFO.md#getBuyingPower) | **GET** /api/v1/buying-power | 매수 가능 금액 조회 |
| *OrderInfoApi* | [**getCommissions**](ORDER_INFO.md#getCommissions) | **GET** /api/v1/commissions | 매매 수수료 조회 |
| *OrderInfoApi* | [**getSellableQuantity**](ORDER_INFO.md#getSellableQuantity) | **GET** /api/v1/sellable-quantity | 판매 가능 수량 조회 |
| *RankingApi* | [**getRankings**](RANKING.md#getRankings) | **GET** /api/v1/rankings | 주식 랭킹 조회 |
| *StockInfoApi* | [**getStockCreditTrades**](STOCK_INFO.md#getStockCreditTrades) | **GET** /api/v1/stocks/{symbol}/credit-trades | 신용거래 동향 조회 |
| *StockInfoApi* | [**getStockInvestorTrading**](STOCK_INFO.md#getStockInvestorTrading) | **GET** /api/v1/stocks/{symbol}/investor-trading | 투자자별 매매동향 조회 |
| *StockInfoApi* | [**getStockProgramTrades**](STOCK_INFO.md#getStockProgramTrades) | **GET** /api/v1/stocks/{symbol}/program-trades | 프로그램매매 동향 조회 |
| *StockInfoApi* | [**getStockSecuritiesLending**](STOCK_INFO.md#getStockSecuritiesLending) | **GET** /api/v1/stocks/{symbol}/securities-lending | 대차거래 동향 조회 |
| *StockInfoApi* | [**getStockShortSelling**](STOCK_INFO.md#getStockShortSelling) | **GET** /api/v1/stocks/{symbol}/short-selling | 공매도 동향 조회 |
| *StockInfoApi* | [**getStockWarnings**](STOCK_INFO.md#getStockWarnings) | **GET** /api/v1/stocks/{symbol}/warnings | 매수 유의사항 조회 |
| *StockInfoApi* | [**getStocks**](STOCK_INFO.md#getStocks) | **GET** /api/v1/stocks | 종목 기본 정보 조회 |
| *StockInfoApi* | [**listStocks**](STOCK_INFO.md#listStocks) | **GET** /api/v1/stocks/all | 마켓별 전체 종목 조회 |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [Account](MODEL_ACCOUNT.md)
 - [AfterMarketSession](MODEL_AFTER_MARKET_SESSION.md)
 - [ApiError](MODEL_API_ERROR.md)
 - [ApiResponse](MODEL_API_RESPONSE.md)
 - [BuyingPowerResponse](MODEL_BUYING_POWER_RESPONSE.md)
 - [Candle](MODEL_CANDLE.md)
 - [CandlePageResponse](MODEL_CANDLE_PAGE_RESPONSE.md)
 - [CfdBalance](MODEL_CFD_BALANCE.md)
 - [Commission](MODEL_COMMISSION.md)
 - [ConditionRequest](MODEL_CONDITION_REQUEST.md)
 - [ConditionalOrderCondition](MODEL_CONDITIONAL_ORDER_CONDITION.md)
 - [ConditionalOrderCreateRequest](MODEL_CONDITIONAL_ORDER_CREATE_REQUEST.md)
 - [ConditionalOrderCreateResponse](MODEL_CONDITIONAL_ORDER_CREATE_RESPONSE.md)
 - [ConditionalOrderDetailResponse](MODEL_CONDITIONAL_ORDER_DETAIL_RESPONSE.md)
 - [ConditionalOrderModifyRequest](MODEL_CONDITIONAL_ORDER_MODIFY_REQUEST.md)
 - [ConditionalOrderResponse](MODEL_CONDITIONAL_ORDER_RESPONSE.md)
 - [Cost](MODEL_COST.md)
 - [CreditTradeDetail](MODEL_CREDIT_TRADE_DETAIL.md)
 - [CreditTradeRecord](MODEL_CREDIT_TRADE_RECORD.md)
 - [CreditTradesResponse](MODEL_CREDIT_TRADES_RESPONSE.md)
 - [Currency](MODEL_CURRENCY.md)
 - [DailyProfitLoss](MODEL_DAILY_PROFIT_LOSS.md)
 - [ErrorResponse](MODEL_ERROR_RESPONSE.md)
 - [ExchangeRateResponse](MODEL_EXCHANGE_RATE_RESPONSE.md)
 - [ForeignerHolding](MODEL_FOREIGNER_HOLDING.md)
 - [HoldingsItem](MODEL_HOLDINGS_ITEM.md)
 - [HoldingsOverview](MODEL_HOLDINGS_OVERVIEW.md)
 - [InstitutionTradingAmount](MODEL_INSTITUTION_TRADING_AMOUNT.md)
 - [InstitutionTradingBreakdown](MODEL_INSTITUTION_TRADING_BREAKDOWN.md)
 - [IntegratedHour](MODEL_INTEGRATED_HOUR.md)
 - [InvestorTradingAmount](MODEL_INVESTOR_TRADING_AMOUNT.md)
 - [InvestorTradingRecord](MODEL_INVESTOR_TRADING_RECORD.md)
 - [InvestorTradingResponse](MODEL_INVESTOR_TRADING_RESPONSE.md)
 - [InvestorTradingVolume](MODEL_INVESTOR_TRADING_VOLUME.md)
 - [KrMarketCalendarResponse](MODEL_KR_MARKET_CALENDAR_RESPONSE.md)
 - [KrMarketDay](MODEL_KR_MARKET_DAY.md)
 - [KrMarketDetail](MODEL_KR_MARKET_DETAIL.md)
 - [ListedStock](MODEL_LISTED_STOCK.md)
 - [MarketCountry](MODEL_MARKET_COUNTRY.md)
 - [MarketIndicatorCandle](MODEL_MARKET_INDICATOR_CANDLE.md)
 - [MarketIndicatorCandlePageResponse](MODEL_MARKET_INDICATOR_CANDLE_PAGE_RESPONSE.md)
 - [MarketIndicatorPriceResponse](MODEL_MARKET_INDICATOR_PRICE_RESPONSE.md)
 - [MarketValue](MODEL_MARKET_VALUE.md)
 - [OAuth2ErrorResponse](MODEL_O_AUTH2_ERROR_RESPONSE.md)
 - [OAuth2TokenResponse](MODEL_O_AUTH2_TOKEN_RESPONSE.md)
 - [Order](MODEL_ORDER.md)
 - [OrderCreateAmountBased](MODEL_ORDER_CREATE_AMOUNT_BASED.md)
 - [OrderCreateQuantityBased](MODEL_ORDER_CREATE_QUANTITY_BASED.md)
 - [OrderCreateRequest](MODEL_ORDER_CREATE_REQUEST.md)
 - [OrderExecution](MODEL_ORDER_EXECUTION.md)
 - [OrderModifyRequest](MODEL_ORDER_MODIFY_REQUEST.md)
 - [OrderOperationResponse](MODEL_ORDER_OPERATION_RESPONSE.md)
 - [OrderResponse](MODEL_ORDER_RESPONSE.md)
 - [OrderStatus](MODEL_ORDER_STATUS.md)
 - [OrderbookEntry](MODEL_ORDERBOOK_ENTRY.md)
 - [OrderbookResponse](MODEL_ORDERBOOK_RESPONSE.md)
 - [OverviewDailyProfitLoss](MODEL_OVERVIEW_DAILY_PROFIT_LOSS.md)
 - [OverviewMarketValue](MODEL_OVERVIEW_MARKET_VALUE.md)
 - [OverviewProfitLoss](MODEL_OVERVIEW_PROFIT_LOSS.md)
 - [PaginatedConditionalOrderResponse](MODEL_PAGINATED_CONDITIONAL_ORDER_RESPONSE.md)
 - [PaginatedOrderResponse](MODEL_PAGINATED_ORDER_RESPONSE.md)
 - [PreMarketSession](MODEL_PRE_MARKET_SESSION.md)
 - [Price](MODEL_PRICE.md)
 - [PriceLimitResponse](MODEL_PRICE_LIMIT_RESPONSE.md)
 - [PriceResponse](MODEL_PRICE_RESPONSE.md)
 - [ProfitLoss](MODEL_PROFIT_LOSS.md)
 - [ProgramTradeRecord](MODEL_PROGRAM_TRADE_RECORD.md)
 - [ProgramTradesResponse](MODEL_PROGRAM_TRADES_RESPONSE.md)
 - [ProgramTradingVolume](MODEL_PROGRAM_TRADING_VOLUME.md)
 - [RankingItem](MODEL_RANKING_ITEM.md)
 - [RankingPrice](MODEL_RANKING_PRICE.md)
 - [RankingResponse](MODEL_RANKING_RESPONSE.md)
 - [RegularMarketSession](MODEL_REGULAR_MARKET_SESSION.md)
 - [SecuritiesLendingRecord](MODEL_SECURITIES_LENDING_RECORD.md)
 - [SecuritiesLendingResponse](MODEL_SECURITIES_LENDING_RESPONSE.md)
 - [SellableQuantityResponse](MODEL_SELLABLE_QUANTITY_RESPONSE.md)
 - [ShortSellingRecord](MODEL_SHORT_SELLING_RECORD.md)
 - [ShortSellingResponse](MODEL_SHORT_SELLING_RESPONSE.md)
 - [StockInfo](MODEL_STOCK_INFO.md)
 - [StockInstitutionTradingBreakdown](MODEL_STOCK_INSTITUTION_TRADING_BREAKDOWN.md)
 - [StockInstitutionTradingVolume](MODEL_STOCK_INSTITUTION_TRADING_VOLUME.md)
 - [StockInvestorTradingRecord](MODEL_STOCK_INVESTOR_TRADING_RECORD.md)
 - [StockInvestorTradingResponse](MODEL_STOCK_INVESTOR_TRADING_RESPONSE.md)
 - [StockWarning](MODEL_STOCK_WARNING.md)
 - [Trade](MODEL_TRADE.md)
 - [UsAfterMarketSession](MODEL_US_AFTER_MARKET_SESSION.md)
 - [UsDayMarketSession](MODEL_US_DAY_MARKET_SESSION.md)
 - [UsMarketCalendarResponse](MODEL_US_MARKET_CALENDAR_RESPONSE.md)
 - [UsMarketDay](MODEL_US_MARKET_DAY.md)
 - [UsPreMarketSession](MODEL_US_PRE_MARKET_SESSION.md)
 - [UsRegularMarketSession](MODEL_US_REGULAR_MARKET_SESSION.md)
 - [createConditionalOrder_200_response](MODEL_CREATE_CONDITIONAL_ORDER_200_RESPONSE.md)
 - [createOrder_200_response](MODEL_CREATE_ORDER_200_RESPONSE.md)
 - [getAccounts_200_response](MODEL_GET_ACCOUNTS_200_RESPONSE.md)
 - [getBuyingPower_200_response](MODEL_GET_BUYING_POWER_200_RESPONSE.md)
 - [getCandles_200_response](MODEL_GET_CANDLES_200_RESPONSE.md)
 - [getCommissions_200_response](MODEL_GET_COMMISSIONS_200_RESPONSE.md)
 - [getConditionalOrder_200_response](MODEL_GET_CONDITIONAL_ORDER_200_RESPONSE.md)
 - [getConditionalOrders_200_response](MODEL_GET_CONDITIONAL_ORDERS_200_RESPONSE.md)
 - [getExchangeRate_200_response](MODEL_GET_EXCHANGE_RATE_200_RESPONSE.md)
 - [getHoldings_200_response](MODEL_GET_HOLDINGS_200_RESPONSE.md)
 - [getKrMarketCalendar_200_response](MODEL_GET_KR_MARKET_CALENDAR_200_RESPONSE.md)
 - [getMarketIndicatorCandles_200_response](MODEL_GET_MARKET_INDICATOR_CANDLES_200_RESPONSE.md)
 - [getMarketIndicatorInvestorTrading_200_response](MODEL_GET_MARKET_INDICATOR_INVESTOR_TRADING_200_RESPONSE.md)
 - [getMarketIndicatorPrices_200_response](MODEL_GET_MARKET_INDICATOR_PRICES_200_RESPONSE.md)
 - [getOrder_200_response](MODEL_GET_ORDER_200_RESPONSE.md)
 - [getOrderbook_200_response](MODEL_GET_ORDERBOOK_200_RESPONSE.md)
 - [getOrders_200_response](MODEL_GET_ORDERS_200_RESPONSE.md)
 - [getPriceLimit_200_response](MODEL_GET_PRICE_LIMIT_200_RESPONSE.md)
 - [getPrices_200_response](MODEL_GET_PRICES_200_RESPONSE.md)
 - [getRankings_200_response](MODEL_GET_RANKINGS_200_RESPONSE.md)
 - [getSellableQuantity_200_response](MODEL_GET_SELLABLE_QUANTITY_200_RESPONSE.md)
 - [getStockCreditTrades_200_response](MODEL_GET_STOCK_CREDIT_TRADES_200_RESPONSE.md)
 - [getStockInvestorTrading_200_response](MODEL_GET_STOCK_INVESTOR_TRADING_200_RESPONSE.md)
 - [getStockProgramTrades_200_response](MODEL_GET_STOCK_PROGRAM_TRADES_200_RESPONSE.md)
 - [getStockSecuritiesLending_200_response](MODEL_GET_STOCK_SECURITIES_LENDING_200_RESPONSE.md)
 - [getStockShortSelling_200_response](MODEL_GET_STOCK_SHORT_SELLING_200_RESPONSE.md)
 - [getStockWarnings_200_response](MODEL_GET_STOCK_WARNINGS_200_RESPONSE.md)
 - [getStocks_200_response](MODEL_GET_STOCKS_200_RESPONSE.md)
 - [getTrades_200_response](MODEL_GET_TRADES_200_RESPONSE.md)
 - [getUsMarketCalendar_200_response](MODEL_GET_US_MARKET_CALENDAR_200_RESPONSE.md)
 - [listStocks_200_response](MODEL_LIST_STOCKS_200_RESPONSE.md)
 - [modifyConditionalOrder_200_response](MODEL_MODIFY_CONDITIONAL_ORDER_200_RESPONSE.md)
 - [modifyOrder_200_response](MODEL_MODIFY_ORDER_200_RESPONSE.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="oauth2ClientCredentials"></a>
### oauth2ClientCredentials

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A

