> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ProgramTradeRecord.md
> 문서 버전: 1.2.17

# ProgramTradeRecord
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **date** | **date** | 매매 기준일 | [default to null] |
| **arbitrage** | [**ProgramTradingVolume**](MODEL_PROGRAM_TRADING_VOLUME.md) | 차익거래 | [default to null] |
| **nonArbitrage** | [**ProgramTradingVolume**](MODEL_PROGRAM_TRADING_VOLUME.md) | 비차익거래 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/date/description`

매매 기준일

### `/properties/arbitrage/description`

차익거래

### `/properties/nonArbitrage/description`

비차익거래

````json
{
  "type": "object",
  "required": [
    "date",
    "arbitrage",
    "nonArbitrage"
  ],
  "properties": {
    "date": {
      "type": "string",
      "format": "date",
      "description": "매매 기준일",
      "example": "2026-07-17"
    },
    "arbitrage": {
      "allOf": [
        {
          "$ref": "#/components/schemas/ProgramTradingVolume"
        }
      ],
      "description": "차익거래"
    },
    "nonArbitrage": {
      "allOf": [
        {
          "$ref": "#/components/schemas/ProgramTradingVolume"
        }
      ],
      "description": "비차익거래"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
