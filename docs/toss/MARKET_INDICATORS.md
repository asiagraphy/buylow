> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/MarketIndicatorsApi.md
> 문서 버전: 1.2.17

# MarketIndicatorsApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMarketIndicatorCandles**](MARKET_INDICATORS.md#getMarketIndicatorCandles) | **GET** /api/v1/market-indicators/{symbol}/candles | 시장 지표 캔들 차트 조회 |
| [**getMarketIndicatorInvestorTrading**](MARKET_INDICATORS.md#getMarketIndicatorInvestorTrading) | **GET** /api/v1/market-indicators/{symbol}/investor-trading | 투자자별 매매대금 조회 |
| [**getMarketIndicatorPrices**](MARKET_INDICATORS.md#getMarketIndicatorPrices) | **GET** /api/v1/market-indicators/prices | 시장 지표 현재가 조회 |


<a name="getMarketIndicatorCandles"></a>
# **getMarketIndicatorCandles**
> getMarketIndicatorCandles_200_response getMarketIndicatorCandles(symbol, interval, count, before)

시장 지표 캔들 차트 조회

    시장 지표(국내 지수·국채)의 캔들(OHLCV) 차트 데이터를 조회합니다. 최대 200개 봉을 반환합니다.  봉은 최신순(`timestamp` 내림차순)으로 정렬됩니다 — 배열의 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다.  지원 심볼은 그룹 상단 **Market Indicators** 설명의 심볼 카탈로그(8종)와 동일하며, 카탈로그에 없는 심볼은 400 `unsupported-symbol` 로 응답합니다. 개별 종목의 캔들은 `GET /api/v1/candles` 를 사용하세요.  분봉(`1m`)은 지수(`KOSPI`·`KOSDAQ`)만 지원합니다. 국채(`KR_BOND_*`)는 일봉(`1d`)만 지원하며, 분봉 요청 시 400 `invalid-request` 로 응답합니다.  **Rate Limits Group**: `MARKET_INDICATOR_CHART` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 시장 지표 심볼. 그룹 상단 Market Indicators 설명의 심볼 카탈로그 참조 | [default to null] |
| **interval** | **String**| 봉 단위. `1m`(분봉)은 지수(`KOSPI`·`KOSDAQ`)만 지원하고, 국채(`KR_BOND_*`)는 `1d`(일봉)만 지원합니다.  | [default to null] [enum: 1m, 1d] |
| **count** | **Integer**| 조회 봉 수 (최대 200) | [optional] [default to 100] |
| **before** | **Date**| 페이지네이션 상한 (inclusive, ISO 8601). 이 시각과 같거나 이전인 봉만 반환합니다. 미지정 시 가장 최신 봉부터 반환. 다음 페이지 요청 시 이전 응답의 `nextBefore` 값을 그대로 전달합니다. 타임존 오프셋의 `+` 는 쿼리스트링에서 `%2B` 로 URL 인코딩해야 합니다 (예: `before=2026-06-11T09:00:00%2B09:00`).  | [optional] [default to null] |

### Return type

[**getMarketIndicatorCandles_200_response**](MODEL_GET_MARKET_INDICATOR_CANDLES_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getMarketIndicatorInvestorTrading"></a>
# **getMarketIndicatorInvestorTrading**
> getMarketIndicatorInvestorTrading_200_response getMarketIndicatorInvestorTrading(symbol, interval, count, until)

투자자별 매매대금 조회

    KRX 시장(코스피·코스닥)의 투자자별 매매대금을 조회합니다. 개인·외국인·기관·기타법인 4개 투자자 분류의 매수·매도 거래대금을 집계 단위(`interval`)별 기록으로 최신순 제공하며, 기관은 7개 세부 분류(`breakdown`)를 함께 제공합니다.  - `KOSPI` / `KOSDAQ` 만 지원합니다. 그 외 심볼은 400 `unsupported-symbol` 로 응답합니다. - 모든 거래대금은 원화(KRW) 정수이며, 별도의 통화 필드는 제공하지 않습니다. - 4개 분류(개인·외국인·기관·기타법인)의 매수 합계와 매도 합계는 시장 전체 기준으로 서로 같습니다. - `foreigner` 는 외국인 전체 합계(등록·미등록 외국인 포함)이며, `institution` 의 `buyAmount`/`sellAmount` 는   `breakdown` 7개 항목의 합과 일치합니다. - 당일 기록은 장 종료 전까지 갱신될 수 있는 잠정치입니다. `updatedAt` 으로 마지막 갱신 시각을 확인하세요. - 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.  **Rate Limits Group**: `MARKET_INDICATOR` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbol** | **String**| 시장 지표 심볼. `KOSPI` / `KOSDAQ` 만 지원 | [default to null] [enum: KOSPI, KOSDAQ] |
| **interval** | **String**| 집계 단위 — 한 기록이 집계하는 기간입니다. - `1d`: 일별 - `1w`: 주별 - `1mo`: 월별 - `1y`: 연도별  | [default to null] [enum: 1d, 1w, 1mo, 1y] |
| **count** | **Integer**| 조회 수 (최대 100) | [optional] [default to 10] |
| **until** | **date**| 조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다. 미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.  | [optional] [default to null] |

### Return type

[**getMarketIndicatorInvestorTrading_200_response**](MODEL_GET_MARKET_INDICATOR_INVESTOR_TRADING_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getMarketIndicatorPrices"></a>
# **getMarketIndicatorPrices**
> getMarketIndicatorPrices_200_response getMarketIndicatorPrices(symbols)

시장 지표 현재가 조회

    시장 지표(국내 지수·국채)의 현재가를 조회합니다. 최대 200건 까지 다건 조회를 지원하며 콤마(`,`)로 구분합니다.  지원 심볼은 그룹 상단 **Market Indicators** 설명의 심볼 카탈로그(8종)를 따르며, 카탈로그에 없는 심볼은 400 `unsupported-symbol` 로 응답합니다.  **Rate Limits Group**: `MARKET_INDICATOR` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **symbols** | **String**| 시장 지표 심볼. 최대 200 개를 콤마(`,`)로 구분. 예: `KOSPI,KOSDAQ`. 심볼 카탈로그의 심볼만 지원한다. | [default to null] |

### Return type

[**getMarketIndicatorPrices_200_response**](MODEL_GET_MARKET_INDICATOR_PRICES_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## GET /api/v1/market-indicators/prices

### `/summary`

시장 지표 현재가 조회

### `/description`

시장 지표(국내 지수·국채)의 현재가를 조회합니다. 최대 200건 까지 다건 조회를 지원하며 콤마(`,`)로 구분합니다.

지원 심볼은 그룹 상단 **Market Indicators** 설명의 심볼 카탈로그(8종)를 따르며, 카탈로그에 없는 심볼은
400 `unsupported-symbol` 로 응답합니다.

**Rate Limits Group**: `MARKET_INDICATOR`


### `/parameters/0/description`

시장 지표 심볼. 최대 200 개를 콤마(`,`)로 구분. 예: `KOSPI,KOSDAQ`. 심볼 카탈로그의 심볼만 지원한다.

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/indices/summary`

지수 (코스피, 코스닥)

### `/responses/200/content/application/json/examples/bonds/summary`

국채 (수익률 %, 단위는 심볼 카탈로그 참조)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedSymbol/summary`

심볼 카탈로그에 없는 심볼

### `/responses/400/content/application/json/examples/invalidBatchSize/summary`

symbols 개수가 허용 범위(1~200) 를 벗어남

### 전체 연산 정의

````json
{
  "tags": [
    "Market Indicators"
  ],
  "summary": "시장 지표 현재가 조회",
  "description": "시장 지표(국내 지수·국채)의 현재가를 조회합니다. 최대 200건 까지 다건 조회를 지원하며 콤마(`,`)로 구분합니다.\n\n지원 심볼은 그룹 상단 **Market Indicators** 설명의 심볼 카탈로그(8종)를 따르며, 카탈로그에 없는 심볼은\n400 `unsupported-symbol` 로 응답합니다.\n\n**Rate Limits Group**: `MARKET_INDICATOR`\n",
  "operationId": "getMarketIndicatorPrices",
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
      "description": "시장 지표 심볼. 최대 200 개를 콤마(`,`)로 구분. 예: `KOSPI,KOSDAQ`. 심볼 카탈로그의 심볼만 지원한다.",
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9_,]+$"
      },
      "example": "KOSPI,KOSDAQ"
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
                      "$ref": "#/components/schemas/MarketIndicatorPriceResponse"
                    }
                  }
                }
              }
            ]
          },
          "examples": {
            "indices": {
              "summary": "지수 (코스피, 코스닥)",
              "value": {
                "result": [
                  {
                    "symbol": "KOSPI",
                    "timestamp": "2026-06-11T15:30:00+09:00",
                    "lastPrice": "2812.45"
                  },
                  {
                    "symbol": "KOSDAQ",
                    "timestamp": "2026-06-11T15:30:00+09:00",
                    "lastPrice": "845.32"
                  }
                ]
              }
            },
            "bonds": {
              "summary": "국채 (수익률 %, 단위는 심볼 카탈로그 참조)",
              "value": {
                "result": [
                  {
                    "symbol": "KR_BOND_10Y",
                    "timestamp": "2026-06-11T15:29:58+09:00",
                    "lastPrice": "3.25"
                  },
                  {
                    "symbol": "KR_BOND_2Y",
                    "timestamp": "2026-06-11T15:29:55+09:00",
                    "lastPrice": "2.98"
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
            "unsupportedSymbol": {
              "summary": "심볼 카탈로그에 없는 심볼",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "unsupported-symbol",
                  "message": "지원하지 않는 심볼입니다.",
                  "data": {
                    "field": "symbols",
                    "allowedValues": [
                      "KOSPI",
                      "KOSDAQ",
                      "KR_BOND_2Y",
                      "KR_BOND_3Y",
                      "KR_BOND_5Y",
                      "KR_BOND_10Y",
                      "KR_BOND_20Y",
                      "KR_BOND_30Y"
                    ]
                  }
                }
              }
            },
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
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorMarketIndicators"
    }
  }
}
````

