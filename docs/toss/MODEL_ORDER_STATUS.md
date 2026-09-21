> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderStatus.md
> 문서 버전: 1.2.17

# OrderStatus
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|




## OpenAPI 원본 스키마

### `/description`

주문 상태.
- `PENDING`: 체결 대기. 주문이 접수되어 체결을 대기 중인 상태
- `PENDING_CANCEL`: 취소 대기. 취소 요청이 접수되어 브로커 응답을 대기 중인 상태
- `PENDING_REPLACE`: 정정 대기. 정정 요청이 접수되어 브로커 응답을 대기 중인 상태
- `PARTIAL_FILLED`: 부분 체결. 주문 수량 중 일부만 체결된 상태
- `FILLED`: 체결 완료. 주문 수량이 전량 체결된 상태
- `CANCELED`: 취소 완료. execution.filledQuantity를 통해 부분 체결 여부를 확인할 수 있음
- `REJECTED`: 거부됨. 브로커가 주문을 거부한 상태. execution.filledQuantity를 통해 부분 체결 여부를 확인할 수 있음
- `CANCEL_REJECTED`: 취소 거부. 브로커가 취소 요청을 거부한 경우 별도 주문 레코드로 생성됨. 원주문은 이전 상태로 복귀함
- `REPLACE_REJECTED`: 정정 거부. 브로커가 정정 요청을 거부한 경우 별도 주문 레코드로 생성됨. 원주문은 이전 상태로 복귀함
- `REPLACED`: 정정됨. 정정 요청이 수락되어 원주문이 대체된 상태. execution.filledQuantity를 통해 부분 체결 여부를 확인할 수 있음

클라이언트는 unknown code 를 허용하도록 구현해야 합니다.


````json
{
  "type": "string",
  "enum": [
    "PENDING",
    "PENDING_CANCEL",
    "PENDING_REPLACE",
    "PARTIAL_FILLED",
    "FILLED",
    "CANCELED",
    "REJECTED",
    "CANCEL_REJECTED",
    "REPLACE_REJECTED",
    "REPLACED"
  ],
  "description": "주문 상태.\n- `PENDING`: 체결 대기. 주문이 접수되어 체결을 대기 중인 상태\n- `PENDING_CANCEL`: 취소 대기. 취소 요청이 접수되어 브로커 응답을 대기 중인 상태\n- `PENDING_REPLACE`: 정정 대기. 정정 요청이 접수되어 브로커 응답을 대기 중인 상태\n- `PARTIAL_FILLED`: 부분 체결. 주문 수량 중 일부만 체결된 상태\n- `FILLED`: 체결 완료. 주문 수량이 전량 체결된 상태\n- `CANCELED`: 취소 완료. execution.filledQuantity를 통해 부분 체결 여부를 확인할 수 있음\n- `REJECTED`: 거부됨. 브로커가 주문을 거부한 상태. execution.filledQuantity를 통해 부분 체결 여부를 확인할 수 있음\n- `CANCEL_REJECTED`: 취소 거부. 브로커가 취소 요청을 거부한 경우 별도 주문 레코드로 생성됨. 원주문은 이전 상태로 복귀함\n- `REPLACE_REJECTED`: 정정 거부. 브로커가 정정 요청을 거부한 경우 별도 주문 레코드로 생성됨. 원주문은 이전 상태로 복귀함\n- `REPLACED`: 정정됨. 정정 요청이 수락되어 원주문이 대체된 상태. execution.filledQuantity를 통해 부분 체결 여부를 확인할 수 있음\n\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n",
  "example": "FILLED"
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
