> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/RegularMarketSession.md
> 문서 버전: 1.2.17

# RegularMarketSession
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **startTime** | **Date** | 정규장 시작. 가장 이른 KRX/NXT 정규장 시작 시각 | [default to null] |
| **singlePriceAuctionStartTime** | **Date** | 정규장 내 종가단일가 구간 시작 (KRX 기준). KRX 휴장이면 null | [optional] [default to null] |
| **endTime** | **Date** | 정규장 종료 (종가단일가 종료) | [default to null] |




## OpenAPI 원본 스키마

### `/description`

정규장 세션. KRX·NXT 정규장의 합집합(가장 이른 시작 ~ 가장 늦은 종료). 종가단일가 구간을 포함

### `/properties/startTime/description`

정규장 시작. 가장 이른 KRX/NXT 정규장 시작 시각

### `/properties/singlePriceAuctionStartTime/description`

정규장 내 종가단일가 구간 시작 (KRX 기준). KRX 휴장이면 null

### `/properties/endTime/description`

정규장 종료 (종가단일가 종료)

````json
{
  "type": "object",
  "description": "정규장 세션. KRX·NXT 정규장의 합집합(가장 이른 시작 ~ 가장 늦은 종료). 종가단일가 구간을 포함",
  "required": [
    "startTime",
    "endTime"
  ],
  "properties": {
    "startTime": {
      "type": "string",
      "format": "date-time",
      "description": "정규장 시작. 가장 이른 KRX/NXT 정규장 시작 시각",
      "example": "2026-03-25T09:00:00+09:00"
    },
    "singlePriceAuctionStartTime": {
      "description": "정규장 내 종가단일가 구간 시작 (KRX 기준). KRX 휴장이면 null",
      "example": "2026-03-25T15:20:00+09:00",
      "oneOf": [
        {
          "type": "string",
          "format": "date-time"
        },
        {
          "type": "null"
        }
      ]
    },
    "endTime": {
      "type": "string",
      "format": "date-time",
      "description": "정규장 종료 (종가단일가 종료)",
      "example": "2026-03-25T15:30:00+09:00"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
