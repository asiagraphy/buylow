> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/OrderInfoApi.md
> 문서 버전: 1.2.17

# OrderInfoApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBuyingPower**](ORDER_INFO.md#getBuyingPower) | **GET** /api/v1/buying-power | 매수 가능 금액 조회 |
| [**getCommissions**](ORDER_INFO.md#getCommissions) | **GET** /api/v1/commissions | 매매 수수료 조회 |
| [**getSellableQuantity**](ORDER_INFO.md#getSellableQuantity) | **GET** /api/v1/sellable-quantity | 판매 가능 수량 조회 |


<a name="getBuyingPower"></a>
# **getBuyingPower**
> getBuyingPower_200_response getBuyingPower(X-Tossinvest-Account, currency)

매수 가능 금액 조회

    매수 주문 시 사용할 수 있는 매수 가능 금액을 조회합니다. 미수거래를 제외한 현금 기반 매수 가능 금액(미수 미발생 기준)을 반환합니다.  **Rate Limits Group**: `ORDER_INFO` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **currency** | [**Currency**](MODEL_CURRENCY.md)| 통화 코드 | [default to null] [enum: KRW, USD] |

### Return type

[**getBuyingPower_200_response**](MODEL_GET_BUYING_POWER_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getCommissions"></a>
# **getCommissions**
> getCommissions_200_response getCommissions(X-Tossinvest-Account)

매매 수수료 조회

    현재 계좌의 시장별 매매 수수료율을 조회합니다. 국내주식과 해외주식의 수수료 정보를 배열로 반환합니다.  **Rate Limits Group**: `ORDER_INFO` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |

### Return type

[**getCommissions_200_response**](MODEL_GET_COMMISSIONS_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getSellableQuantity"></a>
# **getSellableQuantity**
> getSellableQuantity_200_response getSellableQuantity(X-Tossinvest-Account, symbol)

판매 가능 수량 조회

    특정 종목의 판매 가능 수량을 조회합니다.  **Rate Limits Group**: `ORDER_INFO` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **symbol** | **String**| 종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL). 영문 대/소문자, 숫자, '.', '-' 만 허용한다. | [default to null] |

### Return type

[**getSellableQuantity_200_response**](MODEL_GET_SELLABLE_QUANTITY_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## GET /api/v1/buying-power

### `/summary`

매수 가능 금액 조회

### `/description`

매수 주문 시 사용할 수 있는 매수 가능 금액을 조회합니다.
미수거래를 제외한 현금 기반 매수 가능 금액(미수 미발생 기준)을 반환합니다.

**Rate Limits Group**: `ORDER_INFO`


### `/parameters/1/description`

통화 코드

### `/parameters/1/examples/krw/summary`

원화

### `/parameters/1/examples/usd/summary`

달러

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/krw/summary`

원화 응답

### `/responses/200/content/application/json/examples/usd/summary`

달러 응답

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedCurrency/summary`

지원하지 않는 통화

### `/responses/400/content/application/json/examples/accountHeaderRequired/summary`

X-Tossinvest-Account 헤더 누락

### `/responses/404/description`

계좌 없음

### `/responses/404/content/application/json/examples/accountNotFound/summary`

계좌 부재

### 전체 연산 정의

````json
{
  "tags": [
    "Order Info"
  ],
  "summary": "매수 가능 금액 조회",
  "description": "매수 주문 시 사용할 수 있는 매수 가능 금액을 조회합니다.\n미수거래를 제외한 현금 기반 매수 가능 금액(미수 미발생 기준)을 반환합니다.\n\n**Rate Limits Group**: `ORDER_INFO`\n",
  "operationId": "getBuyingPower",
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
      "name": "currency",
      "in": "query",
      "required": true,
      "description": "통화 코드",
      "schema": {
        "$ref": "#/components/schemas/Currency"
      },
      "examples": {
        "krw": {
          "summary": "원화",
          "value": "KRW"
        },
        "usd": {
          "summary": "달러",
          "value": "USD"
        }
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
                    "$ref": "#/components/schemas/BuyingPowerResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "krw": {
              "summary": "원화 응답",
              "value": {
                "result": {
                  "currency": "KRW",
                  "cashBuyingPower": "5000000"
                }
              }
            },
            "usd": {
              "summary": "달러 응답",
              "value": {
                "result": {
                  "currency": "USD",
                  "cashBuyingPower": "3500.5"
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
            "unsupportedCurrency": {
              "summary": "지원하지 않는 통화",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "지원하지 않는 통화입니다.",
                  "data": {
                    "field": "currency",
                    "allowedValues": [
                      "KRW",
                      "USD"
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
      "description": "계좌 없음",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
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
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorOrderInfo"
    }
  }
}
````

## GET /api/v1/sellable-quantity

### `/summary`

판매 가능 수량 조회

### `/description`

특정 종목의 판매 가능 수량을 조회합니다.

**Rate Limits Group**: `ORDER_INFO`


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/kr/summary`

국내주식 응답

### `/responses/200/content/application/json/examples/us/summary`

해외주식 응답

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/accountNotFound/summary`

조회 가능한 계좌가 없음

### `/responses/400/content/application/json/examples/accountHeaderRequired/summary`

X-Tossinvest-Account 헤더 누락

### 전체 연산 정의

````json
{
  "tags": [
    "Order Info"
  ],
  "summary": "판매 가능 수량 조회",
  "description": "특정 종목의 판매 가능 수량을 조회합니다.\n\n**Rate Limits Group**: `ORDER_INFO`\n",
  "operationId": "getSellableQuantity",
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
      "$ref": "#/components/parameters/SymbolQuery"
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
                    "$ref": "#/components/schemas/SellableQuantityResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "kr": {
              "summary": "국내주식 응답",
              "value": {
                "result": {
                  "sellableQuantity": "100"
                }
              }
            },
            "us": {
              "summary": "해외주식 응답",
              "value": {
                "result": {
                  "sellableQuantity": "5.5"
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
            "accountNotFound": {
              "summary": "조회 가능한 계좌가 없음",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "account-not-found",
                  "message": "계좌를 찾을 수 없습니다."
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
      "$ref": "#/components/responses/InternalErrorOrderInfo"
    }
  }
}
````

## GET /api/v1/commissions

### `/summary`

매매 수수료 조회

### `/description`

현재 계좌의 시장별 매매 수수료율을 조회합니다.
국내주식과 해외주식의 수수료 정보를 배열로 반환합니다.

**Rate Limits Group**: `ORDER_INFO`


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/standard/summary`

국내 + 해외 수수료

### `/responses/200/content/application/json/examples/unlimited/summary`

무기한 수수료

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/accountNotFound/summary`

조회 가능한 계좌가 없음

### `/responses/400/content/application/json/examples/accountHeaderRequired/summary`

X-Tossinvest-Account 헤더 누락

### 전체 연산 정의

````json
{
  "tags": [
    "Order Info"
  ],
  "summary": "매매 수수료 조회",
  "description": "현재 계좌의 시장별 매매 수수료율을 조회합니다.\n국내주식과 해외주식의 수수료 정보를 배열로 반환합니다.\n\n**Rate Limits Group**: `ORDER_INFO`\n",
  "operationId": "getCommissions",
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
                    "type": "array",
                    "items": {
                      "$ref": "#/components/schemas/Commission"
                    }
                  }
                }
              }
            ]
          },
          "examples": {
            "standard": {
              "summary": "국내 + 해외 수수료",
              "value": {
                "result": [
                  {
                    "marketCountry": "KR",
                    "commissionRate": "0.00015",
                    "startDate": "2026-01-01",
                    "endDate": "2026-12-31"
                  },
                  {
                    "marketCountry": "US",
                    "commissionRate": "0.001",
                    "startDate": null,
                    "endDate": "2026-06-30"
                  }
                ]
              }
            },
            "unlimited": {
              "summary": "무기한 수수료",
              "value": {
                "result": [
                  {
                    "marketCountry": "KR",
                    "commissionRate": "0.00015",
                    "startDate": "2026-01-01",
                    "endDate": null
                  },
                  {
                    "marketCountry": "US",
                    "commissionRate": "0.0025",
                    "startDate": null,
                    "endDate": null
                  }
                ]
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
            "accountNotFound": {
              "summary": "조회 가능한 계좌가 없음",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "account-not-found",
                  "message": "계좌를 찾을 수 없습니다."
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
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorOrderInfo"
    }
  }
}
````
