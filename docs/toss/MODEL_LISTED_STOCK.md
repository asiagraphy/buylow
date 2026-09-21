> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ListedStock.md
> 문서 버전: 1.2.17

# ListedStock
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **symbol** | **String** | 종목 심볼. | [default to null] |
| **name** | **String** | 종목명 (한글) | [default to null] |
| **securityType** | **String** | 종목 유형 | [default to null] |
| **isCommonShare** | **Boolean** | 보통주 여부 | [default to null] |
| **isinCode** | **String** | ISIN 코드 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/symbol/description`

종목 심볼.

### `/properties/name/description`

종목명 (한글)

### `/properties/securityType/description`

종목 유형

### `/properties/isCommonShare/description`

보통주 여부

### `/properties/isinCode/description`

ISIN 코드

````json
{
  "type": "object",
  "required": [
    "symbol",
    "name",
    "securityType",
    "isCommonShare",
    "isinCode"
  ],
  "properties": {
    "symbol": {
      "type": "string",
      "description": "종목 심볼.",
      "example": "005930"
    },
    "name": {
      "type": "string",
      "description": "종목명 (한글)",
      "example": "삼성전자"
    },
    "securityType": {
      "type": "string",
      "description": "종목 유형",
      "enum": [
        "STOCK",
        "FOREIGN_STOCK",
        "DEPOSITARY_RECEIPT",
        "INFRASTRUCTURE_FUND",
        "REIT",
        "ETF",
        "FOREIGN_ETF",
        "ETN",
        "STOCK_WARRANTS"
      ],
      "example": "STOCK"
    },
    "isCommonShare": {
      "type": "boolean",
      "description": "보통주 여부",
      "example": true
    },
    "isinCode": {
      "type": "string",
      "description": "ISIN 코드",
      "example": "KR7005930003"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
