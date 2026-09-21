> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/OrderHistoryApi.md
> 문서 버전: 1.2.17

# OrderHistoryApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrder**](ORDER_HISTORY.md#getOrder) | **GET** /api/v1/orders/{orderId} | 주문 상세 조회 |
| [**getOrders**](ORDER_HISTORY.md#getOrders) | **GET** /api/v1/orders | 주문 목록 조회 |


<a name="getOrder"></a>
# **getOrder**
> getOrder_200_response getOrder(X-Tossinvest-Account, orderId)

주문 상세 조회

    특정 주문의 상세 정보를 조회합니다. 모든 주문 상태(체결 완료, 취소, 거부 등)의 주문을 조회할 수 있습니다.  **Rate Limits Group**: `ORDER_HISTORY` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **orderId** | **String**| 주문 식별자. 서버에서 발급한 opaque token 입니다.  | [default to null] |

### Return type

[**getOrder_200_response**](MODEL_GET_ORDER_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getOrders"></a>
# **getOrders**
> getOrders_200_response getOrders(X-Tossinvest-Account, status, symbol, from, to, cursor, limit)

주문 목록 조회

    주문 목록을 조회합니다. status 파라미터로 주문 상태를 필터링합니다.  **지원하는 status 값:** - 진행 중 주문: `OPEN` -- PENDING, PARTIAL_FILLED, PENDING_CANCEL, PENDING_REPLACE 상태의 주문을 반환 - 종료된 주문: `CLOSED` -- FILLED, CANCELED, REJECTED, REPLACED 등 종료 상태 주문을 반환합니다.  symbol을 지정하면 해당 종목의 주문만 필터링하여 반환합니다.  **조회 범위:** Open API 가 지원하는 호가 유형(지정가 · 시장가 · 장마감지정가)으로 접수된 주문만 반환합니다. 장후시간외 종가 · 장전시간외 종가 등 Open API 로 주문할 수 없는 호가 유형의 주문은 `OPEN`·`CLOSED` 목록과 주문 상세 조회 모두에서 조회되지 않습니다.  **페이징 동작:** - `status=OPEN`: 모든 대기 중 주문을 전량 반환합니다. `limit`, `cursor` 는 무시되며, `from`/`to` 만 주문 생성일(`orderedAt`, KST 기준) 범위 필터로 적용됩니다 (미지정 시 전체 기간). - `status=CLOSED`: `limit` (기본 20, 최대 100), `cursor`, `from`/`to` 파라미터 모두 적용됩니다.  **Rate Limits Group**: `ORDER_HISTORY` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **status** | **String**| 주문 라이프사이클 그룹 필터. 이 값은 각 주문의 세부 상태(`orders[].status`)를 **그룹화한 라벨**이며, `orders[].status` 와 값 체계가 다릅니다.  - `OPEN`: 진행 중 주문 그룹 — `orders[].status` ∈ `{PENDING, PARTIAL_FILLED, PENDING_CANCEL, PENDING_REPLACE}` - `CLOSED`: 종료된 주문 그룹 — `orders[].status` ∈ `{FILLED, CANCELED, REJECTED, REPLACED, CANCEL_REJECTED, REPLACE_REJECTED, PARTIAL_FILLED}`  예: `status=OPEN` 을 요청하면 응답의 `orders[].status` 는 개별 주문에 따라 `PENDING`, `PARTIAL_FILLED`, `PENDING_CANCEL`, `PENDING_REPLACE` 중 하나로 내려옵니다.  | [default to null] [enum: OPEN, CLOSED] |
| **symbol** | **String**| 종목 심볼. 지정 시 해당 종목의 주문만 조회. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: `005930`·`0101N0`), US: 영문 티커 (`AAPL`). 영문 대/소문자, 숫자, '.', '-' 만 허용한다.  | [optional] [default to null] |
| **from** | **date**| 조회 시작일 (inclusive, KST 기준). 주문 생성 시간(`orderedAt`) 기준. 미지정 시 전체 기간.  | [optional] [default to null] |
| **to** | **date**| 조회 종료일 (inclusive, KST 기준). 주문 생성 시간(`orderedAt`) 기준. 미지정 시 전체 기간.  | [optional] [default to null] |
| **cursor** | **String**| 페이지네이션 커서. `OPEN` 에서는 무시됩니다. `CLOSED` 에서는 다음 페이지 조회에 사용됩니다.  | [optional] [default to null] |
| **limit** | **Integer**| 페이지 크기. `OPEN` 에서는 무시됩니다 (전량 반환). `CLOSED` 에서는 적용됩니다 (기본 20, 최대 100).  | [optional] [default to 20] |

### Return type

[**getOrders_200_response**](MODEL_GET_ORDERS_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## GET /api/v1/orders

### `/summary`

주문 목록 조회

### `/description`

주문 목록을 조회합니다.
status 파라미터로 주문 상태를 필터링합니다.

**지원하는 status 값:**
- 진행 중 주문: `OPEN` -- PENDING, PARTIAL_FILLED, PENDING_CANCEL, PENDING_REPLACE 상태의 주문을 반환
- 종료된 주문: `CLOSED` -- FILLED, CANCELED, REJECTED, REPLACED 등 종료 상태 주문을 반환합니다.

symbol을 지정하면 해당 종목의 주문만 필터링하여 반환합니다.

**조회 범위:**
Open API 가 지원하는 호가 유형(지정가 · 시장가 · 장마감지정가)으로 접수된 주문만 반환합니다.
장후시간외 종가 · 장전시간외 종가 등 Open API 로 주문할 수 없는 호가 유형의 주문은
`OPEN`·`CLOSED` 목록과 주문 상세 조회 모두에서 조회되지 않습니다.

**페이징 동작:**
- `status=OPEN`: 모든 대기 중 주문을 전량 반환합니다. `limit`, `cursor` 는 무시되며, `from`/`to` 만 주문 생성일(`orderedAt`, KST 기준) 범위 필터로 적용됩니다 (미지정 시 전체 기간).
- `status=CLOSED`: `limit` (기본 20, 최대 100), `cursor`, `from`/`to` 파라미터 모두 적용됩니다.

**Rate Limits Group**: `ORDER_HISTORY`


### `/parameters/1/description`

주문 라이프사이클 그룹 필터. 이 값은 각 주문의 세부 상태(`orders[].status`)를 **그룹화한 라벨**이며, `orders[].status` 와 값 체계가 다릅니다.

- `OPEN`: 진행 중 주문 그룹 — `orders[].status` ∈ `{PENDING, PARTIAL_FILLED, PENDING_CANCEL, PENDING_REPLACE}`
- `CLOSED`: 종료된 주문 그룹 — `orders[].status` ∈ `{FILLED, CANCELED, REJECTED, REPLACED, CANCEL_REJECTED, REPLACE_REJECTED, PARTIAL_FILLED}`

예: `status=OPEN` 을 요청하면 응답의 `orders[].status` 는 개별 주문에 따라 `PENDING`, `PARTIAL_FILLED`, `PENDING_CANCEL`, `PENDING_REPLACE` 중 하나로 내려옵니다.


### `/parameters/2/description`

종목 심볼. 지정 시 해당 종목의 주문만 조회.
KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: `005930`·`0101N0`), US: 영문 티커 (`AAPL`).
영문 대/소문자, 숫자, '.', '-' 만 허용한다.


### `/parameters/2/examples/krStock/summary`

국내주식 (삼성전자)

### `/parameters/2/examples/usStock/summary`

해외주식 (Apple)

### `/parameters/3/description`

조회 시작일 (inclusive, KST 기준). 주문 생성 시간(`orderedAt`) 기준. 미지정 시 전체 기간.


### `/parameters/4/description`

조회 종료일 (inclusive, KST 기준). 주문 생성 시간(`orderedAt`) 기준. 미지정 시 전체 기간.


### `/parameters/5/description`

페이지네이션 커서. `OPEN` 에서는 무시됩니다. `CLOSED` 에서는 다음 페이지 조회에 사용됩니다.


### `/parameters/6/description`

페이지 크기. `OPEN` 에서는 무시됩니다 (전량 반환). `CLOSED` 에서는 적용됩니다 (기본 20, 최대 100).


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/pendingMixed/summary`

대기중 주문 — 국내+해외 혼합 (전량 반환)

### `/responses/200/content/application/json/examples/completedWithNextPage/summary`

완료된 주문 — 다음 페이지 있음

### `/responses/200/content/application/json/examples/empty/summary`

주문 없음

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/invalidStatus/summary`

유효하지 않은 주문 상태 필터

### `/responses/400/content/application/json/examples/accountHeaderRequired/summary`

X-Tossinvest-Account 헤더 누락

### 전체 연산 정의

````json
{
  "tags": [
    "Order History"
  ],
  "summary": "주문 목록 조회",
  "description": "주문 목록을 조회합니다.\nstatus 파라미터로 주문 상태를 필터링합니다.\n\n**지원하는 status 값:**\n- 진행 중 주문: `OPEN` -- PENDING, PARTIAL_FILLED, PENDING_CANCEL, PENDING_REPLACE 상태의 주문을 반환\n- 종료된 주문: `CLOSED` -- FILLED, CANCELED, REJECTED, REPLACED 등 종료 상태 주문을 반환합니다.\n\nsymbol을 지정하면 해당 종목의 주문만 필터링하여 반환합니다.\n\n**조회 범위:**\nOpen API 가 지원하는 호가 유형(지정가 · 시장가 · 장마감지정가)으로 접수된 주문만 반환합니다.\n장후시간외 종가 · 장전시간외 종가 등 Open API 로 주문할 수 없는 호가 유형의 주문은\n`OPEN`·`CLOSED` 목록과 주문 상세 조회 모두에서 조회되지 않습니다.\n\n**페이징 동작:**\n- `status=OPEN`: 모든 대기 중 주문을 전량 반환합니다. `limit`, `cursor` 는 무시되며, `from`/`to` 만 주문 생성일(`orderedAt`, KST 기준) 범위 필터로 적용됩니다 (미지정 시 전체 기간).\n- `status=CLOSED`: `limit` (기본 20, 최대 100), `cursor`, `from`/`to` 파라미터 모두 적용됩니다.\n\n**Rate Limits Group**: `ORDER_HISTORY`\n",
  "operationId": "getOrders",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/AccountSeq"
    },
    {
      "name": "status",
      "in": "query",
      "required": true,
      "description": "주문 라이프사이클 그룹 필터. 이 값은 각 주문의 세부 상태(`orders[].status`)를 **그룹화한 라벨**이며, `orders[].status` 와 값 체계가 다릅니다.\n\n- `OPEN`: 진행 중 주문 그룹 — `orders[].status` ∈ `{PENDING, PARTIAL_FILLED, PENDING_CANCEL, PENDING_REPLACE}`\n- `CLOSED`: 종료된 주문 그룹 — `orders[].status` ∈ `{FILLED, CANCELED, REJECTED, REPLACED, CANCEL_REJECTED, REPLACE_REJECTED, PARTIAL_FILLED}`\n\n예: `status=OPEN` 을 요청하면 응답의 `orders[].status` 는 개별 주문에 따라 `PENDING`, `PARTIAL_FILLED`, `PENDING_CANCEL`, `PENDING_REPLACE` 중 하나로 내려옵니다.\n",
      "schema": {
        "type": "string",
        "enum": [
          "OPEN",
          "CLOSED"
        ]
      },
      "example": "OPEN"
    },
    {
      "name": "symbol",
      "in": "query",
      "required": false,
      "description": "종목 심볼. 지정 시 해당 종목의 주문만 조회.\nKRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: `005930`·`0101N0`), US: 영문 티커 (`AAPL`).\n영문 대/소문자, 숫자, '.', '-' 만 허용한다.\n",
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9.\\-]+$"
      },
      "examples": {
        "krStock": {
          "summary": "국내주식 (삼성전자)",
          "value": "005930"
        },
        "usStock": {
          "summary": "해외주식 (Apple)",
          "value": "AAPL"
        }
      }
    },
    {
      "name": "from",
      "in": "query",
      "required": false,
      "description": "조회 시작일 (inclusive, KST 기준). 주문 생성 시간(`orderedAt`) 기준. 미지정 시 전체 기간.\n",
      "schema": {
        "type": "string",
        "format": "date"
      },
      "example": "2026-03-01"
    },
    {
      "name": "to",
      "in": "query",
      "required": false,
      "description": "조회 종료일 (inclusive, KST 기준). 주문 생성 시간(`orderedAt`) 기준. 미지정 시 전체 기간.\n",
      "schema": {
        "type": "string",
        "format": "date"
      },
      "example": "2026-03-31"
    },
    {
      "name": "cursor",
      "in": "query",
      "required": false,
      "description": "페이지네이션 커서. `OPEN` 에서는 무시됩니다. `CLOSED` 에서는 다음 페이지 조회에 사용됩니다.\n",
      "schema": {
        "type": "string"
      }
    },
    {
      "name": "limit",
      "in": "query",
      "required": false,
      "description": "페이지 크기. `OPEN` 에서는 무시됩니다 (전량 반환). `CLOSED` 에서는 적용됩니다 (기본 20, 최대 100).\n",
      "schema": {
        "type": "integer",
        "minimum": 1,
        "maximum": 100,
        "default": 20
      }
    }
  ],
  "responses": {
    "200": {
      "description": "성공",
      "content": {
        "application/json": {
          "schema": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ApiResponse"
              },
              {
                "type": "object",
                "properties": {
                  "result": {
                    "$ref": "#/components/schemas/PaginatedOrderResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "pendingMixed": {
              "summary": "대기중 주문 — 국내+해외 혼합 (전량 반환)",
              "value": {
                "result": {
                  "orders": [
                    {
                      "orderId": "bAGzNvMOOTa5Uy0xVzYNbxDJ3Qpobwau4jDF3hyZZGWbpHm7wha8CFZc7aXVOWAl",
                      "symbol": "005930",
                      "side": "BUY",
                      "orderType": "LIMIT",
                      "timeInForce": "DAY",
                      "status": "PENDING",
                      "price": "70000",
                      "quantity": "10",
                      "orderAmount": null,
                      "currency": "KRW",
                      "orderedAt": "2026-03-29T09:30:00+09:00",
                      "canceledAt": null,
                      "execution": {
                        "filledQuantity": "0",
                        "averageFilledPrice": null,
                        "filledAmount": null,
                        "commission": null,
                        "tax": null,
                        "filledAt": null,
                        "settlementDate": null
                      }
                    },
                    {
                      "orderId": "RpP3_wtsiKe9btBvdendaHoBqOIY_Zb_xPkRfYaqCIvf2FXtMDv_mo7VnD7KB-ia",
                      "symbol": "AAPL",
                      "side": "SELL",
                      "orderType": "LIMIT",
                      "timeInForce": "DAY",
                      "status": "PARTIAL_FILLED",
                      "price": "185.5",
                      "quantity": "5",
                      "orderAmount": null,
                      "currency": "USD",
                      "orderedAt": "2026-03-29T10:00:00+09:00",
                      "canceledAt": null,
                      "execution": {
                        "filledQuantity": "2",
                        "averageFilledPrice": "185.25",
                        "filledAmount": "370.5",
                        "commission": "0.66",
                        "tax": "0",
                        "filledAt": "2026-03-29T10:00:05+09:00",
                        "settlementDate": null
                      }
                    }
                  ],
                  "nextCursor": null,
                  "hasNext": false
                }
              }
            },
            "completedWithNextPage": {
              "summary": "완료된 주문 — 다음 페이지 있음",
              "value": {
                "result": {
                  "orders": [
                    {
                      "orderId": "0d5QIHjmtksbsmM-hBRAgP-ExI8iodGm9fAR5txelPfnMM8XQ_swoJdwL5RpGWMo",
                      "symbol": "005930",
                      "side": "BUY",
                      "orderType": "LIMIT",
                      "timeInForce": "DAY",
                      "status": "FILLED",
                      "price": "70000",
                      "quantity": "10",
                      "orderAmount": null,
                      "currency": "KRW",
                      "orderedAt": "2026-03-28T09:30:00+09:00",
                      "canceledAt": null,
                      "execution": {
                        "filledQuantity": "10",
                        "averageFilledPrice": "70000",
                        "filledAmount": "700000",
                        "commission": "1400",
                        "tax": "0",
                        "filledAt": "2026-03-28T09:31:15+09:00",
                        "settlementDate": "2026-03-30"
                      }
                    }
                  ],
                  "nextCursor": "eyJvcmRlcmVkQXQiOiIyMDI2LTAzLTI4VDA5OjMwOjAwKzA5OjAwIiwib3JkZXJJZCI6Ik9SRDIwMjYwMzI4MDAxIn0=",
                  "hasNext": true
                }
              }
            },
            "empty": {
              "summary": "주문 없음",
              "value": {
                "result": {
                  "orders": [],
                  "nextCursor": null,
                  "hasNext": false
                }
              }
            }
          }
        }
      }
    },
    "400": {
      "description": "잘못된 요청",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "invalidStatus": {
              "summary": "유효하지 않은 주문 상태 필터",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "유효하지 않은 주문 상태 필터입니다. OPEN 또는 CLOSED 만 허용됩니다.",
                  "data": {
                    "field": "status",
                    "allowedValues": [
                      "OPEN",
                      "CLOSED"
                    ]
                  }
                }
              }
            },
            "accountHeaderRequired": {
              "summary": "X-Tossinvest-Account 헤더 누락",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "account-header-required",
                  "message": "x-tossinvest-account 헤더가 필요합니다."
                }
              }
            }
          }
        }
      }
    },
    "401": {
      "$ref": "#/components/responses/Unauthorized"
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorOrderHistory"
    }
  }
}
````