## GET /api/v1/market-indicators/{symbol}/candles

### `/summary`

시장 지표 캔들 차트 조회

### `/description`

시장 지표(국내 지수·국채)의 캔들(OHLCV) 차트 데이터를 조회합니다. 최대 200개 봉을 반환합니다.

봉은 최신순(`timestamp` 내림차순)으로 정렬됩니다 — 배열의 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다.

지원 심볼은 그룹 상단 **Market Indicators** 설명의 심볼 카탈로그(8종)와 동일하며, 카탈로그에 없는 심볼은
400 `unsupported-symbol` 로 응답합니다. 개별 종목의 캔들은 `GET /api/v1/candles` 를 사용하세요.

분봉(`1m`)은 지수(`KOSPI`·`KOSDAQ`)만 지원합니다. 국채(`KR_BOND_*`)는 일봉(`1d`)만 지원하며, 분봉 요청 시
400 `invalid-request` 로 응답합니다.

**Rate Limits Group**: `MARKET_INDICATOR_CHART`


### `/parameters/0/description`

시장 지표 심볼. 그룹 상단 Market Indicators 설명의 심볼 카탈로그 참조

### `/parameters/0/examples/index/summary`

코스피

### `/parameters/0/examples/bond/summary`

한국 국채 10년

### `/parameters/1/description`

