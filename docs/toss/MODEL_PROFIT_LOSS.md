> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ProfitLoss.md
> 문서 버전: 1.2.17

# ProfitLoss
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **amount** | **BigDecimal** | 손익금액 | [default to null] |
| **amountAfterCost** | **BigDecimal** | 세금/수수료 공제 후 손익금액 | [default to null] |
| **rate** | **BigDecimal** | 손익률. 소수비율 (0.1077 = 10.77%) | [default to null] |
| **rateAfterCost** | **BigDecimal** | 세금/수수료 공제 후 손익률. 소수비율 (0.0846 = 8.46%) | [default to null] |




## OpenAPI 원본 스키마

### `/description`

손익. 거래 통화(currency) 기준

### `/properties/amount/description`

손익금액

### `/properties/amountAfterCost/description`

세금/수수료 공제 후 손익금액

### `/properties/rate/description`

손익률. 소수비율 (0.1077 = 10.77%)

### `/properties/rateAfterCost/description`

세금/수수료 공제 후 손익률. 소수비율 (0.0846 = 8.46%)

````json
{
  "type": "object",
  "description": "손익. 거래 통화(currency) 기준",
  "required": [
    "amount",
    "amountAfterCost",
    "rate",
    "rateAfterCost"
  ],
  "properties": {
    "amount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "손익금액",
      "example": "700000"
    },
    "amountAfterCost": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "세금/수수료 공제 후 손익금액",
      "example": "550000"
    },
    "rate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "손익률. 소수비율 (0.1077 = 10.77%)",
      "example": "0.1077"
    },
    "rateAfterCost": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "세금/수수료 공제 후 손익률. 소수비율 (0.0846 = 8.46%)",
      "example": "0.0846"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
