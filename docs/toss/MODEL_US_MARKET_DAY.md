> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/UsMarketDay.md
> 문서 버전: 1.2.17

# UsMarketDay
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **date** | **date** | 영업일 (미국 현지 기준) | [default to null] |
| **dayMarket** | [**UsDayMarketSession**](MODEL_US_DAY_MARKET_SESSION.md) | 데이마켓 세션 (토스증권). 휴장이면 null | [optional] [default to null] |
| **preMarket** | [**UsPreMarketSession**](MODEL_US_PRE_MARKET_SESSION.md) | 프리마켓 세션. 휴장이면 null | [optional] [default to null] |
| **regularMarket** | [**UsRegularMarketSession**](MODEL_US_REGULAR_MARKET_SESSION.md) | 정규장 세션. 휴장이면 null | [optional] [default to null] |
| **afterMarket** | [**UsAfterMarketSession**](MODEL_US_AFTER_MARKET_SESSION.md) | 애프터마켓 세션. 휴장이면 null | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/description`

미국 시장 영업일 정보. 4 세션(`dayMarket`, `preMarket`, `regularMarket`, `afterMarket`) 각각 nullable.
휴장일이면 4 세션 모두 null.


### `/properties/date/description`

영업일 (미국 현지 기준)

### `/properties/dayMarket/description`

데이마켓 세션 (토스증권). 휴장이면 null

### `/properties/preMarket/description`

프리마켓 세션. 휴장이면 null

### `/properties/regularMarket/description`

정규장 세션. 휴장이면 null

### `/properties/afterMarket/description`

애프터마켓 세션. 휴장이면 null

````json
{
  "type": "object",
  "description": "미국 시장 영업일 정보. 4 세션(`dayMarket`, `preMarket`, `regularMarket`, `afterMarket`) 각각 nullable.\n휴장일이면 4 세션 모두 null.\n",
  "required": [
    "date"
  ],
  "properties": {
    "date": {
      "type": "string",
      "format": "date",
      "description": "영업일 (미국 현지 기준)",
      "example": "2026-03-25"
    },
    "dayMarket": {
      "description": "데이마켓 세션 (토스증권). 휴장이면 null",
      "oneOf": [
        {
          "$ref": "#/components/schemas/UsDayMarketSession"
        },
        {
          "type": "null"
        }
      ]
    },
    "preMarket": {
      "description": "프리마켓 세션. 휴장이면 null",
      "oneOf": [
        {
          "$ref": "#/components/schemas/UsPreMarketSession"
        },
        {
          "type": "null"
        }
      ]
    },
    "regularMarket": {
      "description": "정규장 세션. 휴장이면 null",
      "oneOf": [
        {
          "$ref": "#/components/schemas/UsRegularMarketSession"
        },
        {
          "type": "null"
        }
      ]
    },
    "afterMarket": {
      "description": "애프터마켓 세션. 휴장이면 null",
      "oneOf": [
        {
          "$ref": "#/components/schemas/UsAfterMarketSession"
        },
        {
          "type": "null"
        }
      ]
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
