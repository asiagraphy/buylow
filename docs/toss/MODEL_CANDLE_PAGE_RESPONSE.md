> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/CandlePageResponse.md
> 문서 버전: 1.2.17

# CandlePageResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **candles** | [**List**](MODEL_CANDLE.md) | 캔들 목록. 최신순(`timestamp` 내림차순) 정렬 — 배열 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다. | [default to null] |
| **nextBefore** | **Date** | 다음 페이지 조회 시 `before` 쿼리 파라미터에 그대로 전달. 마지막 페이지면 null. | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/candles/description`

캔들 목록. 최신순(`timestamp` 내림차순) 정렬 — 배열 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다.

### `/properties/nextBefore/description`

다음 페이지 조회 시 `before` 쿼리 파라미터에 그대로 전달. 마지막 페이지면 null.

````json
{
  "type": "object",
  "required": [
    "candles"
  ],
  "properties": {
    "candles": {
      "type": "array",
      "description": "캔들 목록. 최신순(`timestamp` 내림차순) 정렬 — 배열 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다.",
      "items": {
        "$ref": "#/components/schemas/Candle"
      }
    },
    "nextBefore": {
      "type": [
        "string",
        "null"
      ],
      "format": "date-time",
      "description": "다음 페이지 조회 시 `before` 쿼리 파라미터에 그대로 전달. 마지막 페이지면 null."
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
