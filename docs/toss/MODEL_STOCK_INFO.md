> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockInfo.md
> 문서 버전: 1.2.17

# StockInfo
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **symbol** | **String** | 종목 심볼. | [default to null] |
| **name** | **String** | 종목명 (한글) | [default to null] |
| **englishName** | **String** | 영문 종목명 | [default to null] |
| **isinCode** | **String** | 국제증권식별번호 (ISO 6166) | [default to null] |
| **market** | **String** | 상장 시장. warnings API의 exchange(거래소 단위)와 달리 시장 세그먼트 단위로 구분 | [default to null] |
| **securityType** | **String** | 종목 유형 | [default to null] |
| **isCommonShare** | **Boolean** | 보통주 여부. 우선주인 경우 false | [default to null] |
| **status** | **String** | 상장 상태 | [default to null] |
| **currency** | [**Currency**](MODEL_CURRENCY.md) |  | [default to null] |
| **listDate** | **date** | 상장일 (YYYY-MM-DD, KST 기준). 정보 미제공 시 null | [optional] [default to null] |
| **delistDate** | **date** | 상장폐지일 (YYYY-MM-DD, KST 기준). 활성 종목은 null | [optional] [default to null] |
| **sharesOutstanding** | **BigDecimal** | 발행주식수 | [default to null] |
| **leverageFactor** | **BigDecimal** | 레버리지 배수. ETF/ETN에만 적용 (1.0, 2.0, -1.0 등). 일반 주식 등 해당 없는 종목은 null | [optional] [default to null] |
| **koreanMarketDetail** | [**KrMarketDetail**](MODEL_KR_MARKET_DETAIL.md) | 국내 시장 상세 정보. 국내 종목(KOSPI, KOSDAQ, KR_ETC)에만 제공되며, 해외 종목은 null | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/symbol/description`

종목 심볼.

### `/properties/name/description`

종목명 (한글)

### `/properties/englishName/description`

영문 종목명

### `/properties/isinCode/description`

국제증권식별번호 (ISO 6166)

### `/properties/market/description`

상장 시장. warnings API의 exchange(거래소 단위)와 달리 시장 세그먼트 단위로 구분

### `/properties/securityType/description`

종목 유형

### `/properties/isCommonShare/description`

보통주 여부. 우선주인 경우 false

### `/properties/status/description`

상장 상태

### `/properties/listDate/description`

상장일 (YYYY-MM-DD, KST 기준). 정보 미제공 시 null

### `/properties/delistDate/description`

상장폐지일 (YYYY-MM-DD, KST 기준). 활성 종목은 null

### `/properties/sharesOutstanding/description`

발행주식수

### `/properties/leverageFactor/description`

레버리지 배수. ETF/ETN에만 적용 (1.0, 2.0, -1.0 등). 일반 주식 등 해당 없는 종목은 null

### `/properties/koreanMarketDetail/description`

국내 시장 상세 정보. 국내 종목(KOSPI, KOSDAQ, KR_ETC)에만 제공되며, 해외 종목은 null

````json
{
  "type": "object",
  "required": [
    "symbol",
    "name",
    "englishName",
    "isinCode",
    "market",
    "securityType",
    "isCommonShare",
    "status",
    "currency",
    "sharesOutstanding"
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
    "englishName": {
      "type": "string",
      "description": "영문 종목명",
      "example": "SamsungElec"
    },
    "isinCode": {
      "type": "string",
      "description": "국제증권식별번호 (ISO 6166)",
      "example": "KR7005930003"
    },
    "market": {
      "type": "string",
      "description": "상장 시장. warnings API의 exchange(거래소 단위)와 달리 시장 세그먼트 단위로 구분",
      "enum": [
        "KOSPI",
        "KOSDAQ",
        "NYSE",
        "NASDAQ",
        "AMEX",
        "KR_ETC",
        "US_ETC"
      ],
      "example": "KOSPI"
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
      "description": "보통주 여부. 우선주인 경우 false",
      "example": true
    },
    "status": {
      "type": "string",
      "description": "상장 상태",
      "enum": [
        "SCHEDULED",
        "ACTIVE",
        "DELISTED"
      ],
      "example": "ACTIVE"
    },
    "currency": {
      "$ref": "#/components/schemas/Currency"
    },
    "listDate": {
      "type": [
        "string",
        "null"
      ],
      "format": "date",
      "description": "상장일 (YYYY-MM-DD, KST 기준). 정보 미제공 시 null",
      "example": "1975-06-11"
    },
    "delistDate": {
      "type": [
        "string",
        "null"
      ],
      "format": "date",
      "description": "상장폐지일 (YYYY-MM-DD, KST 기준). 활성 종목은 null",
      "example": null
    },
    "sharesOutstanding": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "발행주식수",
      "example": "5919637922"
    },
    "leverageFactor": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "레버리지 배수. ETF/ETN에만 적용 (1.0, 2.0, -1.0 등). 일반 주식 등 해당 없는 종목은 null",
      "example": null
    },
    "koreanMarketDetail": {
      "description": "국내 시장 상세 정보. 국내 종목(KOSPI, KOSDAQ, KR_ETC)에만 제공되며, 해외 종목은 null",
      "oneOf": [
        {
          "$ref": "#/components/schemas/KrMarketDetail"
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