봉 단위. `1m`(분봉)은 지수(`KOSPI`·`KOSDAQ`)만 지원하고, 국채(`KR_BOND_*`)는 `1d`(일봉)만 지원합니다.


### `/parameters/2/description`

조회 봉 수 (최대 200)

### `/parameters/3/description`

페이지네이션 상한 (inclusive, ISO 8601). 이 시각과 같거나 이전인 봉만 반환합니다. 미지정 시 가장 최신 봉부터 반환.
다음 페이지 요청 시 이전 응답의 `nextBefore` 값을 그대로 전달합니다.
타임존 오프셋의 `+` 는 쿼리스트링에서 `%2B` 로 URL 인코딩해야 합니다 (예: `before=2026-06-11T09:00:00%2B09:00`).


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/dailyCandles/summary`

일봉 (1d, 코스피)

### `/responses/200/content/application/json/examples/lastPage/summary`

마지막 페이지 (nextBefore null)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedSymbol/summary`

심볼 카탈로그에 없는 심볼

### `/responses/400/content/application/json/examples/unsupportedCandleInterval/summary`

지원하지 않는 캔들 주기

### `/responses/400/content/application/json/examples/bondMinuteNotSupported/summary`

국채 분봉(1m) 미지원 — 일봉만 가능

### 전체 연산 정의

