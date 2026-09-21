> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/CfdBalance.md
> 문서 버전: 1.2.17

# CfdBalance
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **buyBalanceQuantity** | **BigDecimal** | CFD 매수 잔고 수량 (주, 정수) | [default to null] |
| **buyBalanceRate** | **BigDecimal** | CFD 매수 잔고 비율 (소수 비율). 상장주식수 대비 매수 잔고 수량. 예: `0.0002` = 0.02% | [default to null] |
| **sellBalanceQuantity** | **BigDecimal** | CFD 매도 잔고 수량 (주, 정수) | [default to null] |
| **sellBalanceRate** | **BigDecimal** | CFD 매도 잔고 비율 (소수 비율). 상장주식수 대비 매도 잔고 수량. 예: `0.0001` = 0.01% | [default to null] |




## OpenAPI 원본 스키마

### `/properties/buyBalanceQuantity/description`

CFD 매수 잔고 수량 (주, 정수)

### `/properties/buyBalanceRate/description`

CFD 매수 잔고 비율 (소수 비율). 상장주식수 대비 매수 잔고 수량. 예: `0.0002` = 0.02%

### `/properties/sellBalanceQuantity/description`

CFD 매도 잔고 수량 (주, 정수)

### `/properties/sellBalanceRate/description`

CFD 매도 잔고 비율 (소수 비율). 상장주식수 대비 매도 잔고 수량. 예: `0.0001` = 0.01%

````json
{
  "type": "object",
  "required": [
    "buyBalanceQuantity",
    "buyBalanceRate",
    "sellBalanceQuantity",
    "sellBalanceRate"
  ],
  "properties": {
    "buyBalanceQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "CFD 매수 잔고 수량 (주, 정수)",
      "example": "1250000"
    },
    "buyBalanceRate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "CFD 매수 잔고 비율 (소수 비율). 상장주식수 대비 매수 잔고 수량. 예: `0.0002` = 0.02%",
      "example": "0.0002"
    },
    "sellBalanceQuantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "CFD 매도 잔고 수량 (주, 정수)",
      "example": "890000"
    },
    "sellBalanceRate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "CFD 매도 잔고 비율 (소수 비율). 상장주식수 대비 매도 잔고 수량. 예: `0.0001` = 0.01%",
      "example": "0.0001"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
