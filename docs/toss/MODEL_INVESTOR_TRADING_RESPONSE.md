> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/InvestorTradingResponse.md
> 문서 버전: 1.2.17

# InvestorTradingResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **nextUntil** | **date** | 다음 페이지 조회 기준일. 다음 페이지 조회 시 `until` 쿼리 파라미터에 그대로 전달. 더 이상 데이터가 없으면 null | [optional] [default to null] |
| **records** | [**List**](MODEL_INVESTOR_TRADING_RECORD.md) | 집계 기간별 매매대금 기록 목록 (최신순). 데이터가 없으면 빈 배열 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/nextUntil/description`

다음 페이지 조회 기준일. 다음 페이지 조회 시 `until` 쿼리 파라미터에 그대로 전달. 더 이상 데이터가 없으면 null

### `/properties/records/description`

집계 기간별 매매대금 기록 목록 (최신순). 데이터가 없으면 빈 배열

````json
{
  "type": "object",
  "required": [
    "records"
  ],
  "properties": {
    "nextUntil": {
      "type": [
        "string",
        "null"
      ],
      "format": "date",
      "description": "다음 페이지 조회 기준일. 다음 페이지 조회 시 `until` 쿼리 파라미터에 그대로 전달. 더 이상 데이터가 없으면 null",
      "example": "2026-06-09"
    },
    "records": {
      "type": "array",
      "description": "집계 기간별 매매대금 기록 목록 (최신순). 데이터가 없으면 빈 배열",
      "items": {
        "$ref": "#/components/schemas/InvestorTradingRecord"
      }
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
