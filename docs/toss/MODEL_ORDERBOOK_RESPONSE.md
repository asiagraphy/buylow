> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderbookResponse.md
> 문서 버전: 1.2.17

# OrderbookResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **timestamp** | **Date** | 데이터 시각. 데이터 미제공 시 null | [optional] [default to null] |
| **currency** | [**Currency**](MODEL_CURRENCY.md) |  | [default to null] |
| **asks** | [**List**](MODEL_ORDERBOOK_ENTRY.md) | 매도호가 목록 (낮은 가격순) | [default to null] |
| **bids** | [**List**](MODEL_ORDERBOOK_ENTRY.md) | 매수호가 목록 (높은 가격순) | [default to null] |




## OpenAPI 원본 스키마

### `/properties/timestamp/description`

데이터 시각. 데이터 미제공 시 null

### `/properties/asks/description`

매도호가 목록 (낮은 가격순)

### `/properties/bids/description`

매수호가 목록 (높은 가격순)

````json
{
  "type": "object",
  "required": [
    "currency",
    "asks",
    "bids"
  ],
  "properties": {
    "timestamp": {
      "type": [
        "string",
        "null"
      ],
      "format": "date-time",
      "description": "데이터 시각. 데이터 미제공 시 null",
      "example": "2026-03-25T09:30:00.123+09:00"
    },
    "currency": {
      "$ref": "#/components/schemas/Currency"
    },
    "asks": {
      "type": "array",
      "description": "매도호가 목록 (낮은 가격순)",
      "items": {
        "$ref": "#/components/schemas/OrderbookEntry"
      }
    },
    "bids": {
      "type": "array",
      "description": "매수호가 목록 (높은 가격순)",
      "items": {
        "$ref": "#/components/schemas/OrderbookEntry"
      }
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
