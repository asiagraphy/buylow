> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/StockInfoApi.md
> 문서 버전: 1.2.17

# StockInfoApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStockCreditTrades**](STOCK_INFO.md#getStockCreditTrades) | **GET** /api/v1/stocks/{symbol}/credit-trades | 신용거래 동향 조회 |
| [**getStockInvestorTrading**](STOCK_INFO.md#getStockInvestorTrading) | **GET** /api/v1/stocks/{symbol}/investor-trading | 투자자별 매매동향 조회 |
| [**getStockProgramTrades**](STOCK_INFO.md#getStockProgramTrades) | **GET** /api/v1/stocks/{symbol}/program-trades | 프로그램매매 동향 조회 |
| [**getStockSecuritiesLending**](STOCK_INFO.md#getStockSecuritiesLending) | **GET** /api/v1/stocks/{symbol}/securities-lending | 대차거래 동향 조회 |
| [**getStockShortSelling**](STOCK_INFO.md#getStockShortSelling) | **GET** /api/v1/stocks/{symbol}/short-selling | 공매도 동향 조회 |
| [**getStockWarnings**](STOCK_INFO.md#getStockWarnings) | **GET** /api/v1/stocks/{symbol}/warnings | 매수 유의사항 조회 |
| [**getStocks**](STOCK_INFO.md#getStocks) | **GET** /api/v1/stocks | 종목 기본 정보 조회 |
| [**listStocks**](STOCK_INFO.md#listStocks) | **GET** /api/v1/stocks/all | 마켓별 전체 종목 조회 |


<a name="getStockCreditTrades"></a>
# **getStockCreditTrades**
> getStockCreditTrades_200_response getStockCreditTrades(symbol, count, until)

신용거래 동향 조회

    국내(KR) 종목의 신용거래 동향을 일별 시계열로 조회합니다. 신용융자(`marginLoan`)·신용대주(`stockLoan`) 각각의 신규·상환·잔고 수량과 잔고 비율·공여율을 최신순으로 제공합니다.  - 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다. - 자기신용과 유통금융을 합산한 값이며, 모든 수량은 주식 수(주) 정수입니다. - `stockLoan`(신용대주)은 주식을 빌려 매도하는 개인 신용거래입니다. 기관 간 대차거래   (`GET /api/v1/stocks/{symbol}/securities-lending`)와는 다른 데이터입니다. - 해당 일자에 융자·대주 중 한쪽 데이터만 있으면 없는 쪽 객체는 null 입니다. - 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.  **데이터 적시성**: 다음 영업일 새벽에 반영됩니다(T+1). 최신 기록은 전 영업일입니다.  **Rate Limits Group**: `STOCK_TRADING_TREND` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 국내(KR) 종목 심볼. KRX 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0). | [default to null] |
| **count** | **Integer**| 조회 수 (최대 100) | [optional] [default to 10] |
| **until** | **date**| 조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다. 미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.  | [optional] [default to null] |

### Return type

[**getStockCreditTrades_200_response**](MODEL_GET_STOCK_CREDIT_TRADES_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStockInvestorTrading"></a>
# **getStockInvestorTrading**
> getStockInvestorTrading_200_response getStockInvestorTrading(symbol, count, until)

투자자별 매매동향 조회

    국내(KR) 종목의 투자자별 매매동향을 일별 거래량 시계열로 조회합니다. 개인·외국인·기관·기타법인 4개 투자자 분류의 매수·매도·순매수 거래량을 최신순으로 제공하며, 기관은 7개 세부 분류(`breakdown`)를 함께 제공합니다. 외국인 보유 현황(`foreignerHolding`)과 CFD 잔고(`cfd`)도 일자별로 포함합니다.  - 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다. - 거래량은 KRX·NXT 통합 기준이며, 모든 수량은 주식 수(주) 정수입니다. 순매수(`netBuyVolume`)는   매수 − 매도로 계산되며 음수면 순매도입니다. 거래대금(금액) 축은 제공하지 않습니다. - `foreigner` 는 등록외국인 기준입니다. 시장 지표의 투자자별 매매대금   (`GET /api/v1/market-indicators/{symbol}/investor-trading`, 등록·미등록 합계)과 기준이 다릅니다. - 당일 기록은 장중 잠정치로 제공합니다. 잠정치가 제공되지 않는 `individual`(개인)·   `institution.breakdown`(기관 세부)·`otherCorporation`(기타법인)·`foreignerHolding`(외국인 보유)·   `cfd`(CFD 잔고)는 null 이며, `updatedAt` 으로 마지막 갱신 시각을 확인할 수 있습니다. - 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.  **데이터 적시성**: 하나의 일자 기록은 시간에 걸쳐 완성됩니다. 투자자별 매매동향 확정치와 외국인 보유(`foreignerHolding`)는 해당 일자 저녁에 반영됩니다. CFD 잔고(`cfd`)는 다음 영업일 새벽(T+1)에 반영되며, 외국인 보유는 다음 영업일 오전에 확정치로 한 번 더 갱신될 수 있습니다. `updatedAt` 은 이 모든 반영을 포함한 기록 전체의 마지막 갱신 시각입니다.  **Rate Limits Group**: `STOCK_TRADING_TREND` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 국내(KR) 종목 심볼. KRX 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0). | [default to null] |
| **count** | **Integer**| 조회 수 (최대 100) | [optional] [default to 10] |
| **until** | **date**| 조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다. 미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.  | [optional] [default to null] |

### Return type

[**getStockInvestorTrading_200_response**](MODEL_GET_STOCK_INVESTOR_TRADING_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStockProgramTrades"></a>
# **getStockProgramTrades**
> getStockProgramTrades_200_response getStockProgramTrades(symbol, count, until)

프로그램매매 동향 조회

    국내(KR) 종목의 프로그램매매 동향을 일별 거래량 시계열로 조회합니다. 차익거래(`arbitrage`)· 비차익거래(`nonArbitrage`) 각각의 매수·매도·순매수 거래량을 최신순으로 제공합니다.  - 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다. - KRX 시장 거래만 집계하며 NXT 거래는 포함하지 않습니다. 모든 수량은 주식 수(주) 정수입니다.   순매수(`netBuyVolume`)는 매수 − 매도로 계산되며 음수면 순매도입니다. 거래대금(금액) 축은 제공하지 않습니다. - 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.  **데이터 적시성**: 당일 기록도 제공되며, 장 종료 전까지 갱신될 수 있습니다.  **Rate Limits Group**: `STOCK_TRADING_TREND` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 국내(KR) 종목 심볼. KRX 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0). | [default to null] |
| **count** | **Integer**| 조회 수 (최대 100) | [optional] [default to 10] |
| **until** | **date**| 조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다. 미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.  | [optional] [default to null] |

### Return type

[**getStockProgramTrades_200_response**](MODEL_GET_STOCK_PROGRAM_TRADES_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStockSecuritiesLending"></a>
# **getStockSecuritiesLending**
> getStockSecuritiesLending_200_response getStockSecuritiesLending(symbol, count, until)

대차거래 동향 조회

    국내(KR) 종목의 대차거래 동향을 일별 시계열로 조회합니다. 대차 체결·상환·잔고 수량과 잔고 금액을 최신순으로 제공합니다.  - 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다. - 모든 금액은 원화(KRW)이며, 별도의 통화 필드는 제공하지 않습니다. - 대차거래는 기관 투자자 간 주식 대여·차입 거래입니다. 주식을 빌려 매도하는 개인 신용거래인   신용대주(`GET /api/v1/stocks/{symbol}/credit-trades` 의 `stockLoan`)와는 다른 데이터입니다. - 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.  **데이터 적시성**: 일별 확정치는 해당 일자 저녁에 반영됩니다.  **Rate Limits Group**: `STOCK_TRADING_TREND` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 국내(KR) 종목 심볼. KRX 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0). | [default to null] |
| **count** | **Integer**| 조회 수 (최대 100) | [optional] [default to 10] |
| **until** | **date**| 조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다. 미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.  | [optional] [default to null] |

### Return type

[**getStockSecuritiesLending_200_response**](MODEL_GET_STOCK_SECURITIES_LENDING_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStockShortSelling"></a>
# **getStockShortSelling**
> getStockShortSelling_200_response getStockShortSelling(symbol, count, until)

공매도 동향 조회

    국내(KR) 종목의 공매도 동향을 일별 시계열로 조회합니다. 공매도 거래량·거래대금과 함께 해당 일자 전체 거래량·거래대금 대비 공매도 비중을 최신순으로 제공합니다.  - 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다. - 모든 금액은 원화(KRW)이며, 별도의 통화 필드는 제공하지 않습니다. - 비중(`shortSellingVolumeRate`·`shortSellingAmountRate`)의 분모는 정규장 외 세션   (장전·장후 시간외종가, 애프터마켓)을 포함한 해당 일자 누적 거래량·거래대금입니다.   분모 데이터가 없는 날짜는 비중이 null, 분모가 0 이면 `0` 입니다. - 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.  **데이터 적시성**: 일별 확정치는 해당 일자 저녁에 반영됩니다.  **Rate Limits Group**: `STOCK_TRADING_TREND` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 국내(KR) 종목 심볼. KRX 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0). | [default to null] |
| **count** | **Integer**| 조회 수 (최대 100) | [optional] [default to 10] |
| **until** | **date**| 조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다. 미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.  | [optional] [default to null] |

### Return type

[**getStockShortSelling_200_response**](MODEL_GET_STOCK_SHORT_SELLING_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStockWarnings"></a>
# **getStockWarnings**
> getStockWarnings_200_response getStockWarnings(symbol)

매수 유의사항 조회

    종목의 매수 유의사항 및 변동성 완화(VI) 발동 정보를 조회합니다.  **포함 종류**: 정리매매(`LIQUIDATION_TRADING`), 단기과열종목(`OVERHEATED`), 투자경고(`INVESTMENT_WARNING`), 투자위험(`INVESTMENT_RISK`), VI 정적/동적/혼합(`VI_STATIC` / `VI_DYNAMIC` / `VI_STATIC_AND_DYNAMIC`), 신주인수권(`STOCK_WARRANTS`). 전체 enum 은 `StockWarning.warningType` 참조.  **\"활성\"의 시간 기준**: 응답 시점 기준으로 `startDate <= 오늘 <= endDate` 인 항목 (또는 `endDate` 가 `null` 인 진행 중 항목).  **응답 정렬**: `startDate` 내림차순 (최근 발동된 항목부터). `startDate` 가 동일한 경우 정렬 순서는 보장되지 않습니다.  **데이터 적시성**: VI 발동/해제는 거래소 이벤트 발생 후 수 초 내 반영됩니다. 정리매매·단기과열·투자경고/위험 지정은 거래소 공시 기준 일배치로 반영됩니다.  **미존재 vs 빈 배열**: - 종목 자체가 없으면 `404 stock-not-found`. - 종목은 있으나 활성 유의사항이 없으면 `200 OK` + `result: []`.  **Rate Limits Group**: `STOCK` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL). 영문 대/소문자, 숫자, '.', '-' 만 허용한다. | [default to null] |

### Return type

[**getStockWarnings_200_response**](MODEL_GET_STOCK_WARNINGS_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getStocks"></a>
# **getStocks**
> getStocks_200_response getStocks(symbols)

종목 기본 정보 조회

    종목의 기본 정보를 조회합니다. `symbols` 를 콤마로 구분하여 최대 200건 까지 다건 조회를 지원합니다. 종목명, 시장, 통화, 상장 상태, 거래정지 여부 등 트레이딩에서 필요한 참조 데이터를 제공합니다.  **관련 API**: 마켓 전체 종목 목록(유니버스)이 필요하면 [`GET /api/v1/stocks/all`](STOCK_INFO.md#operation/listStocks) 을 사용하세요.  **Rate Limits Group**: `STOCK` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbols** | **String**| 종목 심볼. 콤마로 구분하여 최대 200건. 예: 005930 또는 005930,AAPL. 영문 대/소문자, 숫자, '.', '-' 만 허용한다. | [default to null] |

### Return type

[**getStocks_200_response**](MODEL_GET_STOCKS_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listStocks"></a>
# **listStocks**
> listStocks_200_response listStocks(market, status, securityType, commonShare)

마켓별 전체 종목 조회

    마켓(거래소)별 종목 리스트를 조회합니다. 종목 유니버스 구성 용도이며, 토스증권에서 거래 가능한 종목만 제공합니다. `status`·`securityType`·`commonShare` 로 유니버스를 필터링할 수 있습니다.  **정렬**: `symbol` 오름차순. 필터 조건에 해당하는 종목을 페이지네이션 없이 한 번에 반환합니다.  **응답 규모**: 마켓당 최대 수천 건(예: NASDAQ 약 2,800건, gzip 응답 약 30KB). 일 배치로 갱신되는 저변동 데이터이므로 하루 1회 조회 후 로컬 캐싱을 권장합니다.  **관련 API**: 여기서 얻은 `symbol` 로 [`GET /api/v1/stocks`](STOCK_INFO.md#operation/getStocks)(다건 상세 조회)를 호출해 종목명·통화·상장상태 등 상세 정보를 채울 수 있습니다.  **Rate Limits Group**: `STOCK_ALL` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **market** | **String**| 조회할 마켓(거래소) | [default to null] [enum: KOSPI, KOSDAQ, NYSE, NASDAQ, AMEX, KR_ETC, US_ETC] |
| **status** | **String**| 종목 상태 필터 (미지정 시 ACTIVE) | [optional] [default to ACTIVE] [enum: SCHEDULED, ACTIVE, DELISTED] |
| **securityType** | **String**| 종목 유형 필터 (미지정 시 전체 유형) | [optional] [default to null] [enum: STOCK, FOREIGN_STOCK, DEPOSITARY_RECEIPT, INFRASTRUCTURE_FUND, REIT, ETF, FOREIGN_ETF, ETN, STOCK_WARRANTS] |
| **commonShare** | **Boolean**| 보통주 여부 필터 (true=보통주만, false=우선주만, 미지정 시 전체) | [optional] [default to null] |

### Return type

[**listStocks_200_response**](MODEL_LIST_STOCKS_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## GET /api/v1/stocks

### `/summary`

종목 기본 정보 조회

### `/description`

종목의 기본 정보를 조회합니다. `symbols` 를 콤마로 구분하여 최대 200건 까지 다건 조회를 지원합니다.
종목명, 시장, 통화, 상장 상태, 거래정지 여부 등 트레이딩에서 필요한 참조 데이터를 제공합니다.

**관련 API**: 마켓 전체 종목 목록(유니버스)이 필요하면 [`GET /api/v1/stocks/all`](#operation/listStocks) 을 사용하세요.

**Rate Limits Group**: `STOCK`


### `/parameters/0/description`

종목 심볼. 콤마로 구분하여 최대 200건. 예: 005930 또는 005930,AAPL. 영문 대/소문자, 숫자, '.', '-' 만 허용한다.

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/multiple/summary`

다건 조회 (국내 + 미국)

### `/responses/200/content/application/json/examples/krxStock/summary`

국내 주식 (삼성전자)

### `/responses/200/content/application/json/examples/usStock/summary`

미국 주식 (Apple)

### `/responses/200/content/application/json/examples/etf/summary`

ETF (KODEX 200)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/tooManySymbols/summary`

허용 개수 초과 (1~200건)

### 전체 연산 정의

````json
{
  "tags": [
    "Stock Info"
  ],
  "summary": "종목 기본 정보 조회",
  "description": "종목의 기본 정보를 조회합니다. `symbols` 를 콤마로 구분하여 최대 200건 까지 다건 조회를 지원합니다.\n종목명, 시장, 통화, 상장 상태, 거래정지 여부 등 트레이딩에서 필요한 참조 데이터를 제공합니다.\n\n**관련 API**: 마켓 전체 종목 목록(유니버스)이 필요하면 [`GET /api/v1/stocks/all`](#operation/listStocks) 을 사용하세요.\n\n**Rate Limits Group**: `STOCK`\n",
  "operationId": "getStocks",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "name": "symbols",
      "in": "query",
      "required": true,
      "description": "종목 심볼. 콤마로 구분하여 최대 200건. 예: 005930 또는 005930,AAPL. 영문 대/소문자, 숫자, '.', '-' 만 허용한다.",
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9.,\\-]+$"
      },
      "example": "005930,AAPL"
    }
  ],
  "responses": {
    "200": {
      "description": "성공",
      "content": {
        "application/json": {
          "schema": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ApiResponse"
              },
              {
                "type": "object",
                "properties": {
                  "result": {
                    "type": "array",
                    "items": {
                      "$ref": "#/components/schemas/StockInfo"
                    }
                  }
                }
              }
            ]
          },
          "examples": {
            "multiple": {
              "summary": "다건 조회 (국내 + 미국)",
              "value": {
                "result": [
                  {
                    "symbol": "005930",
                    "name": "삼성전자",
                    "englishName": "SamsungElec",
                    "isinCode": "KR7005930003",
                    "market": "KOSPI",
                    "securityType": "STOCK",
                    "isCommonShare": true,
                    "status": "ACTIVE",
                    "currency": "KRW",
                    "listDate": "1975-06-11",
                    "delistDate": null,
                    "sharesOutstanding": "5919637922",
                    "leverageFactor": null,
                    "koreanMarketDetail": {
                      "liquidationTrading": false,
                      "nxtSupported": true,
                      "krxTradingSuspended": false,
                      "nxtTradingSuspended": false
                    }
                  },
                  {
                    "symbol": "AAPL",
                    "name": "애플",
                    "englishName": "APPLE INC",
                    "isinCode": "US0378331005",
                    "market": "NASDAQ",
                    "securityType": "STOCK",
                    "isCommonShare": true,
                    "status": "ACTIVE",
                    "currency": "USD",
                    "listDate": "1980-12-12",
                    "delistDate": null,
                    "sharesOutstanding": "14702703000",
                    "leverageFactor": null,
                    "koreanMarketDetail": null
                  }
                ]
              }
            },
            "krxStock": {
              "summary": "국내 주식 (삼성전자)",
              "value": {
                "result": [
                  {
                    "symbol": "005930",
                    "name": "삼성전자",
                    "englishName": "SamsungElec",
                    "isinCode": "KR7005930003",
                    "market": "KOSPI",
                    "securityType": "STOCK",
                    "isCommonShare": true,
                    "status": "ACTIVE",
                    "currency": "KRW",
                    "listDate": "1975-06-11",
                    "delistDate": null,
                    "sharesOutstanding": "5919637922",
                    "leverageFactor": null,
                    "koreanMarketDetail": {
                      "liquidationTrading": false,
                      "nxtSupported": true,
                      "krxTradingSuspended": false,
                      "nxtTradingSuspended": false
                    }
                  }
                ]
              }
            },
            "usStock": {
              "summary": "미국 주식 (Apple)",
              "value": {
                "result": [
                  {
                    "symbol": "AAPL",
                    "name": "애플",
                    "englishName": "APPLE INC",
                    "isinCode": "US0378331005",
                    "market": "NASDAQ",
                    "securityType": "STOCK",
                    "isCommonShare": true,
                    "status": "ACTIVE",
                    "currency": "USD",
                    "listDate": "1980-12-12",
                    "delistDate": null,
                    "sharesOutstanding": "14702703000",
                    "leverageFactor": null,
                    "koreanMarketDetail": null
                  }
                ]
              }
            },
            "etf": {
              "summary": "ETF (KODEX 200)",
              "value": {
                "result": [
                  {
                    "symbol": "069500",
                    "name": "KODEX 200",
                    "isinCode": "KR7069500007",
                    "market": "KOSPI",
                    "securityType": "ETF",
                    "isCommonShare": true,
                    "status": "ACTIVE",
                    "currency": "KRW",
                    "listDate": "2002-10-14",
                    "delistDate": null,
                    "sharesOutstanding": "208050000",
                    "leverageFactor": "1",
                    "koreanMarketDetail": {
                      "liquidationTrading": false,
                      "nxtSupported": false,
                      "krxTradingSuspended": false,
                      "nxtTradingSuspended": null
                    }
                  }
                ]
              }
            }
          }
        }
      }
    },
    "400": {
      "description": "잘못된 요청",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "tooManySymbols": {
              "summary": "허용 개수 초과 (1~200건)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다.",
                  "data": {
                    "field": "symbols",
                    "constraint": {
                      "min": 1,
                      "max": 200
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "401": {
      "$ref": "#/components/responses/Unauthorized"
    },
    "403": {
      "$ref": "#/components/responses/Forbidden"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorStock"
    }
  }
}
````

## GET /api/v1/stocks/all

### `/summary`

마켓별 전체 종목 조회

### `/description`

마켓(거래소)별 종목 리스트를 조회합니다. 종목 유니버스 구성 용도이며, 토스증권에서 거래 가능한 종목만 제공합니다.
`status`·`securityType`·`commonShare` 로 유니버스를 필터링할 수 있습니다.

**정렬**: `symbol` 오름차순. 필터 조건에 해당하는 종목을 페이지네이션 없이 한 번에 반환합니다.

**응답 규모**: 마켓당 최대 수천 건(예: NASDAQ 약 2,800건, gzip 응답 약 30KB). 일 배치로 갱신되는 저변동 데이터이므로 하루 1회 조회 후 로컬 캐싱을 권장합니다.

**관련 API**: 여기서 얻은 `symbol` 로 [`GET /api/v1/stocks`](#operation/getStocks)(다건 상세 조회)를 호출해 종목명·통화·상장상태 등 상세 정보를 채울 수 있습니다.

**Rate Limits Group**: `STOCK_ALL`


### `/parameters/0/description`

조회할 마켓(거래소)

### `/parameters/1/description`

종목 상태 필터 (미지정 시 ACTIVE)

### `/parameters/2/description`

종목 유형 필터 (미지정 시 전체 유형)

### `/parameters/3/description`

보통주 여부 필터 (true=보통주만, false=우선주만, 미지정 시 전체)

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/kospi/summary`

KOSPI 종목 (일부 발췌)

### `/responses/200/content/application/json/examples/nasdaq/summary`

NASDAQ 종목 (미국 종목도 한글 name 제공)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/invalidMarket/summary`

허용되지 않은 market

### 전체 연산 정의

````json
{
  "tags": [
    "Stock Info"
  ],
  "summary": "마켓별 전체 종목 조회",
  "description": "마켓(거래소)별 종목 리스트를 조회합니다. 종목 유니버스 구성 용도이며, 토스증권에서 거래 가능한 종목만 제공합니다.\n`status`·`securityType`·`commonShare` 로 유니버스를 필터링할 수 있습니다.\n\n**정렬**: `symbol` 오름차순. 필터 조건에 해당하는 종목을 페이지네이션 없이 한 번에 반환합니다.\n\n**응답 규모**: 마켓당 최대 수천 건(예: NASDAQ 약 2,800건, gzip 응답 약 30KB). 일 배치로 갱신되는 저변동 데이터이므로 하루 1회 조회 후 로컬 캐싱을 권장합니다.\n\n**관련 API**: 여기서 얻은 `symbol` 로 [`GET /api/v1/stocks`](#operation/getStocks)(다건 상세 조회)를 호출해 종목명·통화·상장상태 등 상세 정보를 채울 수 있습니다.\n\n**Rate Limits Group**: `STOCK_ALL`\n",
  "operationId": "listStocks",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "name": "market",
      "in": "query",
      "required": true,
      "description": "조회할 마켓(거래소)",
      "schema": {
        "type": "string",
        "enum": [
          "KOSPI",
          "KOSDAQ",
          "NYSE",
          "NASDAQ",
          "AMEX",
          "KR_ETC",
          "US_ETC"
        ]
      },
      "example": "KOSPI"
    },
    {
      "name": "status",
      "in": "query",
      "required": false,
      "description": "종목 상태 필터 (미지정 시 ACTIVE)",
      "schema": {
        "type": "string",
        "enum": [
          "SCHEDULED",
          "ACTIVE",
          "DELISTED"
        ],
        "default": "ACTIVE"
      },
      "example": "ACTIVE"
    },
    {
      "name": "securityType",
      "in": "query",
      "required": false,
      "description": "종목 유형 필터 (미지정 시 전체 유형)",
      "schema": {
        "type": "string",
        "enum": [
          "STOCK",
          "FOREIGN_STOCK",
          "DEPOSITARY_RECEIPT",
          "INFRASTRUCTURE_FUND",
          "REIT",
          "ETF",
          "FOREIGN_ETF",
          "ETN",
          "STOCK_WARRANTS"
        ]
      },
      "example": "STOCK"
    },
    {
      "name": "commonShare",
      "in": "query",
      "required": false,
      "description": "보통주 여부 필터 (true=보통주만, false=우선주만, 미지정 시 전체)",
      "schema": {
        "type": "boolean"
      },
      "example": true
    }
  ],
  "responses": {
    "200": {
      "description": "성공",
      "content": {
        "application/json": {
          "schema": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ApiResponse"
              },
              {
                "type": "object",
                "properties": {
                  "result": {
                    "type": "array",
                    "items": {
                      "$ref": "#/components/schemas/ListedStock"
                    }
                  }
                }
              }
            ]
          },
          "examples": {
            "kospi": {
              "summary": "KOSPI 종목 (일부 발췌)",
              "value": {
                "result": [
                  {
                    "symbol": "005930",
                    "name": "삼성전자",
                    "securityType": "STOCK",
                    "isCommonShare": true,
                    "isinCode": "KR7005930003"
                  },
                  {
                    "symbol": "069500",
                    "name": "KODEX 200",
                    "securityType": "ETF",
                    "isCommonShare": true,
                    "isinCode": "KR7069500007"
                  }
                ]
              }
            },
            "nasdaq": {
              "summary": "NASDAQ 종목 (미국 종목도 한글 name 제공)",
              "value": {
                "result": [
                  {
                    "symbol": "AAPL",
                    "name": "애플",
                    "securityType": "STOCK",
                    "isCommonShare": true,
                    "isinCode": "US0378331005"
                  }
                ]
              }
            }
          }
        }
      }
    },
    "400": {
      "description": "잘못된 요청",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "invalidMarket": {
              "summary": "허용되지 않은 market",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "유효하지 않은 market 입니다. KOSPI, KOSDAQ, NYSE, NASDAQ, AMEX, KR_ETC, US_ETC 만 허용됩니다.",
                  "data": {
                    "field": "market",
                    "allowedValues": [
                      "KOSPI",
                      "KOSDAQ",
                      "NYSE",
                      "NASDAQ",
                      "AMEX",
                      "KR_ETC",
                      "US_ETC"
                    ]
                  }
                }
              }
            }
          }
        }
      }
    },
    "401": {
      "$ref": "#/components/responses/Unauthorized"
    },
    "403": {
      "$ref": "#/components/responses/Forbidden"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorStock"
    }
  }
}
````

## GET /api/v1/stocks/{symbol}/warnings

### `/summary`

매수 유의사항 조회

### `/description`

종목의 매수 유의사항 및 변동성 완화(VI) 발동 정보를 조회합니다.

**포함 종류**: 정리매매(`LIQUIDATION_TRADING`), 단기과열종목(`OVERHEATED`), 투자경고(`INVESTMENT_WARNING`), 투자위험(`INVESTMENT_RISK`), VI 정적/동적/혼합(`VI_STATIC` / `VI_DYNAMIC` / `VI_STATIC_AND_DYNAMIC`), 신주인수권(`STOCK_WARRANTS`). 전체 enum 은 `StockWarning.warningType` 참조.

**"활성"의 시간 기준**: 응답 시점 기준으로 `startDate <= 오늘 <= endDate` 인 항목 (또는 `endDate` 가 `null` 인 진행 중 항목).

**응답 정렬**: `startDate` 내림차순 (최근 발동된 항목부터). `startDate` 가 동일한 경우 정렬 순서는 보장되지 않습니다.

**데이터 적시성**: VI 발동/해제는 거래소 이벤트 발생 후 수 초 내 반영됩니다. 정리매매·단기과열·투자경고/위험 지정은 거래소 공시 기준 일배치로 반영됩니다.

**미존재 vs 빈 배열**:
- 종목 자체가 없으면 `404 stock-not-found`.
- 종목은 있으나 활성 유의사항이 없으면 `200 OK` + `result: []`.

**Rate Limits Group**: `STOCK`


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/withWarnings/summary`

유의사항이 있는 종목

### `/responses/200/content/application/json/examples/noWarnings/summary`

유의사항이 없는 종목

### 전체 연산 정의

````json
{
  "tags": [
    "Stock Info"
  ],
  "summary": "매수 유의사항 조회",
  "description": "종목의 매수 유의사항 및 변동성 완화(VI) 발동 정보를 조회합니다.\n\n**포함 종류**: 정리매매(`LIQUIDATION_TRADING`), 단기과열종목(`OVERHEATED`), 투자경고(`INVESTMENT_WARNING`), 투자위험(`INVESTMENT_RISK`), VI 정적/동적/혼합(`VI_STATIC` / `VI_DYNAMIC` / `VI_STATIC_AND_DYNAMIC`), 신주인수권(`STOCK_WARRANTS`). 전체 enum 은 `StockWarning.warningType` 참조.\n\n**\"활성\"의 시간 기준**: 응답 시점 기준으로 `startDate <= 오늘 <= endDate` 인 항목 (또는 `endDate` 가 `null` 인 진행 중 항목).\n\n**응답 정렬**: `startDate` 내림차순 (최근 발동된 항목부터). `startDate` 가 동일한 경우 정렬 순서는 보장되지 않습니다.\n\n**데이터 적시성**: VI 발동/해제는 거래소 이벤트 발생 후 수 초 내 반영됩니다. 정리매매·단기과열·투자경고/위험 지정은 거래소 공시 기준 일배치로 반영됩니다.\n\n**미존재 vs 빈 배열**:\n- 종목 자체가 없으면 `404 stock-not-found`.\n- 종목은 있으나 활성 유의사항이 없으면 `200 OK` + `result: []`.\n\n**Rate Limits Group**: `STOCK`\n",
  "operationId": "getStockWarnings",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/Symbol"
    }
  ],
  "responses": {
    "200": {
      "description": "성공",
      "content": {
        "application/json": {
          "schema": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ApiResponse"
              },
              {
                "type": "object",
                "properties": {
                  "result": {
                    "type": "array",
                    "items": {
                      "$ref": "#/components/schemas/StockWarning"
                    }
                  }
                }
              }
            ]
          },
          "examples": {
            "withWarnings": {
              "summary": "유의사항이 있는 종목",
              "value": {
                "result": [
                  {
                    "warningType": "OVERHEATED",
                    "exchange": "KRX",
                    "startDate": "2026-03-20",
                    "endDate": "2026-03-27"
                  },
                  {
                    "warningType": "VI_STATIC",
                    "exchange": "KRX",
                    "startDate": "2026-03-26",
                    "endDate": null
                  }
                ]
              }
            },
            "noWarnings": {
              "summary": "유의사항이 없는 종목",
              "value": {
                "result": []
              }
            }
          }
        }
      }
    },
    "401": {
      "$ref": "#/components/responses/Unauthorized"
    },
    "403": {
      "$ref": "#/components/responses/Forbidden"
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorStock"
    }
  }
}
````

## GET /api/v1/stocks/{symbol}/investor-trading

### `/summary`

투자자별 매매동향 조회

### `/description`

국내(KR) 종목의 투자자별 매매동향을 일별 거래량 시계열로 조회합니다. 개인·외국인·기관·기타법인
4개 투자자 분류의 매수·매도·순매수 거래량을 최신순으로 제공하며, 기관은 7개 세부 분류(`breakdown`)를
함께 제공합니다. 외국인 보유 현황(`foreignerHolding`)과 CFD 잔고(`cfd`)도 일자별로 포함합니다.

- 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다.
- 거래량은 KRX·NXT 통합 기준이며, 모든 수량은 주식 수(주) 정수입니다. 순매수(`netBuyVolume`)는
  매수 − 매도로 계산되며 음수면 순매도입니다. 거래대금(금액) 축은 제공하지 않습니다.
- `foreigner` 는 등록외국인 기준입니다. 시장 지표의 투자자별 매매대금
  (`GET /api/v1/market-indicators/{symbol}/investor-trading`, 등록·미등록 합계)과 기준이 다릅니다.
- 당일 기록은 장중 잠정치로 제공합니다. 잠정치가 제공되지 않는 `individual`(개인)·
  `institution.breakdown`(기관 세부)·`otherCorporation`(기타법인)·`foreignerHolding`(외국인 보유)·
  `cfd`(CFD 잔고)는 null 이며, `updatedAt` 으로 마지막 갱신 시각을 확인할 수 있습니다.
- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.

**데이터 적시성**: 하나의 일자 기록은 시간에 걸쳐 완성됩니다. 투자자별 매매동향 확정치와
외국인 보유(`foreignerHolding`)는 해당 일자 저녁에 반영됩니다. CFD 잔고(`cfd`)는 다음 영업일 새벽(T+1)에
반영되며, 외국인 보유는 다음 영업일 오전에 확정치로 한 번 더 갱신될 수 있습니다.
`updatedAt` 은 이 모든 반영을 포함한 기록 전체의 마지막 갱신 시각입니다.

**Rate Limits Group**: `STOCK_TRADING_TREND`


### `/parameters/1/description`

조회 수 (최대 100)

### `/parameters/2/description`

조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.
미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/daily/summary`

당일 잠정 기록 + 확정 기록 (count=2)

### `/responses/200/content/application/json/examples/noData/summary`

조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedMarket/summary`

국내(KR) 종목이 아님

### `/responses/400/content/application/json/examples/invalidCount/summary`

count 가 허용 범위(1~100)를 벗어남

### 전체 연산 정의

````json
{
  "tags": [
    "Stock Info"
  ],
  "summary": "투자자별 매매동향 조회",
  "description": "국내(KR) 종목의 투자자별 매매동향을 일별 거래량 시계열로 조회합니다. 개인·외국인·기관·기타법인\n4개 투자자 분류의 매수·매도·순매수 거래량을 최신순으로 제공하며, 기관은 7개 세부 분류(`breakdown`)를\n함께 제공합니다. 외국인 보유 현황(`foreignerHolding`)과 CFD 잔고(`cfd`)도 일자별로 포함합니다.\n\n- 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다.\n- 거래량은 KRX·NXT 통합 기준이며, 모든 수량은 주식 수(주) 정수입니다. 순매수(`netBuyVolume`)는\n  매수 − 매도로 계산되며 음수면 순매도입니다. 거래대금(금액) 축은 제공하지 않습니다.\n- `foreigner` 는 등록외국인 기준입니다. 시장 지표의 투자자별 매매대금\n  (`GET /api/v1/market-indicators/{symbol}/investor-trading`, 등록·미등록 합계)과 기준이 다릅니다.\n- 당일 기록은 장중 잠정치로 제공합니다. 잠정치가 제공되지 않는 `individual`(개인)·\n  `institution.breakdown`(기관 세부)·`otherCorporation`(기타법인)·`foreignerHolding`(외국인 보유)·\n  `cfd`(CFD 잔고)는 null 이며, `updatedAt` 으로 마지막 갱신 시각을 확인할 수 있습니다.\n- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.\n\n**데이터 적시성**: 하나의 일자 기록은 시간에 걸쳐 완성됩니다. 투자자별 매매동향 확정치와\n외국인 보유(`foreignerHolding`)는 해당 일자 저녁에 반영됩니다. CFD 잔고(`cfd`)는 다음 영업일 새벽(T+1)에\n반영되며, 외국인 보유는 다음 영업일 오전에 확정치로 한 번 더 갱신될 수 있습니다.\n`updatedAt` 은 이 모든 반영을 포함한 기록 전체의 마지막 갱신 시각입니다.\n\n**Rate Limits Group**: `STOCK_TRADING_TREND`\n",
  "operationId": "getStockInvestorTrading",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/KrSymbol"
    },
    {
      "name": "count",
      "in": "query",
      "required": false,
      "description": "조회 수 (최대 100)",
      "schema": {
        "type": "integer",
        "default": 10,
        "minimum": 1,
        "maximum": 100
      }
    },
    {
      "name": "until",
      "in": "query",
      "required": false,
      "description": "조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.\n미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.\n",
      "schema": {
        "type": "string",
        "format": "date"
      },
      "example": "2026-07-16"
    }
  ],
  "responses": {
    "200": {
      "description": "성공",
      "content": {
        "application/json": {
          "schema": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ApiResponse"
              },
              {
                "type": "object",
                "properties": {
                  "result": {
                    "$ref": "#/components/schemas/StockInvestorTradingResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "daily": {
              "summary": "당일 잠정 기록 + 확정 기록 (count=2)",
              "value": {
                "result": {
                  "nextUntil": "2026-07-15",
                  "records": [
                    {
                      "date": "2026-07-17",
                      "updatedAt": "2026-07-17T14:35:08+09:00",
                      "individual": null,
                      "foreigner": {
                        "buyVolume": "2105300",
                        "sellVolume": "1985400",
                        "netBuyVolume": "119900"
                      },
                      "institution": {
                        "buyVolume": "910200",
                        "sellVolume": "1023400",
                        "netBuyVolume": "-113200",
                        "breakdown": null
                      },
                      "otherCorporation": null,
                      "foreignerHolding": null,
                      "cfd": null
                    },
                    {
                      "date": "2026-07-16",
                      "updatedAt": "2026-07-17T09:12:43+09:00",
                      "individual": {
                        "buyVolume": "8412300",
                        "sellVolume": "8120450",
                        "netBuyVolume": "291850"
                      },
                      "foreigner": {
                        "buyVolume": "4210500",
                        "sellVolume": "4530200",
                        "netBuyVolume": "-319700"
                      },
                      "institution": {
                        "buyVolume": "1953200",
                        "sellVolume": "1915300",
                        "netBuyVolume": "37900",
                        "breakdown": {
                          "financialInvestment": {
                            "buyVolume": "1203400",
                            "sellVolume": "1150200",
                            "netBuyVolume": "53200"
                          },
                          "insurance": {
                            "buyVolume": "45000",
                            "sellVolume": "52300",
                            "netBuyVolume": "-7300"
                          },
                          "trust": {
                            "buyVolume": "120500",
                            "sellVolume": "98700",
                            "netBuyVolume": "21800"
                          },
                          "privateEquityFund": {
                            "buyVolume": "210300",
                            "sellVolume": "187600",
                            "netBuyVolume": "22700"
                          },
                          "bank": {
                            "buyVolume": "15200",
                            "sellVolume": "12400",
                            "netBuyVolume": "2800"
                          },
                          "otherFinancialInstitution": {
                            "buyVolume": "8700",
                            "sellVolume": "11300",
                            "netBuyVolume": "-2600"
                          },
                          "pensionFund": {
                            "buyVolume": "350100",
                            "sellVolume": "402800",
                            "netBuyVolume": "-52700"
                          }
                        }
                      },
                      "otherCorporation": {
                        "buyVolume": "98200",
                        "sellVolume": "112400",
                        "netBuyVolume": "-14200"
                      },
                      "foreignerHolding": {
                        "holdingQuantity": "3012456789",
                        "limitQuantity": "5919637922",
                        "holdingRate": "0.5089"
                      },
                      "cfd": {
                        "buyBalanceQuantity": "1250000",
                        "buyBalanceRate": "0.0002",
                        "sellBalanceQuantity": "890000",
                        "sellBalanceRate": "0.0001"
                      }
                    }
                  ]
                }
              }
            },
            "noData": {
              "summary": "조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)",
              "value": {
                "result": {
                  "nextUntil": null,
                  "records": []
                }
              }
            }
          }
        }
      }
    },
    "400": {
      "description": "잘못된 요청",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "unsupportedMarket": {
              "summary": "국내(KR) 종목이 아님",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "unsupported-market",
                  "message": "지원하지 않는 시장의 종목입니다.",
                  "data": {
                    "field": "symbol",
                    "allowedConditions": {
                      "marketCountry": [
                        "KR"
                      ]
                    }
                  }
                }
              }
            },
            "invalidCount": {
              "summary": "count 가 허용 범위(1~100)를 벗어남",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다.",
                  "data": {
                    "field": "count",
                    "constraint": {
                      "min": 1,
                      "max": 100
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "401": {
      "$ref": "#/components/responses/Unauthorized"
    },
    "403": {
      "$ref": "#/components/responses/Forbidden"
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorTradingTrend"
    }
  }
}
````

## GET /api/v1/stocks/{symbol}/program-trades

### `/summary`

프로그램매매 동향 조회

### `/description`

국내(KR) 종목의 프로그램매매 동향을 일별 거래량 시계열로 조회합니다. 차익거래(`arbitrage`)·
비차익거래(`nonArbitrage`) 각각의 매수·매도·순매수 거래량을 최신순으로 제공합니다.

- 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다.
- KRX 시장 거래만 집계하며 NXT 거래는 포함하지 않습니다. 모든 수량은 주식 수(주) 정수입니다.
  순매수(`netBuyVolume`)는 매수 − 매도로 계산되며 음수면 순매도입니다. 거래대금(금액) 축은 제공하지 않습니다.
- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.

**데이터 적시성**: 당일 기록도 제공되며, 장 종료 전까지 갱신될 수 있습니다.

**Rate Limits Group**: `STOCK_TRADING_TREND`


### `/parameters/1/description`

조회 수 (최대 100)

### `/parameters/2/description`

조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.
미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/daily/summary`

일별 프로그램매매 (count=2)

### `/responses/200/content/application/json/examples/noData/summary`

조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedMarket/summary`

국내(KR) 종목이 아님

### `/responses/400/content/application/json/examples/invalidCount/summary`

count 가 허용 범위(1~100)를 벗어남

### 전체 연산 정의

````json
{
  "tags": [
    "Stock Info"
  ],
  "summary": "프로그램매매 동향 조회",
  "description": "국내(KR) 종목의 프로그램매매 동향을 일별 거래량 시계열로 조회합니다. 차익거래(`arbitrage`)·\n비차익거래(`nonArbitrage`) 각각의 매수·매도·순매수 거래량을 최신순으로 제공합니다.\n\n- 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다.\n- KRX 시장 거래만 집계하며 NXT 거래는 포함하지 않습니다. 모든 수량은 주식 수(주) 정수입니다.\n  순매수(`netBuyVolume`)는 매수 − 매도로 계산되며 음수면 순매도입니다. 거래대금(금액) 축은 제공하지 않습니다.\n- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.\n\n**데이터 적시성**: 당일 기록도 제공되며, 장 종료 전까지 갱신될 수 있습니다.\n\n**Rate Limits Group**: `STOCK_TRADING_TREND`\n",
  "operationId": "getStockProgramTrades",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/KrSymbol"
    },
    {
      "name": "count",
      "in": "query",
      "required": false,
      "description": "조회 수 (최대 100)",
      "schema": {
        "type": "integer",
        "default": 10,
        "minimum": 1,
        "maximum": 100
      }
    },
    {
      "name": "until",
      "in": "query",
      "required": false,
      "description": "조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.\n미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.\n",
      "schema": {
        "type": "string",
        "format": "date"
      },
      "example": "2026-07-16"
    }
  ],
  "responses": {
    "200": {
      "description": "성공",
      "content": {
        "application/json": {
          "schema": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ApiResponse"
              },
              {
                "type": "object",
                "properties": {
                  "result": {
                    "$ref": "#/components/schemas/ProgramTradesResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "daily": {
              "summary": "일별 프로그램매매 (count=2)",
              "value": {
                "result": {
                  "nextUntil": "2026-07-15",
                  "records": [
                    {
                      "date": "2026-07-17",
                      "arbitrage": {
                        "buyVolume": "152300",
                        "sellVolume": "183400",
                        "netBuyVolume": "-31100"
                      },
                      "nonArbitrage": {
                        "buyVolume": "1210500",
                        "sellVolume": "1105200",
                        "netBuyVolume": "105300"
                      }
                    },
                    {
                      "date": "2026-07-16",
                      "arbitrage": {
                        "buyVolume": "98700",
                        "sellVolume": "120400",
                        "netBuyVolume": "-21700"
                      },
                      "nonArbitrage": {
                        "buyVolume": "1350200",
                        "sellVolume": "1298400",
                        "netBuyVolume": "51800"
                      }
                    }
                  ]
                }
              }
            },
            "noData": {
              "summary": "조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)",
              "value": {
                "result": {
                  "nextUntil": null,
                  "records": []
                }
              }
            }
          }
        }
      }
    },
    "400": {
      "description": "잘못된 요청",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "unsupportedMarket": {
              "summary": "국내(KR) 종목이 아님",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "unsupported-market",
                  "message": "지원하지 않는 시장의 종목입니다.",
                  "data": {
                    "field": "symbol",
                    "allowedConditions": {
                      "marketCountry": [
                        "KR"
                      ]
                    }
                  }
                }
              }
            },
            "invalidCount": {
              "summary": "count 가 허용 범위(1~100)를 벗어남",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다.",
                  "data": {
                    "field": "count",
                    "constraint": {
                      "min": 1,
                      "max": 100
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "401": {
      "$ref": "#/components/responses/Unauthorized"
    },
    "403": {
      "$ref": "#/components/responses/Forbidden"
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorTradingTrend"
    }
  }
}
````

## GET /api/v1/stocks/{symbol}/short-selling

### `/summary`

공매도 동향 조회

### `/description`

국내(KR) 종목의 공매도 동향을 일별 시계열로 조회합니다. 공매도 거래량·거래대금과 함께
해당 일자 전체 거래량·거래대금 대비 공매도 비중을 최신순으로 제공합니다.

- 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다.
- 모든 금액은 원화(KRW)이며, 별도의 통화 필드는 제공하지 않습니다.
- 비중(`shortSellingVolumeRate`·`shortSellingAmountRate`)의 분모는 정규장 외 세션
  (장전·장후 시간외종가, 애프터마켓)을 포함한 해당 일자 누적 거래량·거래대금입니다.
  분모 데이터가 없는 날짜는 비중이 null, 분모가 0 이면 `0` 입니다.
- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.

**데이터 적시성**: 일별 확정치는 해당 일자 저녁에 반영됩니다.

**Rate Limits Group**: `STOCK_TRADING_TREND`


### `/parameters/1/description`

조회 수 (최대 100)

### `/parameters/2/description`

조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.
미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/daily/summary`

일별 공매도 (count=2)

### `/responses/200/content/application/json/examples/rateUnavailable/summary`

분모(전체 거래량·거래대금) 데이터가 없어 비중이 null 인 날짜

### `/responses/200/content/application/json/examples/noData/summary`

조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedMarket/summary`

국내(KR) 종목이 아님

### `/responses/400/content/application/json/examples/invalidCount/summary`

count 가 허용 범위(1~100)를 벗어남

### 전체 연산 정의

````json
{
  "tags": [
    "Stock Info"
  ],
  "summary": "공매도 동향 조회",
  "description": "국내(KR) 종목의 공매도 동향을 일별 시계열로 조회합니다. 공매도 거래량·거래대금과 함께\n해당 일자 전체 거래량·거래대금 대비 공매도 비중을 최신순으로 제공합니다.\n\n- 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다.\n- 모든 금액은 원화(KRW)이며, 별도의 통화 필드는 제공하지 않습니다.\n- 비중(`shortSellingVolumeRate`·`shortSellingAmountRate`)의 분모는 정규장 외 세션\n  (장전·장후 시간외종가, 애프터마켓)을 포함한 해당 일자 누적 거래량·거래대금입니다.\n  분모 데이터가 없는 날짜는 비중이 null, 분모가 0 이면 `0` 입니다.\n- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.\n\n**데이터 적시성**: 일별 확정치는 해당 일자 저녁에 반영됩니다.\n\n**Rate Limits Group**: `STOCK_TRADING_TREND`\n",
  "operationId": "getStockShortSelling",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/KrSymbol"
    },
    {
      "name": "count",
      "in": "query",
      "required": false,
      "description": "조회 수 (최대 100)",
      "schema": {
        "type": "integer",
        "default": 10,
        "minimum": 1,
        "maximum": 100
      }
    },
    {
      "name": "until",
      "in": "query",
      "required": false,
      "description": "조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.\n미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.\n",
      "schema": {
        "type": "string",
        "format": "date"
      },
      "example": "2026-07-16"
    }
  ],
  "responses": {
    "200": {
      "description": "성공",
      "content": {
        "application/json": {
          "schema": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ApiResponse"
              },
              {
                "type": "object",
                "properties": {
                  "result": {
                    "$ref": "#/components/schemas/ShortSellingResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "daily": {
              "summary": "일별 공매도 (count=2)",
              "value": {
                "result": {
                  "nextUntil": "2026-07-14",
                  "records": [
                    {
                      "date": "2026-07-16",
                      "updatedAt": "2026-07-16T17:25:43+09:00",
                      "shortSellingVolume": "512300",
                      "shortSellingAmount": "41250000000",
                      "shortSellingVolumeRate": "0.03215",
                      "shortSellingAmountRate": "0.0318"
                    },
                    {
                      "date": "2026-07-15",
                      "updatedAt": "2026-07-15T17:26:02+09:00",
                      "shortSellingVolume": "423100",
                      "shortSellingAmount": "33980000000",
                      "shortSellingVolumeRate": "0.02871",
                      "shortSellingAmountRate": "0.0281"
                    }
                  ]
                }
              }
            },
            "rateUnavailable": {
              "summary": "분모(전체 거래량·거래대금) 데이터가 없어 비중이 null 인 날짜",
              "value": {
                "result": {
                  "nextUntil": null,
                  "records": [
                    {
                      "date": "2026-07-15",
                      "updatedAt": "2026-07-15T17:26:02+09:00",
                      "shortSellingVolume": "423100",
                      "shortSellingAmount": "33980000000",
                      "shortSellingVolumeRate": null,
                      "shortSellingAmountRate": null
                    }
                  ]
                }
              }
            },
            "noData": {
              "summary": "조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)",
              "value": {
                "result": {
                  "nextUntil": null,
                  "records": []
                }
              }
            }
          }
        }
      }
    },
    "400": {
      "description": "잘못된 요청",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "unsupportedMarket": {
              "summary": "국내(KR) 종목이 아님",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "unsupported-market",
                  "message": "지원하지 않는 시장의 종목입니다.",
                  "data": {
                    "field": "symbol",
                    "allowedConditions": {
                      "marketCountry": [
                        "KR"
                      ]
                    }
                  }
                }
              }
            },
            "invalidCount": {
              "summary": "count 가 허용 범위(1~100)를 벗어남",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다.",
                  "data": {
                    "field": "count",
                    "constraint": {
                      "min": 1,
                      "max": 100
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "401": {
      "$ref": "#/components/responses/Unauthorized"
    },
    "403": {
      "$ref": "#/components/responses/Forbidden"
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorTradingTrend"
    }
  }
}
````

## GET /api/v1/stocks/{symbol}/credit-trades

### `/summary`

신용거래 동향 조회

### `/description`

국내(KR) 종목의 신용거래 동향을 일별 시계열로 조회합니다. 신용융자(`marginLoan`)·신용대주(`stockLoan`)
각각의 신규·상환·잔고 수량과 잔고 비율·공여율을 최신순으로 제공합니다.

- 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다.
- 자기신용과 유통금융을 합산한 값이며, 모든 수량은 주식 수(주) 정수입니다.
- `stockLoan`(신용대주)은 주식을 빌려 매도하는 개인 신용거래입니다. 기관 간 대차거래
  (`GET /api/v1/stocks/{symbol}/securities-lending`)와는 다른 데이터입니다.
- 해당 일자에 융자·대주 중 한쪽 데이터만 있으면 없는 쪽 객체는 null 입니다.
- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.

**데이터 적시성**: 다음 영업일 새벽에 반영됩니다(T+1). 최신 기록은 전 영업일입니다.

**Rate Limits Group**: `STOCK_TRADING_TREND`


### `/parameters/1/description`

조회 수 (최대 100)

### `/parameters/2/description`

조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.
미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/daily/summary`

일별 신용거래 (count=2)

### `/responses/200/content/application/json/examples/noData/summary`

조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedMarket/summary`

국내(KR) 종목이 아님

### `/responses/400/content/application/json/examples/invalidCount/summary`

count 가 허용 범위(1~100)를 벗어남

### 전체 연산 정의

````json
{
  "tags": [
    "Stock Info"
  ],
  "summary": "신용거래 동향 조회",
  "description": "국내(KR) 종목의 신용거래 동향을 일별 시계열로 조회합니다. 신용융자(`marginLoan`)·신용대주(`stockLoan`)\n각각의 신규·상환·잔고 수량과 잔고 비율·공여율을 최신순으로 제공합니다.\n\n- 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다.\n- 자기신용과 유통금융을 합산한 값이며, 모든 수량은 주식 수(주) 정수입니다.\n- `stockLoan`(신용대주)은 주식을 빌려 매도하는 개인 신용거래입니다. 기관 간 대차거래\n  (`GET /api/v1/stocks/{symbol}/securities-lending`)와는 다른 데이터입니다.\n- 해당 일자에 융자·대주 중 한쪽 데이터만 있으면 없는 쪽 객체는 null 입니다.\n- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.\n\n**데이터 적시성**: 다음 영업일 새벽에 반영됩니다(T+1). 최신 기록은 전 영업일입니다.\n\n**Rate Limits Group**: `STOCK_TRADING_TREND`\n",
  "operationId": "getStockCreditTrades",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/KrSymbol"
    },
    {
      "name": "count",
      "in": "query",
      "required": false,
      "description": "조회 수 (최대 100)",
      "schema": {
        "type": "integer",
        "default": 10,
        "minimum": 1,
        "maximum": 100
      }
    },
    {
      "name": "until",
      "in": "query",
      "required": false,
      "description": "조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.\n미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.\n",
      "schema": {
        "type": "string",
        "format": "date"
      },
      "example": "2026-07-16"
    }
  ],
  "responses": {
    "200": {
      "description": "성공",
      "content": {
        "application/json": {
          "schema": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ApiResponse"
              },
              {
                "type": "object",
                "properties": {
                  "result": {
                    "$ref": "#/components/schemas/CreditTradesResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "daily": {
              "summary": "일별 신용거래 (count=2)",
              "value": {
                "result": {
                  "nextUntil": "2026-07-14",
                  "records": [
                    {
                      "date": "2026-07-16",
                      "updatedAt": "2026-07-17T02:35:00+09:00",
                      "marginLoan": {
                        "newQuantity": "125300",
                        "returnQuantity": "98200",
                        "balanceQuantity": "2513400",
                        "balanceRate": "0.0042",
                        "tradingRate": "0.09"
                      },
                      "stockLoan": {
                        "newQuantity": "5200",
                        "returnQuantity": "3100",
                        "balanceQuantity": "45200",
                        "balanceRate": "0.0001",
                        "tradingRate": "0.0004"
                      }
                    },
                    {
                      "date": "2026-07-15",
                      "updatedAt": "2026-07-16T02:34:12+09:00",
                      "marginLoan": {
                        "newQuantity": "110200",
                        "returnQuantity": "132400",
                        "balanceQuantity": "2486300",
                        "balanceRate": "0.0042",
                        "tradingRate": "0.085"
                      },
                      "stockLoan": {
                        "newQuantity": "4100",
                        "returnQuantity": "5300",
                        "balanceQuantity": "43100",
                        "balanceRate": "0.0001",
                        "tradingRate": "0.0003"
                      }
                    }
                  ]
                }
              }
            },
            "noData": {
              "summary": "조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)",
              "value": {
                "result": {
                  "nextUntil": null,
                  "records": []
                }
              }
            }
          }
        }
      }
    },
    "400": {
      "description": "잘못된 요청",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "unsupportedMarket": {
              "summary": "국내(KR) 종목이 아님",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "unsupported-market",
                  "message": "지원하지 않는 시장의 종목입니다.",
                  "data": {
                    "field": "symbol",
                    "allowedConditions": {
                      "marketCountry": [
                        "KR"
                      ]
                    }
                  }
                }
              }
            },
            "invalidCount": {
              "summary": "count 가 허용 범위(1~100)를 벗어남",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다.",
                  "data": {
                    "field": "count",
                    "constraint": {
                      "min": 1,
                      "max": 100
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "401": {
      "$ref": "#/components/responses/Unauthorized"
    },
    "403": {
      "$ref": "#/components/responses/Forbidden"
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorTradingTrend"
    }
  }
}
````

## GET /api/v1/stocks/{symbol}/securities-lending

### `/summary`

대차거래 동향 조회

### `/description`

국내(KR) 종목의 대차거래 동향을 일별 시계열로 조회합니다. 대차 체결·상환·잔고 수량과
잔고 금액을 최신순으로 제공합니다.

- 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다.
- 모든 금액은 원화(KRW)이며, 별도의 통화 필드는 제공하지 않습니다.
- 대차거래는 기관 투자자 간 주식 대여·차입 거래입니다. 주식을 빌려 매도하는 개인 신용거래인
  신용대주(`GET /api/v1/stocks/{symbol}/credit-trades` 의 `stockLoan`)와는 다른 데이터입니다.
- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.

**데이터 적시성**: 일별 확정치는 해당 일자 저녁에 반영됩니다.

**Rate Limits Group**: `STOCK_TRADING_TREND`


### `/parameters/1/description`

조회 수 (최대 100)

### `/parameters/2/description`

조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.
미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/daily/summary`

일별 대차거래 (count=2)

### `/responses/200/content/application/json/examples/noData/summary`

조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedMarket/summary`

국내(KR) 종목이 아님

### `/responses/400/content/application/json/examples/invalidCount/summary`

count 가 허용 범위(1~100)를 벗어남

### 전체 연산 정의

````json
{
  "tags": [
    "Stock Info"
  ],
  "summary": "대차거래 동향 조회",
  "description": "국내(KR) 종목의 대차거래 동향을 일별 시계열로 조회합니다. 대차 체결·상환·잔고 수량과\n잔고 금액을 최신순으로 제공합니다.\n\n- 국내(KR) 종목만 지원합니다. 다른 시장의 종목은 400 `unsupported-market` 으로 응답합니다.\n- 모든 금액은 원화(KRW)이며, 별도의 통화 필드는 제공하지 않습니다.\n- 대차거래는 기관 투자자 간 주식 대여·차입 거래입니다. 주식을 빌려 매도하는 개인 신용거래인\n  신용대주(`GET /api/v1/stocks/{symbol}/credit-trades` 의 `stockLoan`)와는 다른 데이터입니다.\n- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.\n\n**데이터 적시성**: 일별 확정치는 해당 일자 저녁에 반영됩니다.\n\n**Rate Limits Group**: `STOCK_TRADING_TREND`\n",
  "operationId": "getStockSecuritiesLending",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/KrSymbol"
    },
    {
      "name": "count",
      "in": "query",
      "required": false,
      "description": "조회 수 (최대 100)",
      "schema": {
        "type": "integer",
        "default": 10,
        "minimum": 1,
        "maximum": 100
      }
    },
    {
      "name": "until",
      "in": "query",
      "required": false,
      "description": "조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.\n미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.\n",
      "schema": {
        "type": "string",
        "format": "date"
      },
      "example": "2026-07-16"
    }
  ],
  "responses": {
    "200": {
      "description": "성공",
      "content": {
        "application/json": {
          "schema": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ApiResponse"
              },
              {
                "type": "object",
                "properties": {
                  "result": {
                    "$ref": "#/components/schemas/SecuritiesLendingResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "daily": {
              "summary": "일별 대차거래 (count=2)",
              "value": {
                "result": {
                  "nextUntil": "2026-07-15",
                  "records": [
                    {
                      "date": "2026-07-17",
                      "updatedAt": "2026-07-17T19:03:21+09:00",
                      "executionQuantity": "210500",
                      "repaymentQuantity": "185300",
                      "balanceQuantity": "15234000",
                      "balanceAmount": "1218720000000"
                    },
                    {
                      "date": "2026-07-16",
                      "updatedAt": "2026-07-16T19:02:45+09:00",
                      "executionQuantity": "198200",
                      "repaymentQuantity": "201400",
                      "balanceQuantity": "15208800",
                      "balanceAmount": "1216704000000"
                    }
                  ]
                }
              }
            },
            "noData": {
              "summary": "조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)",
              "value": {
                "result": {
                  "nextUntil": null,
                  "records": []
                }
              }
            }
          }
        }
      }
    },
    "400": {
      "description": "잘못된 요청",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "unsupportedMarket": {
              "summary": "국내(KR) 종목이 아님",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "unsupported-market",
                  "message": "지원하지 않는 시장의 종목입니다.",
                  "data": {
                    "field": "symbol",
                    "allowedConditions": {
                      "marketCountry": [
                        "KR"
                      ]
                    }
                  }
                }
              }
            },
            "invalidCount": {
              "summary": "count 가 허용 범위(1~100)를 벗어남",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다.",
                  "data": {
                    "field": "count",
                    "constraint": {
                      "min": 1,
                      "max": 100
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "401": {
      "$ref": "#/components/responses/Unauthorized"
    },
    "403": {
      "$ref": "#/components/responses/Forbidden"
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorTradingTrend"
    }
  }
}
````
