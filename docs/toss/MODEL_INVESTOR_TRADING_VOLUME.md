> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InvestorTradingVolume.md
> 문서 버전: 1.2.17

# InvestorTradingVolume
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **buyVolume** | **BigDecimal** | 매수 거래량 (주, 정수) | [default to null] |
| **sellVolume** | **BigDecimal** | 매도 거래량 (주, 정수) | [default to null] |
| **netBuyVolume** | **BigDecimal** | 순매수 거래량 (주, 정수). 매수 거래량 − 매도 거래량, 음수면 순매도 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/buyVolume/description`

매수 거래량 (주, 정수)

### `/properties/sellVolume/description`

매도 거래량 (주, 정수)

### `/properties/netBuyVolume/description`

순매수 거래량 (주, 정수). 매수 거래량 − 매도 거래량, 음수면 순매도

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
      "description": "매수 거래량 (주, 정수)",
      "example": "8412300"
    },
    "sellVolume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "매도 거래량 (주, 정수)",
      "example": "8120450"
    },
    "netBuyVolume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "순매수 거래량 (주, 정수). 매수 거래량 − 매도 거래량, 음수면 순매도",
      "example": "291850"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
