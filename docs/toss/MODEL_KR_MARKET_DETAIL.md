> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/KrMarketDetail.md
> 문서 버전: 1.2.17

# KrMarketDetail
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **liquidationTrading** | **Boolean** | 정리매매 여부 (상장폐지 절차 진행 중). | [default to null] |
| **nxtSupported** | **Boolean** | NXT 대체거래소 지원 여부 | [default to null] |
| **krxTradingSuspended** | **Boolean** | KRX 거래정지 여부 | [default to null] |
| **nxtTradingSuspended** | **Boolean** | NXT 거래정지 여부. NXT 미지원 종목(nxtSupported=false)은 null | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/liquidationTrading/description`

정리매매 여부 (상장폐지 절차 진행 중).

### `/properties/nxtSupported/description`

NXT 대체거래소 지원 여부

### `/properties/krxTradingSuspended/description`

KRX 거래정지 여부

### `/properties/nxtTradingSuspended/description`

NXT 거래정지 여부. NXT 미지원 종목(nxtSupported=false)은 null

````json
{
  "type": "object",
  "required": [
    "liquidationTrading",
    "nxtSupported",
    "krxTradingSuspended"
  ],
  "properties": {
    "liquidationTrading": {
      "type": "boolean",
      "description": "정리매매 여부 (상장폐지 절차 진행 중).",
      "example": false
    },
    "nxtSupported": {
      "type": "boolean",
      "description": "NXT 대체거래소 지원 여부",
      "example": true
    },
    "krxTradingSuspended": {
      "type": "boolean",
      "description": "KRX 거래정지 여부",
      "example": false
    },
    "nxtTradingSuspended": {
      "type": [
        "boolean",
        "null"
      ],
      "description": "NXT 거래정지 여부. NXT 미지원 종목(nxtSupported=false)은 null",
      "example": false
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
