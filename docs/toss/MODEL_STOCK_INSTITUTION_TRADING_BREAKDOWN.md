> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockInstitutionTradingBreakdown.md
> 문서 버전: 1.2.17

# StockInstitutionTradingBreakdown
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **financialInvestment** | [**InvestorTradingVolume**](MODEL_INVESTOR_TRADING_VOLUME.md) | 금융투자 | [default to null] |
| **insurance** | [**InvestorTradingVolume**](MODEL_INVESTOR_TRADING_VOLUME.md) | 보험 | [default to null] |
| **trust** | [**InvestorTradingVolume**](MODEL_INVESTOR_TRADING_VOLUME.md) | 투신 | [default to null] |
| **privateEquityFund** | [**InvestorTradingVolume**](MODEL_INVESTOR_TRADING_VOLUME.md) | 사모펀드 | [default to null] |
| **bank** | [**InvestorTradingVolume**](MODEL_INVESTOR_TRADING_VOLUME.md) | 은행 | [default to null] |
| **otherFinancialInstitution** | [**InvestorTradingVolume**](MODEL_INVESTOR_TRADING_VOLUME.md) | 기타금융 | [default to null] |
| **pensionFund** | [**InvestorTradingVolume**](MODEL_INVESTOR_TRADING_VOLUME.md) | 연기금 | [default to null] |




## OpenAPI 원본 스키마

### `/description`

기관 세부 7개 분류별 매매 거래량

### `/properties/financialInvestment/description`

금융투자

### `/properties/insurance/description`

보험

### `/properties/trust/description`

투신

### `/properties/privateEquityFund/description`

사모펀드

### `/properties/bank/description`

은행

### `/properties/otherFinancialInstitution/description`

기타금융

### `/properties/pensionFund/description`

연기금

````json
{
  "type": "object",
  "description": "기관 세부 7개 분류별 매매 거래량",
  "required": [
    "financialInvestment",
    "insurance",
    "trust",
    "privateEquityFund",
    "bank",
    "otherFinancialInstitution",
    "pensionFund"
  ],
  "properties": {
    "financialInvestment": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingVolume"
        }
      ],
      "description": "금융투자"
    },
    "insurance": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingVolume"
        }
      ],
      "description": "보험"
    },
    "trust": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingVolume"
        }
      ],
      "description": "투신"
    },
    "privateEquityFund": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingVolume"
        }
      ],
      "description": "사모펀드"
    },
    "bank": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingVolume"
        }
      ],
      "description": "은행"
    },
    "otherFinancialInstitution": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingVolume"
        }
      ],
      "description": "기타금융"
    },
    "pensionFund": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingVolume"
        }
      ],
      "description": "연기금"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
