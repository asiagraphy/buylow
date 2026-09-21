> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/asyncapi.json#/channels/connection
> 문서 버전: 1.2.2

# Connection

### `/summary`

웹소켓 연결 수립과 프로토콜 공통 규칙을 다루는 항목입니다. handshake 인증, 선언형(full-replace) 구독 모델, 수신 프레임 구분 규칙, 연결·구독 한도, keepalive, 종료·재연결 동작을 설명합니다. 개별 데이터 채널 (Trade·Orderbook·Order Event)을 구독하기 전에 먼저 읽어보세요.

### `/description`

`wss://openapi-ws.tossinvest.com/ws/v1` 로 요청합니다. `Authorization: Bearer {access_token}`
헤더가 필요하며(`POST /oauth2/token` 으로 발급), HTTP 는 handshake 단계에서만 쓰입니다(성공 시 `101`, 토큰 없음·무효·만료 `401`,
허용 IP 미등록 `403`, 서버 내부 오류 `503`). 허용 IP 는 REST 와 동일한 목록(WTS 설정 > Open API > 허용 IP 관리)이 적용됩니다.
인증은 handshake 시점 1회이며, 연결 유지 중 액세스 토큰이 만료되어도 연결은 끊기지 않습니다.

**구독 선언 (모든 채널 공통)** — 연결 후 JSON **배열 1개**를 텍스트 프레임으로 보냅니다. 배열 하나에 여러 채널
(체결·호가·주문)을 함께 담을 수 있고, 이 배열이 곧 현재 구독 전체입니다 (**선언형 full-replace** — 빠진 항목은
자동 해제, 빈 배열 `[]` 은 전체 해제, subscribe/unsubscribe 액션 없음). 형식은 각 채널 항목의 구독 선언을 참고하세요.
선언 직후 도착하는 구독 ack 의 `rejected[]` 항목은 원인을 수정하기 전에는 재선언에 포함해도 같은 이유로 다시
거부됩니다. 거부된 항목은 선언 목록에서 빼거나 수정한 뒤 다시 선언하세요 — 일부 거부여도 `subscribed` 항목은
정상 구독되고 연결은 유지됩니다.

**수신 프레임 디스패치** — 연결 하나로 아래 프레임들이 섞여 도착합니다. top-level `type` 으로 구분해
처리하세요.

| 프레임 | 구분 | 도착 시점 |
|---|---|---|
| 구독 ack | `"type": "subscriptions"` | 구독 선언 직후 — 데이터보다 먼저 도착 |
| 실시간 데이터 | `"type": "message"` + `topic` | 구독 대상 갱신 시마다 |
| 에러 | `"type": "error"` | 선언 전체 실패 시(기존 구독 유지) 또는 서버 배포 시(`server-shutdown`) |
| keepalive | `"type": "pong"` | 텍스트 `PING`(대문자) 송신 직후 |

**한도**

| 항목 | 한도 | 초과 시 |
|---|---|---|
| 동시 연결 | 계정당 **2개** | 새 연결은 수락되고 가장 오래된 연결이 종료 |
| 연결당 구독 수 | **100건** (`codes` 합산) | `too-many-topics` 에러 프레임 |
| 선언 빈도 | **5회/초** | `rate-limit-exceeded` 에러 프레임 |

구독 수는 채널×종목 조합 기준입니다 — 같은 종목이라도 채널이 다르면 각각 1건입니다 (`trade:us:AAPL` + `orderbook:us:AAPL` = 2건).
`rate-limit-exceeded` 를 받으면 약 1초 대기 후 재선언하세요 (REST 와 달리 `Retry-After` 헤더는 제공되지 않습니다).

**연결 유지** — 서버는 **클라이언트로부터의 수신이 180초간 없으면** 연결을 종료합니다. 서버가 보내주는 데이터는
이 타이머를 리셋하지 않으므로, 데이터를 받고 있는 중에도 180초 이내 주기로 `PING` 을 보내세요(**60초 간격 권장**).
JSON 이 아닌 순수 텍스트 프레임 `PING`(대문자 4글자)을 보내면 `{"type":"pong"}` 으로 응답하며, 웹소켓 표준
ping/pong 프레임도 지원됩니다.

