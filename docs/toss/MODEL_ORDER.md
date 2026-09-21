> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Order.md
> 문서 버전: 1.2.17

# Order
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **orderId** | **String** | 주문 식별자 | [default to null] |
| **symbol** | **String** | 종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커 | [default to null] |
| **side** | **String** | 주문 방향 | [default to null] |
| **orderType** | **String** | 호가 유형. - `LIMIT`: 지정가 - `MARKET`: 시장가  클라이언트는 unknown code 를 허용하도록 구현해야 합니다.  | [default to null] |
| **timeInForce** | **String** | 주문 유효 조건 (Time In Force). `orderType` 과 결합되어 주문 방식이 결정됩니다 (예: `LIMIT` + `CLS` = LOC). - `DAY`: 당일 유효 (Day) - `CLS`: 장 마감 주문 (At the Close) - `OPG`: 장 개시 주문 (At the Opening, 국내 시가단일가)  클라이언트는 unknown code 를 허용하도록 구현해야 합니다.  | [default to null] |
| **status** | [**OrderStatus**](MODEL_ORDER_STATUS.md) |  | [default to null] |
| **price** | **BigDecimal** | 주문 가격 (native currency). MARKET 주문 시 null | [optional] [default to null] |
| **quantity** | **BigDecimal** | 주문 수량 | [default to null] |
| **orderAmount** | **BigDecimal** | 주문 금액 (USD). 금액 기반 US 시장가 매수 주문에만 해당. 그 외 null | [optional] [default to null] |
| **currency** | [**Currency**](MODEL_CURRENCY.md) |  | [default to null] |
| **orderedAt** | **Date** | 주문 시간 (ISO 8601, KST) | [default to null] |
| **canceledAt** | **Date** | 취소 시간 (ISO 8601, KST). 해당 없으면 null | [optional] [default to null] |
| **execution** | [**OrderExecution**](MODEL_ORDER_EXECUTION.md) | 체결 결과. 체결 내역이 없으면 filledQuantity=0 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/orderId/description`

주문 식별자

### `/properties/symbol/description`

종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커

### `/properties/side/description`

주문 방향

### `/properties/orderType/description`

호가 유형.
- `LIMIT`: 지정가
- `MARKET`: 시장가

클라이언트는 unknown code 를 허용하도록 구현해야 합니다.


### `/properties/timeInForce/description`

주문 유효 조건 (Time In Force). `orderType` 과 결합되어 주문 방식이 결정됩니다 (예: `LIMIT` + `CLS` = LOC).
- `DAY`: 당일 유효 (Day)
- `CLS`: 장 마감 주문 (At the Close)
- `OPG`: 장 개시 주문 (At the Opening, 국내 시가단일가)

클라이언트는 unknown code 를 허용하도록 구현해야 합니다.


### `/properties/price/description`

주문 가격 (native currency). MARKET 주문 시 null

### `/properties/quantity/description`

주문 수량

### `/properties/orderAmount/description`

주문 금액 (USD). 금액 기반 US 시장가 매수 주문에만 해당. 그 외 null

### `/properties/orderedAt/description`

주문 시간 (ISO 8601, KST)

### `/properties/canceledAt/description`

취소 시간 (ISO 8601, KST). 해당 없으면 null

### `/properties/execution/description`

체결 결과. 체결 내역이 없으면 filledQuantity=0

````json
{
  "type": "object",
  "required": [
    "orderId",
    "symbol",
    "side",
    "orderType",
    "timeInForce",
    "status",
    "quantity",
    "currency",
    "orderedAt",
    "execution"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "주문 식별자",
      "example": "bAGzNvMOOTa5Uy0xVzYNbxDJ3Qpobwau4jDF3hyZZGWbpHm7wha8CFZc7aXVOWAl"
    },
    "symbol": {
      "type": "string",
      "description": "종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커",
      "example": "005930"
    },
    "side": {
      "type": "string",
      "enum": [
        "BUY",
        "SELL"
      ],
      "description": "주문 방향",
      "example": "BUY"
    },
    "orderType": {
      "type": "string",
      "enum": [
        "LIMIT",
        "MARKET"
      ],
      "description": "호가 유형.\n- `LIMIT`: 지정가\n- `MARKET`: 시장가\n\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n",
      "example": "LIMIT"
    },
    "timeInForce": {
      "type": "string",
      "enum": [
        "DAY",
        "CLS",
        "OPG"
      ],
      "description": "주문 유효 조건 (Time In Force). `orderType` 과 결합되어 주문 방식이 결정됩니다 (예: `LIMIT` + `CLS` = LOC).\n- `DAY`: 당일 유효 (Day)\n- `CLS`: 장 마감 주문 (At the Close)\n- `OPG`: 장 개시 주문 (At the Opening, 국내 시가단일가)\n\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n",
      "example": "DAY"
    },
    "status": {
      "$ref": "#/components/schemas/OrderStatus"
    },
    "price": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "주문 가격 (native currency). MARKET 주문 시 null",
      "example": "70000"
    },
    "quantity": {
      "type": "string",
      "format": "decimal",
      "maxLength": 30,
      "description": "주문 수량",
      "example": "10"
    },
    "orderAmount": {
      "type": [
        "string",
        "null"
      ],
      "format": "decimal",
      "maxLength": 30,
      "description": "주문 금액 (USD). 금액 기반 US 시장가 매수 주문에만 해당. 그 외 null",
      "example": null
    },
    "currency": {
      "$ref": "#/components/schemas/Currency",
      "example": "KRW"
    },
    "orderedAt": {
      "type": "string",
      "format": "date-time",
      "description": "주문 시간 (ISO 8601, KST)",
      "example": "2026-03-29T09:30:00.000+09:00"
    },
    "canceledAt": {
      "type": [
        "string",
        "null"
      ],
      "format": "date-time",
      "description": "취소 시간 (ISO 8601, KST). 해당 없으면 null",
      "example": null
    },
    "execution": {
      "type": "object",
      "description": "체결 결과. 체결 내역이 없으면 filledQuantity=0",
      "allOf": [
        {
          "$ref": "#/components/schemas/OrderExecution"
        }
      ]
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
