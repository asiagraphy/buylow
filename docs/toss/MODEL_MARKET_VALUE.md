> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/MarketValue.md
> 문서 버전: 1.2.17

# MarketValue
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **purchaseAmount** | **BigDecimal** | 매입금액 | [default to null] |
| **amount** | **BigDecimal** | 시장 평가금액 | [default to null] |
| **amountAfterCost** | **BigDecimal** | 세금/수수료 공제 후 평가금액 | [default to null] |




## OpenAPI 원본 스키마

### `/description`

시장 평가. 거래 통화(currency) 기준

### `/properties/purchaseAmount/description`

매입금액

### `/properties/amount/description`

시장 평가금액

### `/properties/amountAfterCost/description`

세금/수수료 공제 후 평가금액

````json
{
  "type": "object",
  "description": "시장 평가. 거래 통화(currency) 기준",
  "required": [
    "purchaseAmount",
    "amount",
    "amountAfterCost"
  ],
  "properties": {
    "purchaseAmount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "매입금액",
      "example": "6500000"
    },
    "amount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "시장 평가금액",
      "example": "7200000"
    },
    "amountAfterCost": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "세금/수수료 공제 후 평가금액",
      "example": "7050000"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
