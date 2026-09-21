> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/ConditionalOrderApi.md
> 문서 버전: 1.2.17

# ConditionalOrderApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelConditionalOrder**](CONDITIONAL_ORDER.md#cancelConditionalOrder) | **DELETE** /api/v1/conditional-orders/{conditionalOrderId} | 조건주문 취소 |
| [**createConditionalOrder**](CONDITIONAL_ORDER.md#createConditionalOrder) | **POST** /api/v1/conditional-orders | 조건주문 생성 |
| [**modifyConditionalOrder**](CONDITIONAL_ORDER.md#modifyConditionalOrder) | **POST** /api/v1/conditional-orders/{conditionalOrderId}/modify | 조건주문 수정 |


<a name="cancelConditionalOrder"></a>
# **cancelConditionalOrder**
> cancelConditionalOrder(X-Tossinvest-Account, conditionalOrderId)

조건주문 취소

    조건주문을 취소합니다. `conditionalOrderId` 로 취소 대상을 식별합니다.  **Rate Limits Group**: `CONDITIONAL_ORDER` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **conditionalOrderId** | **String**| 조건주문 식별자 | [default to null] |

### Return type

null (empty response body)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="createConditionalOrder"></a>
# **createConditionalOrder**
> createConditionalOrder_200_response createConditionalOrder(X-Tossinvest-Account, ConditionalOrderCreateRequest)

조건주문 생성

    특정 종목의 가격을 감시해 조건 충족 시 자동으로 매매(매수/매도)하는 조건주문을 생성합니다.  감시가와 매매 방향(매수/매도)을 설정한 후 가격이 감시가에 도달하면 조건이 발동되어 주문이 생성됩니다.  **발동 세션**: 조건 감시·발동 세션은 시장에 따라 다릅니다. - 국내 주식: KRX 정규장에서만 발동됩니다. - 해외 주식: 장 구분과 상관없이, 거래 가능한 모든 시간대에 발동됩니다.  **타입(`type`)** — 조건의 개수와 관계를 정합니다: - `SINGLE`: `first` 한 조건만 감시합니다. - `OCO` (One-Cancels-the-Other): 두 조건(`first`·`second`)을 동시에 감시하다, 하나의 조건이 충족되면 나머지 조건은 자동 취소됩니다.   `first`/`second` 모두 **매도(SELL)** 이며 `first` 감시가 > 현재가 > `second` 감시가 여야 합니다. 호가유형은 지정가(`LIMIT`)만 지원합니다. - `OTO` (One-Triggers-the-Other): `first` 조건이 체결되면 그때부터 `second` 조건 감시가 시작됩니다.   `first` 는 **매수(BUY)**, `second` 는 **매도(SELL)** 입니다. 호가유형은 지정가(`LIMIT`)만 지원합니다.  **Rate Limits Group**: `CONDITIONAL_ORDER` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **ConditionalOrderCreateRequest** | [**ConditionalOrderCreateRequest**](MODEL_CONDITIONAL_ORDER_CREATE_REQUEST.md)|  | |

### Return type

[**createConditionalOrder_200_response**](MODEL_CREATE_CONDITIONAL_ORDER_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="modifyConditionalOrder"></a>
# **modifyConditionalOrder**
> modifyConditionalOrder_200_response modifyConditionalOrder(X-Tossinvest-Account, conditionalOrderId, ConditionalOrderModifyRequest)

조건주문 수정

    조건주문을 수정합니다. 조건주문 전체를 재설정하므로 본문에 `type`·`expireDate`·`first`(필요 시 `second`) 를 모두 전달합니다. 수량(`quantity`)은 각 감시 조건(`first`/`second`) 안에 입력합니다. (등록과 달리 `expireDate` 가 필수입니다.) 종목은 `conditionalOrderId` 로 식별되므로 본문에 `symbol` 은 필요 없습니다. 본문의 `type` 은 변경 결과 타입이며, 타입 전환(예: SINGLE→OCO)이 허용됩니다. 응답의 `type` 으로 확인하세요.  `conditionalOrderId` 로 수정 대상을 식별합니다.  **주의**: 수정은 기존 조건주문을 취소하고 새 조건주문을 생성하는 방식으로 동작합니다. 따라서 수정 후에는 **새로운 `conditionalOrderId` 가 발급되고 기존 ID 는 무효화**됩니다. 이후 조회·수정·취소에는 반드시 응답으로 반환된 `conditionalOrderId` 를 사용하세요.  **Rate Limits Group**: `CONDITIONAL_ORDER` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **conditionalOrderId** | **String**| 조건주문 식별자 | [default to null] |
| **ConditionalOrderModifyRequest** | [**ConditionalOrderModifyRequest**](MODEL_CONDITIONAL_ORDER_MODIFY_REQUEST.md)|  | |

### Return type

[**modifyConditionalOrder_200_response**](MODEL_MODIFY_CONDITIONAL_ORDER_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## POST /api/v1/conditional-orders

### `/summary`

조건주문 생성

### `/description`

특정 종목의 가격을 감시해 조건 충족 시 자동으로 매매(매수/매도)하는 조건주문을 생성합니다.

감시가와 매매 방향(매수/매도)을 설정한 후 가격이 감시가에 도달하면 조건이 발동되어 주문이 생성됩니다.

**발동 세션**: 조건 감시·발동 세션은 시장에 따라 다릅니다.
- 국내 주식: KRX 정규장에서만 발동됩니다.
- 해외 주식: 장 구분과 상관없이, 거래 가능한 모든 시간대에 발동됩니다.

**타입(`type`)** — 조건의 개수와 관계를 정합니다:
- `SINGLE`: `first` 한 조건만 감시합니다.
- `OCO` (One-Cancels-the-Other): 두 조건(`first`·`second`)을 동시에 감시하다, 하나의 조건이 충족되면 나머지 조건은 자동 취소됩니다.
  `first`/`second` 모두 **매도(SELL)** 이며 `first` 감시가 > 현재가 > `second` 감시가 여야 합니다. 호가유형은 지정가(`LIMIT`)만 지원합니다.
- `OTO` (One-Triggers-the-Other): `first` 조건이 체결되면 그때부터 `second` 조건 감시가 시작됩니다.
  `first` 는 **매수(BUY)**, `second` 는 **매도(SELL)** 입니다. 호가유형은 지정가(`LIMIT`)만 지원합니다.

**Rate Limits Group**: `CONDITIONAL_ORDER`


### `/requestBody/content/application/json/examples/single/summary`

SINGLE 지정가 (LIMIT)

### `/requestBody/content/application/json/examples/singleMarket/summary`

SINGLE 시장가 (MARKET — orderPrice 미입력)

### `/requestBody/content/application/json/examples/oco/summary`

OCO (SELL/SELL, first 감시가 > 현재가 > second 감시가, 지정가만)

### `/requestBody/content/application/json/examples/oto/summary`

OTO (first 매수 → second 매도, 지정가만)

### `/responses/200/description`

성공

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/invalidOrderSide/summary`

매매 유형 오류

### `/responses/400/content/application/json/examples/invalidTriggerPrice/summary`

감시 가격 형식 오류

### `/responses/400/content/application/json/examples/invalidTickSize/summary`

호가 단위 불일치

### `/responses/404/description`

종목 없음

### `/responses/422/description`

비즈니스 규칙 위반

### 전체 연산 정의

````json
{
  "tags": [
    "Conditional Order"
  ],
  "summary": "조건주문 생성",
  "description": "특정 종목의 가격을 감시해 조건 충족 시 자동으로 매매(매수/매도)하는 조건주문을 생성합니다.\n\n감시가와 매매 방향(매수/매도)을 설정한 후 가격이 감시가에 도달하면 조건이 발동되어 주문이 생성됩니다.\n\n**발동 세션**: 조건 감시·발동 세션은 시장에 따라 다릅니다.\n- 국내 주식: KRX 정규장에서만 발동됩니다.\n- 해외 주식: 장 구분과 상관없이, 거래 가능한 모든 시간대에 발동됩니다.\n\n**타입(`type`)** — 조건의 개수와 관계를 정합니다:\n- `SINGLE`: `first` 한 조건만 감시합니다.\n- `OCO` (One-Cancels-the-Other): 두 조건(`first`·`second`)을 동시에 감시하다, 하나의 조건이 충족되면 나머지 조건은 자동 취소됩니다.\n  `first`/`second` 모두 **매도(SELL)** 이며 `first` 감시가 > 현재가 > `second` 감시가 여야 합니다. 호가유형은 지정가(`LIMIT`)만 지원합니다.\n- `OTO` (One-Triggers-the-Other): `first` 조건이 체결되면 그때부터 `second` 조건 감시가 시작됩니다.\n  `first` 는 **매수(BUY)**, `second` 는 **매도(SELL)** 입니다. 호가유형은 지정가(`LIMIT`)만 지원합니다.\n\n**Rate Limits Group**: `CONDITIONAL_ORDER`\n",
  "operationId": "createConditionalOrder",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/AccountSeq"
    }
  ],
  "requestBody": {
    "required": true,
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ConditionalOrderCreateRequest"
        },
        "examples": {
          "single": {
            "summary": "SINGLE 지정가 (LIMIT)",
            "value": {
              "symbol": "005930",
              "type": "SINGLE",
              "quantity": "100",
              "orderType": "LIMIT",
              "clientOrderId": "my-order-001",
              "expireDate": "2026-09-10",
              "first": {
                "orderSide": "SELL",
                "triggerPrice": "295",
                "orderPrice": "295"
              }
            }
          },
          "singleMarket": {
            "summary": "SINGLE 시장가 (MARKET — orderPrice 미입력)",
            "value": {
              "symbol": "005930",
              "type": "SINGLE",
              "quantity": "100",
              "orderType": "MARKET",
              "clientOrderId": "my-order-002",
              "expireDate": "2026-09-10",
              "first": {
                "orderSide": "SELL",
                "triggerPrice": "295"
              }
            }
          },
          "oco": {
            "summary": "OCO (SELL/SELL, first 감시가 > 현재가 > second 감시가, 지정가만)",
            "value": {
              "symbol": "005930",
              "type": "OCO",
              "quantity": "100",
              "orderType": "LIMIT",
              "clientOrderId": "my-order-003",
              "expireDate": "2026-09-10",
              "first": {
                "orderSide": "SELL",
                "triggerPrice": "305",
                "orderPrice": "305"
              },
              "second": {
                "orderSide": "SELL",
                "triggerPrice": "295",
                "orderPrice": "294.5"
              }
            }
          },
          "oto": {
            "summary": "OTO (first 매수 → second 매도, 지정가만)",
            "value": {
              "symbol": "005930",
              "type": "OTO",
              "quantity": "100",
              "orderType": "LIMIT",
              "clientOrderId": "my-order-004",
              "expireDate": "2026-09-10",
              "first": {
                "orderSide": "BUY",
                "triggerPrice": "290",
                "orderPrice": "290"
              },
              "second": {
                "orderSide": "SELL",
                "triggerPrice": "320",
                "orderPrice": "320"
              }
            }
          }
        }
      }
    }
  },
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
                    "$ref": "#/components/schemas/ConditionalOrderCreateResponse"
                  }
                }
              }
            ]
          },
          "example": {
            "result": {
              "conditionalOrderId": "gaZIG-dYMWil8AAXyPmlRg",
              "clientOrderId": "my-order-001"
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
            "invalidOrderSide": {
              "summary": "매매 유형 오류",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "매매 유형이 올바르지 않습니다. (BUY 또는 SELL)",
                  "data": {
                    "field": "first.orderSide"
                  }
                }
              }
            },
            "invalidTriggerPrice": {
              "summary": "감시 가격 형식 오류",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "감시 가격이 유효한 숫자가 아닙니다.",
                  "data": {
                    "field": "first.triggerPrice",
                    "format": "decimal"
                  }
                }
              }
            },
            "invalidTickSize": {
              "summary": "호가 단위 불일치",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "주문 가격이 호가 단위에 맞지 않습니다.",
                  "data": {
                    "field": "first.orderPrice",
                    "tickSize": "50",
                    "nearestPrices": [
                      "24500",
                      "24550"
                    ]
                  }
                }
              }
            }
          }
        }
      }
    },
    "404": {
      "description": "종목 없음",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "stock-not-found",
              "message": "종목을 찾을 수 없습니다."
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

## DELETE /api/v1/conditional-orders/{conditionalOrderId}

### `/summary`

조건주문 취소

### `/description`

조건주문을 취소합니다. `conditionalOrderId` 로 취소 대상을 식별합니다.

**Rate Limits Group**: `CONDITIONAL_ORDER`


### `/parameters/1/description`

조건주문 식별자

### `/responses/204/description`

취소 성공 (No Content)

### `/responses/400/description`

잘못된 요청

### `/responses/404/description`

조건주문 없음

### 전체 연산 정의

````json
{
  "tags": [
    "Conditional Order"
  ],
  "summary": "조건주문 취소",
  "description": "조건주문을 취소합니다. `conditionalOrderId` 로 취소 대상을 식별합니다.\n\n**Rate Limits Group**: `CONDITIONAL_ORDER`\n",
  "operationId": "cancelConditionalOrder",
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
      "description": "조건주문 식별자",
      "schema": {
        "type": "string"
      },
      "example": "gaZIG-dYMWil8AAXyPmlRg"
    }
  ],
  "responses": {
    "204": {
      "description": "취소 성공 (No Content)"
    },
    "400": {
      "description": "잘못된 요청",
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

## POST /api/v1/conditional-orders/{conditionalOrderId}/modify

### `/summary`

조건주문 수정

### `/description`

조건주문을 수정합니다. 조건주문 전체를 재설정하므로 본문에 `type`·`expireDate`·`first`(필요 시 `second`) 를 모두 전달합니다.
수량(`quantity`)은 각 감시 조건(`first`/`second`) 안에 입력합니다.
(등록과 달리 `expireDate` 가 필수입니다.) 종목은 `conditionalOrderId` 로 식별되므로 본문에 `symbol` 은 필요 없습니다.
본문의 `type` 은 변경 결과 타입이며, 타입 전환(예: SINGLE→OCO)이 허용됩니다. 응답의 `type` 으로 확인하세요.

`conditionalOrderId` 로 수정 대상을 식별합니다.

**주의**: 수정은 기존 조건주문을 취소하고 새 조건주문을 생성하는 방식으로 동작합니다.
따라서 수정 후에는 **새로운 `conditionalOrderId` 가 발급되고 기존 ID 는 무효화**됩니다.
이후 조회·수정·취소에는 반드시 응답으로 반환된 `conditionalOrderId` 를 사용하세요.

**Rate Limits Group**: `CONDITIONAL_ORDER`


### `/parameters/1/description`

조건주문 식별자

### `/responses/200/description`

성공

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/invalidTickSize/summary`

호가 단위 불일치

### `/responses/404/description`

조건주문 없음

### `/responses/422/description`

비즈니스 규칙 위반

### 전체 연산 정의

````json
{
  "tags": [
    "Conditional Order"
  ],
  "summary": "조건주문 수정",
  "description": "조건주문을 수정합니다. 조건주문 전체를 재설정하므로 본문에 `type`·`expireDate`·`first`(필요 시 `second`) 를 모두 전달합니다.\n수량(`quantity`)은 각 감시 조건(`first`/`second`) 안에 입력합니다.\n(등록과 달리 `expireDate` 가 필수입니다.) 종목은 `conditionalOrderId` 로 식별되므로 본문에 `symbol` 은 필요 없습니다.\n본문의 `type` 은 변경 결과 타입이며, 타입 전환(예: SINGLE→OCO)이 허용됩니다. 응답의 `type` 으로 확인하세요.\n\n`conditionalOrderId` 로 수정 대상을 식별합니다.\n\n**주의**: 수정은 기존 조건주문을 취소하고 새 조건주문을 생성하는 방식으로 동작합니다.\n따라서 수정 후에는 **새로운 `conditionalOrderId` 가 발급되고 기존 ID 는 무효화**됩니다.\n이후 조회·수정·취소에는 반드시 응답으로 반환된 `conditionalOrderId` 를 사용하세요.\n\n**Rate Limits Group**: `CONDITIONAL_ORDER`\n",
  "operationId": "modifyConditionalOrder",
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
      "description": "조건주문 식별자",
      "schema": {
        "type": "string"
      },
      "example": "gaZIG-dYMWil8AAXyPmlRg"
    }
  ],
  "requestBody": {
    "required": true,
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/ConditionalOrderModifyRequest"
        },
        "example": {
          "type": "OCO",
          "quantity": "100",
          "orderType": "LIMIT",
          "expireDate": "2026-09-10",
          "first": {
            "orderSide": "SELL",
            "triggerPrice": "310",
            "orderPrice": "310"
          },
          "second": {
            "orderSide": "SELL",
            "triggerPrice": "290",
            "orderPrice": "290"
          }
        }
      }
    }
  },
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
                    "$ref": "#/components/schemas/ConditionalOrderResponse"
                  }
                }
              }
            ]
          },
          "example": {
            "result": {
              "conditionalOrderId": "2lEct1uiAwlDtVA5KmgNcA"
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
            "invalidTickSize": {
              "summary": "호가 단위 불일치",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "주문 가격이 호가 단위에 맞지 않습니다.",
                  "data": {
                    "field": "first.orderPrice",
                    "tickSize": "50",
                    "nearestPrices": [
                      "24500",
                      "24550"
                    ]
                  }
                }
              }
            }
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
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "conditional-order-not-found",
              "message": "조건주문을 찾을 수 없습니다."
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
