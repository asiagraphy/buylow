> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ForeignerHolding.md
> 문서 버전: 1.2.17

# ForeignerHolding
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **holdingQuantity** | **BigDecimal** | 외국인 보유 주식 수 (주, 정수) | [default to null] |
| **limitQuantity** | **BigDecimal** | 외국인 보유 한도 주식 수 (주, 정수) | [default to null] |
| **holdingRate** | **BigDecimal** | 외국인 보유 비율 (소수 비율). 상장주식수 대비 보유 주식 수. 예: `0.5089` = 50.89% | [default to null] |




## OpenAPI 원본 스키마

### `/properties/holdingQuantity/description`

외국인 보유 주식 수 (주, 정수)

### `/properties/limitQuantity/description`

외국인 보유 한도 주식 수 (주, 정수)

### `/properties/holdingRate/description`

외국인 보유 비율 (소수 비율). 상장주식수 대비 보유 주식 수. 예: `0.5089` = 50.89%

````json
{
  "type": "object",
  "required": [
    "holdingQuantity",
    "limitQuantity",
    "holdingRate"
  ],
  "properties": {
    "holdingQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "외국인 보유 주식 수 (주, 정수)",
      "example": "3012456789"
    },
    "limitQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "외국인 보유 한도 주식 수 (주, 정수)",
      "example": "5919637922"
    },
    "holdingRate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "외국인 보유 비율 (소수 비율). 상장주식수 대비 보유 주식 수. 예: `0.5089` = 50.89%",
      "example": "0.5089"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
