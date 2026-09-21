> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ProgramTradingVolume.md
> 문서 버전: 1.2.17

# ProgramTradingVolume
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **buyVolume** | **BigDecimal** | 프로그램 매수 거래량 (주, 정수) | [default to null] |
| **sellVolume** | **BigDecimal** | 프로그램 매도 거래량 (주, 정수) | [default to null] |
| **netBuyVolume** | **BigDecimal** | 프로그램 순매수 거래량 (주, 정수). 매수 − 매도, 음수면 순매도 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/buyVolume/description`

프로그램 매수 거래량 (주, 정수)

### `/properties/sellVolume/description`

프로그램 매도 거래량 (주, 정수)

### `/properties/netBuyVolume/description`

프로그램 순매수 거래량 (주, 정수). 매수 − 매도, 음수면 순매도

````json
{
  "type": "object",
  "required": [
    "buyVolume",
    "sellVolume",
    "netBuyVolume"
  ],
  "properties": {
    "buyVolume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "프로그램 매수 거래량 (주, 정수)",
      "example": "152300"
    },
    "sellVolume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "프로그램 매도 거래량 (주, 정수)",
      "example": "183400"
    },
    "netBuyVolume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "프로그램 순매수 거래량 (주, 정수). 매수 − 매도, 음수면 순매도",
      "example": "-31100"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