**종료·재연결** — 서버 배포 시에는 종료 직전에 `{"type":"error","error":{"code":"server-shutdown",...}}` 프레임이
먼저 도착합니다 — 받으면 재연결 후 구독을 다시 선언하세요. 그 외의 경우(idle 초과, 주문 채널 backpressure,
동시 연결 한도 초과로 가장 오래된 연결이 밀려나는 경우 등)에는 별도 close code 없이 종료될 수 있어 클라이언트에는
비정상 종료로 보일 수 있습니다. 끊김을 감지하면 지수 백오프(1s → 2s → 4s ..., jitter 포함 — REST `429` 대응과
동일)로 재시도하며 구독을 다시 선언하세요.
재연결하기 전에 쓰던 연결을 먼저 닫아 주세요. 이전 연결이 남아 있으면 새로 연결할 때마다 앞의 연결이 밀려나 끊김이 반복될 수 있습니다.

### `/messages/subscriptionsAck/summary`

구독 선언 직후 내려오는 확정·거부 결과 (데이터보다 먼저 도착)

### `/messages/subscriptionsAck/payload/description`

구독 선언 직후 내려오는 ack. 구독 확정(`subscribed`)·거부(`rejected`) 결과를 담습니다.

### `/messages/subscriptionsAck/payload/properties/id/description`

요청에 `id` 가 있을 때만 echo

### `/messages/subscriptionsAck/payload/properties/subscribed/description`

구독 확정된 full key 목록 (시세 `trade:us:AAPL`, 주문 `personal:order:3`)

### `/messages/subscriptionsAck/payload/properties/rejected/description`

구독 실패 항목 + 사유 (나머지는 정상 구독)

### `/messages/subscriptionsAck/payload/properties/rejected/items/properties/target/description`

실패한 full key

### `/messages/subscriptionsAck/payload/properties/rejected/items/properties/code/description`

`stock-not-found` · `symbol-market-mismatch` · `account-not-found`

### `/messages/subscriptionsAck/examples/0/summary`

구독 ack (전부 확정)

### `/messages/subscriptionsAck/examples/1/summary`

구독 ack (일부 거부 — 나머지는 정상 구독)

### `/messages/errorFrame/summary`

선언 전체 실패(기존 구독 유지) 또는 서버 배포 시(server-shutdown) 도착

### `/messages/errorFrame/payload/description`

선언 전체가 실패했을 때(기존 구독 유지) 또는 서버 배포 시(`server-shutdown`, 프레임 직후 연결 종료 — 재연결 필요) 내려오는 프레임. `type` 은 `error` 고정입니다.

### `/messages/errorFrame/payload/properties/error/properties/code/description`

`wrong-format` · `no-type` · `invalid-type` · `no-codes` · `too-many-topics` · `too-many` · `rate-limit-exceeded` · `internal-error` · `server-shutdown`

### `/messages/errorFrame/payload/properties/id/description`

요청에 `id` 가 있을 때만 echo

### `/messages/errorFrame/examples/0/summary`

선언 실패

### `/messages/errorFrame/examples/1/summary`

서버 배포 시 도착 (프레임 직후 연결 종료 — 재연결 필요)

### `/messages/ping/summary`

keepalive 요청 — JSON 이 아닌 순수 텍스트 프레임 (대문자 4글자, 60초 간격 권장)

### `/messages/ping/payload/description`

따옴표 없는 순수 텍스트 PING 을 그대로 보냅니다. JSON 으로 감싸지 마세요 — 서버가 {"type":"pong"} 으로 응답합니다.

### `/messages/ping/examples/0/summary`

keepalive 요청 (60초 간격 권장)

### `/messages/pong/summary`

텍스트 PING(대문자) 에 대한 keepalive 응답

### `/messages/pong/payload/description`

텍스트 `PING`(대문자) 에 대한 keepalive 응답.

### `/messages/pong/examples/0/summary`

keepalive 응답

## 전체 채널 정의

