> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/HoldingsOverview.md
> 문서 버전: 1.2.17

# HoldingsOverview
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **totalPurchaseAmount** | [**Price**](MODEL_PRICE.md) | 투자원금. 전체 보유 종목의 통화별 합산 | [default to null] |
| **marketValue** | [**OverviewMarketValue**](MODEL_OVERVIEW_MARKET_VALUE.md) |  | [default to null] |
| **profitLoss** | [**OverviewProfitLoss**](MODEL_OVERVIEW_PROFIT_LOSS.md) |  | [default to null] |
| **dailyProfitLoss** | [**OverviewDailyProfitLoss**](MODEL_OVERVIEW_DAILY_PROFIT_LOSS.md) |  | [default to null] |
| **items** | [**List**](MODEL_HOLDINGS_ITEM.md) | 보유 종목 목록. 보유 종목이 없으면 빈 배열 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/totalPurchaseAmount/description`

투자원금. 전체 보유 종목의 통화별 합산

### `/properties/items/description`

보유 종목 목록. 보유 종목이 없으면 빈 배열

````json
{
  "type": "object",
  "required": [
    "totalPurchaseAmount",
    "marketValue",
    "profitLoss",
    "dailyProfitLoss",
    "items"
  ],
  "properties": {
    "totalPurchaseAmount": {
      "description": "투자원금. 전체 보유 종목의 통화별 합산",
      "allOf": [
        {
          "$ref": "#/components/schemas/Price"
        }
      ]
    },
    "marketValue": {
      "$ref": "#/components/schemas/OverviewMarketValue"
    },
    "profitLoss": {
      "$ref": "#/components/schemas/OverviewProfitLoss"
    },
    "dailyProfitLoss": {
      "$ref": "#/components/schemas/OverviewDailyProfitLoss"
    },
    "items": {
      "type": "array",
      "description": "보유 종목 목록. 보유 종목이 없으면 빈 배열",
      "items": {
        "$ref": "#/components/schemas/HoldingsItem"
      }
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
