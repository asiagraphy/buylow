> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/KrMarketCalendarResponse.md
> 문서 버전: 1.2.17

# KrMarketCalendarResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **today** | [**KrMarketDay**](MODEL_KR_MARKET_DAY.md) |  | [default to null] |
| **previousBusinessDay** | [**KrMarketDay**](MODEL_KR_MARKET_DAY.md) |  | [default to null] |
| **nextBusinessDay** | [**KrMarketDay**](MODEL_KR_MARKET_DAY.md) |  | [default to null] |




## OpenAPI 원본 스키마


````json
{
  "type": "object",
  "required": [
    "today",
    "previousBusinessDay",
    "nextBusinessDay"
  ],
  "properties": {
    "today": {
      "$ref": "#/components/schemas/KrMarketDay"
    },
    "previousBusinessDay": {
      "$ref": "#/components/schemas/KrMarketDay"
    },
    "nextBusinessDay": {
      "$ref": "#/components/schemas/KrMarketDay"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
