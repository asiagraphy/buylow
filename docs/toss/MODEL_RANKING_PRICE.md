> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/RankingPrice.md
> 문서 버전: 1.2.17

# RankingPrice
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **lastPrice** | **BigDecimal** | 현재가 | [default to null] |
| **basePrice** | **BigDecimal** | 기준가. `TOP_GAINERS` / `TOP_LOSERS` 는 `duration` 시작 시점 기준가, 나머지 타입은 `duration` 과 무관하게 항상 전일 기준가.  | [default to null] |
| **changeRate** | **BigDecimal** | 등락률, 소수비율 (`0.0125` = 1.25%). `(lastPrice - basePrice) / basePrice`. `basePrice` 가 0 이면 null. `basePrice` 의 의미를 따라 `TOP_GAINERS` / `TOP_LOSERS` 는 기간 등락률, 나머지 타입은 전일 대비 등락률입니다.  | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/lastPrice/description`

현재가

### `/properties/basePrice/description`

기준가. `TOP_GAINERS` / `TOP_LOSERS` 는 `duration` 시작 시점 기준가,
나머지 타입은 `duration` 과 무관하게 항상 전일 기준가.


### `/properties/changeRate/description`

등락률, 소수비율 (`0.0125` = 1.25%). `(lastPrice - basePrice) / basePrice`.
`basePrice` 가 0 이면 null.
`basePrice` 의 의미를 따라 `TOP_GAINERS` / `TOP_LOSERS` 는 기간 등락률,
나머지 타입은 전일 대비 등락률입니다.


````json
{
  "type": "object",
  "required": [
    "lastPrice",
    "basePrice"
  ],
  "properties": {
    "lastPrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "현재가",
      "example": "56500"
    },
    "basePrice": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "기준가. `TOP_GAINERS` / `TOP_LOSERS` 는 `duration` 시작 시점 기준가,\n나머지 타입은 `duration` 과 무관하게 항상 전일 기준가.\n",
      "example": "55800"
    },
    "changeRate": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "등락률, 소수비율 (`0.0125` = 1.25%). `(lastPrice - basePrice) / basePrice`.\n`basePrice` 가 0 이면 null.\n`basePrice` 의 의미를 따라 `TOP_GAINERS` / `TOP_LOSERS` 는 기간 등락률,\n나머지 타입은 전일 대비 등락률입니다.\n",
      "example": "0.0125"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
