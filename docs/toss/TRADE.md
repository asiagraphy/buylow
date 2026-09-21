> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/asyncapi.json#/channels/realtime-trade
> 문서 버전: 1.2.2

# Trade

### `/summary`

종목의 실시간 체결(체결가·체결량)을 구독하는 채널입니다. `trade:us`(미국)·`trade:kr`(국내 통합) type 에 종목 symbol 을 선언하면 체결이 발생할 때마다 프레임을 전달받습니다. 시세 데이터는 LOSSY — 수신이 밀리면 중간 프레임이 유실될 수 있습니다.

### `/description`

다른 채널과 하나의 배열에 함께 선언할 수 있으며, 배열이 곧 현재 구독 전체입니다(full-replace — **Connection** 참고).
선언 직후 구독 ack 가 먼저 도착합니다. 존재하지 않는 symbol 은 `stock-not-found`, 시장 불일치는
`symbol-market-mismatch` 로 해당 항목만 ack 의 `rejected` 에 담겨 거부됩니다.

구독 직후 초기 스냅샷은 전송되지 않으며 다음 체결부터 푸시됩니다 — 연결 시점의 상태가 필요하면 REST(`GET /api/v1/trades`)로 먼저 조회하세요.
푸시는 모든 세션에서 제공됩니다. 미국은 프리·정규·애프터·데이마켓, 국내는 KRX 정규장과 NXT 프리·정규·애프터마켓 합산입니다.

유실 시 항상 최신 상태가 우선이며, 유실 감지용 sequence 필드는 제공되지 않습니다.
프레임에는 누적 거래량·매수/매도 구분이 없고 유실 가능성이 있어, 수신 프레임 합산으로 누적 거래량을 재구성할 수 없습니다 —
누적값이 필요하면 REST 캔들·현재가를 사용하세요.

### `/messages/declare/summary`

예: [{"type":"trade:us","codes":["AAPL","TSLA"]}]

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

체결 구독 선언 (미국 + 국내 혼합)

### `/messages/tradeStream/summary`

topic 은 trade:{시장}:{symbol} — ack 의 subscribed full key 와 동일

### `/messages/tradeStream/payload/description`

실시간 체결 프레임. `data` 는 REST 체결 조회(`GET /api/v1/trades`)의 체결 항목과 동일한 모양입니다.

### `/messages/tradeStream/payload/properties/topic/description`

`trade:{시장}:{symbol}` — `subscribed` 에 echo 된 full key 와 동일 (예: `trade:us:AAPL`)

### `/messages/tradeStream/payload/properties/data/properties/price/description`

체결가

### `/messages/tradeStream/payload/properties/data/properties/volume/description`

체결 수량

### `/messages/tradeStream/payload/properties/data/properties/timestamp/description`

체결 시각

### `/messages/tradeStream/payload/properties/data/properties/currency/description`

통화 코드.
- KRW: 한국 원화
- USD: 미국 달러

클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.


### `/messages/tradeStream/examples/0/summary`

실시간 체결

## 전체 채널 정의

