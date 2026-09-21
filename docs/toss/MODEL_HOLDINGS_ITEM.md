> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/HoldingsItem.md
> 문서 버전: 1.2.17

# HoldingsItem
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **symbol** | **String** | 종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 티커 | [default to null] |
| **name** | **String** | 종목명 | [default to null] |
| **marketCountry** | [**MarketCountry**](MODEL_MARKET_COUNTRY.md) |  | [default to null] |
| **currency** | [**Currency**](MODEL_CURRENCY.md) |  | [default to null] |
| **quantity** | **BigDecimal** | 보유 수량 | [default to null] |
| **lastPrice** | **BigDecimal** | 현재가. 거래 통화(currency) 기준 | [default to null] |
| **averagePurchasePrice** | **BigDecimal** | 매수 평균가. 거래 통화(currency) 기준 | [default to null] |
| **marketValue** | [**MarketValue**](MODEL_MARKET_VALUE.md) |  | [default to null] |
| **profitLoss** | [**ProfitLoss**](MODEL_PROFIT_LOSS.md) |  | [default to null] |
| **dailyProfitLoss** | [**DailyProfitLoss**](MODEL_DAILY_PROFIT_LOSS.md) |  | [default to null] |
| **cost** | [**Cost**](MODEL_COST.md) |  | [default to null] |




## OpenAPI 원본 스키마

### `/properties/symbol/description`

종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 티커

### `/properties/name/description`

종목명

### `/properties/quantity/description`

보유 수량

### `/properties/lastPrice/description`

현재가. 거래 통화(currency) 기준

### `/properties/averagePurchasePrice/description`

매수 평균가. 거래 통화(currency) 기준

````json
{
  "type": "object",
  "required": [
    "symbol",
    "name",
    "marketCountry",
    "currency",
    "quantity",
    "lastPrice",
    "averagePurchasePrice",
    "marketValue",
    "profitLoss",
    "dailyProfitLoss",
    "cost"
  ],
  "properties": {
    "symbol": {
      "type": "string",
      "description": "종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 티커",
      "example": "005930"
    },
    "name": {
      "type": "string",
      "description": "종목명",
      "example": "삼성전자"
    },
    "marketCountry": {
      "$ref": "#/components/schemas/MarketCountry"
    },
    "currency": {
      "$ref": "#/components/schemas/Currency"
    },
    "quantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "보유 수량",
      "example": "100"
    },
    "lastPrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "현재가. 거래 통화(currency) 기준",
      "example": "72000"
    },
    "averagePurchasePrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "매수 평균가. 거래 통화(currency) 기준",
      "example": "65000"
    },
    "marketValue": {
      "$ref": "#/components/schemas/MarketValue"
    },
    "profitLoss": {
      "$ref": "#/components/schemas/ProfitLoss"
    },
    "dailyProfitLoss": {
      "$ref": "#/components/schemas/DailyProfitLoss"
    },
    "cost": {
      "$ref": "#/components/schemas/Cost"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
