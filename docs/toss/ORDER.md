> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/OrderApi.md
> 문서 버전: 1.2.17

# OrderApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelOrder**](ORDER.md#cancelOrder) | **POST** /api/v1/orders/{orderId}/cancel | 주문 취소 |
| [**createOrder**](ORDER.md#createOrder) | **POST** /api/v1/orders | 주문 생성 |
| [**modifyOrder**](ORDER.md#modifyOrder) | **POST** /api/v1/orders/{orderId}/modify | 주문 정정 |


<a name="cancelOrder"></a>
# **cancelOrder**
> modifyOrder_200_response cancelOrder(X-Tossinvest-Account, orderId, body)

주문 취소

    기존 주문을 취소합니다. 이미 체결된 주문은 취소할 수 없습니다.  **Rate Limits Group**: `ORDER` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **orderId** | **String**| 주문 식별자. 서버에서 발급한 opaque token 입니다.  | [default to null] |
| **body** | **Object**|  | [optional] |

### Return type

[**modifyOrder_200_response**](MODEL_MODIFY_ORDER_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="createOrder"></a>
# **createOrder**
> createOrder_200_response createOrder(X-Tossinvest-Account, OrderCreateRequest)

주문 생성

    매수 또는 매도 주문을 생성합니다.  **수량 지정 방식** — `quantity`, `orderAmount` 중 정확히 하나를 사용: - `quantity`: 주문 수량 (주 단위). 지정한 수량만큼 주문. 소수점 수량은 미국 주식 시장가 매도(`MARKET`+`SELL`)에만 허용 (그 외는 정수만) - `orderAmount`: 주문 금액 (달러). 지정한 금액만큼 주문하며, 체결 수량은 시장가에 따라 결정. US MARKET 전용  **소수점 거래 접수 시간**: 금액 주문 (`orderAmount`) 과 소수점 수량 주문은 정규장 시작부터 **정규장 종료 1시간 전**까지만 접수할 수 있습니다. 그 외 시간에 호출 시 각각 `422 amount-order-outside-regular-hours` / `422 fractional-quantity-outside-regular-hours` 를 반환합니다.  **Rate Limits Group**: `ORDER` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **OrderCreateRequest** | [**OrderCreateRequest**](MODEL_ORDER_CREATE_REQUEST.md)|  | |

### Return type

[**createOrder_200_response**](MODEL_CREATE_ORDER_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="modifyOrder"></a>
# **modifyOrder**
> modifyOrder_200_response modifyOrder(X-Tossinvest-Account, orderId, OrderModifyRequest)

주문 정정

    기존 주문의 가격 또는 수량을 정정합니다.  **KR 주식:** `quantity` 필수. 양의 정수만 허용합니다.  **US 주식:** `quantity` 제공 불가. 가격 변경만 지원합니다. `quantity` 제공 시 `400 us-modify-quantity-not-supported` 에러를 반환합니다.  **Rate Limits Group**: `ORDER` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **orderId** | **String**| 주문 식별자. 서버에서 발급한 opaque token 입니다.  | [default to null] |
| **OrderModifyRequest** | [**OrderModifyRequest**](MODEL_ORDER_MODIFY_REQUEST.md)|  | |

### Return type

[**modifyOrder_200_response**](MODEL_MODIFY_ORDER_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## POST /api/v1/orders

### `/summary`

주문 생성

### `/description`

매수 또는 매도 주문을 생성합니다.

**수량 지정 방식** — `quantity`, `orderAmount` 중 정확히 하나를 사용:
- `quantity`: 주문 수량 (주 단위). 지정한 수량만큼 주문. 소수점 수량은 미국 주식 시장가 매도(`MARKET`+`SELL`)에만 허용 (그 외는 정수만)
- `orderAmount`: 주문 금액 (달러). 지정한 금액만큼 주문하며, 체결 수량은 시장가에 따라 결정. US MARKET 전용

**소수점 거래 접수 시간**: 금액 주문 (`orderAmount`) 과 소수점 수량 주문은 정규장 시작부터 **정규장 종료 1시간 전**까지만 접수할 수 있습니다.
그 외 시간에 호출 시 각각 `422 amount-order-outside-regular-hours` / `422 fractional-quantity-outside-regular-hours` 를 반환합니다.

**Rate Limits Group**: `ORDER`


### `/requestBody/content/application/json/examples/krLimitBuy/summary`

국내주식 지정가 매수

### `/requestBody/content/application/json/examples/usMarketBuyAmount/summary`

해외주식 소수점 시장가 매수 (금액)

### `/requestBody/content/application/json/examples/usMarketSellFractionalQuantity/summary`

해외주식 소수점 시장가 매도 (수량)

### `/requestBody/content/application/json/examples/usLocBuy/summary`

해외주식 종가 지정가 매수 (LOC = LIMIT + CLS)

### `/responses/200/description`

성공

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/invalidOrderType/summary`

지원하지 않는 호가 유형

### `/responses/400/content/application/json/examples/invalidTimeInForce/summary`

지원하지 않는 유효 조건

### `/responses/400/content/application/json/examples/clsConditionNotMet/summary`

종가(CLS) 주문 조건 불충족

### `/responses/400/content/application/json/examples/invalidSide/summary`

잘못된 주문 방향

### `/responses/400/content/application/json/examples/quantityOrAmountRequired/summary`

수량 또는 금액 미지정

### `/responses/400/content/application/json/examples/limitPriceRequired/summary`

지정가 주문 가격 미지정

### `/responses/400/content/application/json/examples/invalidTickSize/summary`

호가 단위 불일치

### `/responses/400/content/application/json/examples/confirmHighValueRequired/summary`

1억원 이상 주문 확인 필요

### `/responses/400/content/application/json/examples/amountUsMarketOnly/summary`

금액 주문 조건 불충족

### `/responses/400/content/application/json/examples/invalidQuantityFormat/summary`

주문 수량 형식 오류

### `/responses/400/content/application/json/examples/fractionalQuantityUsSellOnly/summary`

소수점 수량은 US 시장가 매도에만 허용

### `/responses/400/content/application/json/examples/fractionalQuantityScaleExceeded/summary`

소수점 수량 6자리 초과

### `/responses/400/content/application/json/examples/accountHeaderRequired/summary`

X-Tossinvest-Account 헤더 누락

### `/responses/409/description`

중복 요청

### `/responses/409/content/application/json/examples/requestInProgress/summary`

동일 주문 키에 대해 처리 중인 요청 있음

### `/responses/409/content/application/json/examples/oppositePendingOrderExists/summary`

반대 방향 미체결 주문 존재

### `/responses/422/description`

비즈니스 규칙 위반

### `/responses/422/content/application/json/examples/insufficientBuyingPower/summary`

주문 가능 금액 부족

### `/responses/422/content/application/json/examples/outsideOrderHours/summary`

주문 접수 불가 시간

### `/responses/422/content/application/json/examples/stockRestricted/summary`

종목 주문 제한

### `/responses/422/content/application/json/examples/priceOutOfRange/summary`

주문 가격 허용 범위 초과

### `/responses/422/content/application/json/examples/orderTypeNotAllowed/summary`

현재 사용 불가 호가 유형

### `/responses/422/content/application/json/examples/prerequisiteRequired/summary`

사전 자격 요건 미충족 (약관 동의/교육 이수/위험고지 등록)

### `/responses/422/content/application/json/examples/marketNotSupportedForStock/summary`

종목-마켓 조합 거래 불가 (KR)

### `/responses/422/content/application/json/examples/investorExchangeNotIntegrated/summary`

투자자지시 거래소가 통합(SOR)이 아님 (KR)

### `/responses/422/content/application/json/examples/amountOrderOutsideRegularHours/summary`

접수 시간(정규장 종료 1시간 전 마감) 외 금액 주문 불가

### `/responses/422/content/application/json/examples/fractionalQuantityOutsideRegularHours/summary`

접수 시간(정규장 종료 1시간 전 마감) 외 소수점 수량 주문 불가

### `/responses/422/content/application/json/examples/accountRestricted/summary`

계좌 거래 제한 (사고 계좌, 거래 정지 등)

### `/responses/422/content/application/json/examples/maxOrderAmountExceeded/summary`

30억원 초과 주문 (KR)

### `/responses/422/content/application/json/examples/idempotencyKeyConflict/summary`

동일 clientOrderId 로 이전과 다른 본문 재요청 (멱등성 키 충돌)

### `/responses/500/description`

주문 처리 중 일시적 오류 또는 시스템 점검

### `/responses/500/content/application/json/examples/internalError/summary`

주문 처리 중 일시적 오류

### `/responses/500/content/application/json/examples/maintenance/summary`

점검 중

### 전체 연산 정의

````json
{
  "tags": [
    "Order"
  ],
  "summary": "주문 생성",
  "description": "매수 또는 매도 주문을 생성합니다.\n\n**수량 지정 방식** — `quantity`, `orderAmount` 중 정확히 하나를 사용:\n- `quantity`: 주문 수량 (주 단위). 지정한 수량만큼 주문. 소수점 수량은 미국 주식 시장가 매도(`MARKET`+`SELL`)에만 허용 (그 외는 정수만)\n- `orderAmount`: 주문 금액 (달러). 지정한 금액만큼 주문하며, 체결 수량은 시장가에 따라 결정. US MARKET 전용\n\n**소수점 거래 접수 시간**: 금액 주문 (`orderAmount`) 과 소수점 수량 주문은 정규장 시작부터 **정규장 종료 1시간 전**까지만 접수할 수 있습니다.\n그 외 시간에 호출 시 각각 `422 amount-order-outside-regular-hours` / `422 fractional-quantity-outside-regular-hours` 를 반환합니다.\n\n**Rate Limits Group**: `ORDER`\n",
  "operationId": "createOrder",
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
          "$ref": "#/components/schemas/OrderCreateRequest"
        },
        "examples": {
          "krLimitBuy": {
            "summary": "국내주식 지정가 매수",
            "value": {
              "clientOrderId": "my-order-001",
              "symbol": "005930",
              "side": "BUY",
              "orderType": "LIMIT",
              "quantity": "10",
              "price": "70000"
            }
          },
          "usMarketBuyAmount": {
            "summary": "해외주식 소수점 시장가 매수 (금액)",
            "value": {
              "symbol": "AAPL",
              "side": "BUY",
              "orderType": "MARKET",
              "orderAmount": "100.5"
            }
          },
          "usMarketSellFractionalQuantity": {
            "summary": "해외주식 소수점 시장가 매도 (수량)",
            "value": {
              "symbol": "AAPL",
              "side": "SELL",
              "orderType": "MARKET",
              "quantity": "0.5"
            }
          },
          "usLocBuy": {
            "summary": "해외주식 종가 지정가 매수 (LOC = LIMIT + CLS)",
            "value": {
              "symbol": "AAPL",
              "side": "BUY",
              "orderType": "LIMIT",
              "timeInForce": "CLS",
              "quantity": "10",
              "price": "185.5"
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
                    "$ref": "#/components/schemas/OrderResponse"
                  }
                }
              }
            ]
          },
          "example": {
            "result": {
              "orderId": "0d5QIHjmtksbsmM-hBRAgP-ExI8iodGm9fAR5txelPfnMM8XQ_swoJdwL5RpGWMo",
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
            "invalidOrderType": {
              "summary": "지원하지 않는 호가 유형",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "호가 유형이 올바르지 않습니다.",
                  "data": {
                    "field": "orderType",
                    "allowedValues": [
                      "LIMIT",
                      "MARKET"
                    ]
                  }
                }
              }
            },
            "invalidTimeInForce": {
              "summary": "지원하지 않는 유효 조건",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "주문 유효 조건이 올바르지 않습니다.",
                  "data": {
                    "field": "timeInForce",
                    "allowedValues": [
                      "DAY",
                      "CLS"
                    ]
                  }
                }
              }
            },
            "clsConditionNotMet": {
              "summary": "종가(CLS) 주문 조건 불충족",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "종가 주문(CLS)은 미국 주식 지정가 주문에만 사용할 수 있습니다.",
                  "data": {
                    "field": "timeInForce",
                    "allowedConditions": {
                      "marketCountry": "US",
                      "orderType": "LIMIT"
                    }
                  }
                }
              }
            },
            "invalidSide": {
              "summary": "잘못된 주문 방향",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "주문 방향이 올바르지 않습니다.",
                  "data": {
                    "field": "side",
                    "allowedValues": [
                      "BUY",
                      "SELL"
                    ]
                  }
                }
              }
            },
            "quantityOrAmountRequired": {
              "summary": "수량 또는 금액 미지정",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "주문 수량 또는 금액 중 하나를 지정해야 합니다.",
                  "data": {
                    "field": "quantity,orderAmount"
                  }
                }
              }
            },
            "limitPriceRequired": {
              "summary": "지정가 주문 가격 미지정",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "지정가 주문 시 가격을 지정해야 합니다.",
                  "data": {
                    "field": "price"
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
                    "field": "price",
                    "tickSize": "100",
                    "nearestPrices": [
                      "50100",
                      "50200"
                    ]
                  }
                }
              }
            },
            "confirmHighValueRequired": {
              "summary": "1억원 이상 주문 확인 필요",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "confirm-high-value-required",
                  "message": "1억원 이상 주문은 확인이 필요합니다.",
                  "data": {
                    "field": "confirmHighValueOrder",
                    "limits": {
                      "threshold": "100000000",
                      "currency": "KRW"
                    }
                  }
                }
              }
            },
            "amountUsMarketOnly": {
              "summary": "금액 주문 조건 불충족",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "금액 주문은 미국 주식 시장가 주문에만 사용할 수 있습니다.",
                  "data": {
                    "field": "orderAmount",
                    "allowedConditions": {
                      "marketCountry": "US",
                      "orderType": "MARKET"
                    }
                  }
                }
              }
            },
            "invalidQuantityFormat": {
              "summary": "주문 수량 형식 오류",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "주문 수량이 유효한 숫자가 아닙니다.",
                  "data": {
                    "field": "quantity",
                    "format": "decimal",
                    "pattern": "^-?\\d+(\\.\\d+)?$",
                    "maxLength": 30
                  }
                }
              }
            },
            "fractionalQuantityUsSellOnly": {
              "summary": "소수점 수량은 US 시장가 매도에만 허용",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "소수점 수량 주문은 미국 주식 시장가 매도 주문에만 사용할 수 있습니다. 소수점 매수는 orderAmount(금액) 주문을 사용해 주세요.",
                  "data": {
                    "field": "quantity",
                    "allowedConditions": {
                      "marketCountry": "US",
                      "orderType": "MARKET",
                      "side": "SELL"
                    }
                  }
                }
              }
            },
            "fractionalQuantityScaleExceeded": {
              "summary": "소수점 수량 6자리 초과",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "소수점 수량은 소수점 6자리까지 지원합니다.",
                  "data": {
                    "field": "quantity",
                    "constraint": {
                      "maxScale": 6
                    }
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
    "409": {
      "description": "중복 요청",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "requestInProgress": {
              "summary": "동일 주문 키에 대해 처리 중인 요청 있음",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "request-in-progress",
                  "message": "동일 주문 키에 대해 처리 중인 요청이 있습니다. 잠시 후 다시 시도해 주세요."
                }
              }
            },
            "oppositePendingOrderExists": {
              "summary": "반대 방향 미체결 주문 존재",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "opposite-pending-order-exists",
                  "message": "동일 종목에 반대 방향의 체결 대기 주문이 있습니다."
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
          },
          "examples": {
            "insufficientBuyingPower": {
              "summary": "주문 가능 금액 부족",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "insufficient-buying-power",
                  "message": "주문 가능 금액이 부족합니다."
                }
              }
            },
            "outsideOrderHours": {
              "summary": "주문 접수 불가 시간",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "order-hours-closed",
                  "message": "현재 해당 주문을 접수할 수 없는 시간입니다.",
                  "data": {
                    "retryAfterAt": "2026-01-02T09:00:00+09:00"
                  }
                }
              }
            },
            "stockRestricted": {
              "summary": "종목 주문 제한",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "stock-restricted",
                  "message": "해당 종목은 현재 주문이 제한되어 있습니다."
                }
              }
            },
            "priceOutOfRange": {
              "summary": "주문 가격 허용 범위 초과",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "price-out-of-range",
                  "message": "주문 가격이 허용 범위를 벗어났습니다."
                }
              }
            },
            "orderTypeNotAllowed": {
              "summary": "현재 사용 불가 호가 유형",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "order-type-not-allowed",
                  "message": "현재 사용할 수 없는 호가 유형입니다."
                }
              }
            },
            "prerequisiteRequired": {
              "summary": "사전 자격 요건 미충족 (약관 동의/교육 이수/위험고지 등록)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "prerequisite-required",
                  "message": "주문 전 필요한 사전 자격 요건이 충족되지 않았습니다."
                }
              }
            },
            "marketNotSupportedForStock": {
              "summary": "종목-마켓 조합 거래 불가 (KR)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "market-not-supported-for-stock",
                  "message": "해당 종목은 이 시장에서 거래할 수 없습니다."
                }
              }
            },
            "investorExchangeNotIntegrated": {
              "summary": "투자자지시 거래소가 통합(SOR)이 아님 (KR)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "investor-exchange-not-integrated",
                  "message": "투자자지시 거래소가 통합(SOR) 으로 설정되어 있어야 주문할 수 있습니다."
                }
              }
            },
            "amountOrderOutsideRegularHours": {
              "summary": "접수 시간(정규장 종료 1시간 전 마감) 외 금액 주문 불가",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "amount-order-outside-regular-hours",
                  "message": "미국 주식 금액 주문은 정규장 종료 1시간 전까지만 접수할 수 있습니다.",
                  "data": {
                    "field": "orderAmount",
                    "regularHours": {
                      "start": "2026-03-30T09:30:00-04:00",
                      "end": "2026-03-30T16:00:00-04:00"
                    },
                    "orderableHours": {
                      "start": "2026-03-30T09:30:00-04:00",
                      "end": "2026-03-30T15:00:00-04:00"
                    }
                  }
                }
              }
            },
            "fractionalQuantityOutsideRegularHours": {
              "summary": "접수 시간(정규장 종료 1시간 전 마감) 외 소수점 수량 주문 불가",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "fractional-quantity-outside-regular-hours",
                  "message": "미국 주식 소수점 수량 주문은 정규장 종료 1시간 전까지만 접수할 수 있습니다.",
                  "data": {
                    "field": "quantity",
                    "regularHours": {
                      "start": "2026-03-30T09:30:00-04:00",
                      "end": "2026-03-30T16:00:00-04:00"
                    },
                    "orderableHours": {
                      "start": "2026-03-30T09:30:00-04:00",
                      "end": "2026-03-30T15:00:00-04:00"
                    }
                  }
                }
              }
            },
            "accountRestricted": {
              "summary": "계좌 거래 제한 (사고 계좌, 거래 정지 등)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "account-restricted",
                  "message": "계좌 상태가 주문을 허용하지 않습니다."
                }
              }
            },
            "maxOrderAmountExceeded": {
              "summary": "30억원 초과 주문 (KR)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "max-order-amount-exceeded",
                  "message": "최대 주문가능금액을 초과하였습니다.",
                  "data": {
                    "limits": {
                      "maxAmount": "3000000000",
                      "currency": "KRW"
                    }
                  }
                }
              }
            },
            "idempotencyKeyConflict": {
              "summary": "동일 clientOrderId 로 이전과 다른 본문 재요청 (멱등성 키 충돌)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "idempotency-key-conflict",
                  "message": "동일한 clientOrderId 로 다른 내용의 주문을 요청할 수 없습니다."
                }
              }
            }
          }
        }
      }
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "description": "주문 처리 중 일시적 오류 또는 시스템 점검",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "internalError": {
              "summary": "주문 처리 중 일시적 오류",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "internal-error",
                  "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
                }
              }
            },
            "maintenance": {
              "summary": "점검 중",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "maintenance",
                  "message": "점검 중입니다. 잠시 후 다시 시도해 주세요.",
                  "data": {
                    "retryAfterSeconds": 600
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
````

## POST /api/v1/orders/{orderId}/modify

### `/summary`

주문 정정

### `/description`

기존 주문의 가격 또는 수량을 정정합니다.

**KR 주식:** `quantity` 필수. 양의 정수만 허용합니다.

**US 주식:** `quantity` 제공 불가. 가격 변경만 지원합니다. `quantity` 제공 시 `400 us-modify-quantity-not-supported` 에러를 반환합니다.

**Rate Limits Group**: `ORDER`


### `/requestBody/content/application/json/examples/krModify/summary`

국내주식 가격+수량 정정

### `/requestBody/content/application/json/examples/usModify/summary`

해외주식 가격 정정

### `/responses/200/description`

성공

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/invalidPrice/summary`

지정가 주문 가격 미지정

### `/responses/400/content/application/json/examples/invalidQuantityKr/summary`

국내주식 주문 수량 오류

### `/responses/400/content/application/json/examples/invalidTickSize/summary`

호가 단위 불일치

### `/responses/400/content/application/json/examples/invalidParameter/summary`

주문 파라미터 오류

### `/responses/400/content/application/json/examples/usModifyQuantityNotSupported/summary`

미국 주식 주문 정정은 가격만 지원

### `/responses/400/content/application/json/examples/confirmHighValueRequired/summary`

정정 후 1억원 이상 주문 확인 필요

### `/responses/400/content/application/json/examples/accountHeaderRequired/summary`

X-Tossinvest-Account 헤더 누락

### `/responses/404/description`

주문 또는 계좌 없음

### `/responses/404/content/application/json/examples/orderNotFound/summary`

주문을 찾을 수 없음

### `/responses/404/content/application/json/examples/accountNotFound/summary`

계좌 부재

### `/responses/409/description`

정정 불가 상태

### `/responses/409/content/application/json/examples/alreadyFilled/summary`

이미 체결된 주문

### `/responses/409/content/application/json/examples/alreadyCanceled/summary`

이미 취소된 주문

### `/responses/409/content/application/json/examples/alreadyModified/summary`

이미 정정된 주문

### `/responses/409/content/application/json/examples/rejectedOrder/summary`

거부된 주문 정정 시도

### `/responses/409/content/application/json/examples/alreadyProcessing/summary`

주문 처리 중

### `/responses/422/description`

비즈니스 규칙 위반

### `/responses/422/content/application/json/examples/modifyRestricted/summary`

정정 불가 주문

### `/responses/422/content/application/json/examples/outsideOrderHours/summary`

주문 접수 불가 시간

### `/responses/422/content/application/json/examples/investorExchangeNotIntegrated/summary`

투자자지시 거래소가 통합(SOR)이 아님 (KR)

### `/responses/422/content/application/json/examples/prerequisiteRequired/summary`

사전 자격 요건 미충족 (약관 동의/교육 이수/위험고지 등록)

### `/responses/422/content/application/json/examples/accountRestricted/summary`

계좌 정정 제한 (사고 계좌 등)

### `/responses/422/content/application/json/examples/maxOrderAmountExceeded/summary`

30억원 초과 정정 (KR)

### 전체 연산 정의

````json
{
  "tags": [
    "Order"
  ],
  "summary": "주문 정정",
  "description": "기존 주문의 가격 또는 수량을 정정합니다.\n\n**KR 주식:** `quantity` 필수. 양의 정수만 허용합니다.\n\n**US 주식:** `quantity` 제공 불가. 가격 변경만 지원합니다. `quantity` 제공 시 `400 us-modify-quantity-not-supported` 에러를 반환합니다.\n\n**Rate Limits Group**: `ORDER`\n",
  "operationId": "modifyOrder",
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
  "requestBody": {
    "required": true,
    "content": {
      "application/json": {
        "schema": {
          "$ref": "#/components/schemas/OrderModifyRequest"
        },
        "examples": {
          "krModify": {
            "summary": "국내주식 가격+수량 정정",
            "value": {
              "orderType": "LIMIT",
              "quantity": "15",
              "price": "71000"
            }
          },
          "usModify": {
            "summary": "해외주식 가격 정정",
            "value": {
              "orderType": "LIMIT",
              "price": "185.5"
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
                    "$ref": "#/components/schemas/OrderOperationResponse"
                  }
                }
              }
            ]
          },
          "example": {
            "result": {
              "orderId": "5nfzdqmzfnAw3LFXWHPRy0UNi7y_WZlphJh5hRIsi25-NIfm_GtQgXima5QD2hUz"
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
            "invalidPrice": {
              "summary": "지정가 주문 가격 미지정",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "지정가 주문에는 가격이 필요합니다.",
                  "data": {
                    "field": "price"
                  }
                }
              }
            },
            "invalidQuantityKr": {
              "summary": "국내주식 주문 수량 오류",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "주문 수량이 유효하지 않습니다.",
                  "data": {
                    "field": "quantity",
                    "constraint": {
                      "min": 1,
                      "integerOnly": true
                    }
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
                    "field": "price",
                    "tickSize": "100",
                    "nearestPrices": [
                      "50100",
                      "50200"
                    ]
                  }
                }
              }
            },
            "invalidParameter": {
              "summary": "주문 파라미터 오류",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다."
                }
              }
            },
            "usModifyQuantityNotSupported": {
              "summary": "미국 주식 주문 정정은 가격만 지원",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "us-modify-quantity-not-supported",
                  "message": "미국 주식 주문 정정은 가격만 지원합니다.",
                  "data": {
                    "field": "quantity"
                  }
                }
              }
            },
            "confirmHighValueRequired": {
              "summary": "정정 후 1억원 이상 주문 확인 필요",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "confirm-high-value-required",
                  "message": "1억원 이상 주문은 확인이 필요합니다.",
                  "data": {
                    "field": "confirmHighValueOrder",
                    "limits": {
                      "threshold": "100000000",
                      "currency": "KRW"
                    }
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
      "description": "주문 또는 계좌 없음",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "orderNotFound": {
              "summary": "주문을 찾을 수 없음",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "order-not-found",
                  "message": "주문을 찾을 수 없습니다."
                }
              }
            },
            "accountNotFound": {
              "summary": "계좌 부재",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "account-not-found",
                  "message": "계좌를 찾을 수 없습니다."
                }
              }
            }
          }
        }
      }
    },
    "409": {
      "description": "정정 불가 상태",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "alreadyFilled": {
              "summary": "이미 체결된 주문",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "already-filled",
                  "message": "이미 체결된 주문입니다."
                }
              }
            },
            "alreadyCanceled": {
              "summary": "이미 취소된 주문",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "already-canceled",
                  "message": "이미 취소된 주문입니다."
                }
              }
            },
            "alreadyModified": {
              "summary": "이미 정정된 주문",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "already-modified",
                  "message": "이미 정정된 주문입니다."
                }
              }
            },
            "rejectedOrder": {
              "summary": "거부된 주문 정정 시도",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "already-rejected",
                  "message": "거부된 주문은 정정/취소할 수 없습니다."
                }
              }
            },
            "alreadyProcessing": {
              "summary": "주문 처리 중",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "already-processing",
                  "message": "주문이 처리 중입니다. 잠시 후 다시 시도해 주세요.",
                  "data": {
                    "retryAfterSeconds": 1
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
          },
          "examples": {
            "modifyRestricted": {
              "summary": "정정 불가 주문",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "modify-restricted",
                  "message": "해당 주문은 정정할 수 없습니다."
                }
              }
            },
            "outsideOrderHours": {
              "summary": "주문 접수 불가 시간",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "order-hours-closed",
                  "message": "현재 해당 주문을 접수할 수 없는 시간입니다.",
                  "data": {
                    "retryAfterAt": "2026-01-02T09:00:00+09:00"
                  }
                }
              }
            },
            "investorExchangeNotIntegrated": {
              "summary": "투자자지시 거래소가 통합(SOR)이 아님 (KR)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "investor-exchange-not-integrated",
                  "message": "투자자지시 거래소가 통합(SOR) 으로 설정되어 있어야 주문할 수 있습니다."
                }
              }
            },
            "prerequisiteRequired": {
              "summary": "사전 자격 요건 미충족 (약관 동의/교육 이수/위험고지 등록)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "prerequisite-required",
                  "message": "주문 전 필요한 사전 자격 요건이 충족되지 않았습니다."
                }
              }
            },
            "accountRestricted": {
              "summary": "계좌 정정 제한 (사고 계좌 등)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "account-restricted",
                  "message": "계좌 상태가 주문을 허용하지 않습니다."
                }
              }
            },
            "maxOrderAmountExceeded": {
              "summary": "30억원 초과 정정 (KR)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "max-order-amount-exceeded",
                  "message": "최대 주문가능금액을 초과하였습니다.",
                  "data": {
                    "limits": {
                      "maxAmount": "3000000000",
                      "currency": "KRW"
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorOrder"
    }
  }
}
````

