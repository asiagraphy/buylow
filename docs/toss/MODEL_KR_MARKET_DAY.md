> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/KrMarketDay.md
> 문서 버전: 1.2.17

# KrMarketDay
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **date** | **date** | 영업일 (KST 기준) | [default to null] |
| **integrated** | [**IntegratedHour**](MODEL_INTEGRATED_HOUR.md) | 거래 가능 시간 (통합 모드 (KRX+NXT) 기준). 둘 다 휴장이면 null | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/date/description`

영업일 (KST 기준)

### `/properties/integrated/description`

거래 가능 시간 (통합 모드 (KRX+NXT) 기준). 둘 다 휴장이면 null

````json
{
  "type": "object",
  "required": [
    "date"
  ],
  "properties": {
    "date": {
      "type": "string",
      "format": "date",
      "description": "영업일 (KST 기준)",
      "example": "2026-03-25"
    },
    "integrated": {
      "description": "거래 가능 시간 (통합 모드 (KRX+NXT) 기준). 둘 다 휴장이면 null",
      "oneOf": [
        {
          "$ref": "#/components/schemas/IntegratedHour"
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
