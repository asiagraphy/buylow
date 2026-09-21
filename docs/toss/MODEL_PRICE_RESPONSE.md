> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/PriceResponse.md
> 문서 버전: 1.2.17

# PriceResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **symbol** | **String** | 종목 심볼 | [default to null] |
| **timestamp** | **Date** | 데이터 시각. 체결 미발생 등으로 시각이 없을 경우 null | [optional] [default to null] |
| **lastPrice** | **BigDecimal** | 현재가 | [default to null] |
| **currency** | [**Currency**](MODEL_CURRENCY.md) |  | [default to null] |




## OpenAPI 원본 스키마

### `/properties/symbol/description`

종목 심볼

### `/properties/timestamp/description`

데이터 시각. 체결 미발생 등으로 시각이 없을 경우 null

### `/properties/lastPrice/description`

현재가

````json
{
  "type": "object",
  "required": [
    "symbol",
    "lastPrice",
    "currency"
  ],
  "properties": {
    "symbol": {
      "type": "string",
      "description": "종목 심볼",
      "example": "005930"
    },
    "timestamp": {
      "type": [
        "string",
        "null"
      ],
      "format": "date-time",
      "description": "데이터 시각. 체결 미발생 등으로 시각이 없을 경우 null",
      "example": "2026-03-25T09:30:00.123+09:00"
    },
    "lastPrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "현재가",
      "example": "72000"
    },
    "currency": {
      "$ref": "#/components/schemas/Currency"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
