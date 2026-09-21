> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/MarketDataApi.md
> 문서 버전: 1.2.17

# MarketDataApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCandles**](MARKET_DATA.md#getCandles) | **GET** /api/v1/candles | 캔들 차트 조회 |
| [**getOrderbook**](MARKET_DATA.md#getOrderbook) | **GET** /api/v1/orderbook | 호가 조회 |
| [**getPriceLimit**](MARKET_DATA.md#getPriceLimit) | **GET** /api/v1/price-limits | 상/하한가 조회 |
| [**getPrices**](MARKET_DATA.md#getPrices) | **GET** /api/v1/prices | 현재가 조회 |
| [**getTrades**](MARKET_DATA.md#getTrades) | **GET** /api/v1/trades | 최근 체결 내역 조회 |


<a name="getCandles"></a>
# **getCandles**
> getCandles_200_response getCandles(symbol, interval, count, before, adjusted)

캔들 차트 조회

    종목의 캔들(OHLCV) 차트 데이터를 조회합니다. 최대 200개 봉을 반환합니다.  봉은 최신순(`timestamp` 내림차순)으로 정렬됩니다 — 배열의 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다.  **Rate Limits Group**: `MARKET_DATA_CHART` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL). 영문 대/소문자, 숫자, '.', '-' 만 허용한다. | [default to null] |
| **interval** | **String**| 봉 단위 | [default to null] [enum: 1m, 1d] |
| **count** | **Integer**| 조회 봉 수 (최대 200) | [optional] [default to 100] |
| **before** | **Date**| 페이지네이션 상한 (inclusive, ISO 8601). 이 시각과 같거나 이전인 봉만 반환합니다. 미지정 시 가장 최신 봉부터 반환. 다음 페이지 요청 시 이전 응답의 `nextBefore` 값을 그대로 전달합니다. 타임존 오프셋의 `+` 는 쿼리스트링에서 `%2B` 로 URL 인코딩해야 합니다 (예: `before=2026-03-25T09:00:00%2B09:00`).  | [optional] [default to null] |
| **adjusted** | **Boolean**| 수정주가 적용 여부. `true` 면 수정주가 적용, `false` 면 미적용. | [optional] [default to true] |

### Return type

[**getCandles_200_response**](MODEL_GET_CANDLES_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getOrderbook"></a>
# **getOrderbook**
> getOrderbook_200_response getOrderbook(symbol)

호가 조회

    매수/매도 호가 및 잔량을 조회합니다.  **Rate Limits Group**: `MARKET_DATA` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL). 영문 대/소문자, 숫자, '.', '-' 만 허용한다. | [default to null] |

### Return type

[**getOrderbook_200_response**](MODEL_GET_ORDERBOOK_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getPriceLimit"></a>
# **getPriceLimit**
> getPriceLimit_200_response getPriceLimit(symbol)

상/하한가 조회

    종목의 당일 상한가 및 하한가를 조회합니다.  **Rate Limits Group**: `MARKET_DATA` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL). 영문 대/소문자, 숫자, '.', '-' 만 허용한다. | [default to null] |

### Return type

[**getPriceLimit_200_response**](MODEL_GET_PRICE_LIMIT_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getPrices"></a>
# **getPrices**
> getPrices_200_response getPrices(symbols)

현재가 조회

    종목의 현재가 정보를 조회합니다. 최대 200건 까지 다건 조회를 지원하며 콤마(`,`)로 구분합니다.  **Rate Limits Group**: `MARKET_DATA` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbols** | **String**| 종목 심볼. 최대 200 개를 콤마(`,`)로 구분. 예: `005930,000660` 또는 `AAPL,MSFT`. 영문 대/소문자, 숫자, '.', '-' 만 허용한다. | [default to null] |

### Return type

[**getPrices_200_response**](MODEL_GET_PRICES_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getTrades"></a>
# **getTrades**
> getTrades_200_response getTrades(symbol, count)

최근 체결 내역 조회

    당일 최근 체결 내역을 조회합니다.  **Rate Limits Group**: `MARKET_DATA` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL). 영문 대/소문자, 숫자, '.', '-' 만 허용한다. | [default to null] |
| **count** | **Integer**| 조회 건수 (최대 50) | [optional] [default to 50] |

### Return type

[**getTrades_200_response**](MODEL_GET_TRADES_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## GET /api/v1/orderbook

### `/summary`

호가 조회

### `/description`

매수/매도 호가 및 잔량을 조회합니다.

**Rate Limits Group**: `MARKET_DATA`


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/krStock/summary`

국내 주식 (삼성전자)

### `/responses/200/content/application/json/examples/usStock/summary`

해외 주식 (Apple)

### 전체 연산 정의

````json
{
  "tags": [
    "Market Data"
  ],
  "summary": "호가 조회",
  "description": "매수/매도 호가 및 잔량을 조회합니다.\n\n**Rate Limits Group**: `MARKET_DATA`\n",
  "operationId": "getOrderbook",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
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
                    "$ref": "#/components/schemas/OrderbookResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "krStock": {
              "summary": "국내 주식 (삼성전자)",
              "value": {
                "result": {
                  "timestamp": "2026-03-25T09:30:00.123+09:00",
                  "currency": "KRW",
                  "asks": [
                    {
                      "price": "72300",
                      "volume": "1200"
                    },
                    {
                      "price": "72200",
                      "volume": "3400"
                    },
                    {
                      "price": "72100",
                      "volume": "8500"
                    }
                  ],
                  "bids": [
                    {
                      "price": "72000",
                      "volume": "5200"
                    },
                    {
                      "price": "71900",
                      "volume": "4100"
                    },
                    {
                      "price": "71800",
                      "volume": "2700"
                    }
                  ]
                }
              }
            },
            "usStock": {
              "summary": "해외 주식 (Apple)",
              "value": {
                "result": {
                  "timestamp": "2026-03-25T22:30:00.456+09:00",
                  "currency": "USD",
                  "asks": [
                    {
                      "price": "185.75",
                      "volume": "250"
                    },
                    {
                      "price": "185.70",
                      "volume": "410"
                    }
                  ],
                  "bids": [
                    {
                      "price": "185.65",
                      "volume": "180"
                    },
                    {
                      "price": "185.60",
                      "volume": "320"
                    }
                  ]
                }
              }
            }
          }
        }
      }
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorMarketData"
    }
  }
}
````

## GET /api/v1/prices

### `/summary`

현재가 조회

### `/description`

종목의 현재가 정보를 조회합니다. 최대 200건 까지 다건 조회를 지원하며 콤마(`,`)로 구분합니다.

**Rate Limits Group**: `MARKET_DATA`


### `/parameters/0/description`

종목 심볼. 최대 200 개를 콤마(`,`)로 구분. 예: `005930,000660` 또는 `AAPL,MSFT`. 영문 대/소문자, 숫자, '.', '-' 만 허용한다.

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/krStock/summary`

국내 주식 (삼성전자)

### `/responses/200/content/application/json/examples/usStock/summary`

해외 주식 (Apple)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/invalidBatchSize/summary`

symbols 개수가 허용 범위(1~200) 를 벗어남

### 전체 연산 정의

````json
{
  "tags": [
    "Market Data"
  ],
  "summary": "현재가 조회",
  "description": "종목의 현재가 정보를 조회합니다. 최대 200건 까지 다건 조회를 지원하며 콤마(`,`)로 구분합니다.\n\n**Rate Limits Group**: `MARKET_DATA`\n",
  "operationId": "getPrices",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "name": "symbols",
      "in": "query",
      "required": true,
      "description": "종목 심볼. 최대 200 개를 콤마(`,`)로 구분. 예: `005930,000660` 또는 `AAPL,MSFT`. 영문 대/소문자, 숫자, '.', '-' 만 허용한다.",
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9.,\\-]+$"
      },
      "example": "005930,000660"
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
                      "$ref": "#/components/schemas/PriceResponse"
                    }
                  }
                }
              }
            ]
          },
          "examples": {
            "krStock": {
              "summary": "국내 주식 (삼성전자)",
              "value": {
                "result": [
                  {
                    "symbol": "005930",
                    "timestamp": "2026-03-25T09:30:00.123+09:00",
                    "lastPrice": "72000",
                    "currency": "KRW"
                  }
                ]
              }
            },
            "usStock": {
              "summary": "해외 주식 (Apple)",
              "value": {
                "result": [
                  {
                    "symbol": "AAPL",
                    "timestamp": "2026-03-25T22:30:00.456+09:00",
                    "lastPrice": "185.70",
                    "currency": "USD"
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
            "invalidBatchSize": {
              "summary": "symbols 개수가 허용 범위(1~200) 를 벗어남",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다.",
                  "data": {
                    "field": "symbols",
                    "constraint": {
                      "min": 1,
                      "max": 200
                    }
                  }
                }
              }
            }
          }
        }
      }
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorMarketData"
    }
  }
}
````

## GET /api/v1/trades

### `/summary`

최근 체결 내역 조회

### `/description`

당일 최근 체결 내역을 조회합니다.

**Rate Limits Group**: `MARKET_DATA`


### `/parameters/1/description`

조회 건수 (최대 50)

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/krStock/summary`

국내 주식 (삼성전자)

### `/responses/200/content/application/json/examples/usStock/summary`

해외 주식 (Apple)

### 전체 연산 정의

````json
{
  "tags": [
    "Market Data"
  ],
  "summary": "최근 체결 내역 조회",
  "description": "당일 최근 체결 내역을 조회합니다.\n\n**Rate Limits Group**: `MARKET_DATA`\n",
  "operationId": "getTrades",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/SymbolQuery"
    },
    {
      "name": "count",
      "in": "query",
      "required": false,
      "description": "조회 건수 (최대 50)",
      "schema": {
        "type": "integer",
        "default": 50,
        "minimum": 1,
        "maximum": 50
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
                    "type": "array",
                    "items": {
                      "$ref": "#/components/schemas/Trade"
                    }
                  }
                }
              }
            ]
          },
          "examples": {
            "krStock": {
              "summary": "국내 주식 (삼성전자)",
              "value": {
                "result": [
                  {
                    "price": "72000",
                    "volume": "120",
                    "timestamp": "2026-03-25T09:30:42.000+09:00",
                    "currency": "KRW"
                  },
                  {
                    "price": "71900",
                    "volume": "50",
                    "timestamp": "2026-03-25T09:30:41.500+09:00",
                    "currency": "KRW"
                  },
                  {
                    "price": "72000",
                    "volume": "200",
                    "timestamp": "2026-03-25T09:30:40.800+09:00",
                    "currency": "KRW"
                  }
                ]
              }
            },
            "usStock": {
              "summary": "해외 주식 (Apple)",
              "value": {
                "result": [
                  {
                    "price": "185.70",
                    "volume": "15",
                    "timestamp": "2026-03-25T22:30:42.100+09:00",
                    "currency": "USD"
                  },
                  {
                    "price": "185.75",
                    "volume": "8",
                    "timestamp": "2026-03-25T22:30:41.700+09:00",
                    "currency": "USD"
                  }
                ]
              }
            }
          }
        }
      }
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorMarketData"
    }
  }
}
````

