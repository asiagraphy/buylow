> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/SecuritiesLendingRecord.md
> 문서 버전: 1.2.17

# SecuritiesLendingRecord
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **date** | **date** | 매매 기준일 | [default to null] |
| **updatedAt** | **Date** | 해당 기록의 마지막 갱신 시각 | [default to null] |
| **executionQuantity** | **BigDecimal** | 대차 체결 수량 (주, 정수) | [default to null] |
| **repaymentQuantity** | **BigDecimal** | 대차 상환 수량 (주, 정수) | [default to null] |
| **balanceQuantity** | **BigDecimal** | 대차 잔고 수량 (주, 정수) | [default to null] |
| **balanceAmount** | **BigDecimal** | 대차 잔고 금액 (KRW, 정수) | [default to null] |




## OpenAPI 원본 스키마

### `/properties/date/description`

매매 기준일

### `/properties/updatedAt/description`

해당 기록의 마지막 갱신 시각

### `/properties/executionQuantity/description`

대차 체결 수량 (주, 정수)

### `/properties/repaymentQuantity/description`

대차 상환 수량 (주, 정수)

### `/properties/balanceQuantity/description`

대차 잔고 수량 (주, 정수)

### `/properties/balanceAmount/description`

대차 잔고 금액 (KRW, 정수)

````json
{
  "type": "object",
  "required": [
    "date",
    "updatedAt",
    "executionQuantity",
    "repaymentQuantity",
    "balanceQuantity",
    "balanceAmount"
  ],
  "properties": {
    "date": {
      "type": "string",
      "format": "date",
      "description": "매매 기준일",
      "example": "2026-07-17"
    },
    "updatedAt": {
      "type": "string",
      "format": "date-time",
      "description": "해당 기록의 마지막 갱신 시각",
      "example": "2026-07-17T19:03:21+09:00"
    },
    "executionQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "대차 체결 수량 (주, 정수)",
      "example": "210500"
    },
    "repaymentQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "대차 상환 수량 (주, 정수)",
      "example": "185300"
    },
    "balanceQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "대차 잔고 수량 (주, 정수)",
      "example": "15234000"
    },
    "balanceAmount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "대차 잔고 금액 (KRW, 정수)",
      "example": "1218720000000"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