````json
{
  "tags": [
    "Market Indicators"
  ],
  "summary": "시장 지표 캔들 차트 조회",
  "description": "시장 지표(국내 지수·국채)의 캔들(OHLCV) 차트 데이터를 조회합니다. 최대 200개 봉을 반환합니다.\n\n봉은 최신순(`timestamp` 내림차순)으로 정렬됩니다 — 배열의 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다.\n\n지원 심볼은 그룹 상단 **Market Indicators** 설명의 심볼 카탈로그(8종)와 동일하며, 카탈로그에 없는 심볼은\n400 `unsupported-symbol` 로 응답합니다. 개별 종목의 캔들은 `GET /api/v1/candles` 를 사용하세요.\n\n분봉(`1m`)은 지수(`KOSPI`·`KOSDAQ`)만 지원합니다. 국채(`KR_BOND_*`)는 일봉(`1d`)만 지원하며, 분봉 요청 시\n400 `invalid-request` 로 응답합니다.\n\n**Rate Limits Group**: `MARKET_INDICATOR_CHART`\n",
  "operationId": "getMarketIndicatorCandles",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "name": "symbol",
      "in": "path",
      "required": true,
      "description": "시장 지표 심볼. 그룹 상단 Market Indicators 설명의 심볼 카탈로그 참조",
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9_]+$"
      },
      "examples": {
        "index": {
          "summary": "코스피",
          "value": "KOSPI"
        },
        "bond": {
          "summary": "한국 국채 10년",
          "value": "KR_BOND_10Y"
        }
      }
    },
    {
      "name": "interval",
      "in": "query",
      "required": true,
      "description": "봉 단위. `1m`(분봉)은 지수(`KOSPI`·`KOSDAQ`)만 지원하고, 국채(`KR_BOND_*`)는 `1d`(일봉)만 지원합니다.\n",
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
      "description": "페이지네이션 상한 (inclusive, ISO 8601). 이 시각과 같거나 이전인 봉만 반환합니다. 미지정 시 가장 최신 봉부터 반환.\n다음 페이지 요청 시 이전 응답의 `nextBefore` 값을 그대로 전달합니다.\n타임존 오프셋의 `+` 는 쿼리스트링에서 `%2B` 로 URL 인코딩해야 합니다 (예: `before=2026-06-11T09:00:00%2B09:00`).\n",
      "schema": {
        "type": "string",
        "format": "date-time"
      },
      "example": "2026-06-11T09:00:00+09:00"
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
                    "$ref": "#/components/schemas/MarketIndicatorCandlePageResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "dailyCandles": {
              "summary": "일봉 (1d, 코스피)",
              "value": {
                "result": {
                  "candles": [
                    {
                      "timestamp": "2026-06-11T09:00:00+09:00",
                      "openPrice": "2798.32",
                      "highPrice": "2820.15",
                      "lowPrice": "2790.1",
                      "closePrice": "2812.45",
                      "volume": "542000000"
                    },
                    {
                      "timestamp": "2026-06-10T09:00:00+09:00",
                      "openPrice": "2785.6",
                      "highPrice": "2801.22",
                      "lowPrice": "2779.85",
                      "closePrice": "2798.1",
                      "volume": "498000000"
                    }
                  ],
                  "nextBefore": "2026-06-10T09:00:00+09:00"
                }
              }
            },
            "lastPage": {
              "summary": "마지막 페이지 (nextBefore null)",
              "value": {
                "result": {
                  "candles": [
                    {
                      "timestamp": "2026-06-05T09:00:00+09:00",
                      "openPrice": "2750.4",
                      "highPrice": "2772.3",
                      "lowPrice": "2748.15",
                      "closePrice": "2768.9",
                      "volume": "471000000"
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
            "unsupportedSymbol": {
              "summary": "심볼 카탈로그에 없는 심볼",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "unsupported-symbol",
                  "message": "지원하지 않는 심볼입니다.",
                  "data": {
                    "field": "symbol",
                    "allowedValues": [
                      "KOSPI",
                      "KOSDAQ",
                      "KR_BOND_2Y",
                      "KR_BOND_3Y",
                      "KR_BOND_5Y",
                      "KR_BOND_10Y",
                      "KR_BOND_20Y",
                      "KR_BOND_30Y"
                    ]
                  }
                }
              }
            },
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
            },
            "bondMinuteNotSupported": {
              "summary": "국채 분봉(1m) 미지원 — 일봉만 가능",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "지원하지 않는 캔들 주기입니다.",
                  "data": {
                    "field": "interval",
                    "allowedValues": [
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
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorMarketIndicators"
    }
  }
}
````

## GET /api/v1/market-indicators/{symbol}/investor-trading

### `/summary`

투자자별 매매대금 조회

### `/description`

KRX 시장(코스피·코스닥)의 투자자별 매매대금을 조회합니다. 개인·외국인·기관·기타법인 4개 투자자 분류의
매수·매도 거래대금을 집계 단위(`interval`)별 기록으로 최신순 제공하며, 기관은 7개 세부 분류(`breakdown`)를
함께 제공합니다.

- `KOSPI` / `KOSDAQ` 만 지원합니다. 그 외 심볼은 400 `unsupported-symbol` 로 응답합니다.
- 모든 거래대금은 원화(KRW) 정수이며, 별도의 통화 필드는 제공하지 않습니다.
- 4개 분류(개인·외국인·기관·기타법인)의 매수 합계와 매도 합계는 시장 전체 기준으로 서로 같습니다.
- `foreigner` 는 외국인 전체 합계(등록·미등록 외국인 포함)이며, `institution` 의 `buyAmount`/`sellAmount` 는
  `breakdown` 7개 항목의 합과 일치합니다.
- 당일 기록은 장 종료 전까지 갱신될 수 있는 잠정치입니다. `updatedAt` 으로 마지막 갱신 시각을 확인하세요.
- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.

**Rate Limits Group**: `MARKET_INDICATOR`


### `/parameters/0/description`

시장 지표 심볼. `KOSPI` / `KOSDAQ` 만 지원

### `/parameters/1/description`

집계 단위 — 한 기록이 집계하는 기간입니다.
- `1d`: 일별
- `1w`: 주별
- `1mo`: 월별
- `1y`: 연도별


### `/parameters/2/description`

조회 수 (최대 100)

### `/parameters/3/description`

조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.
미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/daily/summary`

일별 집계 (코스피, count=2)

### `/responses/200/content/application/json/examples/noData/summary`

조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedSymbol/summary`

지원하지 않는 심볼 (KOSPI/KOSDAQ 외)

### `/responses/400/content/application/json/examples/invalidInterval/summary`

지원하지 않는 집계 단위

### `/responses/400/content/application/json/examples/invalidCount/summary`

count 가 허용 범위(1~100)를 벗어남

### 전체 연산 정의

````json
{
  "tags": [
    "Market Indicators"
  ],
  "summary": "투자자별 매매대금 조회",
  "description": "KRX 시장(코스피·코스닥)의 투자자별 매매대금을 조회합니다. 개인·외국인·기관·기타법인 4개 투자자 분류의\n매수·매도 거래대금을 집계 단위(`interval`)별 기록으로 최신순 제공하며, 기관은 7개 세부 분류(`breakdown`)를\n함께 제공합니다.\n\n- `KOSPI` / `KOSDAQ` 만 지원합니다. 그 외 심볼은 400 `unsupported-symbol` 로 응답합니다.\n- 모든 거래대금은 원화(KRW) 정수이며, 별도의 통화 필드는 제공하지 않습니다.\n- 4개 분류(개인·외국인·기관·기타법인)의 매수 합계와 매도 합계는 시장 전체 기준으로 서로 같습니다.\n- `foreigner` 는 외국인 전체 합계(등록·미등록 외국인 포함)이며, `institution` 의 `buyAmount`/`sellAmount` 는\n  `breakdown` 7개 항목의 합과 일치합니다.\n- 당일 기록은 장 종료 전까지 갱신될 수 있는 잠정치입니다. `updatedAt` 으로 마지막 갱신 시각을 확인하세요.\n- 다음 페이지는 응답의 `nextUntil` 값을 `until` 파라미터로 전달해 조회합니다.\n\n**Rate Limits Group**: `MARKET_INDICATOR`\n",
  "operationId": "getMarketIndicatorInvestorTrading",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "name": "symbol",
      "in": "path",
      "required": true,
      "description": "시장 지표 심볼. `KOSPI` / `KOSDAQ` 만 지원",
      "schema": {
        "type": "string",
        "enum": [
          "KOSPI",
          "KOSDAQ"
        ]
      },
      "example": "KOSPI"
    },
    {
      "name": "interval",
      "in": "query",
      "required": true,
      "description": "집계 단위 — 한 기록이 집계하는 기간입니다.\n- `1d`: 일별\n- `1w`: 주별\n- `1mo`: 월별\n- `1y`: 연도별\n",
      "schema": {
        "type": "string",
        "enum": [
          "1d",
          "1w",
          "1mo",
          "1y"
        ]
      }
    },
    {
      "name": "count",
      "in": "query",
      "required": false,
      "description": "조회 수 (최대 100)",
      "schema": {
        "type": "integer",
        "default": 10,
        "minimum": 1,
        "maximum": 100
      }
    },
    {
      "name": "until",
      "in": "query",
      "required": false,
      "description": "조회 기준일 (inclusive, `YYYY-MM-DD`). 이 날짜까지의 데이터를 최신순으로 `count` 개 반환합니다.\n미지정 시 가장 최신 데이터부터 반환. 다음 페이지 요청 시 이전 응답의 `nextUntil` 값을 그대로 전달합니다.\n",
      "schema": {
        "type": "string",
        "format": "date"
      },
      "example": "2026-06-11"
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
                    "$ref": "#/components/schemas/InvestorTradingResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "daily": {
              "summary": "일별 집계 (코스피, count=2)",
              "value": {
                "result": {
                  "nextUntil": "2026-06-09",
                  "records": [
                    {
                      "date": "2026-06-11",
                      "updatedAt": "2026-06-11T18:10:00+09:00",
                      "individual": {
                        "buyAmount": "5200000000000",
                        "sellAmount": "5350000000000"
                      },
                      "foreigner": {
                        "buyAmount": "3800000000000",
                        "sellAmount": "3600000000000"
                      },
                      "institution": {
                        "buyAmount": "2100000000000",
                        "sellAmount": "2180000000000",
                        "breakdown": {
                          "financialInvestment": {
                            "buyAmount": "900000000000",
                            "sellAmount": "950000000000"
                          },
                          "insurance": {
                            "buyAmount": "150000000000",
                            "sellAmount": "140000000000"
                          },
                          "trust": {
                            "buyAmount": "280000000000",
                            "sellAmount": "300000000000"
                          },
                          "privateEquityFund": {
                            "buyAmount": "120000000000",
                            "sellAmount": "130000000000"
                          },
                          "bank": {
                            "buyAmount": "50000000000",
                            "sellAmount": "60000000000"
                          },
                          "otherFinancialInstitution": {
                            "buyAmount": "100000000000",
                            "sellAmount": "110000000000"
                          },
                          "pensionFund": {
                            "buyAmount": "500000000000",
                            "sellAmount": "490000000000"
                          }
                        }
                      },
                      "otherCorporation": {
                        "buyAmount": "450000000000",
                        "sellAmount": "420000000000"
                      }
                    },
                    {
                      "date": "2026-06-10",
                      "updatedAt": "2026-06-10T18:10:00+09:00",
                      "individual": {
                        "buyAmount": "4900000000000",
                        "sellAmount": "4800000000000"
                      },
                      "foreigner": {
                        "buyAmount": "3500000000000",
                        "sellAmount": "3700000000000"
                      },
                      "institution": {
                        "buyAmount": "2300000000000",
                        "sellAmount": "2250000000000",
                        "breakdown": {
                          "financialInvestment": {
                            "buyAmount": "1000000000000",
                            "sellAmount": "980000000000"
                          },
                          "insurance": {
                            "buyAmount": "160000000000",
                            "sellAmount": "150000000000"
                          },
                          "trust": {
                            "buyAmount": "300000000000",
                            "sellAmount": "290000000000"
                          },
                          "privateEquityFund": {
                            "buyAmount": "130000000000",
                            "sellAmount": "125000000000"
                          },
                          "bank": {
                            "buyAmount": "60000000000",
                            "sellAmount": "55000000000"
                          },
                          "otherFinancialInstitution": {
                            "buyAmount": "110000000000",
                            "sellAmount": "105000000000"
                          },
                          "pensionFund": {
                            "buyAmount": "540000000000",
                            "sellAmount": "545000000000"
                          }
                        }
                      },
                      "otherCorporation": {
                        "buyAmount": "400000000000",
                        "sellAmount": "350000000000"
                      }
                    }
                  ]
                }
              }
            },
            "noData": {
              "summary": "조회 범위에 데이터 없음 (records 빈 배열, nextUntil null)",
              "value": {
                "result": {
                  "nextUntil": null,
                  "records": []
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
            "unsupportedSymbol": {
              "summary": "지원하지 않는 심볼 (KOSPI/KOSDAQ 외)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "unsupported-symbol",
                  "message": "지원하지 않는 심볼입니다.",
                  "data": {
                    "field": "symbol",
                    "allowedValues": [
                      "KOSPI",
                      "KOSDAQ"
                    ]
                  }
                }
              }
            },
            "invalidInterval": {
              "summary": "지원하지 않는 집계 단위",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다.",
                  "data": {
                    "field": "interval",
                    "allowedValues": [
                      "1d",
                      "1w",
                      "1mo",
                      "1y"
                    ]
                  }
                }
              }
            },
            "invalidCount": {
              "summary": "count 가 허용 범위(1~100)를 벗어남",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다.",
                  "data": {
                    "field": "count",
                    "constraint": {
                      "min": 1,
                      "max": 100
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
      "$ref": "#/components/responses/InternalErrorMarketIndicators"
    }
  }
}
````
