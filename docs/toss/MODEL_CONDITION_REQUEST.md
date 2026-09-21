> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionRequest.md
> 문서 버전: 1.2.17

# ConditionRequest
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **orderSide** | **String** | 매매 유형 (매수/매도) | [default to null] |
| **triggerPrice** | **BigDecimal** | 감시 가격. 현재가가 이 값에 닿으면 주문을 생성합니다. | [default to null] |
| **orderPrice** | **BigDecimal** | [orderType=LIMIT] 주문 가격(지정가). 트리거 시 이 가격의 지정가 주문을 생성합니다. MARKET 이면 보내지 않습니다. - KR: 정수 (원 단위). 호가 단위에 맞아야 합니다 (예: 50,000~200,000원 구간은 100원 단위). - US: 소수점 (달러 단위). 호가 단위에 맞아야 합니다 ($1 미만은 0.0001, $1 이상은 0.01 단위).  호가 단위에 맞지 않으면 `400 invalid-request` 에러와 함께 올바른 호가 단위가 `data`에 포함됩니다.  | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/description`

감시 조건 (leg). 가격이 `triggerPrice` 에 닿으면 `orderSide`(매수/매도) 주문을 냅니다.
수량(`quantity`)·호가유형(`orderType`)은 그룹 공통이라 상위 요청에 있습니다.
호가유형이 `LIMIT` 이면 `orderPrice` 가 필수이고, `MARKET` 이면 `orderPrice` 를 보내면 안 됩니다.
`orderPrice` 는 호가 단위에 맞아야 하며, 맞지 않으면 `400 invalid-request` 에러와 함께 올바른 호가 단위가 `data`에 포함됩니다.


### `/properties/orderSide/description`

매매 유형 (매수/매도)

### `/properties/triggerPrice/description`

감시 가격. 현재가가 이 값에 닿으면 주문을 생성합니다.

### `/properties/orderPrice/description`

[orderType=LIMIT] 주문 가격(지정가). 트리거 시 이 가격의 지정가 주문을 생성합니다. MARKET 이면 보내지 않습니다.
- KR: 정수 (원 단위). 호가 단위에 맞아야 합니다 (예: 50,000~200,000원 구간은 100원 단위).
- US: 소수점 (달러 단위). 호가 단위에 맞아야 합니다 ($1 미만은 0.0001, $1 이상은 0.01 단위).

호가 단위에 맞지 않으면 `400 invalid-request` 에러와 함께 올바른 호가 단위가 `data`에 포함됩니다.


````json
{
  "type": "object",
  "required": [
    "orderSide",
    "triggerPrice"
  ],
  "description": "감시 조건 (leg). 가격이 `triggerPrice` 에 닿으면 `orderSide`(매수/매도) 주문을 냅니다.\n수량(`quantity`)·호가유형(`orderType`)은 그룹 공통이라 상위 요청에 있습니다.\n호가유형이 `LIMIT` 이면 `orderPrice` 가 필수이고, `MARKET` 이면 `orderPrice` 를 보내면 안 됩니다.\n`orderPrice` 는 호가 단위에 맞아야 하며, 맞지 않으면 `400 invalid-request` 에러와 함께 올바른 호가 단위가 `data`에 포함됩니다.\n",
  "properties": {
    "orderSide": {
      "type": "string",
      "enum": [
        "BUY",
        "SELL"
      ],
      "description": "매매 유형 (매수/매도)",
      "example": "SELL"
    },
    "triggerPrice": {
      "type": "string",
      "format": "decimal",
      "pattern": "^\\d+(\\.\\d+)?$",
      "maxLength": 30,
      "description": "감시 가격. 현재가가 이 값에 닿으면 주문을 생성합니다.",
      "example": "305"
    },
    "orderPrice": {
      "type": "string",
      "format": "decimal",
      "pattern": "^\\d+(\\.\\d+)?$",
      "maxLength": 30,
      "description": "[orderType=LIMIT] 주문 가격(지정가). 트리거 시 이 가격의 지정가 주문을 생성합니다. MARKET 이면 보내지 않습니다.\n- KR: 정수 (원 단위). 호가 단위에 맞아야 합니다 (예: 50,000~200,000원 구간은 100원 단위).\n- US: 소수점 (달러 단위). 호가 단위에 맞아야 합니다 ($1 미만은 0.0001, $1 이상은 0.01 단위).\n\n호가 단위에 맞지 않으면 `400 invalid-request` 에러와 함께 올바른 호가 단위가 `data`에 포함됩니다.\n",
      "example": "305"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
