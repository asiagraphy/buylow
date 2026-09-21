> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Cost.md
> 문서 버전: 1.2.17

# Cost
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **commission** | **BigDecimal** | 수수료 | [default to null] |
| **tax** | **BigDecimal** | 세금. 세금이 없는 경우 null | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/description`

비용. 거래 통화(currency) 기준

### `/properties/commission/description`

수수료

### `/properties/tax/description`

세금. 세금이 없는 경우 null

````json
{
  "type": "object",
  "description": "비용. 거래 통화(currency) 기준",
  "required": [
    "commission"
  ],
  "properties": {
    "commission": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "수수료",
      "example": "14400"
    },
    "tax": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "세금. 세금이 없는 경우 null",
      "example": "135600"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
