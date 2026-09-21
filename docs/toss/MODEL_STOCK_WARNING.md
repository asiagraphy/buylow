> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockWarning.md
> 문서 버전: 1.2.17

# StockWarning
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **warningType** | **String** | 유의사항 유형. 클라이언트는 unknown code 를 허용하도록 구현해야 합니다.  | 값 | 의미 | |------|------| | `LIQUIDATION_TRADING` | 정리매매 (상장폐지 절차 진행 중) | | `OVERHEATED` | 단기과열종목 지정 | | `INVESTMENT_WARNING` | 투자경고종목 지정 | | `INVESTMENT_RISK` | 투자위험종목 지정 | | `VI_STATIC_AND_DYNAMIC` | 변동성 완화장치(VI) 정적 + 동적 동시 발동 | | `VI_STATIC` | 변동성 완화장치(VI) 정적 발동 | | `VI_DYNAMIC` | 변동성 완화장치(VI) 동적 발동 | | `STOCK_WARRANTS` | 신주인수권증서/증권 |  | [default to null] |
| **exchange** | **String** | 거래소 코드 (KRX, NXT 등 물리적 거래소 단위). stocks API의 market(상장 시장 단위)과 추상화 수준이 다름. 거래소 무관 경고는 null | [optional] [default to null] |
| **startDate** | **date** | 적용 시작일 (inclusive, YYYY-MM-DD, KST 기준). 시작일 미정 시 null | [optional] [default to null] |
| **endDate** | **date** | 적용 종료일 (inclusive, YYYY-MM-DD, KST 기준). 진행 중이거나 미정 시 null | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/warningType/description`

유의사항 유형.
클라이언트는 unknown code 를 허용하도록 구현해야 합니다.

| 값 | 의미 |
|------|------|
| `LIQUIDATION_TRADING` | 정리매매 (상장폐지 절차 진행 중) |
| `OVERHEATED` | 단기과열종목 지정 |
| `INVESTMENT_WARNING` | 투자경고종목 지정 |
| `INVESTMENT_RISK` | 투자위험종목 지정 |
| `VI_STATIC_AND_DYNAMIC` | 변동성 완화장치(VI) 정적 + 동적 동시 발동 |
| `VI_STATIC` | 변동성 완화장치(VI) 정적 발동 |
| `VI_DYNAMIC` | 변동성 완화장치(VI) 동적 발동 |
| `STOCK_WARRANTS` | 신주인수권증서/증권 |


### `/properties/exchange/description`

거래소 코드 (KRX, NXT 등 물리적 거래소 단위). stocks API의 market(상장 시장 단위)과 추상화 수준이 다름. 거래소 무관 경고는 null

### `/properties/startDate/description`

적용 시작일 (inclusive, YYYY-MM-DD, KST 기준). 시작일 미정 시 null

### `/properties/endDate/description`

적용 종료일 (inclusive, YYYY-MM-DD, KST 기준). 진행 중이거나 미정 시 null

````json
{
  "type": "object",
  "required": [
    "warningType"
  ],
  "properties": {
    "warningType": {
      "type": "string",
      "description": "유의사항 유형.\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n\n| 값 | 의미 |\n|------|------|\n| `LIQUIDATION_TRADING` | 정리매매 (상장폐지 절차 진행 중) |\n| `OVERHEATED` | 단기과열종목 지정 |\n| `INVESTMENT_WARNING` | 투자경고종목 지정 |\n| `INVESTMENT_RISK` | 투자위험종목 지정 |\n| `VI_STATIC_AND_DYNAMIC` | 변동성 완화장치(VI) 정적 + 동적 동시 발동 |\n| `VI_STATIC` | 변동성 완화장치(VI) 정적 발동 |\n| `VI_DYNAMIC` | 변동성 완화장치(VI) 동적 발동 |\n| `STOCK_WARRANTS` | 신주인수권증서/증권 |\n",
      "enum": [
        "LIQUIDATION_TRADING",
        "OVERHEATED",
        "INVESTMENT_WARNING",
        "INVESTMENT_RISK",
        "VI_STATIC_AND_DYNAMIC",
        "VI_STATIC",
        "VI_DYNAMIC",
        "STOCK_WARRANTS"
      ],
      "example": "VI_STATIC"
    },
    "exchange": {
      "type": [
        "string",
        "null"
      ],
      "description": "거래소 코드 (KRX, NXT 등 물리적 거래소 단위). stocks API의 market(상장 시장 단위)과 추상화 수준이 다름. 거래소 무관 경고는 null",
      "example": "KRX"
    },
    "startDate": {
      "type": [
        "string",
        "null"
      ],
      "format": "date",
      "description": "적용 시작일 (inclusive, YYYY-MM-DD, KST 기준). 시작일 미정 시 null",
      "example": "2026-03-26"
    },
    "endDate": {
      "type": [
        "string",
        "null"
      ],
      "format": "date",
      "description": "적용 종료일 (inclusive, YYYY-MM-DD, KST 기준). 진행 중이거나 미정 시 null",
      "example": "2026-03-27"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
