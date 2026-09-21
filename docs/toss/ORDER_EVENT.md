> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/asyncapi.json#/channels/realtime-order
> 문서 버전: 1.2.2

# Order Event

### `/summary`

본인 계좌의 주문 이벤트를 실시간으로 구독하는 채널입니다. `personal:order` type 에 종목 symbol 이 아닌 계좌 `accountSeq` 를 선언합니다. 주문 데이터는 LOSSLESS 로 연결 세션 내에서 유실 없이 전달되며, REST 주문 상세와 동일한 모양의 payload 를 받습니다.

### `/description`

구독할 `accountSeq` 는 `GET /api/v1/accounts` 응답에서 확인합니다 — 값은 숫자이므로 문자열로 변환해 `codes` 에 넣으세요. 본인 종합매매·활성 계좌만 구독되고
(부적격 계좌는 `account-not-found` 로 해당 계좌만 거부), 국내/미국 **주식** 주문만 전달됩니다.

`data.order` 는 `GET /api/v1/orders/{orderId}` 응답과 같은 모양이지만 `execution.filledAt` 은 포함하지
않습니다. `topic` 은 `personal:order:{accountSeq}` 이며 내부 계좌번호는 노출되지 않습니다.

미소비분(backlog)을 건너뛰지 않고 유지하며, 클라이언트 수신이 2초 이상 계속 막히면(backpressure) 서버가
연결을 끊습니다. 무손실 보장은 연결 세션 내부에 한정되어 끊긴 구간의 이벤트는 다시 전달되지 않으므로,
재연결 후 다시 선언하고 `GET /api/v1/orders` 로 주문 상태를 재동기화하세요.

### `/messages/declare/summary`

예: [{"type":"personal:order","codes":["3"]}]

### `/messages/declare/payload/description`

구독 선언 — 클라이언트 → 서버 JSON 배열 텍스트 프레임. 배열 1개가 곧 현재 구독 전체입니다(선언형 full-replace).
새 배열은 기존 구독을 전부 대체하고, 빠진 항목은 자동 해제되며, 빈 배열 `[]` 은 전체 해제입니다.
subscribe/unsubscribe 액션은 없습니다.

원소는 아래 4가지 중 하나이며, `type` 에 따라 `codes` 에 넣는 값이 다릅니다:

| type | codes 에 넣는 값 | 예시 |
|---|---|---|
| `trade:us` · `orderbook:us` | 미국 종목 symbol (영문 티커) | `{"type":"trade:us","codes":["AAPL","TSLA"]}` |
| `trade:kr` · `orderbook:kr` | 국내 종목 symbol (6자리 숫자) | `{"type":"orderbook:kr","codes":["005930"]}` |
| `personal:order` | 계좌 `accountSeq` — 종목 symbol 아님 | `{"type":"personal:order","codes":["3"]}` |
| (type 없음) | `id` 만 있는 원소 — 응답에 echo 되는 요청 식별자 | `{"id":"req-1"}` |

### `/messages/declare/payload/items/oneOf/0/description`

선택 원소. 배열 어디에나 1개 넣을 수 있으며, 이 선언에 대한 응답(`subscriptions` ack·`error` 프레임)에
같은 값이 `id` 로 echo 됩니다. 어떤 선언에 대한 응답인지 구분할 때 사용하세요.

### `/messages/declare/payload/items/oneOf/0/properties/id/description`

요청 식별자 (임의 문자열)

### `/messages/declare/payload/items/oneOf/1/description`

실시간 체결을 구독합니다. `type` 은 `trade:{시장}` 형식 — 미국은 `trade:us`, 국내(통합 시세, KRX+NXT)는 `trade:kr`.
`codes` 에는 해당 시장의 종목 symbol 만 넣습니다 — 시장이 다른 symbol 은 `symbol-market-mismatch` 로 해당 항목만 거부됩니다.

