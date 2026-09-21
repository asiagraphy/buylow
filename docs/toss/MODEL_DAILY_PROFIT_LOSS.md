> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/DailyProfitLoss.md
> 문서 버전: 1.2.17

# DailyProfitLoss
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **amount** | **BigDecimal** | 일간 손익금액 | [default to null] |
| **rate** | **BigDecimal** | 일간 손익률. 소수비율 (0.0141 = 1.41%) | [default to null] |




## OpenAPI 원본 스키마

### `/description`

일간 손익. 거래 통화(currency) 기준

### `/properties/amount/description`

일간 손익금액

### `/properties/rate/description`

일간 손익률. 소수비율 (0.0141 = 1.41%)

````json
{
  "type": "object",
  "description": "일간 손익. 거래 통화(currency) 기준",
  "required": [
    "amount",
    "rate"
  ],
  "properties": {
    "amount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "일간 손익금액",
      "example": "100000"
    },
    "rate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "일간 손익률. 소수비율 (0.0141 = 1.41%)",
      "example": "0.0141"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
