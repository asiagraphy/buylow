> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/MarketIndicatorCandle.md
> 문서 버전: 1.2.17

# MarketIndicatorCandle
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **timestamp** | **Date** | 봉 시작 시각 | [default to null] |
| **openPrice** | **BigDecimal** | 시가 | [default to null] |
| **highPrice** | **BigDecimal** | 고가 | [default to null] |
| **lowPrice** | **BigDecimal** | 저가 | [default to null] |
| **closePrice** | **BigDecimal** | 종가 | [default to null] |
| **volume** | **BigDecimal** | 거래량 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/timestamp/description`

봉 시작 시각

### `/properties/openPrice/description`

시가

### `/properties/highPrice/description`

고가

### `/properties/lowPrice/description`

저가

### `/properties/closePrice/description`

종가

### `/properties/volume/description`

거래량

````json
{
  "type": "object",
  "required": [
    "timestamp",
    "openPrice",
    "highPrice",
    "lowPrice",
    "closePrice",
    "volume"
  ],
  "properties": {
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "봉 시작 시각",
      "example": "2026-06-11T09:00:00+09:00"
    },
    "openPrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "시가",
      "example": "2798.32"
    },
    "highPrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "고가",
      "example": "2820.15"
    },
    "lowPrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "저가",
      "example": "2790.1"
    },
    "closePrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "종가",
      "example": "2812.45"
    },
    "volume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "거래량",
      "example": "542000000"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
