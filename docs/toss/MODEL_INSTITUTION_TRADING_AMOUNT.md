> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InstitutionTradingAmount.md
> 문서 버전: 1.2.17

# InstitutionTradingAmount
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **buyAmount** | **BigDecimal** | 기관 합계 매수 거래대금 (KRW, 정수). `breakdown` 7개 항목의 `buyAmount` 합과 일치 | [default to null] |
| **sellAmount** | **BigDecimal** | 기관 합계 매도 거래대금 (KRW, 정수). `breakdown` 7개 항목의 `sellAmount` 합과 일치 | [default to null] |
| **breakdown** | [**InstitutionTradingBreakdown**](MODEL_INSTITUTION_TRADING_BREAKDOWN.md) |  | [default to null] |




## OpenAPI 원본 스키마

### `/properties/buyAmount/description`

기관 합계 매수 거래대금 (KRW, 정수). `breakdown` 7개 항목의 `buyAmount` 합과 일치

### `/properties/sellAmount/description`

기관 합계 매도 거래대금 (KRW, 정수). `breakdown` 7개 항목의 `sellAmount` 합과 일치

````json
{
  "type": "object",
  "required": [
    "buyAmount",
    "sellAmount",
    "breakdown"
  ],
  "properties": {
    "buyAmount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "기관 합계 매수 거래대금 (KRW, 정수). `breakdown` 7개 항목의 `buyAmount` 합과 일치",
      "example": "2100000000000"
    },
    "sellAmount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "기관 합계 매도 거래대금 (KRW, 정수). `breakdown` 7개 항목의 `sellAmount` 합과 일치",
      "example": "2180000000000"
    },
    "breakdown": {
      "$ref": "#/components/schemas/InstitutionTradingBreakdown"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
