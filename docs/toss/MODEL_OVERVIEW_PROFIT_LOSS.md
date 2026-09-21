> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OverviewProfitLoss.md
> 문서 버전: 1.2.17

# OverviewProfitLoss
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **amount** | [**Price**](MODEL_PRICE.md) | 손익금액 | [default to null] |
| **amountAfterCost** | [**Price**](MODEL_PRICE.md) | 세금/수수료 공제 후 손익금액 | [default to null] |
| **rate** | **BigDecimal** | 손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.1516 = 15.16% | [default to null] |
| **rateAfterCost** | **BigDecimal** | 세금/수수료 공제 후 손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.1406 = 14.06% | [default to null] |




## OpenAPI 원본 스키마

### `/description`

손익. 전체 보유 종목의 통화별 합산

### `/properties/amount/description`

손익금액

### `/properties/amountAfterCost/description`

세금/수수료 공제 후 손익금액

### `/properties/rate/description`

손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.1516 = 15.16%

### `/properties/rateAfterCost/description`

세금/수수료 공제 후 손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.1406 = 14.06%

````json
{
  "type": "object",
  "description": "손익. 전체 보유 종목의 통화별 합산",
  "required": [
    "amount",
    "amountAfterCost",
    "rate",
    "rateAfterCost"
  ],
  "properties": {
    "amount": {
      "description": "손익금액",
      "allOf": [
        {
          "$ref": "#/components/schemas/Price"
        }
      ]
    },
    "amountAfterCost": {
      "description": "세금/수수료 공제 후 손익금액",
      "allOf": [
        {
          "$ref": "#/components/schemas/Price"
        }
      ]
    },
    "rate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.1516 = 15.16%",
      "example": "0.1516"
    },
    "rateAfterCost": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "세금/수수료 공제 후 손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.1406 = 14.06%",
      "example": "0.1406"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
