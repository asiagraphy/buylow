> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/CreditTradeDetail.md
> 문서 버전: 1.2.17

# CreditTradeDetail
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **newQuantity** | **BigDecimal** | 신규 수량 (주, 정수) | [default to null] |
| **returnQuantity** | **BigDecimal** | 상환 수량 (주, 정수) | [default to null] |
| **balanceQuantity** | **BigDecimal** | 잔고 수량 (주, 정수) | [default to null] |
| **balanceRate** | **BigDecimal** | 잔고 비율 (소수 비율). 상장주식수 대비 잔고 수량. 예: `0.0042` = 0.42% | [default to null] |
| **tradingRate** | **BigDecimal** | 공여율 (소수 비율). 매매일의 종목 전체 거래량 중 해당 신용거래 유형의 거래량 비율. 예: `0.09` = 9% | [default to null] |




## OpenAPI 원본 스키마

### `/properties/newQuantity/description`

신규 수량 (주, 정수)

### `/properties/returnQuantity/description`

상환 수량 (주, 정수)

### `/properties/balanceQuantity/description`

잔고 수량 (주, 정수)

### `/properties/balanceRate/description`

잔고 비율 (소수 비율). 상장주식수 대비 잔고 수량. 예: `0.0042` = 0.42%

### `/properties/tradingRate/description`

공여율 (소수 비율). 매매일의 종목 전체 거래량 중 해당 신용거래 유형의 거래량 비율. 예: `0.09` = 9%

````json
{
  "type": "object",
  "required": [
    "newQuantity",
    "returnQuantity",
    "balanceQuantity",
    "balanceRate",
    "tradingRate"
  ],
  "properties": {
    "newQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "신규 수량 (주, 정수)",
      "example": "125300"
    },
    "returnQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "상환 수량 (주, 정수)",
      "example": "98200"
    },
    "balanceQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "잔고 수량 (주, 정수)",
      "example": "2513400"
    },
    "balanceRate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "잔고 비율 (소수 비율). 상장주식수 대비 잔고 수량. 예: `0.0042` = 0.42%",
      "example": "0.0042"
    },
    "tradingRate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "공여율 (소수 비율). 매매일의 종목 전체 거래량 중 해당 신용거래 유형의 거래량 비율. 예: `0.09` = 9%",
      "example": "0.09"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