## POST /api/v1/orders/{orderId}/cancel

### `/summary`

주문 취소

### `/description`

기존 주문을 취소합니다. 이미 체결된 주문은 취소할 수 없습니다.

**Rate Limits Group**: `ORDER`


### `/responses/200/description`

성공

### `/responses/409/description`

취소 불가 상태

### `/responses/409/content/application/json/examples/alreadyFilled/summary`

이미 체결된 주문

### `/responses/409/content/application/json/examples/alreadyCanceled/summary`

이미 취소된 주문

### `/responses/409/content/application/json/examples/alreadyModified/summary`

이미 정정된 주문

### `/responses/409/content/application/json/examples/rejectedOrder/summary`

거부된 주문 취소 시도

### `/responses/409/content/application/json/examples/alreadyProcessing/summary`

주문 처리 중

### `/responses/422/description`

비즈니스 규칙 위반

### `/responses/422/content/application/json/examples/cancelRestricted/summary`

취소 불가 주문

### `/responses/422/content/application/json/examples/outsideOrderHours/summary`

취소 접수 불가 시간

### 전체 연산 정의

````json
{
  "tags": [
    "Order"
  ],
  "summary": "주문 취소",
  "description": "기존 주문을 취소합니다. 이미 체결된 주문은 취소할 수 없습니다.\n\n**Rate Limits Group**: `ORDER`\n",
  "operationId": "cancelOrder",
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
  "requestBody": {
    "required": false,
    "content": {
      "application/json": {
        "schema": {
          "type": "object"
        },
        "example": {}
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
                    "$ref": "#/components/schemas/OrderOperationResponse"
                  }
                }
              }
            ]
          },
          "example": {
            "result": {
              "orderId": "Kx9mTqR2vLwE7oPn3YhBjCf1dAsU6gZi8rNk4bWcXeJtMlSyDuQaHp5oVzI0FvRw"
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
    "409": {
      "description": "취소 불가 상태",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "alreadyFilled": {
              "summary": "이미 체결된 주문",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "already-filled",
                  "message": "이미 체결된 주문입니다."
                }
              }
            },
            "alreadyCanceled": {
              "summary": "이미 취소된 주문",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "already-canceled",
                  "message": "이미 취소된 주문입니다."
                }
              }
            },
            "alreadyModified": {
              "summary": "이미 정정된 주문",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "already-modified",
                  "message": "이미 정정된 주문입니다."
                }
              }
            },
            "rejectedOrder": {
              "summary": "거부된 주문 취소 시도",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "already-rejected",
                  "message": "거부된 주문은 정정/취소할 수 없습니다."
                }
              }
            },
            "alreadyProcessing": {
              "summary": "주문 처리 중",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "already-processing",
                  "message": "주문이 처리 중입니다. 잠시 후 다시 시도해 주세요.",
                  "data": {
                    "retryAfterSeconds": 1
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
          },
          "examples": {
            "cancelRestricted": {
              "summary": "취소 불가 주문",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "cancel-restricted",
                  "message": "해당 주문은 취소할 수 없습니다."
                }
              }
            },
            "outsideOrderHours": {
              "summary": "취소 접수 불가 시간",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "order-hours-closed",
                  "message": "현재 해당 주문을 접수할 수 없는 시간입니다."
                }
              }
            }
          }
        }
      }
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorOrder"
    }
  }
}
````
