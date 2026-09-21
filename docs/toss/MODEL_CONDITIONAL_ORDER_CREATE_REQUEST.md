> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderCreateRequest.md
> 문서 버전: 1.2.17

# ConditionalOrderCreateRequest
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **symbol** | **String** | 종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커 | [default to null] |
| **type** | **String** | 조건주문 타입 (조건의 개수와 관계). - `SINGLE`: 한 조건만 감시 - `OCO` (One-Cancels-the-Other): 두 조건을 동시에 감시, 하나의 조건 충족 시 나머지 조건 자동 취소 - `OTO` (One-Triggers-the-Other): `first` 조건 체결 후 `second` 조건 감시 시작  | [default to null] |
| **quantity** | **BigDecimal** | 매매 수량 (주 단위). 조건주문 그룹 공통값 — OCO/OTO 는 동일 포지션이라 first/second 가 같은 수량을 씁니다. | [default to null] |
| **orderType** | **String** | 호가유형 (그룹 공통). `LIMIT`(지정가) 이면 각 조건의 `orderPrice` 가 필수이고, `MARKET`(시장가) 이면 `orderPrice` 를 지정할 수 없습니다. OCO/OTO 는 지정가(`LIMIT`)만 지원합니다.  | [default to null] |
| **clientOrderId** | **String** | 멱등키 (선택) — 주문 생성 API 와 동일. 동일한 값으로 재요청 시 중복 생성을 방지합니다. | [optional] [default to null] |
| **expireDate** | **date** | 조건주문 만료일 (YYYY-MM-DD, 필수). 만료일까지 조건이 충족되지 않으면 자동 만료됩니다. | [default to null] |
| **first** | [**ConditionRequest**](MODEL_CONDITION_REQUEST.md) | 첫번째 감시 조건 (필수). OTO 는 먼저 감시할 부모 조건입니다. | [default to null] |
| **second** | [**ConditionRequest**](MODEL_CONDITION_REQUEST.md) | 두번째 감시 조건. SINGLE 은 생략(설정하지 않음), OCO/OTO 는 필수. 그 외 구조·규칙은 first 와 동일합니다. | [optional] [default to null] |
| **confirmHighValueOrder** | **Boolean** | 1억원 이상 주문 동의 여부 | [optional] [default to false] |




## OpenAPI 원본 스키마

### `/properties/symbol/description`

종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커

### `/properties/type/description`

조건주문 타입 (조건의 개수와 관계).
- `SINGLE`: 한 조건만 감시
- `OCO` (One-Cancels-the-Other): 두 조건을 동시에 감시, 하나의 조건 충족 시 나머지 조건 자동 취소
- `OTO` (One-Triggers-the-Other): `first` 조건 체결 후 `second` 조건 감시 시작


### `/properties/quantity/description`

매매 수량 (주 단위). 조건주문 그룹 공통값 — OCO/OTO 는 동일 포지션이라 first/second 가 같은 수량을 씁니다.

### `/properties/orderType/description`

호가유형 (그룹 공통). `LIMIT`(지정가) 이면 각 조건의 `orderPrice` 가 필수이고, `MARKET`(시장가) 이면 `orderPrice` 를 지정할 수 없습니다.
OCO/OTO 는 지정가(`LIMIT`)만 지원합니다.


### `/properties/clientOrderId/description`

멱등키 (선택) — 주문 생성 API 와 동일. 동일한 값으로 재요청 시 중복 생성을 방지합니다.

### `/properties/expireDate/description`

조건주문 만료일 (YYYY-MM-DD, 필수). 만료일까지 조건이 충족되지 않으면 자동 만료됩니다.

### `/properties/first/description`

첫번째 감시 조건 (필수). OTO 는 먼저 감시할 부모 조건입니다.

### `/properties/second/description`

두번째 감시 조건. SINGLE 은 생략(설정하지 않음), OCO/OTO 는 필수. 그 외 구조·규칙은 first 와 동일합니다.

### `/properties/confirmHighValueOrder/description`

1억원 이상 주문 동의 여부

### `/description`

조건주문 생성 요청. "이 가격(triggerPrice)에 닿으면 매수/매도(orderSide) 주문" 만 입력하면 됩니다.
가격이 감시가(triggerPrice)에 닿으면 트리거됩니다.
타입은 `type`(SINGLE/OCO/OTO)으로 지정합니다.


````json
{
  "type": "object",
  "required": [
    "symbol",
    "type",
    "quantity",
    "orderType",
    "expireDate",
    "first"
  ],
  "properties": {
    "symbol": {
      "type": "string",
      "description": "종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커",
      "example": "005930"
    },
    "type": {
      "type": "string",
      "enum": [
        "SINGLE",
        "OCO",
        "OTO"
      ],
      "description": "조건주문 타입 (조건의 개수와 관계).\n- `SINGLE`: 한 조건만 감시\n- `OCO` (One-Cancels-the-Other): 두 조건을 동시에 감시, 하나의 조건 충족 시 나머지 조건 자동 취소\n- `OTO` (One-Triggers-the-Other): `first` 조건 체결 후 `second` 조건 감시 시작\n",
      "example": "OCO"
    },
    "quantity": {
      "type": "string",
      "format": "decimal",
      "pattern": "^\\d+(\\.\\d+)?$",
      "maxLength": 30,
      "description": "매매 수량 (주 단위). 조건주문 그룹 공통값 — OCO/OTO 는 동일 포지션이라 first/second 가 같은 수량을 씁니다.",
      "example": "100"
    },
    "orderType": {
      "type": "string",
      "enum": [
        "LIMIT",
        "MARKET"
      ],
      "description": "호가유형 (그룹 공통). `LIMIT`(지정가) 이면 각 조건의 `orderPrice` 가 필수이고, `MARKET`(시장가) 이면 `orderPrice` 를 지정할 수 없습니다.\nOCO/OTO 는 지정가(`LIMIT`)만 지원합니다.\n",
      "example": "LIMIT"
    },
    "clientOrderId": {
      "type": "string",
      "maxLength": 36,
      "pattern": "^[a-zA-Z0-9\\-_]+$",
      "description": "멱등키 (선택) — 주문 생성 API 와 동일. 동일한 값으로 재요청 시 중복 생성을 방지합니다.",
      "example": "my-order-001"
    },
    "expireDate": {
      "type": "string",
      "format": "date",
      "description": "조건주문 만료일 (YYYY-MM-DD, 필수). 만료일까지 조건이 충족되지 않으면 자동 만료됩니다.",
      "example": "2026-09-10"
    },
    "first": {
      "allOf": [
        {
          "$ref": "#/components/schemas/ConditionRequest"
        }
      ],
      "description": "첫번째 감시 조건 (필수). OTO 는 먼저 감시할 부모 조건입니다."
    },
    "second": {
      "allOf": [
        {
          "$ref": "#/components/schemas/ConditionRequest"
        }
      ],
      "description": "두번째 감시 조건. SINGLE 은 생략(설정하지 않음), OCO/OTO 는 필수. 그 외 구조·규칙은 first 와 동일합니다.",
      "nullable": true
    },
    "confirmHighValueOrder": {
      "type": "boolean",
      "default": false,
      "description": "1억원 이상 주문 동의 여부"
    }
  },
  "description": "조건주문 생성 요청. \"이 가격(triggerPrice)에 닿으면 매수/매도(orderSide) 주문\" 만 입력하면 됩니다.\n가격이 감시가(triggerPrice)에 닿으면 트리거됩니다.\n타입은 `type`(SINGLE/OCO/OTO)으로 지정합니다.\n"
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
