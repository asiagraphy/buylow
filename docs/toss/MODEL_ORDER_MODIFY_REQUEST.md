> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderModifyRequest.md
> 문서 버전: 1.2.17

# OrderModifyRequest
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **orderType** | **String** | 변경할 호가 유형. - `LIMIT`: 지정가 - `MARKET`: 시장가  | [default to null] |
| **quantity** | **BigDecimal** | 변경할 수량. **KR 주식: 필수.** 양의 정수만 허용합니다 (미전달/0/음수/소수점은 `400 invalid-request`). US 주식: 전달 불가. 제공 시 `400 us-modify-quantity-not-supported` 에러.  | [optional] [default to null] |
| **price** | **BigDecimal** | 변경할 가격. `orderType`이 `LIMIT` 일 때만 사용합니다. - `LIMIT`: 필수. 미전달 시 `400 invalid-request`. - `MARKET`: 전달 불가. 전달 시 `400 invalid-request`. - KR: 정수 (원 단위). 호가 단위에 맞아야 합니다. 맞지 않으면 `400 invalid-request` 에러. - US: 소수점 (달러 단위).   - $1 미만: 소수점 넷째 자리까지 (그 이하 자릿수는 절삭).   - $1 이상: 소수점 둘째 자리까지 (그 이하 자릿수는 절삭).  | [optional] [default to null] |
| **confirmHighValueOrder** | **Boolean** | 착오주문 방지를 위한 주문 확인 플래그. 기본값 `false`. 1억원 이상의 주문 시 `true`가 아니면 `400 confirm-high-value-required` 에러를 반환합니다. 사용자가 해당 주문의 금액을 인지하고 있음을 표시하기 위한 필드입니다. 30억원 이상의 주문은 본 플래그와 무관하게 `422 max-order-amount-exceeded` 에러를 반환합니다.  | [optional] [default to false] |




## OpenAPI 원본 스키마

### `/properties/orderType/description`

변경할 호가 유형.
- `LIMIT`: 지정가
- `MARKET`: 시장가


### `/properties/quantity/description`

변경할 수량.
**KR 주식: 필수.** 양의 정수만 허용합니다 (미전달/0/음수/소수점은 `400 invalid-request`).
US 주식: 전달 불가. 제공 시 `400 us-modify-quantity-not-supported` 에러.


### `/properties/price/description`

변경할 가격. `orderType`이 `LIMIT` 일 때만 사용합니다.
- `LIMIT`: 필수. 미전달 시 `400 invalid-request`.
- `MARKET`: 전달 불가. 전달 시 `400 invalid-request`.
- KR: 정수 (원 단위). 호가 단위에 맞아야 합니다. 맞지 않으면 `400 invalid-request` 에러.
- US: 소수점 (달러 단위).
  - $1 미만: 소수점 넷째 자리까지 (그 이하 자릿수는 절삭).
  - $1 이상: 소수점 둘째 자리까지 (그 이하 자릿수는 절삭).


### `/properties/confirmHighValueOrder/description`

착오주문 방지를 위한 주문 확인 플래그. 기본값 `false`.
1억원 이상의 주문 시 `true`가 아니면 `400 confirm-high-value-required` 에러를 반환합니다.
사용자가 해당 주문의 금액을 인지하고 있음을 표시하기 위한 필드입니다.
30억원 이상의 주문은 본 플래그와 무관하게 `422 max-order-amount-exceeded` 에러를 반환합니다.


````json
{
  "type": "object",
  "required": [
    "orderType"
  ],
  "properties": {
    "orderType": {
      "type": "string",
      "enum": [
        "LIMIT",
        "MARKET"
      ],
      "description": "변경할 호가 유형.\n- `LIMIT`: 지정가\n- `MARKET`: 시장가\n",
      "example": "LIMIT"
    },
    "quantity": {
      "type": "string",
      "format": "decimal",
      "pattern": "^\\d+$",
      "maxLength": 30,
      "description": "변경할 수량.\n**KR 주식: 필수.** 양의 정수만 허용합니다 (미전달/0/음수/소수점은 `400 invalid-request`).\nUS 주식: 전달 불가. 제공 시 `400 us-modify-quantity-not-supported` 에러.\n",
      "example": "15"
    },
    "price": {
      "type": "string",
      "format": "decimal",
      "pattern": "^\\d+(\\.\\d+)?$",
      "maxLength": 30,
      "description": "변경할 가격. `orderType`이 `LIMIT` 일 때만 사용합니다.\n- `LIMIT`: 필수. 미전달 시 `400 invalid-request`.\n- `MARKET`: 전달 불가. 전달 시 `400 invalid-request`.\n- KR: 정수 (원 단위). 호가 단위에 맞아야 합니다. 맞지 않으면 `400 invalid-request` 에러.\n- US: 소수점 (달러 단위).\n  - $1 미만: 소수점 넷째 자리까지 (그 이하 자릿수는 절삭).\n  - $1 이상: 소수점 둘째 자리까지 (그 이하 자릿수는 절삭).\n",
      "example": "71000"
    },
    "confirmHighValueOrder": {
      "type": "boolean",
      "description": "착오주문 방지를 위한 주문 확인 플래그. 기본값 `false`.\n1억원 이상의 주문 시 `true`가 아니면 `400 confirm-high-value-required` 에러를 반환합니다.\n사용자가 해당 주문의 금액을 인지하고 있음을 표시하기 위한 필드입니다.\n30억원 이상의 주문은 본 플래그와 무관하게 `422 max-order-amount-exceeded` 에러를 반환합니다.\n",
      "default": false,
      "example": false
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