## GET /api/v1/price-limits

### `/summary`

상/하한가 조회

### `/description`

종목의 당일 상한가 및 하한가를 조회합니다.

**Rate Limits Group**: `MARKET_DATA`


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/krStock/summary`

국내 주식 (삼성전자)

### `/responses/200/content/application/json/examples/usStock/summary`

해외 주식 (Apple, 가격제한 없음)

### 전체 연산 정의

````json
{
  "tags": [
    "Market Data"
  ],
  "summary": "상/하한가 조회",
  "description": "종목의 당일 상한가 및 하한가를 조회합니다.\n\n**Rate Limits Group**: `MARKET_DATA`\n",
  "operationId": "getPriceLimit",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
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
                    "$ref": "#/components/schemas/PriceLimitResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "krStock": {
              "summary": "국내 주식 (삼성전자)",
              "value": {
                "result": {
                  "timestamp": "2026-03-25T09:30:00.123+09:00",
                  "upperLimitPrice": "93000",
                  "lowerLimitPrice": "50400",
                  "currency": "KRW"
                }
              }
            },
            "usStock": {
              "summary": "해외 주식 (Apple, 가격제한 없음)",
              "value": {
                "result": {
                  "timestamp": "2026-03-25T22:30:00.456+09:00",
                  "upperLimitPrice": null,
                  "lowerLimitPrice": null,
                  "currency": "USD"
                }
              }
            }
          }
        }
      }
    },
    "404": {
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorMarketData"
    }
  }
}
````

## GET /api/v1/candles

### `/summary`

캔들 차트 조회

### `/description`

종목의 캔들(OHLCV) 차트 데이터를 조회합니다. 최대 200개 봉을 반환합니다.

봉은 최신순(`timestamp` 내림차순)으로 정렬됩니다 — 배열의 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다.

**Rate Limits Group**: `MARKET_DATA_CHART`


### `/parameters/1/description`

봉 단위

### `/parameters/2/description`

조회 봉 수 (최대 200)

### `/parameters/3/description`

페이지네이션 상한 (inclusive, ISO 8601). 이 시각과 같거나 이전인 봉만 반환합니다. 미지정 시 가장 최신 봉부터 반환.
다음 페이지 요청 시 이전 응답의 `nextBefore` 값을 그대로 전달합니다.
타임존 오프셋의 `+` 는 쿼리스트링에서 `%2B` 로 URL 인코딩해야 합니다 (예: `before=2026-03-25T09:00:00%2B09:00`).


### `/parameters/4/description`

수정주가 적용 여부. `true` 면 수정주가 적용, `false` 면 미적용.

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/dailyCandles/summary`

