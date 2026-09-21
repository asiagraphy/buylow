> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Trade.md
> 문서 버전: 1.2.17

# Trade
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **price** | **BigDecimal** | 체결가 | [default to null] |
| **volume** | **BigDecimal** | 체결 수량 | [default to null] |
| **timestamp** | **Date** | 체결 시각 | [default to null] |
| **currency** | [**Currency**](MODEL_CURRENCY.md) |  | [default to null] |




## OpenAPI 원본 스키마

### `/properties/price/description`

체결가

### `/properties/volume/description`

체결 수량

### `/properties/timestamp/description`

체결 시각

````json
{
  "type": "object",
  "required": [
    "price",
    "volume",
    "timestamp",
    "currency"
  ],
  "properties": {
    "price": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "체결가",
      "example": "72000"
    },
    "volume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "체결 수량",
      "example": "120"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time",
      "description": "체결 시각",
      "example": "2026-03-25T09:30:42.000+09:00"
    },
    "currency": {
      "$ref": "#/components/schemas/Currency"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
