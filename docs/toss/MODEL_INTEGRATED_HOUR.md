> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/IntegratedHour.md
> 문서 버전: 1.2.17

# IntegratedHour
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **preMarket** | [**PreMarketSession**](MODEL_PRE_MARKET_SESSION.md) | 프리마켓 (NXT 접속매매). NXT 프리마켓이 휴장이면 null | [optional] [default to null] |
| **regularMarket** | [**RegularMarketSession**](MODEL_REGULAR_MARKET_SESSION.md) | 정규장. KRX·NXT 정규장의 합집합. 둘 다 휴장이면 null | [optional] [default to null] |
| **afterMarket** | [**AfterMarketSession**](MODEL_AFTER_MARKET_SESSION.md) | 애프터마켓. KRX·NXT 애프터마켓의 합집합. 둘 다 휴장이면 null | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/description`

거래 가능 시간. 장전/장후 시간외종가 제외, 통합 모드 (KRX+NXT) 기준.
세 세션(`preMarket`, `regularMarket`, `afterMarket`) 각각 nullable. 해당 세션이 KRX·NXT 모두 휴장이면 null,
세 세션 모두 null 이면 상위 `integrated` 자체가 null.


### `/properties/preMarket/description`

프리마켓 (NXT 접속매매). NXT 프리마켓이 휴장이면 null

### `/properties/regularMarket/description`

정규장. KRX·NXT 정규장의 합집합. 둘 다 휴장이면 null

### `/properties/afterMarket/description`

애프터마켓. KRX·NXT 애프터마켓의 합집합. 둘 다 휴장이면 null

````json
{
  "type": "object",
  "description": "거래 가능 시간. 장전/장후 시간외종가 제외, 통합 모드 (KRX+NXT) 기준.\n세 세션(`preMarket`, `regularMarket`, `afterMarket`) 각각 nullable. 해당 세션이 KRX·NXT 모두 휴장이면 null,\n세 세션 모두 null 이면 상위 `integrated` 자체가 null.\n",
  "properties": {
    "preMarket": {
      "description": "프리마켓 (NXT 접속매매). NXT 프리마켓이 휴장이면 null",
      "oneOf": [
        {
          "$ref": "#/components/schemas/PreMarketSession"
        },
        {
          "type": "null"
        }
      ]
    },
    "regularMarket": {
      "description": "정규장. KRX·NXT 정규장의 합집합. 둘 다 휴장이면 null",
      "oneOf": [
        {
          "$ref": "#/components/schemas/RegularMarketSession"
        },
        {
          "type": "null"
        }
      ]
    },
    "afterMarket": {
      "description": "애프터마켓. KRX·NXT 애프터마켓의 합집합. 둘 다 휴장이면 null",
      "oneOf": [
        {
          "$ref": "#/components/schemas/AfterMarketSession"
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
