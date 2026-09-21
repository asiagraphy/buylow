> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/PreMarketSession.md
> 문서 버전: 1.2.17

# PreMarketSession
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **startTime** | **Date** | 프리마켓 시작 | [default to null] |
| **singlePriceAuctionStartTime** | **Date** | 프리마켓 내 시가단일가 구간 시작 (NXT 프리마켓 접속매매 종료). 단일가 정보 결손 시 null | [optional] [default to null] |
| **endTime** | **Date** | 프리마켓 종료 (시가단일가 종료) | [default to null] |




## OpenAPI 원본 스키마

### `/description`

프리마켓 세션

### `/properties/startTime/description`

프리마켓 시작

### `/properties/singlePriceAuctionStartTime/description`

프리마켓 내 시가단일가 구간 시작 (NXT 프리마켓 접속매매 종료). 단일가 정보 결손 시 null

### `/properties/endTime/description`

프리마켓 종료 (시가단일가 종료)

````json
{
  "type": "object",
  "description": "프리마켓 세션",
  "required": [
    "startTime",
    "endTime"
  ],
  "properties": {
    "startTime": {
      "type": "string",
      "format": "date-time",
      "description": "프리마켓 시작",
      "example": "2026-03-25T08:00:00+09:00"
    },
    "singlePriceAuctionStartTime": {
      "description": "프리마켓 내 시가단일가 구간 시작 (NXT 프리마켓 접속매매 종료). 단일가 정보 결손 시 null",
      "example": "2026-03-25T08:50:00+09:00",
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
      "description": "프리마켓 종료 (시가단일가 종료)",
      "example": "2026-03-25T09:00:00+09:00"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
