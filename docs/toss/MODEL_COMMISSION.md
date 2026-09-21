> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Commission.md
> 문서 버전: 1.2.17

# Commission
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **marketCountry** | [**MarketCountry**](MODEL_MARKET_COUNTRY.md) |  | [default to null] |
| **commissionRate** | **BigDecimal** | 매매 수수료율 (소수 비율). 예: `0.00015` = 0.015% | [default to null] |
| **startDate** | **date** | 수수료 적용 시작일 (YYYY-MM-DD, KST 기준). 해외주식은 null | [optional] [default to null] |
| **endDate** | **date** | 수수료 적용 종료일 (YYYY-MM-DD, KST 기준). 무기한 적용 시 null | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/commissionRate/description`

매매 수수료율 (소수 비율). 예: `0.00015` = 0.015%

### `/properties/startDate/description`

수수료 적용 시작일 (YYYY-MM-DD, KST 기준). 해외주식은 null

### `/properties/endDate/description`

수수료 적용 종료일 (YYYY-MM-DD, KST 기준). 무기한 적용 시 null

````json
{
  "type": "object",
  "required": [
    "marketCountry",
    "commissionRate"
  ],
  "properties": {
    "marketCountry": {
      "$ref": "#/components/schemas/MarketCountry"
    },
    "commissionRate": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "매매 수수료율 (소수 비율). 예: `0.00015` = 0.015%",
      "example": "0.00015"
    },
    "startDate": {
      "type": [
        "string",
        "null"
      ],
      "format": "date",
      "description": "수수료 적용 시작일 (YYYY-MM-DD, KST 기준). 해외주식은 null",
      "example": "2026-01-01"
    },
    "endDate": {
      "type": [
        "string",
        "null"
      ],
      "format": "date",
      "description": "수수료 적용 종료일 (YYYY-MM-DD, KST 기준). 무기한 적용 시 null",
      "example": "2026-12-31"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
