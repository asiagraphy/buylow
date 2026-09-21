> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Price.md
> 문서 버전: 1.2.17

# Price
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **krw** | **BigDecimal** | KRW로 거래되는 국내 종목의 합산 금액. 국내 종목이 없으면 0 | [default to null] |
| **usd** | **BigDecimal** | USD로 거래되는 해외 종목의 합산 금액. 해외 종목이 없으면 null | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/description`

통화별 합산 금액. 각 통화 필드는 해당 통화로 거래된 종목의 합만 포함합니다 (환율 환산을 통한 통화 간 합산 미포함).

### `/properties/krw/description`

KRW로 거래되는 국내 종목의 합산 금액. 국내 종목이 없으면 0

### `/properties/usd/description`

USD로 거래되는 해외 종목의 합산 금액. 해외 종목이 없으면 null

````json
{
  "type": "object",
  "description": "통화별 합산 금액. 각 통화 필드는 해당 통화로 거래된 종목의 합만 포함합니다 (환율 환산을 통한 통화 간 합산 미포함).",
  "required": [
    "krw"
  ],
  "properties": {
    "krw": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "KRW로 거래되는 국내 종목의 합산 금액. 국내 종목이 없으면 0"
    },
    "usd": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "USD로 거래되는 해외 종목의 합산 금액. 해외 종목이 없으면 null"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
