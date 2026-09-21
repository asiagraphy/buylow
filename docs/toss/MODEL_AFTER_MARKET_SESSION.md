> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/AfterMarketSession.md
> 문서 버전: 1.2.17

# AfterMarketSession
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **startTime** | **Date** | 애프터마켓 시작. 가장 이른 KRX/NXT 애프터마켓 시작 시각 | [default to null] |
| **singlePriceAuctionEndTime** | **Date** | 애프터마켓 내 시가단일가 구간 종료 (NXT 기준). NXT 애프터마켓이 휴장이면 null | [optional] [default to null] |
| **endTime** | **Date** | 애프터마켓 전체 종료. 가장 늦은 KRX/NXT 애프터마켓 종료 시각 | [default to null] |




## OpenAPI 원본 스키마

### `/description`

애프터마켓 세션. KRX·NXT 애프터마켓의 합집합(가장 이른 시작 ~ 가장 늦은 종료)

### `/properties/startTime/description`

애프터마켓 시작. 가장 이른 KRX/NXT 애프터마켓 시작 시각

### `/properties/singlePriceAuctionEndTime/description`

애프터마켓 내 시가단일가 구간 종료 (NXT 기준). NXT 애프터마켓이 휴장이면 null

### `/properties/endTime/description`

애프터마켓 전체 종료. 가장 늦은 KRX/NXT 애프터마켓 종료 시각

````json
{
  "type": "object",
  "description": "애프터마켓 세션. KRX·NXT 애프터마켓의 합집합(가장 이른 시작 ~ 가장 늦은 종료)",
  "required": [
    "startTime",
    "endTime"
  ],
  "properties": {
    "startTime": {
      "type": "string",
      "format": "date-time",
      "description": "애프터마켓 시작. 가장 이른 KRX/NXT 애프터마켓 시작 시각",
      "example": "2026-03-25T15:30:00+09:00"
    },
    "singlePriceAuctionEndTime": {
      "description": "애프터마켓 내 시가단일가 구간 종료 (NXT 기준). NXT 애프터마켓이 휴장이면 null",
      "example": "2026-03-25T15:40:00+09:00",
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
      "description": "애프터마켓 전체 종료. 가장 늦은 KRX/NXT 애프터마켓 종료 시각",
      "example": "2026-03-25T20:00:00+09:00"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
