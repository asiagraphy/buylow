> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OverviewDailyProfitLoss.md
> 문서 버전: 1.2.17

# OverviewDailyProfitLoss
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **amount** | [**Price**](MODEL_PRICE.md) | 일간 손익금액 | [default to null] |
| **rate** | **BigDecimal** | 일간 손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.0185 = 1.85% | [default to null] |




## OpenAPI 원본 스키마

### `/description`

일간 손익. 전체 보유 종목의 통화별 합산

### `/properties/amount/description`

일간 손익금액

### `/properties/rate/description`

일간 손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.0185 = 1.85%

````json
{
  "type": "object",
  "description": "일간 손익. 전체 보유 종목의 통화별 합산",
  "required": [
    "amount",
    "rate"
  ],
  "properties": {
    "amount": {
      "description": "일간 손익금액",
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
      "description": "일간 손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.0185 = 1.85%",
      "example": "0.0185"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
