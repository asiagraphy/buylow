> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/ConditionalOrderHistoryApi.md
> 문서 버전: 1.2.17

# ConditionalOrderHistoryApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getConditionalOrder**](CONDITIONAL_ORDER_HISTORY.md#getConditionalOrder) | **GET** /api/v1/conditional-orders/{conditionalOrderId} | 조건주문 상세 조회 |
| [**getConditionalOrders**](CONDITIONAL_ORDER_HISTORY.md#getConditionalOrders) | **GET** /api/v1/conditional-orders | 조건주문 목록 조회 |


<a name="getConditionalOrder"></a>
# **getConditionalOrder**
> getConditionalOrder_200_response getConditionalOrder(X-Tossinvest-Account, conditionalOrderId)

조건주문 상세 조회

    조건주문 단건 상세를 조회합니다. 진행 중 + 종료된 조건주문을 모두 조회할 수 있습니다. `conditionalOrderId` 로 조건주문을 식별합니다.  **Rate Limits Group**: `CONDITIONAL_ORDER_HISTORY` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **conditionalOrderId** | **String**| 조건주문 식별자 (등록/목록 응답의 `conditionalOrderId`) | [default to null] |

### Return type

[**getConditionalOrder_200_response**](MODEL_GET_CONDITIONAL_ORDER_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getConditionalOrders"></a>
# **getConditionalOrders**
> getConditionalOrders_200_response getConditionalOrders(X-Tossinvest-Account, status, symbol, cursor, limit)

조건주문 목록 조회

    조건주문 목록을 조회합니다.  **모든 타입 반환**: 이 API 로 등록한 조건주문뿐 아니라 다른 채널(토스증권 앱 등)에서 등록한 조건주문도 함께 반환됩니다. 타입별 필터는 제공하지 않으며, 응답의 `type` 필드로 구분합니다.  **지원하는 status 값:** - `OPEN`: 진행 중(감시 중·일시중지·주문 진행 중 포함) 조건주문 - `CLOSED`: 종료된(완료·만료) 조건주문  `symbol` 을 지정하면 해당 종목의 조건주문만 반환합니다. `OPEN`/`CLOSED` 모두에서 사용할 수 있습니다.  **페이징**: 커서 기반. 응답의 `nextCursor` 를 다음 요청의 `cursor` 로 전달합니다. `limit` 기본 20, 최대 100.  **Rate Limits Group**: `CONDITIONAL_ORDER_HISTORY` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **status** | **String**| 조건주문 라이프사이클 그룹 필터. - `OPEN`: 진행 중 — 응답의 `status` ∈ `{WATCHING, PAUSED, ORDERING, ORDERED}` - `CLOSED`: 종료 — 응답의 `status` ∈ `{COMPLETED, EXPIRED}`  | [default to null] [enum: OPEN, CLOSED] |
| **symbol** | **String**| 종목 심볼 필터 (선택). `OPEN`/`CLOSED` 모두에서 사용할 수 있습니다. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: `005930`·`0101N0`), US: 영문 티커 (`AAPL`).  | [optional] [default to null] |
| **cursor** | **String**| 이전 응답의 `nextCursor` 값. 미지정 시 첫 페이지. | [optional] [default to null] |
| **limit** | **Integer**| 페이지 크기 (기본 20, 최대 100) | [optional] [default to 20] |

### Return type

[**getConditionalOrders_200_response**](MODEL_GET_CONDITIONAL_ORDERS_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## GET /api/v1/conditional-orders

### `/summary`

조건주문 목록 조회

### `/description`

조건주문 목록을 조회합니다.

**모든 타입 반환**: 이 API 로 등록한 조건주문뿐 아니라
다른 채널(토스증권 앱 등)에서 등록한 조건주문도 함께 반환됩니다.
타입별 필터는 제공하지 않으며, 응답의 `type` 필드로 구분합니다.

**지원하는 status 값:**
- `OPEN`: 진행 중(감시 중·일시중지·주문 진행 중 포함) 조건주문
- `CLOSED`: 종료된(완료·만료) 조건주문

`symbol` 을 지정하면 해당 종목의 조건주문만 반환합니다. `OPEN`/`CLOSED` 모두에서 사용할 수 있습니다.

**페이징**: 커서 기반. 응답의 `nextCursor` 를 다음 요청의 `cursor` 로 전달합니다.
`limit` 기본 20, 최대 100.

**Rate Limits Group**: `CONDITIONAL_ORDER_HISTORY`


### `/parameters/1/description`

조건주문 라이프사이클 그룹 필터.
- `OPEN`: 진행 중 — 응답의 `status` ∈ `{WATCHING, PAUSED, ORDERING, ORDERED}`
- `CLOSED`: 종료 — 응답의 `status` ∈ `{COMPLETED, EXPIRED}`


### `/parameters/2/description`

종목 심볼 필터 (선택). `OPEN`/`CLOSED` 모두에서 사용할 수 있습니다.
KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: `005930`·`0101N0`), US: 영문 티커 (`AAPL`).


### `/parameters/3/description`

이전 응답의 `nextCursor` 값. 미지정 시 첫 페이지.

### `/parameters/4/description`

페이지 크기 (기본 20, 최대 100)

### `/responses/200/description`

성공

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/invalidStatus/summary`

지원하지 않는 status

### `/responses/422/description`

비즈니스 규칙 위반

### 전체 연산 정의

````json
{
  "tags": [
    "Conditional Order History"
  ],
  "summary": "조건주문 목록 조회",
  "description": "조건주문 목록을 조회합니다.\n\n**모든 타입 반환**: 이 API 로 등록한 조건주문뿐 아니라\n다른 채널(토스증권 앱 등)에서 등록한 조건주문도 함께 반환됩니다.\n타입별 필터는 제공하지 않으며, 응답의 `type` 필드로 구분합니다.\n\n**지원하는 status 값:**\n- `OPEN`: 진행 중(감시 중·일시중지·주문 진행 중 포함) 조건주문\n- `CLOSED`: 종료된(완료·만료) 조건주문\n\n`symbol` 을 지정하면 해당 종목의 조건주문만 반환합니다. `OPEN`/`CLOSED` 모두에서 사용할 수 있습니다.\n\n**페이징**: 커서 기반. 응답의 `nextCursor` 를 다음 요청의 `cursor` 로 전달합니다.\n`limit` 기본 20, 최대 100.\n\n**Rate Limits Group**: `CONDITIONAL_ORDER_HISTORY`\n",
  "operationId": "getConditionalOrders",
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
      "description": "조건주문 라이프사이클 그룹 필터.\n- `OPEN`: 진행 중 — 응답의 `status` ∈ `{WATCHING, PAUSED, ORDERING, ORDERED}`\n- `CLOSED`: 종료 — 응답의 `status` ∈ `{COMPLETED, EXPIRED}`\n",
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
      "description": "종목 심볼 필터 (선택). `OPEN`/`CLOSED` 모두에서 사용할 수 있습니다.\nKRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: `005930`·`0101N0`), US: 영문 티커 (`AAPL`).\n",
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9.\\-]+$"
      },
      "example": "005930"
    },
    {
      "name": "cursor",
      "in": "query",
      "required": false,
      "description": "이전 응답의 `nextCursor` 값. 미지정 시 첫 페이지.",
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9_\\-]+$"
      }
    },
    {
      "name": "limit",
      "in": "query",
      "required": false,
      "description": "페이지 크기 (기본 20, 최대 100)",
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
                    "$ref": "#/components/schemas/PaginatedConditionalOrderResponse"
                  }
                }
              }
            ]
          },
          "example": {
            "result": {
              "conditionalOrders": [
                {
                  "conditionalOrderId": "gaZIG-dYMWil8AAXyPmlRg",
                  "type": "OCO",
                  "status": "WATCHING",
                  "symbol": "005930",
                  "market": "KR",
                  "quantity": "100",
                  "orderType": "LIMIT",
                  "expireDate": "2026-09-10",
                  "first": {
                    "type": "STOP",
                    "status": "WATCHING",
                    "triggerPrice": "305",
                    "targetProfitRate": null,
                    "orderPrice": "305",
                    "triggeredOrderId": null
                  },
                  "second": {
                    "type": "STOP",
                    "status": "WATCHING",
                    "triggerPrice": "295",
                    "targetProfitRate": null,
                    "orderPrice": "294.5",
                    "triggeredOrderId": null
                  },
                  "createdAt": "2026-06-12T09:00:00+09:00"
                }
              ],
              "nextCursor": "bmV4dC1rZXk",
              "hasNext": true
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
              "summary": "지원하지 않는 status",
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
            }
          }
        }
      }
    },
    "422": {
      "description": "비즈니스 규칙 위반",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          }
        }
      }
    }
  }
}
````

## GET /api/v1/conditional-orders/{conditionalOrderId}

### `/summary`

조건주문 상세 조회

### `/description`

조건주문 단건 상세를 조회합니다. 진행 중 + 종료된 조건주문을 모두 조회할 수 있습니다.
`conditionalOrderId` 로 조건주문을 식별합니다.

**Rate Limits Group**: `CONDITIONAL_ORDER_HISTORY`


### `/parameters/1/description`

조건주문 식별자 (등록/목록 응답의 `conditionalOrderId`)

### `/responses/200/description`

성공

### `/responses/400/description`

잘못된 요청 (형식이 잘못된 `conditionalOrderId` 등)

### `/responses/404/description`

조건주문 없음

### 전체 연산 정의

````json
{
  "tags": [
    "Conditional Order History"
  ],
  "summary": "조건주문 상세 조회",
  "description": "조건주문 단건 상세를 조회합니다. 진행 중 + 종료된 조건주문을 모두 조회할 수 있습니다.\n`conditionalOrderId` 로 조건주문을 식별합니다.\n\n**Rate Limits Group**: `CONDITIONAL_ORDER_HISTORY`\n",
  "operationId": "getConditionalOrder",
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
      "name": "conditionalOrderId",
      "in": "path",
      "required": true,
      "description": "조건주문 식별자 (등록/목록 응답의 `conditionalOrderId`)",
      "schema": {
        "type": "string"
      },
      "example": "gaZIG-dYMWil8AAXyPmlRg"
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
                    "$ref": "#/components/schemas/ConditionalOrderDetailResponse"
                  }
                }
              }
            ]
          },
          "example": {
            "result": {
              "conditionalOrderId": "gaZIG-dYMWil8AAXyPmlRg",
              "type": "OCO",
              "status": "WATCHING",
              "symbol": "005930",
              "market": "KR",
              "quantity": "100",
              "orderType": "LIMIT",
              "expireDate": "2026-09-10",
              "first": {
                "type": "STOP",
                "status": "WATCHING",
                "triggerPrice": "305",
                "targetProfitRate": null,
                "orderPrice": "305",
                "triggeredOrderId": null
              },
              "second": {
                "type": "STOP",
                "status": "WATCHING",
                "triggerPrice": "295",
                "targetProfitRate": null,
                "orderPrice": "294.5",
                "triggeredOrderId": null
              },
              "createdAt": "2026-06-12T09:00:00+09:00"
            }
          }
        }
      }
    },
    "400": {
      "description": "잘못된 요청 (형식이 잘못된 `conditionalOrderId` 등)",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          }
        }
      }
    },
    "404": {
      "description": "조건주문 없음",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          }
        }
      }
    }
  }
}
````