````json
{
  "address": "/ws/v1",
  "title": "Connection",
  "summary": "웹소켓 연결 수립과 프로토콜 공통 규칙을 다루는 항목입니다. handshake 인증, 선언형(full-replace) 구독 모델, 수신 프레임 구분 규칙, 연결·구독 한도, keepalive, 종료·재연결 동작을 설명합니다. 개별 데이터 채널 (Trade·Orderbook·Order Event)을 구독하기 전에 먼저 읽어보세요.",
  "description": "`wss://openapi-ws.tossinvest.com/ws/v1` 로 요청합니다. `Authorization: Bearer {access_token}`\n헤더가 필요하며(`POST /oauth2/token` 으로 발급), HTTP 는 handshake 단계에서만 쓰입니다(성공 시 `101`, 토큰 없음·무효·만료 `401`,\n허용 IP 미등록 `403`, 서버 내부 오류 `503`). 허용 IP 는 REST 와 동일한 목록(WTS 설정 > Open API > 허용 IP 관리)이 적용됩니다.\n인증은 handshake 시점 1회이며, 연결 유지 중 액세스 토큰이 만료되어도 연결은 끊기지 않습니다.\n\n**구독 선언 (모든 채널 공통)** — 연결 후 JSON **배열 1개**를 텍스트 프레임으로 보냅니다. 배열 하나에 여러 채널\n(체결·호가·주문)을 함께 담을 수 있고, 이 배열이 곧 현재 구독 전체입니다 (**선언형 full-replace** — 빠진 항목은\n자동 해제, 빈 배열 `[]` 은 전체 해제, subscribe/unsubscribe 액션 없음). 형식은 각 채널 항목의 구독 선언을 참고하세요.\n선언 직후 도착하는 구독 ack 의 `rejected[]` 항목은 원인을 수정하기 전에는 재선언에 포함해도 같은 이유로 다시\n거부됩니다. 거부된 항목은 선언 목록에서 빼거나 수정한 뒤 다시 선언하세요 — 일부 거부여도 `subscribed` 항목은\n정상 구독되고 연결은 유지됩니다.\n\n**수신 프레임 디스패치** — 연결 하나로 아래 프레임들이 섞여 도착합니다. top-level `type` 으로 구분해\n처리하세요.\n\n| 프레임 | 구분 | 도착 시점 |\n|---|---|---|\n| 구독 ack | `\"type\": \"subscriptions\"` | 구독 선언 직후 — 데이터보다 먼저 도착 |\n| 실시간 데이터 | `\"type\": \"message\"` + `topic` | 구독 대상 갱신 시마다 |\n| 에러 | `\"type\": \"error\"` | 선언 전체 실패 시(기존 구독 유지) 또는 서버 배포 시(`server-shutdown`) |\n| keepalive | `\"type\": \"pong\"` | 텍스트 `PING`(대문자) 송신 직후 |\n\n**한도**\n\n| 항목 | 한도 | 초과 시 |\n|---|---|---|\n| 동시 연결 | 계정당 **2개** | 새 연결은 수락되고 가장 오래된 연결이 종료 |\n| 연결당 구독 수 | **100건** (`codes` 합산) | `too-many-topics` 에러 프레임 |\n| 선언 빈도 | **5회/초** | `rate-limit-exceeded` 에러 프레임 |\n\n구독 수는 채널×종목 조합 기준입니다 — 같은 종목이라도 채널이 다르면 각각 1건입니다 (`trade:us:AAPL` + `orderbook:us:AAPL` = 2건).\n`rate-limit-exceeded` 를 받으면 약 1초 대기 후 재선언하세요 (REST 와 달리 `Retry-After` 헤더는 제공되지 않습니다).\n\n**연결 유지** — 서버는 **클라이언트로부터의 수신이 180초간 없으면** 연결을 종료합니다. 서버가 보내주는 데이터는\n이 타이머를 리셋하지 않으므로, 데이터를 받고 있는 중에도 180초 이내 주기로 `PING` 을 보내세요(**60초 간격 권장**).\nJSON 이 아닌 순수 텍스트 프레임 `PING`(대문자 4글자)을 보내면 `{\"type\":\"pong\"}` 으로 응답하며, 웹소켓 표준\nping/pong 프레임도 지원됩니다.\n\n**종료·재연결** — 서버 배포 시에는 종료 직전에 `{\"type\":\"error\",\"error\":{\"code\":\"server-shutdown\",...}}` 프레임이\n먼저 도착합니다 — 받으면 재연결 후 구독을 다시 선언하세요. 그 외의 경우(idle 초과, 주문 채널 backpressure,\n동시 연결 한도 초과로 가장 오래된 연결이 밀려나는 경우 등)에는 별도 close code 없이 종료될 수 있어 클라이언트에는\n비정상 종료로 보일 수 있습니다. 끊김을 감지하면 지수 백오프(1s → 2s → 4s ..., jitter 포함 — REST `429` 대응과\n동일)로 재시도하며 구독을 다시 선언하세요.\n재연결하기 전에 쓰던 연결을 먼저 닫아 주세요. 이전 연결이 남아 있으면 새로 연결할 때마다 앞의 연결이 밀려나 끊김이 반복될 수 있습니다.",
  "messages": {
    "subscriptionsAck": {
      "name": "subscriptionsAck",
      "title": "[수신] 구독 ack",
      "summary": "구독 선언 직후 내려오는 확정·거부 결과 (데이터보다 먼저 도착)",
      "payload": {
        "type": "object",
        "description": "구독 선언 직후 내려오는 ack. 구독 확정(`subscribed`)·거부(`rejected`) 결과를 담습니다.",
        "required": [
          "type",
          "subscribed",
          "rejected"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "subscriptions"
            ]
          },
          "id": {
            "type": "string",
            "description": "요청에 `id` 가 있을 때만 echo",
            "example": "req-1"
          },
          "subscribed": {
            "type": "array",
            "description": "구독 확정된 full key 목록 (시세 `trade:us:AAPL`, 주문 `personal:order:3`)",
            "items": {
              "type": "string"
            }
          },
          "rejected": {
            "type": "array",
            "description": "구독 실패 항목 + 사유 (나머지는 정상 구독)",
            "items": {
              "type": "object",
              "required": [
                "target",
                "code",
                "message"
              ],
              "properties": {
                "target": {
                  "type": "string",
                  "description": "실패한 full key",
                  "example": "trade:us:NOPE"
                },
                "code": {
                  "type": "string",
                  "description": "`stock-not-found` · `symbol-market-mismatch` · `account-not-found`",
                  "example": "stock-not-found"
                },
                "message": {
                  "type": "string",
                  "example": "해당 종목을 찾을 수 없습니다."
                }
              }
            }
          }
        }
      },
      "examples": [
        {
          "name": "subscriptionsAck",
          "summary": "구독 ack (전부 확정)",
          "payload": {
            "type": "subscriptions",
            "id": "req-1",
            "subscribed": [
              "trade:us:AAPL",
              "trade:us:TSLA",
              "orderbook:kr:005930",
              "personal:order:3"
            ],
            "rejected": []
          }
        },
        {
          "name": "subscriptionsAckPartialReject",
          "summary": "구독 ack (일부 거부 — 나머지는 정상 구독)",
          "payload": {
            "type": "subscriptions",
            "id": "req-2",
            "subscribed": [
              "trade:kr:005930"
            ],
            "rejected": [
              {
                "target": "trade:kr:999999",
                "code": "stock-not-found",
                "message": "해당 종목을 찾을 수 없습니다."
              }
            ]
          }
        }
      ]
    },
    "errorFrame": {
      "name": "errorFrame",
      "title": "[수신] 에러",
      "summary": "선언 전체 실패(기존 구독 유지) 또는 서버 배포 시(server-shutdown) 도착",
      "payload": {
        "type": "object",
        "description": "선언 전체가 실패했을 때(기존 구독 유지) 또는 서버 배포 시(`server-shutdown`, 프레임 직후 연결 종료 — 재연결 필요) 내려오는 프레임. `type` 은 `error` 고정입니다.",
        "required": [
          "type",
          "error"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "error"
            ]
          },
          "error": {
            "type": "object",
            "required": [
              "code",
              "message"
            ],
            "properties": {
              "code": {
                "type": "string",
                "description": "`wrong-format` · `no-type` · `invalid-type` · `no-codes` · `too-many-topics` · `too-many` · `rate-limit-exceeded` · `internal-error` · `server-shutdown`",
                "example": "rate-limit-exceeded"
              },
              "message": {
                "type": "string",
                "example": "declare rate limit exceeded"
              }
            }
          },
          "id": {
            "type": "string",
            "description": "요청에 `id` 가 있을 때만 echo",
            "example": "req-1"
          }
        }
      },
      "examples": [
        {
          "name": "errorFrame",
          "summary": "선언 실패",
          "payload": {
            "type": "error",
            "error": {
              "code": "no-codes",
              "message": "codes must be a non-empty array of strings"
            },
            "id": "req-1"
          }
        },
        {
          "name": "serverShutdown",
          "summary": "서버 배포 시 도착 (프레임 직후 연결 종료 — 재연결 필요)",
          "payload": {
            "type": "error",
            "error": {
              "code": "server-shutdown",
              "message": "서버가 재시작됩니다. 재연결해주세요."
            }
          }
        }
      ]
    },
    "ping": {
      "name": "ping",
      "title": "[송신] PING",
      "summary": "keepalive 요청 — JSON 이 아닌 순수 텍스트 프레임 (대문자 4글자, 60초 간격 권장)",
      "contentType": "text/plain",
      "payload": {
        "type": "string",
        "const": "PING",
        "description": "따옴표 없는 순수 텍스트 PING 을 그대로 보냅니다. JSON 으로 감싸지 마세요 — 서버가 {\"type\":\"pong\"} 으로 응답합니다."
      },
      "examples": [
        {
          "name": "ping",
          "summary": "keepalive 요청 (60초 간격 권장)",
          "payload": "PING"
        }
      ]
    },
    "pong": {
      "name": "pong",
      "title": "[수신] pong",
      "summary": "텍스트 PING(대문자) 에 대한 keepalive 응답",
      "payload": {
        "type": "object",
        "description": "텍스트 `PING`(대문자) 에 대한 keepalive 응답.",
        "required": [
          "type"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "pong"
            ]
          }
        }
      },
      "examples": [
        {
          "name": "pong",
          "summary": "keepalive 응답",
          "payload": {
            "type": "pong"
          }
        }
      ]
    }
  }
}
````

