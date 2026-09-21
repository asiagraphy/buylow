> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InvestorTradingAmount.md
> 문서 버전: 1.2.17

# InvestorTradingAmount
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **buyAmount** | **BigDecimal** | 매수 거래대금 (KRW, 정수) | [default to null] |
| **sellAmount** | **BigDecimal** | 매도 거래대금 (KRW, 정수) | [default to null] |




## OpenAPI 원본 스키마

### `/properties/buyAmount/description`

매수 거래대금 (KRW, 정수)

### `/properties/sellAmount/description`

매도 거래대금 (KRW, 정수)

````json
{
  "type": "object",
  "required": [
    "buyAmount",
    "sellAmount"
  ],
  "properties": {
    "buyAmount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "매수 거래대금 (KRW, 정수)",
      "example": "5200000000000"
    },
    "sellAmount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "매도 거래대금 (KRW, 정수)",
      "example": "5350000000000"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