## GET /api/v1/orders/{orderId}

### `/summary`

주문 상세 조회

### `/description`

특정 주문의 상세 정보를 조회합니다.
모든 주문 상태(체결 완료, 취소, 거부 등)의 주문을 조회할 수 있습니다.

**Rate Limits Group**: `ORDER_HISTORY`


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/krLimitFilled/summary`

국내주식 지정가 매수 — 체결 완료

### `/responses/200/content/application/json/examples/usMarketPartialFilled/summary`

해외주식 시장가 매수 — 부분 체결

### `/responses/200/content/application/json/examples/rejected/summary`

주문 거부

### 전체 연산 정의

````json
{
  "tags": [
    "Order History"
  ],
  "summary": "주문 상세 조회",
  "description": "특정 주문의 상세 정보를 조회합니다.\n모든 주문 상태(체결 완료, 취소, 거부 등)의 주문을 조회할 수 있습니다.\n\n**Rate Limits Group**: `ORDER_HISTORY`\n",
  "operationId": "getOrder",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/AccountSeq"
    },
    {
      "$ref": "#/components/parameters/OrderId"
    }
  ],
  "responses": {
    "200": {
      "description": "성공",
      "content": {
        "application/json": {
          "schema": {
            "allOf": [
              {
                "$ref": "#/components/schemas/ApiResponse"
              },
              {
                "type": "object",
                "properties": {
                  "result": {
                    "$ref": "#/components/schemas/Order"
                  }
                }
              }
            ]
          },
          "examples": {
            "krLimitFilled": {
              "summary": "국내주식 지정가 매수 — 체결 완료",
              "value": {
                "result": {
                  "orderId": "0d5QIHjmtksbsmM-hBRAgP-ExI8iodGm9fAR5txelPfnMM8XQ_swoJdwL5RpGWMo",
                  "symbol": "005930",
                  "side": "BUY",
                  "orderType": "LIMIT",
                  "timeInForce": "DAY",
                  "status": "FILLED",
                  "price": "70000",
                  "quantity": "10",
                  "orderAmount": null,
                  "currency": "KRW",
                  "orderedAt": "2026-03-28T09:30:00+09:00",
                  "canceledAt": null,
                  "execution": {
                    "filledQuantity": "10",
                    "averageFilledPrice": "70000",
                    "filledAmount": "700000",
                    "commission": "1400",
                    "tax": "0",
                    "filledAt": "2026-03-28T09:31:15+09:00",
                    "settlementDate": "2026-03-30"
                  }
                }
              }
            },
            "usMarketPartialFilled": {
              "summary": "해외주식 시장가 매수 — 부분 체결",
              "value": {
                "result": {
                  "orderId": "J4lDkgVA-pMiRPOqXd2nBjxTj8hsTVhzOhIth7i1Izq14XYxIg1r_QTDEH7RTL8d",
                  "symbol": "AAPL",
                  "side": "BUY",
                  "orderType": "MARKET",
                  "timeInForce": "DAY",
                  "status": "PARTIAL_FILLED",
                  "price": null,
                  "quantity": "5",
                  "orderAmount": null,
                  "currency": "USD",
                  "orderedAt": "2026-03-28T23:30:00+09:00",
                  "canceledAt": null,
                  "execution": {
                    "filledQuantity": "3",
                    "averageFilledPrice": "185.25",
                    "filledAmount": "555.75",
                    "commission": "0.99",
                    "tax": "0",
                    "filledAt": "2026-03-28T23:30:05+09:00",
                    "settlementDate": null
                  }
                }
              }
            },
            "rejected": {
              "summary": "주문 거부",
              "value": {
                "result": {
                  "orderId": "Oqqsu76YSdwKZsdKbPwy-D7buUwy-RH2xZYbYSzAyAnlPy48Al5Lb7FyMKwibw4i",
                  "symbol": "AAPL",
                  "side": "BUY",
                  "orderType": "MARKET",
                  "timeInForce": "DAY",
                  "status": "REJECTED",
                  "price": null,
                  "quantity": "0.5",
                  "orderAmount": null,
                  "currency": "USD",
                  "orderedAt": "2026-03-28T23:30:00+09:00",
                  "canceledAt": null,
                  "execution": {
                    "filledQuantity": "0",
                    "averageFilledPrice": null,
                    "filledAmount": null,
                    "commission": null,
                    "tax": null,
                    "filledAt": null,
                    "settlementDate": null
                  }
                }
              }
            }
          }
        }
      }
    },
    "400": {
      "$ref": "#/components/responses/AccountHeaderRequired"
    },
    "401": {
      "$ref": "#/components/responses/Unauthorized"
    },
    "404": {
      "$ref": "#/components/responses/OrderNotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorOrderHistory"
    }
  }
}
````
