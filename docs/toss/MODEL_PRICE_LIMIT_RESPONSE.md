> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/PriceLimitResponse.md
> 문서 버전: 1.2.17

# PriceLimitResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **timestamp** | **Date** | 데이터 시각 | [default to null] |
| **upperLimitPrice** | **BigDecimal** | 상한가. 미국 주식 등 가격제한이 없는 시장에서는 null | [optional] [default to null] |
| **lowerLimitPrice** | **BigDecimal** | 하한가. 미국 주식 등 가격제한이 없는 시장에서는 null | [optional] [default to null] |
| **currency** | [**Currency**](MODEL_CURRENCY.md) |  | [default to null] |




## OpenAPI 원본 스키마

### `/properties/timestamp/description`

데이터 시각

### `/properties/upperLimitPrice/description`

상한가. 미국 주식 등 가격제한이 없는 시장에서는 null

### `/properties/lowerLimitPrice/description`

하한가. 미국 주식 등 가격제한이 없는 시장에서는 null

````json
{
  "type": "object",
  "required": [
    "timestamp",
    "currency"
  ],
  "properties": {
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "데이터 시각",
      "example": "2026-03-25T09:30:00.123+09:00"
    },
    "upperLimitPrice": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "상한가. 미국 주식 등 가격제한이 없는 시장에서는 null",
      "example": "93000"
    },
    "lowerLimitPrice": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "하한가. 미국 주식 등 가격제한이 없는 시장에서는 null",
      "example": "50400"
    },
    "currency": {
      "$ref": "#/components/schemas/Currency"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
