> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/UsDayMarketSession.md
> 문서 버전: 1.2.17

# UsDayMarketSession
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **startTime** | **Date** | 데이마켓 시작 | [default to null] |
| **endTime** | **Date** | 데이마켓 종료 | [default to null] |




## OpenAPI 원본 스키마

### `/description`

데이마켓 세션 (토스증권)

### `/properties/startTime/description`

데이마켓 시작

### `/properties/endTime/description`

데이마켓 종료

````json
{
  "type": "object",
  "description": "데이마켓 세션 (토스증권)",
  "required": [
    "startTime",
    "endTime"
  ],
  "properties": {
    "startTime": {
      "type": "string",
      "format": "date-time",
      "description": "데이마켓 시작",
      "example": "2026-03-25T09:00:00+09:00"
    },
    "endTime": {
      "type": "string",
      "format": "date-time",
      "description": "데이마켓 종료",
      "example": "2026-03-25T16:50:00+09:00"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
