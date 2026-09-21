> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Account.md
> 문서 버전: 1.2.17

# Account
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **accountNo** | **String** | 계좌번호 | [default to null] |
| **accountSeq** | **Long** | 계좌 식별 키. 주문 등 API 호출 시 이 값을 사용 | [default to null] |
| **accountType** | **String** | 계좌 유형. 현재는 BROKERAGE 만 지원합니다. - BROKERAGE: 종합매매. 국내·해외 주식 통합 매매 계좌 - OVERSEAS_DERIVATIVES: 해외파생. 해외 파생상품 거래 계좌 - PENSION_SAVINGS: 연금저축. 세제혜택 연금저축 계좌 - RESHORING_INVESTMENT: RIA 계좌  클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.  | [default to null] |




## OpenAPI 원본 스키마

### `/properties/accountNo/description`

계좌번호

### `/properties/accountSeq/description`

계좌 식별 키. 주문 등 API 호출 시 이 값을 사용

### `/properties/accountType/description`

계좌 유형. 현재는 BROKERAGE 만 지원합니다.
- BROKERAGE: 종합매매. 국내·해외 주식 통합 매매 계좌
- OVERSEAS_DERIVATIVES: 해외파생. 해외 파생상품 거래 계좌
- PENSION_SAVINGS: 연금저축. 세제혜택 연금저축 계좌
- RESHORING_INVESTMENT: RIA 계좌

클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.


````json
{
  "type": "object",
  "required": [
    "accountNo",
    "accountSeq",
    "accountType"
  ],
  "properties": {
    "accountNo": {
      "type": "string",
      "description": "계좌번호",
      "example": "12345678901"
    },
    "accountSeq": {
      "type": "integer",
      "format": "int64",
      "description": "계좌 식별 키. 주문 등 API 호출 시 이 값을 사용",
      "example": 1
    },
    "accountType": {
      "type": "string",
      "enum": [
        "BROKERAGE",
        "OVERSEAS_DERIVATIVES",
        "PENSION_SAVINGS",
        "RESHORING_INVESTMENT"
      ],
      "description": "계좌 유형. 현재는 BROKERAGE 만 지원합니다.\n- BROKERAGE: 종합매매. 국내·해외 주식 통합 매매 계좌\n- OVERSEAS_DERIVATIVES: 해외파생. 해외 파생상품 거래 계좌\n- PENSION_SAVINGS: 연금저축. 세제혜택 연금저축 계좌\n- RESHORING_INVESTMENT: RIA 계좌\n\n클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.\n",
      "example": "BROKERAGE"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
