> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/asyncapi.json#/channels/realtime-orderbook
> 문서 버전: 1.2.2

# Orderbook

### `/summary`

종목의 실시간 호가(매도/매수)를 구독하는 채널입니다. `orderbook:us`·`orderbook:kr` type 에 종목 symbol 을 선언하면 호가가 갱신될 때마다 프레임을 전달받습니다. 시세 데이터는 LOSSY — 수신이 밀리면 중간 프레임이 유실될 수 있습니다.

### `/description`

다른 채널과 하나의 배열에 함께 선언할 수 있으며, 배열이 곧 현재 구독 전체입니다(full-replace —
**Connection** 참고). 존재하지 않는 symbol 은 `stock-not-found`, 시장 불일치는 `symbol-market-mismatch` 로
해당 항목만 ack 의 `rejected` 에 담겨 거부됩니다.

구독 직후 초기 스냅샷은 전송되지 않으며 다음 호가 갱신부터 푸시됩니다 — 연결 시점의 상태가 필요하면 REST(`GET /api/v1/orderbook`)로 먼저 조회하세요.
푸시는 모든 세션에서 제공됩니다. 미국은 프리·정규·애프터·데이마켓, 국내는 KRX 정규장과 NXT 프리·정규·애프터마켓 합산입니다.

유실 시 항상 최신 상태가 우선이며, 유실 감지용 sequence 필드는 제공되지 않습니다.

### `/messages/declare/summary`

예: [{"type":"orderbook:kr","codes":["005930"]}]

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

호가 구독 선언

### `/messages/orderbookStream/summary`

topic 은 orderbook:{시장}:{symbol}

### `/messages/orderbookStream/payload/description`

실시간 호가 프레임. `data` 는 REST 호가 조회(`GET /api/v1/orderbook`)의 응답과 동일한 모양입니다.

### `/messages/orderbookStream/payload/properties/topic/description`

`orderbook:{시장}:{symbol}` (예: `orderbook:kr:005930`)

### `/messages/orderbookStream/payload/properties/data/properties/timestamp/description`

데이터 시각. 데이터 미제공 시 null

### `/messages/orderbookStream/payload/properties/data/properties/currency/description`

통화 코드.
- KRW: 한국 원화
- USD: 미국 달러

클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.


### `/messages/orderbookStream/payload/properties/data/properties/asks/description`

매도호가 목록 (낮은 가격순)

### `/messages/orderbookStream/payload/properties/data/properties/asks/items/properties/price/description`

호가

### `/messages/orderbookStream/payload/properties/data/properties/asks/items/properties/volume/description`

잔량

### `/messages/orderbookStream/payload/properties/data/properties/bids/description`

매수호가 목록 (높은 가격순)

### `/messages/orderbookStream/payload/properties/data/properties/bids/items/properties/price/description`

호가

### `/messages/orderbookStream/payload/properties/data/properties/bids/items/properties/volume/description`

잔량

### `/messages/orderbookStream/examples/0/summary`

실시간 호가

## 전체 채널 정의

