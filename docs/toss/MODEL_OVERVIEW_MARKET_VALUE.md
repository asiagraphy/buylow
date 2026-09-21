> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OverviewMarketValue.md
> 문서 버전: 1.2.17

# OverviewMarketValue
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **amount** | [**Price**](MODEL_PRICE.md) | 시장 평가금액 | [default to null] |
| **amountAfterCost** | [**Price**](MODEL_PRICE.md) | 세금/수수료 공제 후 평가금액 | [default to null] |




## OpenAPI 원본 스키마

### `/description`

시장 평가금액. 전체 보유 종목의 통화별 합산

### `/properties/amount/description`

시장 평가금액

### `/properties/amountAfterCost/description`

세금/수수료 공제 후 평가금액

````json
{
  "type": "object",
  "description": "시장 평가금액. 전체 보유 종목의 통화별 합산",
  "required": [
    "amount",
    "amountAfterCost"
  ],
  "properties": {
    "amount": {
      "description": "시장 평가금액",
      "allOf": [
        {
          "$ref": "#/components/schemas/Price"
        }
      ]
    },
    "amountAfterCost": {
      "description": "세금/수수료 공제 후 평가금액",
      "allOf": [
        {
          "$ref": "#/components/schemas/Price"
        }
      ]
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