일봉 (1d)

### `/responses/200/content/application/json/examples/minuteCandles/summary`

분봉 (1m)

### `/responses/200/content/application/json/examples/lastPage/summary`

마지막 페이지 (nextBefore null)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedCandleInterval/summary`

지원하지 않는 캔들 주기

### 전체 연산 정의

````json
{
  "tags": [
    "Market Data"
  ],
  "summary": "캔들 차트 조회",
  "description": "종목의 캔들(OHLCV) 차트 데이터를 조회합니다. 최대 200개 봉을 반환합니다.\n\n봉은 최신순(`timestamp` 내림차순)으로 정렬됩니다 — 배열의 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다.\n\n**Rate Limits Group**: `MARKET_DATA_CHART`\n",
  "operationId": "getCandles",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "$ref": "#/components/parameters/SymbolQuery"
    },
    {
      "name": "interval",
      "in": "query",
      "required": true,
      "description": "봉 단위",
      "schema": {
        "type": "string",
        "enum": [
          "1m",
          "1d"
        ]
      }
    },
    {
      "name": "count",
      "in": "query",
      "required": false,
      "description": "조회 봉 수 (최대 200)",
      "schema": {
        "type": "integer",
        "default": 100,
        "minimum": 1,
        "maximum": 200
      }
    },
    {
      "name": "before",
      "in": "query",
      "required": false,
      "description": "페이지네이션 상한 (inclusive, ISO 8601). 이 시각과 같거나 이전인 봉만 반환합니다. 미지정 시 가장 최신 봉부터 반환.\n다음 페이지 요청 시 이전 응답의 `nextBefore` 값을 그대로 전달합니다.\n타임존 오프셋의 `+` 는 쿼리스트링에서 `%2B` 로 URL 인코딩해야 합니다 (예: `before=2026-03-25T09:00:00%2B09:00`).\n",
      "schema": {
        "type": "string",
        "format": "date-time"
      },
      "example": "2026-03-25T09:00:00+09:00"
    },
    {
      "name": "adjusted",
      "in": "query",
      "required": false,
      "description": "수정주가 적용 여부. `true` 면 수정주가 적용, `false` 면 미적용.",
      "schema": {
        "type": "boolean",
        "default": true
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
                    "$ref": "#/components/schemas/CandlePageResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "dailyCandles": {
              "summary": "일봉 (1d)",
              "value": {
                "result": {
                  "candles": [
                    {
                      "timestamp": "2026-03-25T00:00:00+09:00",
                      "openPrice": "71600",
                      "highPrice": "72300",
                      "lowPrice": "71500",
                      "closePrice": "72000",
                      "volume": "3521000",
                      "currency": "KRW"
                    },
                    {
                      "timestamp": "2026-03-24T00:00:00+09:00",
                      "openPrice": "71200",
                      "highPrice": "71800",
                      "lowPrice": "71000",
                      "closePrice": "71600",
                      "volume": "2984000",
                      "currency": "KRW"
                    }
                  ],
                  "nextBefore": "2026-03-24T00:00:00+09:00"
                }
              }
            },
            "minuteCandles": {
              "summary": "분봉 (1m)",
              "value": {
                "result": {
                  "candles": [
                    {
                      "timestamp": "2026-03-25T09:32:00+09:00",
                      "openPrice": "72000",
                      "highPrice": "72100",
                      "lowPrice": "71950",
                      "closePrice": "72050",
                      "volume": "15200",
                      "currency": "KRW"
                    },
                    {
                      "timestamp": "2026-03-25T09:31:00+09:00",
                      "openPrice": "71950",
                      "highPrice": "72050",
                      "lowPrice": "71900",
                      "closePrice": "72000",
                      "volume": "18400",
                      "currency": "KRW"
                    }
                  ],
                  "nextBefore": "2026-03-25T09:31:00+09:00"
                }
              }
            },
            "lastPage": {
              "summary": "마지막 페이지 (nextBefore null)",
              "value": {
                "result": {
                  "candles": [
                    {
                      "timestamp": "2026-03-20T00:00:00+09:00",
                      "openPrice": "70800",
                      "highPrice": "71200",
                      "lowPrice": "70500",
                      "closePrice": "71000",
                      "volume": "2112000",
                      "currency": "KRW"
                    }
                  ],
                  "nextBefore": null
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
            "unsupportedCandleInterval": {
              "summary": "지원하지 않는 캔들 주기",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "지원하지 않는 캔들 주기입니다.",
                  "data": {
                    "field": "interval",
                    "allowedValues": [
                      "1m",
                      "1d"
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
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorMarketData"
    }
  }
}
````
