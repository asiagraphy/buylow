> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/UsRegularMarketSession.md
> 문서 버전: 1.2.17

# UsRegularMarketSession
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **startTime** | **Date** | 정규장 시작 | [default to null] |
| **endTime** | **Date** | 정규장 종료 | [default to null] |




## OpenAPI 원본 스키마

### `/description`

정규장 세션

### `/properties/startTime/description`

정규장 시작

### `/properties/endTime/description`

정규장 종료

````json
{
  "type": "object",
  "description": "정규장 세션",
  "required": [
    "startTime",
    "endTime"
  ],
  "properties": {
    "startTime": {
      "type": "string",
      "format": "date-time",
      "description": "정규장 시작",
      "example": "2026-03-25T22:30:00+09:00"
    },
    "endTime": {
      "type": "string",
      "format": "date-time",
      "description": "정규장 종료",
      "example": "2026-03-26T05:00:00+09:00"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
