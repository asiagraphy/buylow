> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/BuyingPowerResponse.md
> 문서 버전: 1.2.17

# BuyingPowerResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **currency** | [**Currency**](MODEL_CURRENCY.md) |  | [default to null] |
| **cashBuyingPower** | **BigDecimal** | 현금 기반 매수 가능 금액 (미수 미발생 기준). 순수 현금으로 매수할 수 있는 금액. KRW: 정수 (원 단위). USD: 소수점 포함 (달러 단위).  | [default to null] |




## OpenAPI 원본 스키마

### `/properties/cashBuyingPower/description`

현금 기반 매수 가능 금액 (미수 미발생 기준).
순수 현금으로 매수할 수 있는 금액.
KRW: 정수 (원 단위). USD: 소수점 포함 (달러 단위).


````json
{
  "type": "object",
  "required": [
    "currency",
    "cashBuyingPower"
  ],
  "properties": {
    "currency": {
      "$ref": "#/components/schemas/Currency"
    },
    "cashBuyingPower": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "현금 기반 매수 가능 금액 (미수 미발생 기준).\n순수 현금으로 매수할 수 있는 금액.\nKRW: 정수 (원 단위). USD: 소수점 포함 (달러 단위).\n",
      "example": "5000000"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
