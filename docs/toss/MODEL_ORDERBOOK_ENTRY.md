> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderbookEntry.md
> 문서 버전: 1.2.17

# OrderbookEntry
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **price** | **BigDecimal** | 호가 | [default to null] |
| **volume** | **BigDecimal** | 잔량 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/price/description`

호가

### `/properties/volume/description`

잔량

````json
{
  "type": "object",
  "required": [
    "price",
    "volume"
  ],
  "properties": {
    "price": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "호가",
      "example": "72100"
    },
    "volume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "잔량",
      "example": "8500"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
