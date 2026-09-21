> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderExecution.md
> 문서 버전: 1.2.17

# OrderExecution
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **filledQuantity** | **BigDecimal** | 체결 수량 | [default to null] |
| **averageFilledPrice** | **BigDecimal** | 평균 체결 가격 (native currency). 부분 체결 시 체결된 건의 평균, 미체결 시 null | [default to null] |
| **filledAmount** | **BigDecimal** | 총 체결 금액 (native currency) | [default to null] |
| **commission** | **BigDecimal** | 총 체결 수수료 (native currency) | [default to null] |
| **tax** | **BigDecimal** | 총 체결 세금 (native currency) | [default to null] |
| **filledAt** | **Date** | 최종 체결 시간 (ISO 8601, KST) | [default to null] |
| **settlementDate** | **date** | 결제 예정일 (YYYY-MM-DD, KST 기준). 미결제 시 null | [default to null] |




## OpenAPI 원본 스키마

### `/properties/filledQuantity/description`

체결 수량

### `/properties/averageFilledPrice/description`

평균 체결 가격 (native currency). 부분 체결 시 체결된 건의 평균, 미체결 시 null

### `/properties/filledAmount/description`

총 체결 금액 (native currency)

### `/properties/commission/description`

총 체결 수수료 (native currency)

### `/properties/tax/description`

총 체결 세금 (native currency)

### `/properties/filledAt/description`

최종 체결 시간 (ISO 8601, KST)

### `/properties/settlementDate/description`

결제 예정일 (YYYY-MM-DD, KST 기준). 미결제 시 null

````json
{
  "type": "object",
  "required": [
    "filledQuantity",
    "averageFilledPrice",
    "filledAmount",
    "commission",
    "tax",
    "filledAt",
    "settlementDate"
  ],
  "properties": {
    "filledQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "체결 수량",
      "example": "10"
    },
    "averageFilledPrice": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "평균 체결 가격 (native currency). 부분 체결 시 체결된 건의 평균, 미체결 시 null",
      "example": "70000"
    },
    "filledAmount": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "총 체결 금액 (native currency)",
      "example": "700000"
    },
    "commission": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "총 체결 수수료 (native currency)",
      "example": "1400"
    },
    "tax": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "총 체결 세금 (native currency)",
      "example": "0"
    },
    "filledAt": {
      "type": [
        "string",
        "null"
      ],
      "format": "date-time",
      "description": "최종 체결 시간 (ISO 8601, KST)",
      "example": "2026-03-28T09:31:15.000+09:00"
    },
    "settlementDate": {
      "type": [
        "string",
        "null"
      ],
      "format": "date",
      "description": "결제 예정일 (YYYY-MM-DD, KST 기준). 미결제 시 null",
      "example": "2026-03-30"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
