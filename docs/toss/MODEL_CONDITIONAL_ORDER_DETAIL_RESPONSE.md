> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderDetailResponse.md
> 문서 버전: 1.2.17

# ConditionalOrderDetailResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **conditionalOrderId** | **String** | 조건주문 식별자. 상세 조회·수정·취소에 사용합니다.  | [default to null] |
| **type** | **String** | 조건주문 타입. - `SINGLE`: 한 조건만 감시 - `OCO` (One-Cancels-the-Other): 두 조건을 동시에 감시, 하나의 조건 충족 시 나머지 조건 자동 취소 - `OTO` (One-Triggers-the-Other): `first` 조건 체결 후 `second` 조건 감시 시작  | [default to null] |
| **status** | **String** | 조건주문(그룹) 상태 — 살아있는 조건(leg)의 상태를 대표로 따릅니다. leg 전용 상태인 `HOLDING`·`CANCELED` 는 최상위 status 로는 내려오지 않습니다 (조건별 상태 `first.status`/`second.status` 에서만 노출). - `WATCHING`: 조건 감시 중 - `PAUSED`: 일시중지 - `ORDERING`: 조건 충족 — 주문 생성 진행 중 - `ORDERED`: 주문 생성됨 - `COMPLETED`: 완료 - `EXPIRED`: 만료  | [default to null] |
| **symbol** | **String** | 종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커 | [default to null] |
| **market** | **String** | 시장 구분 | [default to null] |
| **quantity** | **BigDecimal** | 매매 수량 (주 단위, 그룹 공통). | [default to null] |
| **orderType** | **String** | 호가유형 (그룹 공통). LIMIT(지정가)/MARKET(시장가). | [default to null] |
| **expireDate** | **date** | 조건주문 만료일 (조건주문 1건의 모든 감시 조건이 공유). 이 날짜까지 미충족 시 자동 만료됩니다. | [optional] [default to null] |
| **first** | [**ConditionalOrderCondition**](MODEL_CONDITIONAL_ORDER_CONDITION.md) | 첫번째 감시 조건 (OTO 는 부모) | [default to null] |
| **second** | [**ConditionalOrderCondition**](MODEL_CONDITIONAL_ORDER_CONDITION.md) | 두번째 감시 조건. OCO/OTO 만 존재하며 단일(SINGLE)은 null. | [optional] [default to null] |
| **createdAt** | **Date** | 조건주문 등록 시각 (KST) | [default to null] |




## OpenAPI 원본 스키마

### `/description`

조건주문 조회 응답 (목록 항목 / 상세 공용). 모든 타입을 단일 스키마로 표현하며,
감시 조건은 `first`/`second` 로 내려갑니다 (SINGLE 은 `first` 만, OCO/OTO 는 `second` 도 존재).


### `/properties/conditionalOrderId/description`

조건주문 식별자. 상세 조회·수정·취소에 사용합니다.


### `/properties/type/description`

조건주문 타입.
- `SINGLE`: 한 조건만 감시
- `OCO` (One-Cancels-the-Other): 두 조건을 동시에 감시, 하나의 조건 충족 시 나머지 조건 자동 취소
- `OTO` (One-Triggers-the-Other): `first` 조건 체결 후 `second` 조건 감시 시작


### `/properties/status/description`

조건주문(그룹) 상태 — 살아있는 조건(leg)의 상태를 대표로 따릅니다.
leg 전용 상태인 `HOLDING`·`CANCELED` 는 최상위 status 로는 내려오지 않습니다 (조건별 상태 `first.status`/`second.status` 에서만 노출).
- `WATCHING`: 조건 감시 중
- `PAUSED`: 일시중지
- `ORDERING`: 조건 충족 — 주문 생성 진행 중
- `ORDERED`: 주문 생성됨
- `COMPLETED`: 완료
- `EXPIRED`: 만료


### `/properties/symbol/description`

종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커

### `/properties/market/description`

시장 구분

### `/properties/quantity/description`

매매 수량 (주 단위, 그룹 공통).

### `/properties/orderType/description`

호가유형 (그룹 공통). LIMIT(지정가)/MARKET(시장가).

