> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderCondition.md
> 문서 버전: 1.2.17

# ConditionalOrderCondition
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | **String** | 감시 조건 세부 타입 (그룹 타입을 구성하는 단위). - `STOP`: 가격 트리거 - `PROFIT_RATE`: 목표 수익률(%) 트리거  그룹(OCO/OTO)의 `first` 와 `second` 는 항상 동일한 타입입니다.  | [default to null] |
| **status** | **String** | 조건(leg) 단위 상태. 최상위 조건주문 `status` 와 달리 leg 전용인 `HOLDING`·`CANCELED` 를 포함합니다. - `HOLDING`: 선행 조건(OTO first) 체결 전 대기 (leg 전용) - `CANCELED`: 취소됨 (완료된 OCO 에서 자동취소된 반대편 조건)  | [default to null] |
| **triggerPrice** | **BigDecimal** | 이 가격에 닿으면 트리거됩니다. 현재 지원 조건은 항상 값이 존재하나, 향후 수익률(PROFIT_RATE)·추종형 조건은 고정 트리거가가 없어 null 일 수 있습니다.  | [optional] [default to null] |
| **targetProfitRate** | **BigDecimal** | [PROFIT_RATE 전용] 감시 수익률. **퍼센트(%) 단위**입니다 (예: `10.5` = +10.5%). PROFIT_RATE 이 아닌 조건이면 null.  | [optional] [default to null] |
| **orderPrice** | **BigDecimal** | 주문 가격(지정가). 그룹 호가유형(orderType)이 LIMIT 이면 값이 있고, MARKET 이면 null. | [optional] [default to null] |
| **triggeredOrderId** | **String** | 조건 충족으로 생성된 주문의 ID. 일반 주문 API(`GET /orders/{orderId}` 등)에 그대로 사용할 수 있습니다. 주문 생성 전이면 null.  | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/type/description`

감시 조건 세부 타입 (그룹 타입을 구성하는 단위).
- `STOP`: 가격 트리거
- `PROFIT_RATE`: 목표 수익률(%) 트리거

그룹(OCO/OTO)의 `first` 와 `second` 는 항상 동일한 타입입니다.


### `/properties/status/description`

조건(leg) 단위 상태. 최상위 조건주문 `status` 와 달리 leg 전용인 `HOLDING`·`CANCELED` 를 포함합니다.
- `HOLDING`: 선행 조건(OTO first) 체결 전 대기 (leg 전용)
- `CANCELED`: 취소됨 (완료된 OCO 에서 자동취소된 반대편 조건)


### `/properties/triggerPrice/description`

이 가격에 닿으면 트리거됩니다.
현재 지원 조건은 항상 값이 존재하나, 향후 수익률(PROFIT_RATE)·추종형 조건은 고정 트리거가가 없어 null 일 수 있습니다.


### `/properties/targetProfitRate/description`

[PROFIT_RATE 전용] 감시 수익률. **퍼센트(%) 단위**입니다 (예: `10.5` = +10.5%).
PROFIT_RATE 이 아닌 조건이면 null.


### `/properties/orderPrice/description`

주문 가격(지정가). 그룹 호가유형(orderType)이 LIMIT 이면 값이 있고, MARKET 이면 null.

### `/properties/triggeredOrderId/description`

조건 충족으로 생성된 주문의 ID. 일반 주문 API(`GET /orders/{orderId}` 등)에 그대로 사용할 수 있습니다. 주문 생성 전이면 null.


````json
{
  "type": "object",
  "required": [
    "type",
    "status"
  ],
  "properties": {
    "type": {
      "type": "string",
      "enum": [
        "STOP",
        "PROFIT_RATE"
      ],
      "description": "감시 조건 세부 타입 (그룹 타입을 구성하는 단위).\n- `STOP`: 가격 트리거\n- `PROFIT_RATE`: 목표 수익률(%) 트리거\n\n그룹(OCO/OTO)의 `first` 와 `second` 는 항상 동일한 타입입니다.\n",
      "example": "STOP"
    },
    "status": {
      "type": "string",
      "enum": [
        "WATCHING",
        "HOLDING",
        "PAUSED",
        "ORDERING",
        "ORDERED",
        "COMPLETED",
        "EXPIRED",
        "CANCELED"
      ],
      "description": "조건(leg) 단위 상태. 최상위 조건주문 `status` 와 달리 leg 전용인 `HOLDING`·`CANCELED` 를 포함합니다.\n- `HOLDING`: 선행 조건(OTO first) 체결 전 대기 (leg 전용)\n- `CANCELED`: 취소됨 (완료된 OCO 에서 자동취소된 반대편 조건)\n",
      "example": "WATCHING"
    },
    "triggerPrice": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "description": "이 가격에 닿으면 트리거됩니다.\n현재 지원 조건은 항상 값이 존재하나, 향후 수익률(PROFIT_RATE)·추종형 조건은 고정 트리거가가 없어 null 일 수 있습니다.\n",
      "example": "295"
    },
    "targetProfitRate": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "description": "[PROFIT_RATE 전용] 감시 수익률. **퍼센트(%) 단위**입니다 (예: `10.5` = +10.5%).\nPROFIT_RATE 이 아닌 조건이면 null.\n",
      "example": "10.5"
    },
    "orderPrice": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "description": "주문 가격(지정가). 그룹 호가유형(orderType)이 LIMIT 이면 값이 있고, MARKET 이면 null.",
      "example": "294.5"
    },
    "triggeredOrderId": {
      "type": [
        "string",
        "null"
      ],
      "description": "조건 충족으로 생성된 주문의 ID. 일반 주문 API(`GET /orders/{orderId}` 등)에 그대로 사용할 수 있습니다. 주문 생성 전이면 null.\n"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
