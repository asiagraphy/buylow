> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockInstitutionTradingVolume.md
> 문서 버전: 1.2.17

# StockInstitutionTradingVolume
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **buyVolume** | **BigDecimal** | 기관 합계 매수 거래량 (주, 정수). `breakdown` 7개 항목의 `buyVolume` 합과 일치 | [default to null] |
| **sellVolume** | **BigDecimal** | 기관 합계 매도 거래량 (주, 정수). `breakdown` 7개 항목의 `sellVolume` 합과 일치 | [default to null] |
| **netBuyVolume** | **BigDecimal** | 기관 합계 순매수 거래량 (주, 정수). 매수 − 매도, 음수면 순매도. `breakdown` 7개 항목의 `netBuyVolume` 합과 일치 | [default to null] |
| **breakdown** | [**StockInstitutionTradingBreakdown**](MODEL_STOCK_INSTITUTION_TRADING_BREAKDOWN.md) | 기관 세부 7개 분류별 거래량. 당일 잠정 기록에는 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다 | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/buyVolume/description`

기관 합계 매수 거래량 (주, 정수). `breakdown` 7개 항목의 `buyVolume` 합과 일치

### `/properties/sellVolume/description`

기관 합계 매도 거래량 (주, 정수). `breakdown` 7개 항목의 `sellVolume` 합과 일치

### `/properties/netBuyVolume/description`

기관 합계 순매수 거래량 (주, 정수). 매수 − 매도, 음수면 순매도. `breakdown` 7개 항목의 `netBuyVolume` 합과 일치

### `/properties/breakdown/description`

기관 세부 7개 분류별 거래량. 당일 잠정 기록에는 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다

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
      "description": "기관 합계 매수 거래량 (주, 정수). `breakdown` 7개 항목의 `buyVolume` 합과 일치",
      "example": "1953200"
    },
    "sellVolume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "기관 합계 매도 거래량 (주, 정수). `breakdown` 7개 항목의 `sellVolume` 합과 일치",
      "example": "1915300"
    },
    "netBuyVolume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "기관 합계 순매수 거래량 (주, 정수). 매수 − 매도, 음수면 순매도. `breakdown` 7개 항목의 `netBuyVolume` 합과 일치",
      "example": "37900"
    },
    "breakdown": {
      "description": "기관 세부 7개 분류별 거래량. 당일 잠정 기록에는 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다",
      "oneOf": [
        {
          "$ref": "#/components/schemas/StockInstitutionTradingBreakdown"
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
