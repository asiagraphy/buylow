> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/CreditTradeRecord.md
> 문서 버전: 1.2.17

# CreditTradeRecord
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **date** | **date** | 매매 기준일 | [default to null] |
| **updatedAt** | **Date** | 해당 기록의 마지막 갱신 시각 | [default to null] |
| **marginLoan** | [**CreditTradeDetail**](MODEL_CREDIT_TRADE_DETAIL.md) | 신용융자 (돈을 빌려 매수하는 신용거래). 해당 일자의 융자 데이터가 없으면 null | [optional] [default to null] |
| **stockLoan** | [**CreditTradeDetail**](MODEL_CREDIT_TRADE_DETAIL.md) | 신용대주 (주식을 빌려 매도하는 개인 신용거래). 기관 간 대차거래 (`GET /api/v1/stocks/{symbol}/securities-lending`)와는 다른 데이터입니다. 해당 일자의 대주 데이터가 없으면 null  | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/date/description`

매매 기준일

### `/properties/updatedAt/description`

해당 기록의 마지막 갱신 시각

### `/properties/marginLoan/description`

신용융자 (돈을 빌려 매수하는 신용거래). 해당 일자의 융자 데이터가 없으면 null

### `/properties/stockLoan/description`

신용대주 (주식을 빌려 매도하는 개인 신용거래). 기관 간 대차거래
(`GET /api/v1/stocks/{symbol}/securities-lending`)와는 다른 데이터입니다.
해당 일자의 대주 데이터가 없으면 null


````json
{
  "type": "object",
  "required": [
    "date",
    "updatedAt"
  ],
  "properties": {
    "date": {
      "type": "string",
      "format": "date",
      "description": "매매 기준일",
      "example": "2026-07-16"
    },
    "updatedAt": {
      "type": "string",
      "format": "date-time",
      "description": "해당 기록의 마지막 갱신 시각",
      "example": "2026-07-17T02:35:00+09:00"
    },
    "marginLoan": {
      "description": "신용융자 (돈을 빌려 매수하는 신용거래). 해당 일자의 융자 데이터가 없으면 null",
      "oneOf": [
        {
          "$ref": "#/components/schemas/CreditTradeDetail"
        },
        {
          "type": "null"
        }
      ]
    },
    "stockLoan": {
      "description": "신용대주 (주식을 빌려 매도하는 개인 신용거래). 기관 간 대차거래\n(`GET /api/v1/stocks/{symbol}/securities-lending`)와는 다른 데이터입니다.\n해당 일자의 대주 데이터가 없으면 null\n",
      "oneOf": [
        {
          "$ref": "#/components/schemas/CreditTradeDetail"
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
