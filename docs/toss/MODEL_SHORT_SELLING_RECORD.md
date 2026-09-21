> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ShortSellingRecord.md
> 문서 버전: 1.2.17

# ShortSellingRecord
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **date** | **date** | 매매 기준일 | [default to null] |
| **updatedAt** | **Date** | 해당 기록의 마지막 갱신 시각 | [default to null] |
| **shortSellingVolume** | **BigDecimal** | 공매도 거래량 (주, 정수) | [default to null] |
| **shortSellingAmount** | **BigDecimal** | 공매도 거래대금 (KRW, 정수) | [default to null] |
| **shortSellingVolumeRate** | **BigDecimal** | 공매도 거래량 비중 (소수 비율, 소수 다섯째 자리까지). 해당 일자 전체 거래량 대비 공매도 거래량. 분모인 전체 거래량은 정규장 외 세션(장전·장후 시간외종가, 애프터마켓)을 포함한 당일 누적입니다. 기준 거래량 데이터가 없는 날짜는 null, 기준 거래량이 0 이면 `0`. 예: `0.03215` = 3.215%  | [optional] [default to null] |
| **shortSellingAmountRate** | **BigDecimal** | 공매도 거래대금 비중 (소수 비율, 소수 넷째 자리까지). 해당 일자 전체 거래대금 대비 공매도 거래대금. 분모인 전체 거래대금은 정규장 외 세션(장전·장후 시간외종가, 애프터마켓)을 포함한 당일 누적입니다. 기준 거래대금 데이터가 없는 날짜는 null, 기준 거래대금이 0 이면 `0`. 예: `0.0318` = 3.18%  | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/date/description`

매매 기준일

### `/properties/updatedAt/description`

해당 기록의 마지막 갱신 시각

### `/properties/shortSellingVolume/description`

공매도 거래량 (주, 정수)

### `/properties/shortSellingAmount/description`

공매도 거래대금 (KRW, 정수)

### `/properties/shortSellingVolumeRate/description`

공매도 거래량 비중 (소수 비율, 소수 다섯째 자리까지). 해당 일자 전체 거래량 대비 공매도 거래량.
분모인 전체 거래량은 정규장 외 세션(장전·장후 시간외종가, 애프터마켓)을 포함한 당일 누적입니다.
기준 거래량 데이터가 없는 날짜는 null, 기준 거래량이 0 이면 `0`. 예: `0.03215` = 3.215%


### `/properties/shortSellingAmountRate/description`

공매도 거래대금 비중 (소수 비율, 소수 넷째 자리까지). 해당 일자 전체 거래대금 대비 공매도 거래대금.
분모인 전체 거래대금은 정규장 외 세션(장전·장후 시간외종가, 애프터마켓)을 포함한 당일 누적입니다.
기준 거래대금 데이터가 없는 날짜는 null, 기준 거래대금이 0 이면 `0`. 예: `0.0318` = 3.18%


````json
{
  "type": "object",
  "required": [
    "date",
    "updatedAt",
    "shortSellingVolume",
    "shortSellingAmount"
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
      "description": "해당 기록의 마지막 갱신 시각",
      "example": "2026-07-16T17:25:43+09:00"
    },
    "shortSellingVolume": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "공매도 거래량 (주, 정수)",
      "example": "512300"
    },
    "shortSellingAmount": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "공매도 거래대금 (KRW, 정수)",
      "example": "41250000000"
    },
    "shortSellingVolumeRate": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "공매도 거래량 비중 (소수 비율, 소수 다섯째 자리까지). 해당 일자 전체 거래량 대비 공매도 거래량.\n분모인 전체 거래량은 정규장 외 세션(장전·장후 시간외종가, 애프터마켓)을 포함한 당일 누적입니다.\n기준 거래량 데이터가 없는 날짜는 null, 기준 거래량이 0 이면 `0`. 예: `0.03215` = 3.215%\n",
      "example": "0.03215"
    },
    "shortSellingAmountRate": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "공매도 거래대금 비중 (소수 비율, 소수 넷째 자리까지). 해당 일자 전체 거래대금 대비 공매도 거래대금.\n분모인 전체 거래대금은 정규장 외 세션(장전·장후 시간외종가, 애프터마켓)을 포함한 당일 누적입니다.\n기준 거래대금 데이터가 없는 날짜는 null, 기준 거래대금이 0 이면 `0`. 예: `0.0318` = 3.18%\n",
      "example": "0.0318"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