### `/messages/declare/payload/items/oneOf/1/properties/type/description`

`trade:us` = 미국 체결, `trade:kr` = 국내 체결 (통합 시세)

### `/messages/declare/payload/items/oneOf/1/properties/codes/description`

종목 symbol 목록. `trade:us` 는 영문 티커(`AAPL`·`TSLA`), `trade:kr` 는 6자리 숫자(`005930`). 표기는 종목 마스터 그대로 사용하세요(미국 티커는 대문자) — 종목 마스터에 없는 symbol 이나 소문자 등 다른 표기는 `stock-not-found` 로 해당 항목만 거부됩니다.

### `/messages/declare/payload/items/oneOf/2/description`

실시간 호가(매도/매수)를 구독합니다. `type` 은 `orderbook:{시장}` 형식 — 미국은 `orderbook:us`, 국내(통합 시세, KRX+NXT)는 `orderbook:kr`.
`codes` 에는 해당 시장의 종목 symbol 만 넣습니다 — 시장이 다른 symbol 은 `symbol-market-mismatch` 로 해당 항목만 거부됩니다.

### `/messages/declare/payload/items/oneOf/2/properties/type/description`

`orderbook:us` = 미국 호가, `orderbook:kr` = 국내 호가 (통합 시세)

### `/messages/declare/payload/items/oneOf/2/properties/codes/description`

종목 symbol 목록. `orderbook:us` 는 영문 티커(`AAPL`·`TSLA`), `orderbook:kr` 는 6자리 숫자(`005930`). 표기는 종목 마스터 그대로 사용하세요(미국 티커는 대문자) — 종목 마스터에 없는 symbol 이나 소문자 등 다른 표기는 `stock-not-found` 로 해당 항목만 거부됩니다.

### `/messages/declare/payload/items/oneOf/3/description`

본인 계좌의 주문 이벤트를 구독합니다. `type` 은 고정값 `personal:order` 이며,
`codes` 에는 종목 symbol 이 아니라 **계좌 `accountSeq`** 를 넣습니다 (`GET /api/v1/accounts` 응답의 `accountSeq` 값 — 응답은 숫자이므로 문자열로 변환해 넣으세요).
본인 소유가 아니거나 구독 부적격인 계좌는 `account-not-found` 로 해당 계좌만 거부됩니다.

### `/messages/declare/payload/items/oneOf/3/properties/type/description`

고정값

### `/messages/declare/payload/items/oneOf/3/properties/codes/description`

계좌 `accountSeq` 목록 (종목 symbol 아님). `GET /api/v1/accounts` 응답의 `accountSeq` 를 문자열로 변환해 사용합니다 (REST 응답은 숫자, `codes` 는 문자열 배열).

### `/messages/declare/examples/0/summary`

주문 이벤트 구독 선언

### `/messages/orderStream/summary`

topic 은 personal:order:{accountSeq}

### `/messages/orderStream/payload/description`

실시간 주문 이벤트 프레임. 본인 계좌의 주문 상태 변화마다 푸시됩니다.

### `/messages/orderStream/payload/properties/topic/description`

`personal:order:{accountSeq}` (예: `personal:order:3`)

### `/messages/orderStream/payload/properties/data/description`

`personal:order` 실시간 주문 이벤트. `message` 프레임의 `data` 로 내려갑니다.

### `/messages/orderStream/payload/properties/data/properties/event/description`

주문 이벤트 종류.
- `PENDING`: 접수
- `PARTIAL_FILL` / `FILL`: 부분 체결 / 전량 체결
- `CANCELING` / `CANCELED`: 취소 중 / 취소됨
- `REPLACING` / `REPLACED`: 정정 중 / 정정됨
- `REJECTED` / `CANCEL_REJECTED` / `REPLACE_REJECTED`: 주문 / 취소 / 정정 거부

클라이언트는 unknown code 를 허용하도록 구현해야 합니다.