````json
{
  "address": "/ws/v1",
  "title": "Trade",
  "summary": "종목의 실시간 체결(체결가·체결량)을 구독하는 채널입니다. `trade:us`(미국)·`trade:kr`(국내 통합) type 에 종목 symbol 을 선언하면 체결이 발생할 때마다 프레임을 전달받습니다. 시세 데이터는 LOSSY — 수신이 밀리면 중간 프레임이 유실될 수 있습니다.",
  "description": "다른 채널과 하나의 배열에 함께 선언할 수 있으며, 배열이 곧 현재 구독 전체입니다(full-replace — **Connection** 참고).\n선언 직후 구독 ack 가 먼저 도착합니다. 존재하지 않는 symbol 은 `stock-not-found`, 시장 불일치는\n`symbol-market-mismatch` 로 해당 항목만 ack 의 `rejected` 에 담겨 거부됩니다.\n\n구독 직후 초기 스냅샷은 전송되지 않으며 다음 체결부터 푸시됩니다 — 연결 시점의 상태가 필요하면 REST(`GET /api/v1/trades`)로 먼저 조회하세요.\n푸시는 모든 세션에서 제공됩니다. 미국은 프리·정규·애프터·데이마켓, 국내는 KRX 정규장과 NXT 프리·정규·애프터마켓 합산입니다.\n\n유실 시 항상 최신 상태가 우선이며, 유실 감지용 sequence 필드는 제공되지 않습니다.\n프레임에는 누적 거래량·매수/매도 구분이 없고 유실 가능성이 있어, 수신 프레임 합산으로 누적 거래량을 재구성할 수 없습니다 —\n누적값이 필요하면 REST 캔들·현재가를 사용하세요.",
  "messages": {
    "declare": {
      "name": "tradeDeclare",
      "title": "[송신] 구독 선언",
      "summary": "예: [{\"type\":\"trade:us\",\"codes\":[\"AAPL\",\"TSLA\"]}]",
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
          "name": "tradeDeclare",
          "summary": "체결 구독 선언 (미국 + 국내 혼합)",
          "payload": [
            {
              "id": "req-1"
            },
            {
              "type": "trade:us",
              "codes": [
                "AAPL",
                "TSLA"
              ]
            },
            {
              "type": "trade:kr",
              "codes": [
                "005930"
              ]
            }
          ]
        }
      ]
    },
    "tradeStream": {
      "name": "tradeStream",
      "title": "[수신] 체결 프레임",
      "summary": "topic 은 trade:{시장}:{symbol} — ack 의 subscribed full key 와 동일",
      "payload": {
        "type": "object",
        "description": "실시간 체결 프레임. `data` 는 REST 체결 조회(`GET /api/v1/trades`)의 체결 항목과 동일한 모양입니다.",
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
            "description": "`trade:{시장}:{symbol}` — `subscribed` 에 echo 된 full key 와 동일 (예: `trade:us:AAPL`)",
            "example": "trade:us:AAPL"
          },
          "data": {
            "type": "object",
            "required": [
              "price",
              "volume",
              "timestamp",
              "currency"
            ],
            "properties": {
              "price": {
                "type": "string",
                "format": "decimal",
                "maxLength": 30,
                "description": "체결가",
                "example": "72000"
              },
              "volume": {
                "type": "string",
                "format": "decimal",
                "maxLength": 30,
                "description": "체결 수량",
                "example": "120"
              },
              "timestamp": {
                "type": "string",
                "format": "date-time",
                "description": "체결 시각",
                "example": "2026-03-25T09:30:42.000+09:00"
              },
              "currency": {
                "type": "string",
                "enum": [
                  "KRW",
                  "USD"
                ],
                "description": "통화 코드.\n- KRW: 한국 원화\n- USD: 미국 달러\n\n클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.\n"
              }
            }
          }
        }
      },
      "examples": [
        {
          "name": "tradeMessage",
          "summary": "실시간 체결",
          "payload": {
            "type": "message",
            "topic": "trade:us:AAPL",
            "data": {
              "price": "243.26",
              "volume": "8",
              "timestamp": "2026-06-18T23:30:00.000+09:00",
              "currency": "USD"
            }
          }
        }
      ]
    }
  }
}
````

## 연결된 연산

### subscribeTrade

````json
{
  "action": "send",
  "channel": {
    "$ref": "#/channels/realtime-trade"
  },
  "title": "[송신] 체결 구독 선언",
  "summary": "trade:us / trade:kr 항목을 담은 선언 배열 전송 (full-replace)",
  "messages": [
    {
      "$ref": "#/channels/realtime-trade/messages/declare"
    }
  ]
}
````

### receiveTrade

````json
{
  "action": "receive",
  "channel": {
    "$ref": "#/channels/realtime-trade"
  },
  "title": "[수신] 실시간 체결",
  "summary": "구독 종목이 체결될 때마다 푸시",
  "messages": [
    {
      "$ref": "#/channels/realtime-trade/messages/tradeStream"
    }
  ]
}
````

[전체 AsyncAPI 정의·서버·보안·내부 참조](ASYNCAPI_SPEC.md) · [연동 가이드](OVERVIEW.md)
