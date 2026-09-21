> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/RankingItem.md
> 문서 버전: 1.2.17

# RankingItem
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **rank** | **Integer** | 순위. 1부터 시작 | [default to null] |
| **symbol** | **String** | 종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL) | [default to null] |
| **currency** | [**Currency**](MODEL_CURRENCY.md) |  | [default to null] |
| **price** | [**RankingPrice**](MODEL_RANKING_PRICE.md) |  | [default to null] |
| **tradingVolume** | **BigDecimal** | 거래량 (`duration` 누적). 집계 기준은 `type` 이 결정합니다 — `TOSS_SECURITIES_*` 는 토스증권 체결 기준, 그 외(`MARKET_*` / `TOP_*`)는 시장 전체 기준.  | [default to null] |
| **tradingAmount** | **BigDecimal** | 거래대금 (`duration` 누적). 집계 기준은 `tradingVolume` 과 동일합니다. | [default to null] |




## OpenAPI 원본 스키마

### `/properties/rank/description`

순위. 1부터 시작

### `/properties/symbol/description`

종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL)

### `/properties/tradingVolume/description`

거래량 (`duration` 누적). 집계 기준은 `type` 이 결정합니다 —
`TOSS_SECURITIES_*` 는 토스증권 체결 기준, 그 외(`MARKET_*` / `TOP_*`)는 시장 전체 기준.


### `/properties/tradingAmount/description`

거래대금 (`duration` 누적). 집계 기준은 `tradingVolume` 과 동일합니다.

````json
{
  "type": "object",
  "required": [
    "rank",
    "symbol",
    "currency",
    "price",
    "tradingVolume",
    "tradingAmount"
  ],
  "properties": {
    "rank": {
      "type": "integer",
      "description": "순위. 1부터 시작",
      "example": 1
    },
    "symbol": {
      "type": "string",
      "description": "종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL)",
      "example": "005930"
    },
    "currency": {
      "$ref": "#/components/schemas/Currency"
    },
    "price": {
      "$ref": "#/components/schemas/RankingPrice"
    },
    "tradingVolume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "거래량 (`duration` 누적). 집계 기준은 `type` 이 결정합니다 —\n`TOSS_SECURITIES_*` 는 토스증권 체결 기준, 그 외(`MARKET_*` / `TOP_*`)는 시장 전체 기준.\n",
      "example": "18432100"
    },
    "tradingAmount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "거래대금 (`duration` 누적). 집계 기준은 `tradingVolume` 과 동일합니다.",
      "example": "1041436650000"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
