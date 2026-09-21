> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/SellableQuantityResponse.md
> 문서 버전: 1.2.17

# SellableQuantityResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **sellableQuantity** | **BigDecimal** | 판매 가능 수량. KR: 정수 (주 단위). US: 소수점 포함 가능 (주 단위).  | [default to null] |




## OpenAPI 원본 스키마

### `/properties/sellableQuantity/description`

판매 가능 수량.
KR: 정수 (주 단위). US: 소수점 포함 가능 (주 단위).


````json
{
  "type": "object",
  "required": [
    "sellableQuantity"
  ],
  "properties": {
    "sellableQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "판매 가능 수량.\nKR: 정수 (주 단위). US: 소수점 포함 가능 (주 단위).\n",
      "example": "100"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