### `/messages/orderStream/payload/properties/data/properties/accountSeq/description`

주문이 발생한 계좌의 `accountSeq` (구독 시 보낸 code 값). topic 의 accountSeq 와 동일

### `/messages/orderStream/payload/properties/data/properties/order/description`

주문 스냅샷. 필드/포맷은 REST 주문 조회(`GET /api/v1/orders/{orderId}`)와 동일하나, `execution.filledAt` 은 포함하지 않습니다.

### `/messages/orderStream/payload/properties/data/properties/order/properties/orderId/description`

주문 식별자. REST 와 동일한 암호화 식별자로, 주문 상세 조회에 그대로 사용할 수 있습니다.

### `/messages/orderStream/payload/properties/data/properties/order/properties/symbol/description`

종목 심볼. KRX: 6자리 숫자, US: 영문 티커

### `/messages/orderStream/payload/properties/data/properties/order/properties/side/description`

주문 방향

### `/messages/orderStream/payload/properties/data/properties/order/properties/orderType/description`

호가 유형.
- `LIMIT`: 지정가
- `MARKET`: 시장가

클라이언트는 unknown code 를 허용하도록 구현해야 합니다.


### `/messages/orderStream/payload/properties/data/properties/order/properties/timeInForce/description`

주문 유효 조건 (Time In Force). `orderType` 과 결합되어 주문 방식이 결정됩니다 (예: `LIMIT` + `CLS` = LOC).
- `DAY`: 당일 유효 (Day)
- `CLS`: 장 마감 주문 (At the Close)
- `OPG`: 장 개시 주문 (At the Opening). 현재는 지원하지 않습니다.

클라이언트는 unknown code 를 허용하도록 구현해야 합니다.


### `/messages/orderStream/payload/properties/data/properties/order/properties/status/description`

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


### `/messages/orderStream/payload/properties/data/properties/order/properties/price/description`

주문 가격 (native currency). MARKET 주문 시 null

### `/messages/orderStream/payload/properties/data/properties/order/properties/quantity/description`

주문 수량

### `/messages/orderStream/payload/properties/data/properties/order/properties/orderAmount/description`

주문 금액 (USD). 금액 기반 US 시장가 매수 주문에만 해당. 그 외 null

### `/messages/orderStream/payload/properties/data/properties/order/properties/currency/description`

통화 코드.
- KRW: 한국 원화
- USD: 미국 달러

클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.


### `/messages/orderStream/payload/properties/data/properties/order/properties/orderedAt/description`

주문 시간 (ISO 8601, KST, 밀리초 `.SSS`)

### `/messages/orderStream/payload/properties/data/properties/order/properties/canceledAt/description`

취소 시간 (ISO 8601, KST). 해당 없으면 null

### `/messages/orderStream/payload/properties/data/properties/order/properties/execution/description`

체결 결과. 체결 내역이 없으면 filledQuantity=0

### `/messages/orderStream/payload/properties/data/properties/order/properties/execution/properties/filledQuantity/description`

체결 수량

### `/messages/orderStream/payload/properties/data/properties/order/properties/execution/properties/averageFilledPrice/description`

평균 체결 가격 (native currency). 부분 체결 시 체결된 건의 평균, 미체결 시 null

### `/messages/orderStream/payload/properties/data/properties/order/properties/execution/properties/filledAmount/description`

총 체결 금액 (native currency)

### `/messages/orderStream/payload/properties/data/properties/order/properties/execution/properties/commission/description`

총 체결 수수료 (native currency)

### `/messages/orderStream/payload/properties/data/properties/order/properties/execution/properties/tax/description`

총 체결 세금 (native currency)

### `/messages/orderStream/payload/properties/data/properties/order/properties/execution/properties/settlementDate/description`

결제 예정일 (YYYY-MM-DD, KST 기준). 미결제 시 null

### `/messages/orderStream/examples/0/summary`

전량 체결 이벤트

## 전체 채널 정의