````json
{
  "address": "/ws/v1",
  "title": "Orderbook",
  "summary": "종목의 실시간 호가(매도/매수)를 구독하는 채널입니다. `orderbook:us`·`orderbook:kr` type 에 종목 symbol 을 선언하면 호가가 갱신될 때마다 프레임을 전달받습니다. 시세 데이터는 LOSSY — 수신이 밀리면 중간 프레임이 유실될 수 있습니다.",
  "description": "다른 채널과 하나의 배열에 함께 선언할 수 있으며, 배열이 곧 현재 구독 전체입니다(full-replace —\n**Connection** 참고). 존재하지 않는 symbol 은 `stock-not-found`, 시장 불일치는 `symbol-market-mismatch` 로\n해당 항목만 ack 의 `rejected` 에 담겨 거부됩니다.\n\n구독 직후 초기 스냅샷은 전송되지 않으며 다음 호가 갱신부터 푸시됩니다 — 연결 시점의 상태가 필요하면 REST(`GET /api/v1/orderbook`)로 먼저 조회하세요.\n푸시는 모든 세션에서 제공됩니다. 미국은 프리·정규·애프터·데이마켓, 국내는 KRX 정규장과 NXT 프리·정규·애프터마켓 합산입니다.\n\n유실 시 항상 최신 상태가 우선이며, 유실 감지용 sequence 필드는 제공되지 않습니다.",
  "messages": {
    "declare": {
      "name": "orderbookDeclare",
      "title": "[송신] 구독 선언",
      "summary": "예: [{\"type\":\"orderbook:kr\",\"codes\":[\"005930\"]}]",
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
          "name": "orderbookDeclare",
          "summary": "호가 구독 선언",
          "payload": [
            {
              "type": "orderbook:kr",
              "codes": [
                "005930",
                "035420"
              ]
            }
          ]
        }
      ]
    },
    "orderbookStream": {
      "name": "orderbookStream",
      "title": "[수신] 호가 프레임",
      "summary": "topic 은 orderbook:{시장}:{symbol}",
      "payload": {
        "type": "object",
        "description": "실시간 호가 프레임. `data` 는 REST 호가 조회(`GET /api/v1/orderbook`)의 응답과 동일한 모양입니다.",
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
            "description": "`orderbook:{시장}:{symbol}` (예: `orderbook:kr:005930`)",
            "example": "orderbook:kr:005930"
          },
          "data": {
            "type": "object",
            "required": [
              "currency",
              "asks",
              "bids"
            ],
            "properties": {
              "timestamp": {
                "type": [
                  "string",
                  "null"
                ],
                "format": "date-time",
                "description": "데이터 시각. 데이터 미제공 시 null",
                "example": "2026-03-25T09:30:00.123+09:00"
              },
              "currency": {
                "type": "string",
                "enum": [
                  "KRW",
                  "USD"
                ],
                "description": "통화 코드.\n- KRW: 한국 원화\n- USD: 미국 달러\n\n클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.\n"
              },
              "asks": {
                "type": "array",
                "description": "매도호가 목록 (낮은 가격순)",
                "items": {
                  "type": "object",
                  "required": [
                    "price",
                    "volume"
                  ],
                  "properties": {
                    "price": {
                      "type": "string",
                      "format": "decimal",
                      "maxLength": 30,
                      "description": "호가",
                      "example": "72100"
                    },
                    "volume": {
                      "type": "string",
                      "format": "decimal",
                      "maxLength": 30,
                      "description": "잔량",
                      "example": "8500"
                    }
                  }
                }
              },
              "bids": {
                "type": "array",
                "description": "매수호가 목록 (높은 가격순)",
                "items": {
                  "type": "object",
                  "required": [
                    "price",
                    "volume"
                  ],
                  "properties": {
                    "price": {
                      "type": "string",
                      "format": "decimal",
                      "maxLength": 30,
                      "description": "호가",
                      "example": "72100"
                    },
                    "volume": {
                      "type": "string",
                      "format": "decimal",
                      "maxLength": 30,
                      "description": "잔량",
                      "example": "8500"
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
          "name": "orderbookMessage",
          "summary": "실시간 호가",
          "payload": {
            "type": "message",
            "topic": "orderbook:kr:005930",
            "data": {
              "timestamp": "2026-06-18T23:30:00.000+09:00",
              "currency": "KRW",
              "asks": [
                {
                  "price": "71500",
                  "volume": "5"
                }
              ],
              "bids": [
                {
                  "price": "71400",
                  "volume": "10"
                }
              ]
            }
          }
        }
      ]
    }
  }
}
````

## 연결된 연산

### subscribeOrderbook

````json
{
  "action": "send",
  "channel": {
    "$ref": "#/channels/realtime-orderbook"
  },
  "title": "[송신] 호가 구독 선언",
  "summary": "orderbook:us / orderbook:kr 항목을 담은 선언 배열 전송 (full-replace)",
  "messages": [
    {
      "$ref": "#/channels/realtime-orderbook/messages/declare"
    }
  ]
}
````

### receiveOrderbook

````json
{
  "action": "receive",
  "channel": {
    "$ref": "#/channels/realtime-orderbook"
  },
  "title": "[수신] 실시간 호가",
  "summary": "구독 종목의 호가가 갱신될 때마다 푸시",
  "messages": [
    {
      "$ref": "#/channels/realtime-orderbook/messages/orderbookStream"
    }
  ]
}
````

[전체 AsyncAPI 정의·서버·보안·내부 참조](ASYNCAPI_SPEC.md) · [연동 가이드](OVERVIEW.md)
