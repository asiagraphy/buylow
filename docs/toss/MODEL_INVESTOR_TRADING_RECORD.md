> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InvestorTradingRecord.md
> 문서 버전: 1.2.17

# InvestorTradingRecord
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **date** | **date** | 집계 기준일. `interval` 이 나타내는 집계 기간의 대표 일자 | [default to null] |
| **updatedAt** | **Date** | 해당 기록의 마지막 갱신 시각. 당일 기록은 장 종료 전까지 갱신될 수 있으므로, 이 값으로 확정치·잠정치 여부를 판단할 수 있습니다.  | [default to null] |
| **individual** | [**InvestorTradingAmount**](MODEL_INVESTOR_TRADING_AMOUNT.md) | 개인 | [default to null] |
| **foreigner** | [**InvestorTradingAmount**](MODEL_INVESTOR_TRADING_AMOUNT.md) | 외국인 합계 (등록·미등록 외국인 포함) | [default to null] |
| **institution** | [**InstitutionTradingAmount**](MODEL_INSTITUTION_TRADING_AMOUNT.md) | 기관 합계. `buyAmount`/`sellAmount` 는 `breakdown` 7개 항목의 합과 일치합니다 | [default to null] |
| **otherCorporation** | [**InvestorTradingAmount**](MODEL_INVESTOR_TRADING_AMOUNT.md) | 기타법인 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/date/description`

집계 기준일. `interval` 이 나타내는 집계 기간의 대표 일자

### `/properties/updatedAt/description`

해당 기록의 마지막 갱신 시각. 당일 기록은 장 종료 전까지 갱신될 수 있으므로,
이 값으로 확정치·잠정치 여부를 판단할 수 있습니다.


### `/properties/individual/description`

개인

### `/properties/foreigner/description`

외국인 합계 (등록·미등록 외국인 포함)

### `/properties/institution/description`

기관 합계. `buyAmount`/`sellAmount` 는 `breakdown` 7개 항목의 합과 일치합니다

### `/properties/otherCorporation/description`

기타법인

````json
{
  "type": "object",
  "required": [
    "date",
    "updatedAt",
    "individual",
    "foreigner",
    "institution",
    "otherCorporation"
  ],
  "properties": {
    "date": {
      "type": "string",
      "format": "date",
      "description": "집계 기준일. `interval` 이 나타내는 집계 기간의 대표 일자",
      "example": "2026-06-11"
    },
    "updatedAt": {
      "type": "string",
      "format": "date-time",
      "description": "해당 기록의 마지막 갱신 시각. 당일 기록은 장 종료 전까지 갱신될 수 있으므로,\n이 값으로 확정치·잠정치 여부를 판단할 수 있습니다.\n",
      "example": "2026-06-11T18:10:00+09:00"
    },
    "individual": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingAmount"
        }
      ],
      "description": "개인"
    },
    "foreigner": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingAmount"
        }
      ],
      "description": "외국인 합계 (등록·미등록 외국인 포함)"
    },
    "institution": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InstitutionTradingAmount"
        }
      ],
      "description": "기관 합계. `buyAmount`/`sellAmount` 는 `breakdown` 7개 항목의 합과 일치합니다"
    },
    "otherCorporation": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingAmount"
        }
      ],
      "description": "기타법인"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
