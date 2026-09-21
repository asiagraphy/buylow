> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/RankingResponse.md
> 문서 버전: 1.2.17

# RankingResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **rankedAt** | **Date** | 랭킹 집계 기준 시각. `rankings` 가 빈 배열이면 null | [optional] [default to null] |
| **rankings** | [**List**](MODEL_RANKING_ITEM.md) | 랭킹 종목 목록 (순위 오름차순). 집계 데이터가 없으면 빈 배열. 항목 수는 `count` 이하일 수 있습니다. | [default to null] |




## OpenAPI 원본 스키마

### `/properties/rankedAt/description`

랭킹 집계 기준 시각. `rankings` 가 빈 배열이면 null

### `/properties/rankings/description`

랭킹 종목 목록 (순위 오름차순). 집계 데이터가 없으면 빈 배열. 항목 수는 `count` 이하일 수 있습니다.

````json
{
  "type": "object",
  "required": [
    "rankings"
  ],
  "properties": {
    "rankedAt": {
      "type": [
        "string",
        "null"
      ],
      "format": "date-time",
      "description": "랭킹 집계 기준 시각. `rankings` 가 빈 배열이면 null",
      "example": "2026-06-10T14:30:00+09:00"
    },
    "rankings": {
      "type": "array",
      "description": "랭킹 종목 목록 (순위 오름차순). 집계 데이터가 없으면 빈 배열. 항목 수는 `count` 이하일 수 있습니다.",
      "items": {
        "$ref": "#/components/schemas/RankingItem"
      }
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