## 연결된 연산

### receiveSubscriptionsAck

````json
{
  "action": "receive",
  "channel": {
    "$ref": "#/channels/connection"
  },
  "title": "[수신] 구독 ack",
  "summary": "선언 직후 확정·거부 결과 (모든 채널 공통)",
  "messages": [
    {
      "$ref": "#/channels/connection/messages/subscriptionsAck"
    }
  ]
}
````

### receiveError

````json
{
  "action": "receive",
  "channel": {
    "$ref": "#/channels/connection"
  },
  "title": "[수신] 에러",
  "summary": "선언 전체 실패(기존 구독 유지) 또는 서버 배포 시 도착 (모든 채널 공통)",
  "messages": [
    {
      "$ref": "#/channels/connection/messages/errorFrame"
    }
  ]
}
````

### sendPing

````json
{
  "action": "send",
  "channel": {
    "$ref": "#/channels/connection"
  },
  "title": "[송신] PING",
  "summary": "keepalive 요청 — JSON 이 아닌 순수 텍스트 프레임 (대문자 4글자, 60초 간격 권장)",
  "messages": [
    {
      "$ref": "#/channels/connection/messages/ping"
    }
  ]
}
````

### receivePong

````json
{
  "action": "receive",
  "channel": {
    "$ref": "#/channels/connection"
  },
  "title": "[수신] pong",
  "summary": "텍스트 PING 에 대한 keepalive 응답",
  "messages": [
    {
      "$ref": "#/channels/connection/messages/pong"
    }
  ]
}
````

[전체 AsyncAPI 정의·서버·보안·내부 참조](ASYNCAPI_SPEC.md) · [연동 가이드](OVERVIEW.md)
