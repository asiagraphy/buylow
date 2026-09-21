> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderModifyRequest.md
> 문서 버전: 1.2.17

# ConditionalOrderModifyRequest
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **String** | 변경 결과 타입. 수정 시 타입 전환(예: SINGLE→OCO)이 허용됩니다.  | [default to null] |
| **quantity** | **BigDecimal** | 매매 수량 (주 단위, 그룹 공통). | [default to null] |
| **orderType** | **String** | 호가유형 (그룹 공통). LIMIT(지정가)/MARKET(시장가). OCO/OTO 는 지정가만 지원합니다. | [default to null] |
| **expireDate** | **date** | 조건주문 만료일 (수정 시 필수) | [default to null] |
| **first** | [**ConditionRequest**](MODEL_CONDITION_REQUEST.md) | 첫번째 감시 조건 (필수). OTO 는 먼저 감시할 부모 조건입니다. | [default to null] |
| **second** | [**ConditionRequest**](MODEL_CONDITION_REQUEST.md) | 두번째 감시 조건. SINGLE 은 생략(설정하지 않음), OCO/OTO 는 필수. 그 외 구조·규칙은 first 와 동일합니다. | [optional] [default to null] |
| **confirmHighValueOrder** | **Boolean** | 1억원 이상 주문 동의 여부 | [optional] [default to false] |




## OpenAPI 원본 스키마

### `/properties/type/description`

변경 결과 타입. 수정 시 타입 전환(예: SINGLE→OCO)이 허용됩니다.


### `/properties/quantity/description`

매매 수량 (주 단위, 그룹 공통).

### `/properties/orderType/description`

호가유형 (그룹 공통). LIMIT(지정가)/MARKET(시장가). OCO/OTO 는 지정가만 지원합니다.

### `/properties/expireDate/description`

조건주문 만료일 (수정 시 필수)

### `/properties/first/description`

첫번째 감시 조건 (필수). OTO 는 먼저 감시할 부모 조건입니다.

### `/properties/second/description`

두번째 감시 조건. SINGLE 은 생략(설정하지 않음), OCO/OTO 는 필수. 그 외 구조·규칙은 first 와 동일합니다.

### `/properties/confirmHighValueOrder/description`

1억원 이상 주문 동의 여부

### `/description`

조건주문 수정 요청. 등록과 동일하게 "이 가격에 닿으면 매매" 만 입력하며,
조건주문 전체를 재설정하므로 유지할 조건도 함께 전달해야 합니다.
종목은 `conditionalOrderId` 로 식별되므로 수정 요청에는 `symbol` 이 필요 없습니다.


````json
{
  "type": "object",
  "required": [
    "type",
    "quantity",
    "orderType",
    "expireDate",
    "first"
  ],
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "SINGLE",
        "OCO",
        "OTO"
      ],
      "description": "변경 결과 타입. 수정 시 타입 전환(예: SINGLE→OCO)이 허용됩니다.\n",
      "example": "OCO"
    },
    "quantity": {
      "type": "string",
      "format": "decimal",
      "pattern": "^\\d+(\\.\\d+)?$",
      "maxLength": 30,
      "description": "매매 수량 (주 단위, 그룹 공통).",
      "example": "100"
    },
    "orderType": {
      "type": "string",
      "enum": [
        "LIMIT",
        "MARKET"
      ],
      "description": "호가유형 (그룹 공통). LIMIT(지정가)/MARKET(시장가). OCO/OTO 는 지정가만 지원합니다.",
      "example": "LIMIT"
    },
    "expireDate": {
      "type": "string",
      "format": "date",
      "description": "조건주문 만료일 (수정 시 필수)",
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
  "description": "조건주문 수정 요청. 등록과 동일하게 \"이 가격에 닿으면 매매\" 만 입력하며,\n조건주문 전체를 재설정하므로 유지할 조건도 함께 전달해야 합니다.\n종목은 `conditionalOrderId` 로 식별되므로 수정 요청에는 `symbol` 이 필요 없습니다.\n"
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