````json
{
  "address": "/ws/v1",
  "title": "Order Event",
  "summary": "본인 계좌의 주문 이벤트를 실시간으로 구독하는 채널입니다. `personal:order` type 에 종목 symbol 이 아닌 계좌 `accountSeq` 를 선언합니다. 주문 데이터는 LOSSLESS 로 연결 세션 내에서 유실 없이 전달되며, REST 주문 상세와 동일한 모양의 payload 를 받습니다.",
  "description": "구독할 `accountSeq` 는 `GET /api/v1/accounts` 응답에서 확인합니다 — 값은 숫자이므로 문자열로 변환해 `codes` 에 넣으세요. 본인 종합매매·활성 계좌만 구독되고\n(부적격 계좌는 `account-not-found` 로 해당 계좌만 거부), 국내/미국 **주식** 주문만 전달됩니다.\n\n`data.order` 는 `GET /api/v1/orders/{orderId}` 응답과 같은 모양이지만 `execution.filledAt` 은 포함하지\n않습니다. `topic` 은 `personal:order:{accountSeq}` 이며 내부 계좌번호는 노출되지 않습니다.\n\n미소비분(backlog)을 건너뛰지 않고 유지하며, 클라이언트 수신이 2초 이상 계속 막히면(backpressure) 서버가\n연결을 끊습니다. 무손실 보장은 연결 세션 내부에 한정되어 끊긴 구간의 이벤트는 다시 전달되지 않으므로,\n재연결 후 다시 선언하고 `GET /api/v1/orders` 로 주문 상태를 재동기화하세요.",
  "messages": {
    "declare": {
      "name": "orderDeclare",
      "title": "[송신] 구독 선언",
      "summary": "예: [{\"type\":\"personal:order\",\"codes\":[\"3\"]}]",
      "payload": {
        "type": "array",
        "description": "구독 선언 — 클라이언트 → 서버 JSON 배열 텍스트 프레임. 배열 1개가 곧 현재 구독 전체입니다(선언형 full-replace).\n새 배열은 기존 구독을 전부 대체하고, 빠진 항목은 자동 해제되며, 빈 배열 `[]` 은 전체 해제입니다.\nsubscribe/unsubscribe 액션은 없습니다.\n\n원소는 아래 4가지 중 하나이며, `type` 에 따라 `codes` 에 넣는 값이 다릅니다:\n\n| type | codes 에 넣는 값 | 예시 |\n|---|---|---|\n| `trade:us` · `orderbook:us` | 미국 종목 symbol (영문 티커) | `{\"type\":\"trade:us\",\"codes\":[\"AAPL\",\"TSLA\"]}` |\n| `trade:kr` · `orderbook:kr` | 국내 종목 symbol (6자리 숫자) | `{\"type\":\"orderbook:kr\",\"codes\":[\"005930\"]}` |\n| `personal:order` | 계좌 `accountSeq` — 종목 symbol 아님 | `{\"type\":\"personal:order\",\"codes\":[\"3\"]}` |\n| (type 없음) | `id` 만 있는 원소 — 응답에 echo 되는 요청 식별자 | `{\"id\":\"req-1\"}` |",
        "items": {
          "oneOf": [
            {
              "title": "요청 id (선택)",
              "type": "object",
              "description": "선택 원소. 배열 어디에나 1개 넣을 수 있으며, 이 선언에 대한 응답(`subscriptions` ack·`error` 프레임)에\n같은 값이 `id` 로 echo 됩니다. 어떤 선언에 대한 응답인지 구분할 때 사용하세요.",
              "required": [
                "id"
              ],
              "properties": {
                "id": {
                  "type": "string",
                  "description": "요청 식별자 (임의 문자열)",
                  "example": "req-1"
                }
              }
            },
            {
              "title": "체결 구독 (trade)",
              "type": "object",
              "description": "실시간 체결을 구독합니다. `type` 은 `trade:{시장}` 형식 — 미국은 `trade:us`, 국내(통합 시세, KRX+NXT)는 `trade:kr`.\n`codes` 에는 해당 시장의 종목 symbol 만 넣습니다 — 시장이 다른 symbol 은 `symbol-market-mismatch` 로 해당 항목만 거부됩니다.",
              "required": [
                "type",
                "codes"
              ],
              "properties": {
                "type": {
                  "type": "string",
                  "enum": [
                    "trade:us",
                    "trade:kr"
                  ],
                  "description": "`trade:us` = 미국 체결, `trade:kr` = 국내 체결 (통합 시세)",
                  "example": "trade:us"
                },
                "codes": {
                  "type": "array",
                  "minItems": 1,
                  "items": {
                    "type": "string"
                  },
                  "description": "종목 symbol 목록. `trade:us` 는 영문 티커(`AAPL`·`TSLA`), `trade:kr` 는 6자리 숫자(`005930`). 표기는 종목 마스터 그대로 사용하세요(미국 티커는 대문자) — 종목 마스터에 없는 symbol 이나 소문자 등 다른 표기는 `stock-not-found` 로 해당 항목만 거부됩니다.",
                  "example": [
                    "AAPL",
                    "TSLA"
                  ]
                }
              }
            },
            {
              "title": "호가 구독 (orderbook)",
              "type": "object",
              "description": "실시간 호가(매도/매수)를 구독합니다. `type` 은 `orderbook:{시장}` 형식 — 미국은 `orderbook:us`, 국내(통합 시세, KRX+NXT)는 `orderbook:kr`.\n`codes` 에는 해당 시장의 종목 symbol 만 넣습니다 — 시장이 다른 symbol 은 `symbol-market-mismatch` 로 해당 항목만 거부됩니다.",
              "required": [
                "type",
                "codes"
              ],
              "properties": {
                "type": {
                  "type": "string",
                  "enum": [
                    "orderbook:us",
                    "orderbook:kr"
                  ],
                  "description": "`orderbook:us` = 미국 호가, `orderbook:kr` = 국내 호가 (통합 시세)",
                  "example": "orderbook:kr"
                },
                "codes": {
                  "type": "array",
                  "minItems": 1,
                  "items": {
                    "type": "string"
                  },
                  "description": "종목 symbol 목록. `orderbook:us` 는 영문 티커(`AAPL`·`TSLA`), `orderbook:kr` 는 6자리 숫자(`005930`). 표기는 종목 마스터 그대로 사용하세요(미국 티커는 대문자) — 종목 마스터에 없는 symbol 이나 소문자 등 다른 표기는 `stock-not-found` 로 해당 항목만 거부됩니다.",
                  "example": [
                    "005930"
                  ]
                }
              }
            },
            {
              "title": "주문 이벤트 구독 (personal:order)",
              "type": "object",
              "description": "본인 계좌의 주문 이벤트를 구독합니다. `type` 은 고정값 `personal:order` 이며,\n`codes` 에는 종목 symbol 이 아니라 **계좌 `accountSeq`** 를 넣습니다 (`GET /api/v1/accounts` 응답의 `accountSeq` 값 — 응답은 숫자이므로 문자열로 변환해 넣으세요).\n본인 소유가 아니거나 구독 부적격인 계좌는 `account-not-found` 로 해당 계좌만 거부됩니다.",
              "required": [
                "type",
                "codes"
              ],
              "properties": {
                "type": {
                  "type": "string",
                  "enum": [
                    "personal:order"
                  ],
                  "description": "고정값",
                  "example": "personal:order"
                },
                "codes": {
                  "type": "array",
                  "minItems": 1,
                  "items": {
                    "type": "string"
                  },
                  "description": "계좌 `accountSeq` 목록 (종목 symbol 아님). `GET /api/v1/accounts` 응답의 `accountSeq` 를 문자열로 변환해 사용합니다 (REST 응답은 숫자, `codes` 는 문자열 배열).",
                  "example": [
                    "3"
                  ]
                }
              }
            }
          ]
        }
      },
      "examples": [
        {
          "name": "orderDeclare",
          "summary": "주문 이벤트 구독 선언",
          "payload": [
            {
              "type": "personal:order",
              "codes": [
                "3"
              ]
            }
          ]
        }
      ]
    },
    "orderStream": {
      "name": "orderStream",
      "title": "[수신] 주문 이벤트 프레임",
      "summary": "topic 은 personal:order:{accountSeq}",
      "payload": {
        "type": "object",
        "description": "실시간 주문 이벤트 프레임. 본인 계좌의 주문 상태 변화마다 푸시됩니다.",
        "required": [
          "type",
          "topic",
          "data"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "message"
            ]
          },
          "topic": {
            "type": "string",
            "description": "`personal:order:{accountSeq}` (예: `personal:order:3`)",
            "example": "personal:order:3"
          },
          "data": {
            "type": "object",
            "description": "`personal:order` 실시간 주문 이벤트. `message` 프레임의 `data` 로 내려갑니다.",
            "required": [
              "event",
              "accountSeq",
              "order"
            ],
            "properties": {
              "event": {
                "type": "string",
                "enum": [
                  "PENDING",
                  "PARTIAL_FILL",
                  "FILL",
                  "CANCELING",
                  "CANCELED",
                  "REPLACING",
                  "REPLACED",
                  "REJECTED",
                  "CANCEL_REJECTED",
                  "REPLACE_REJECTED"
                ],
                "description": "주문 이벤트 종류.\n- `PENDING`: 접수\n- `PARTIAL_FILL` / `FILL`: 부분 체결 / 전량 체결\n- `CANCELING` / `CANCELED`: 취소 중 / 취소됨\n- `REPLACING` / `REPLACED`: 정정 중 / 정정됨\n- `REJECTED` / `CANCEL_REJECTED` / `REPLACE_REJECTED`: 주문 / 취소 / 정정 거부\n\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n",
                "example": "FILL"
              },
              "accountSeq": {
                "type": "string",
                "description": "주문이 발생한 계좌의 `accountSeq` (구독 시 보낸 code 값). topic 의 accountSeq 와 동일",
                "example": "3"
              },
              "order": {
                "type": "object",
                "description": "주문 스냅샷. 필드/포맷은 REST 주문 조회(`GET /api/v1/orders/{orderId}`)와 동일하나, `execution.filledAt` 은 포함하지 않습니다.",
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
                    "description": "주문 식별자. REST 와 동일한 암호화 식별자로, 주문 상세 조회에 그대로 사용할 수 있습니다.",
                    "example": "bAGzNvMOOTa5Uy0xVzYNbxDJ3Qpobwau4jDF3hyZZGWbpHm7wha8CFZc7aXVOWAl"
                  },
                  "symbol": {
                    "type": "string",
                    "description": "종목 심볼. KRX: 6자리 숫자, US: 영문 티커",
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
                    "description": "주문 유효 조건 (Time In Force). `orderType` 과 결합되어 주문 방식이 결정됩니다 (예: `LIMIT` + `CLS` = LOC).\n- `DAY`: 당일 유효 (Day)\n- `CLS`: 장 마감 주문 (At the Close)\n- `OPG`: 장 개시 주문 (At the Opening). 현재는 지원하지 않습니다.\n\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n",
                    "example": "DAY"
                  },
                  "status": {
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
                    "type": "string",
                    "enum": [
                      "KRW",
                      "USD"
                    ],
                    "description": "통화 코드.\n- KRW: 한국 원화\n- USD: 미국 달러\n\n클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.\n",
                    "example": "KRW"
                  },
                  "orderedAt": {
                    "type": "string",
                    "format": "date-time",
                    "description": "주문 시간 (ISO 8601, KST, 밀리초 `.SSS`)",
                    "example": "2026-06-23T09:30:00.000+09:00"
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
                    "required": [
                      "filledQuantity",
                      "averageFilledPrice",
                      "filledAmount",
                      "commission",
                      "tax",
                      "settlementDate"
                    ],
                    "properties": {
                      "filledQuantity": {
                        "type": "string",
                        "format": "decimal",
                        "maxLength": 30,
                        "description": "체결 수량",
                        "example": "10"
                      },
                      "averageFilledPrice": {
                        "type": [
                          "string",
                          "null"
                        ],
                        "format": "decimal",
                        "maxLength": 30,
                        "description": "평균 체결 가격 (native currency). 부분 체결 시 체결된 건의 평균, 미체결 시 null",
                        "example": "70000"
                      },
                      "filledAmount": {
                        "type": [
                          "string",
                          "null"
                        ],
                        "format": "decimal",
                        "maxLength": 30,
                        "description": "총 체결 금액 (native currency)",
                        "example": "700000"
                      },
                      "commission": {
                        "type": [
                          "string",
                          "null"
                        ],
                        "format": "decimal",
                        "maxLength": 30,
                        "description": "총 체결 수수료 (native currency)",
                        "example": "1400"
                      },
                      "tax": {
                        "type": [
                          "string",
                          "null"
                        ],
                        "format": "decimal",
                        "maxLength": 30,
                        "description": "총 체결 세금 (native currency)",
                        "example": "0"
                      },
                      "settlementDate": {
                        "type": [
                          "string",
                          "null"
                        ],
                        "format": "date",
                        "description": "결제 예정일 (YYYY-MM-DD, KST 기준). 미결제 시 null",
                        "example": "2026-06-25"
                      }
                    }
                  }
                }
              }
            }
          }
        }
      },
      "examples": [
        {
          "name": "orderMessage",
          "summary": "전량 체결 이벤트",
          "payload": {
            "type": "message",
            "topic": "personal:order:3",
            "data": {
              "event": "FILL",
              "accountSeq": "3",
              "order": {
                "orderId": "bAGzNvMOOTa5Uy0xVzYNbxDJ3Qpobwau4jDF3hyZZGWbpHm7wha8CFZc7aXVOWAl",
                "symbol": "AAPL",
                "side": "BUY",
                "orderType": "LIMIT",
                "timeInForce": "DAY",
                "status": "FILLED",
                "price": "100.5",
                "quantity": "10",
                "orderAmount": null,
                "currency": "USD",
                "orderedAt": "2026-06-23T09:30:00.000+09:00",
                "canceledAt": null,
                "execution": {
                  "filledQuantity": "10",
                  "averageFilledPrice": "100",
                  "filledAmount": "1000",
                  "commission": "1.23",
                  "tax": "0",
                  "settlementDate": "2026-06-25"
                }
              }
            }
          }
        }
      ]
    }
  }
}
````

## 연결된 연산

### subscribeOrder

````json
{
  "action": "send",
  "channel": {
    "$ref": "#/channels/realtime-order"
  },
  "title": "[송신] 주문 구독 선언",
  "summary": "personal:order 항목(accountSeq)을 담은 선언 배열 전송 (full-replace)",
  "messages": [
    {
      "$ref": "#/channels/realtime-order/messages/declare"
    }
  ]
}
````

### receiveOrder

````json
{
  "action": "receive",
  "channel": {
    "$ref": "#/channels/realtime-order"
  },
  "title": "[수신] 실시간 주문 이벤트",
  "summary": "본인 계좌 주문 상태 변화마다 푸시",
  "messages": [
    {
      "$ref": "#/channels/realtime-order/messages/orderStream"
    }
  ]
}
````

[전체 AsyncAPI 정의·서버·보안·내부 참조](ASYNCAPI_SPEC.md) · [연동 가이드](OVERVIEW.md)
