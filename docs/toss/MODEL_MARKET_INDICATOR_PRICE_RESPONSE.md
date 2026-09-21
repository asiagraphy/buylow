> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/MarketIndicatorPriceResponse.md
> 문서 버전: 1.2.17

# MarketIndicatorPriceResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **symbol** | **String** | 시장 지표 심볼. `GET /api/v1/market-indicators/prices` 의 심볼 카탈로그 참조 | [default to null] |
| **timestamp** | **Date** | 데이터 시각. 데이터 미제공 시 null | [optional] [default to null] |
| **lastPrice** | **BigDecimal** | 현재가. 시장 호가 그대로이며, 통화·단위는 심볼 카탈로그를 따릅니다 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/symbol/description`

시장 지표 심볼. `GET /api/v1/market-indicators/prices` 의 심볼 카탈로그 참조

### `/properties/timestamp/description`

데이터 시각. 데이터 미제공 시 null

### `/properties/lastPrice/description`

현재가. 시장 호가 그대로이며, 통화·단위는 심볼 카탈로그를 따릅니다

````json
{
  "type": "object",
  "required": [
    "symbol",
    "lastPrice"
  ],
  "properties": {
    "symbol": {
      "type": "string",
      "description": "시장 지표 심볼. `GET /api/v1/market-indicators/prices` 의 심볼 카탈로그 참조",
      "example": "KOSPI"
    },
    "timestamp": {
      "type": [
        "string",
        "null"
      ],
      "format": "date-time",
      "description": "데이터 시각. 데이터 미제공 시 null",
      "example": "2026-06-11T15:30:00+09:00"
    },
    "lastPrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "현재가. 시장 호가 그대로이며, 통화·단위는 심볼 카탈로그를 따릅니다",
      "example": "2812.45"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
