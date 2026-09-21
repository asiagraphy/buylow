> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/StockInvestorTradingRecord.md
> 문서 버전: 1.2.17

# StockInvestorTradingRecord
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **date** | **date** | 매매 기준일 | [default to null] |
| **updatedAt** | **Date** | 기록 전체의 마지막 갱신 시각 (투자자별 매매동향과 `foreignerHolding`·`cfd` 반영 포함). 당일 기록은 장중 잠정치로 계속 갱신되며, `cfd` 반영(T+1)과 외국인 보유 확정 갱신으로 다음 영업일에도 갱신될 수 있습니다.  | [default to null] |
| **individual** | [**InvestorTradingVolume**](MODEL_INVESTOR_TRADING_VOLUME.md) | 개인. 당일 잠정 기록에는 개인 잠정치가 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다 | [optional] [default to null] |
| **foreigner** | [**InvestorTradingVolume**](MODEL_INVESTOR_TRADING_VOLUME.md) | 등록외국인. 미등록 외국인은 포함하지 않으며, 시장 지표의 투자자별 매매대금 (`GET /api/v1/market-indicators/{symbol}/investor-trading`)의 `foreigner`(등록·미등록 합계)와 기준이 다릅니다  | [default to null] |
| **institution** | [**StockInstitutionTradingVolume**](MODEL_STOCK_INSTITUTION_TRADING_VOLUME.md) | 기관 합계 | [default to null] |
| **otherCorporation** | [**InvestorTradingVolume**](MODEL_INVESTOR_TRADING_VOLUME.md) | 기타법인. 당일 잠정 기록에는 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다 | [optional] [default to null] |
| **foreignerHolding** | [**ForeignerHolding**](MODEL_FOREIGNER_HOLDING.md) | 외국인 보유 현황. 해당 일자의 보유 데이터가 아직 반영되지 않았으면 null (당일 저녁 반영, 다음 영업일 오전 확정 갱신될 수 있음) | [optional] [default to null] |
| **cfd** | [**CfdBalance**](MODEL_CFD_BALANCE.md) | CFD(차액결제거래) 잔고 현황. 해당 일자의 잔고 데이터가 아직 반영되지 않았으면 null (다음 영업일 새벽 반영, T+1) | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/date/description`

매매 기준일

### `/properties/updatedAt/description`

기록 전체의 마지막 갱신 시각 (투자자별 매매동향과 `foreignerHolding`·`cfd` 반영 포함).
당일 기록은 장중 잠정치로 계속 갱신되며, `cfd` 반영(T+1)과 외국인 보유 확정 갱신으로
다음 영업일에도 갱신될 수 있습니다.


### `/properties/individual/description`

개인. 당일 잠정 기록에는 개인 잠정치가 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다

### `/properties/foreigner/description`

등록외국인. 미등록 외국인은 포함하지 않으며, 시장 지표의 투자자별 매매대금
(`GET /api/v1/market-indicators/{symbol}/investor-trading`)의 `foreigner`(등록·미등록 합계)와 기준이 다릅니다


### `/properties/institution/description`

기관 합계

### `/properties/otherCorporation/description`

기타법인. 당일 잠정 기록에는 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다

### `/properties/foreignerHolding/description`

외국인 보유 현황. 해당 일자의 보유 데이터가 아직 반영되지 않았으면 null (당일 저녁 반영, 다음 영업일 오전 확정 갱신될 수 있음)

### `/properties/cfd/description`

CFD(차액결제거래) 잔고 현황. 해당 일자의 잔고 데이터가 아직 반영되지 않았으면 null (다음 영업일 새벽 반영, T+1)

````json
{
  "type": "object",
  "required": [
    "date",
    "updatedAt",
    "foreigner",
    "institution"
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
      "description": "기록 전체의 마지막 갱신 시각 (투자자별 매매동향과 `foreignerHolding`·`cfd` 반영 포함).\n당일 기록은 장중 잠정치로 계속 갱신되며, `cfd` 반영(T+1)과 외국인 보유 확정 갱신으로\n다음 영업일에도 갱신될 수 있습니다.\n",
      "example": "2026-07-16T17:29:12+09:00"
    },
    "individual": {
      "description": "개인. 당일 잠정 기록에는 개인 잠정치가 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다",
      "oneOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingVolume"
        },
        {
          "type": "null"
        }
      ]
    },
    "foreigner": {
      "allOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingVolume"
        }
      ],
      "description": "등록외국인. 미등록 외국인은 포함하지 않으며, 시장 지표의 투자자별 매매대금\n(`GET /api/v1/market-indicators/{symbol}/investor-trading`)의 `foreigner`(등록·미등록 합계)와 기준이 다릅니다\n"
    },
    "institution": {
      "allOf": [
        {
          "$ref": "#/components/schemas/StockInstitutionTradingVolume"
        }
      ],
      "description": "기관 합계"
    },
    "otherCorporation": {
      "description": "기타법인. 당일 잠정 기록에는 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다",
      "oneOf": [
        {
          "$ref": "#/components/schemas/InvestorTradingVolume"
        },
        {
          "type": "null"
        }
      ]
    },
    "foreignerHolding": {
      "description": "외국인 보유 현황. 해당 일자의 보유 데이터가 아직 반영되지 않았으면 null (당일 저녁 반영, 다음 영업일 오전 확정 갱신될 수 있음)",
      "oneOf": [
        {
          "$ref": "#/components/schemas/ForeignerHolding"
        },
        {
          "type": "null"
        }
      ]
    },
    "cfd": {
      "description": "CFD(차액결제거래) 잔고 현황. 해당 일자의 잔고 데이터가 아직 반영되지 않았으면 null (다음 영업일 새벽 반영, T+1)",
      "oneOf": [
        {
          "$ref": "#/components/schemas/CfdBalance"
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
