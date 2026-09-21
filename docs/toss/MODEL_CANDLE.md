> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Candle.md
> 문서 버전: 1.2.17

# Candle
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **timestamp** | **Date** | 봉 기준 시각 - `1m`: 봉 종료 시각. 해당 봉은 `[timestamp - 1분, timestamp)` 구간의 체결을 집계합니다. - `1d`: 해당 거래일 (시각은 현지 자정 고정)  | [default to null] |
| **openPrice** | **BigDecimal** | 시가 | [default to null] |
| **highPrice** | **BigDecimal** | 고가 | [default to null] |
| **lowPrice** | **BigDecimal** | 저가 | [default to null] |
| **closePrice** | **BigDecimal** | 종가 | [default to null] |
| **volume** | **BigDecimal** | 거래량 | [default to null] |
| **currency** | [**Currency**](MODEL_CURRENCY.md) |  | [default to null] |




## OpenAPI 원본 스키마

### `/properties/timestamp/description`

봉 기준 시각
- `1m`: 봉 종료 시각. 해당 봉은 `[timestamp - 1분, timestamp)` 구간의 체결을 집계합니다.
- `1d`: 해당 거래일 (시각은 현지 자정 고정)


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
    "volume",
    "currency"
  ],
  "properties": {
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "봉 기준 시각\n- `1m`: 봉 종료 시각. 해당 봉은 `[timestamp - 1분, timestamp)` 구간의 체결을 집계합니다.\n- `1d`: 해당 거래일 (시각은 현지 자정 고정)\n",
      "example": "2026-03-25T09:00:00+09:00"
    },
    "openPrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "시가",
      "example": "71600"
    },
    "highPrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "고가",
      "example": "72300"
    },
    "lowPrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "저가",
      "example": "71500"
    },
    "closePrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "종가",
      "example": "72000"
    },
    "volume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "거래량",
      "example": "3521000"
    },
    "currency": {
      "$ref": "#/components/schemas/Currency"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