### `/properties/expireDate/description`

조건주문 만료일 (조건주문 1건의 모든 감시 조건이 공유). 이 날짜까지 미충족 시 자동 만료됩니다.

### `/properties/first/description`

첫번째 감시 조건 (OTO 는 부모)

### `/properties/second/description`

두번째 감시 조건. OCO/OTO 만 존재하며 단일(SINGLE)은 null.

### `/properties/createdAt/description`

조건주문 등록 시각 (KST)

````json
{
  "type": "object",
  "required": [
    "conditionalOrderId",
    "type",
    "status",
    "symbol",
    "market",
    "quantity",
    "orderType",
    "first",
    "createdAt"
  ],
  "description": "조건주문 조회 응답 (목록 항목 / 상세 공용). 모든 타입을 단일 스키마로 표현하며,\n감시 조건은 `first`/`second` 로 내려갑니다 (SINGLE 은 `first` 만, OCO/OTO 는 `second` 도 존재).\n",
  "properties": {
    "conditionalOrderId": {
      "type": "string",
      "description": "조건주문 식별자. 상세 조회·수정·취소에 사용합니다.\n",
      "example": "gaZIG-dYMWil8AAXyPmlRg"
    },
    "type": {
      "type": "string",
      "enum": [
        "SINGLE",
        "OCO",
        "OTO"
      ],
      "description": "조건주문 타입.\n- `SINGLE`: 한 조건만 감시\n- `OCO` (One-Cancels-the-Other): 두 조건을 동시에 감시, 하나의 조건 충족 시 나머지 조건 자동 취소\n- `OTO` (One-Triggers-the-Other): `first` 조건 체결 후 `second` 조건 감시 시작\n",
      "example": "OCO"
    },
    "status": {
      "type": "string",
      "enum": [
        "WATCHING",
        "PAUSED",
        "ORDERING",
        "ORDERED",
        "COMPLETED",
        "EXPIRED"
      ],
      "description": "조건주문(그룹) 상태 — 살아있는 조건(leg)의 상태를 대표로 따릅니다.\nleg 전용 상태인 `HOLDING`·`CANCELED` 는 최상위 status 로는 내려오지 않습니다 (조건별 상태 `first.status`/`second.status` 에서만 노출).\n- `WATCHING`: 조건 감시 중\n- `PAUSED`: 일시중지\n- `ORDERING`: 조건 충족 — 주문 생성 진행 중\n- `ORDERED`: 주문 생성됨\n- `COMPLETED`: 완료\n- `EXPIRED`: 만료\n",
      "example": "WATCHING"
    },
    "symbol": {
      "type": "string",
      "description": "종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커",
      "example": "005930"
    },
    "market": {
      "type": "string",
      "enum": [
        "KR",
        "US"
      ],
      "description": "시장 구분",
      "example": "KR"
    },
    "quantity": {
      "type": "string",
      "format": "decimal",
      "description": "매매 수량 (주 단위, 그룹 공통).",
      "example": "100"
    },
    "orderType": {
      "type": "string",
      "enum": [
        "LIMIT",
        "MARKET"
      ],
      "description": "호가유형 (그룹 공통). LIMIT(지정가)/MARKET(시장가).",
      "example": "LIMIT"
    },
    "expireDate": {
      "type": "string",
      "format": "date",
      "description": "조건주문 만료일 (조건주문 1건의 모든 감시 조건이 공유). 이 날짜까지 미충족 시 자동 만료됩니다.",
      "example": "2026-09-10"
    },
    "first": {
      "allOf": [
        {
          "$ref": "#/components/schemas/ConditionalOrderCondition"
        }
      ],
      "description": "첫번째 감시 조건 (OTO 는 부모)"
    },
    "second": {
      "allOf": [
        {
          "$ref": "#/components/schemas/ConditionalOrderCondition"
        }
      ],
      "description": "두번째 감시 조건. OCO/OTO 만 존재하며 단일(SINGLE)은 null.",
      "nullable": true
    },
    "createdAt": {
      "type": "string",
      "format": "date-time",
      "description": "조건주문 등록 시각 (KST)",
      "example": "2026-06-12T09:00:00+09:00"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
