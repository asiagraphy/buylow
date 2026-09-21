> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ExchangeRateResponse.md
> 문서 버전: 1.2.17

# ExchangeRateResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **baseCurrency** | [**Currency**](MODEL_CURRENCY.md) | 기준 통화 | [default to null] |
| **quoteCurrency** | [**Currency**](MODEL_CURRENCY.md) | 표시 통화 (quote currency) | [default to null] |
| **rate** | **BigDecimal** | 매수 환율 (1 baseCurrency = ? quoteCurrency) | [default to null] |
| **midRate** | **BigDecimal** | 매매기준율 (은행간 mid rate) | [default to null] |
| **basisPoint** | **BigDecimal** | 매매기준율(midRate) 대비 basis points. (rate - midRate) / midRate * 10000 | [default to null] |
| **rateChangeType** | **String** | 등락 구분 | [default to null] |
| **validFrom** | **Date** | 환율 유효 시작 시각 | [default to null] |
| **validUntil** | **Date** | 환율 유효 종료 시각 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/baseCurrency/description`

기준 통화

### `/properties/quoteCurrency/description`

표시 통화 (quote currency)

### `/properties/rate/description`

매수 환율 (1 baseCurrency = ? quoteCurrency)

### `/properties/midRate/description`

매매기준율 (은행간 mid rate)

### `/properties/basisPoint/description`

매매기준율(midRate) 대비 basis points. (rate - midRate) / midRate * 10000

### `/properties/rateChangeType/description`

등락 구분

### `/properties/validFrom/description`

환율 유효 시작 시각

### `/properties/validUntil/description`

환율 유효 종료 시각

````json
{
  "type": "object",
  "required": [
    "baseCurrency",
    "quoteCurrency",
    "rate",
    "midRate",
    "basisPoint",
    "rateChangeType",
    "validFrom",
    "validUntil"
  ],
  "properties": {
    "baseCurrency": {
      "$ref": "#/components/schemas/Currency",
      "description": "기준 통화",
      "example": "USD"
    },
    "quoteCurrency": {
      "$ref": "#/components/schemas/Currency",
      "description": "표시 통화 (quote currency)",
      "example": "KRW"
    },
    "rate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "매수 환율 (1 baseCurrency = ? quoteCurrency)",
      "example": "1380.5"
    },
    "midRate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "매매기준율 (은행간 mid rate)",
      "example": "1375"
    },
    "basisPoint": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "매매기준율(midRate) 대비 basis points. (rate - midRate) / midRate * 10000",
      "example": "40"
    },
    "rateChangeType": {
      "type": "string",
      "description": "등락 구분",
      "enum": [
        "UP",
        "EQUAL",
        "DOWN"
      ],
      "example": "UP"
    },
    "validFrom": {
      "type": "string",
      "format": "date-time",
      "description": "환율 유효 시작 시각",
      "example": "2026-03-25T09:30:00+09:00"
    },
    "validUntil": {
      "type": "string",
      "format": "date-time",
      "description": "환율 유효 종료 시각",
      "example": "2026-03-25T09:31:00+09:00"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
