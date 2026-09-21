> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/UsMarketCalendarResponse.md
> 문서 버전: 1.2.17

# UsMarketCalendarResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **today** | [**UsMarketDay**](MODEL_US_MARKET_DAY.md) |  | [default to null] |
| **previousBusinessDay** | [**UsMarketDay**](MODEL_US_MARKET_DAY.md) |  | [default to null] |
| **nextBusinessDay** | [**UsMarketDay**](MODEL_US_MARKET_DAY.md) |  | [default to null] |




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
      "$ref": "#/components/schemas/UsMarketDay"
    },
    "previousBusinessDay": {
      "$ref": "#/components/schemas/UsMarketDay"
    },
    "nextBusinessDay": {
      "$ref": "#/components/schemas/UsMarketDay"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
