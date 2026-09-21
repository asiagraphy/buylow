> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/RankingApi.md
> 문서 버전: 1.2.17

# RankingApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRankings**](RANKING.md#getRankings) | **GET** /api/v1/rankings | 주식 랭킹 조회 |


<a name="getRankings"></a>
# **getRankings**
> getRankings_200_response getRankings(type, marketCountry, duration, excludeInvestmentCaution, count)

주식 랭킹 조회

    지정한 시장(`marketCountry`) · 기간(`duration`) · 기준(`type`)의 주식 랭킹을 조회합니다. 상위 100위까지 제공합니다.  - `TOP_GAINERS` / `TOP_LOSERS` 는 `duration=realtime` 을 지원하지 않습니다 (400 `unsupported-ranking-duration`). - `tradingVolume` / `tradingAmount` 의 집계 기준은 `type` 이 결정합니다 — `TOSS_SECURITIES_*` 는 토스증권 체결 기준, 그 외(`MARKET_*` / `TOP_*`)는 시장 전체 기준. - `price.basePrice` 는 `TOP_GAINERS` / `TOP_LOSERS` 만 `duration` 시작 시점 기준가이며, 나머지 타입은 `duration` 과 무관하게 항상 전일 기준가입니다. `price.changeRate` 도 같은 의미를 따릅니다 (기간 등락률 vs 전일 대비 등락률). - 응답 항목 수는 `count` 보다 적을 수 있습니다 (시세 조회에 실패한 종목은 제외). - 랭킹이 집계되지 않은 조합은 에러가 아닌 빈 `rankings` 배열로 응답하며, 이때 `rankedAt` 은 null 입니다.  **Rate Limits Group**: `RANKING` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**| 랭킹 종류. 이름에 포함된 지표가 랭킹 기준값입니다 — `*_TRADING_AMOUNT` → `tradingAmount`, `*_TRADING_VOLUME` → `tradingVolume`, `TOP_GAINERS` / `TOP_LOSERS` → `price.changeRate`. - `MARKET_TRADING_AMOUNT`: 시장 거래대금 상위 - `MARKET_TRADING_VOLUME`: 시장 거래량 상위 - `TOP_GAINERS`: 급상승 (등락률 상위) — `realtime` 미지원 - `TOP_LOSERS`: 급하락 (등락률 하위) — `realtime` 미지원 - `TOSS_SECURITIES_TRADING_AMOUNT`: 토스증권 거래대금 상위 - `TOSS_SECURITIES_TRADING_VOLUME`: 토스증권 거래량 상위  | [default to null] [enum: MARKET_TRADING_AMOUNT, MARKET_TRADING_VOLUME, TOP_GAINERS, TOP_LOSERS, TOSS_SECURITIES_TRADING_AMOUNT, TOSS_SECURITIES_TRADING_VOLUME] |
| **marketCountry** | [**MarketCountry**](MODEL_MARKET_COUNTRY.md)| 조회 시장 | [default to null] [enum: KR, US] |
| **duration** | **String**| 랭킹 산정 기간. 모든 기간은 거래일 기준입니다. - `realtime`: 실시간 - `1d`: 1일 - `1w`: 1주 - `1mo`: 1개월 - `3mo`: 3개월 - `6mo`: 6개월 - `1y`: 1년  | [default to null] [enum: realtime, 1d, 1w, 1mo, 3mo, 6mo, 1y] |
| **excludeInvestmentCaution** | **Boolean**| 투자 유의 종목 제외 여부 | [optional] [default to false] |
| **count** | **Integer**| 조회 수 (최대 100). 응답 항목 수는 `count` 이하일 수 있습니다. | [optional] [default to 100] |

### Return type

[**getRankings_200_response**](MODEL_GET_RANKINGS_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## GET /api/v1/rankings

### `/summary`

주식 랭킹 조회

### `/description`

지정한 시장(`marketCountry`) · 기간(`duration`) · 기준(`type`)의 주식 랭킹을 조회합니다. 상위 100위까지 제공합니다.

- `TOP_GAINERS` / `TOP_LOSERS` 는 `duration=realtime` 을 지원하지 않습니다 (400 `unsupported-ranking-duration`).
- `tradingVolume` / `tradingAmount` 의 집계 기준은 `type` 이 결정합니다 — `TOSS_SECURITIES_*` 는 토스증권 체결 기준, 그 외(`MARKET_*` / `TOP_*`)는 시장 전체 기준.
- `price.basePrice` 는 `TOP_GAINERS` / `TOP_LOSERS` 만 `duration` 시작 시점 기준가이며, 나머지 타입은 `duration` 과 무관하게 항상 전일 기준가입니다. `price.changeRate` 도 같은 의미를 따릅니다 (기간 등락률 vs 전일 대비 등락률).
- 응답 항목 수는 `count` 보다 적을 수 있습니다 (시세 조회에 실패한 종목은 제외).
- 랭킹이 집계되지 않은 조합은 에러가 아닌 빈 `rankings` 배열로 응답하며, 이때 `rankedAt` 은 null 입니다.

**Rate Limits Group**: `RANKING`


### `/parameters/0/description`

랭킹 종류. 이름에 포함된 지표가 랭킹 기준값입니다 — `*_TRADING_AMOUNT` → `tradingAmount`, `*_TRADING_VOLUME` → `tradingVolume`, `TOP_GAINERS` / `TOP_LOSERS` → `price.changeRate`.
- `MARKET_TRADING_AMOUNT`: 시장 거래대금 상위
- `MARKET_TRADING_VOLUME`: 시장 거래량 상위
- `TOP_GAINERS`: 급상승 (등락률 상위) — `realtime` 미지원
- `TOP_LOSERS`: 급하락 (등락률 하위) — `realtime` 미지원
- `TOSS_SECURITIES_TRADING_AMOUNT`: 토스증권 거래대금 상위
- `TOSS_SECURITIES_TRADING_VOLUME`: 토스증권 거래량 상위


### `/parameters/1/description`

조회 시장

### `/parameters/2/description`

랭킹 산정 기간. 모든 기간은 거래일 기준입니다.
- `realtime`: 실시간
- `1d`: 1일
- `1w`: 1주
- `1mo`: 1개월
- `3mo`: 3개월
- `6mo`: 6개월
- `1y`: 1년


### `/parameters/3/description`

투자 유의 종목 제외 여부

### `/parameters/4/description`

조회 수 (최대 100). 응답 항목 수는 `count` 이하일 수 있습니다.

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/marketTradingAmount/summary`

시장 거래대금 상위 (KR / realtime)

### `/responses/200/content/application/json/examples/tossSecuritiesTradingVolume/summary`

토스증권 거래량 상위 (US / 1d) — trading* 값은 토스증권 체결 기준

### `/responses/200/content/application/json/examples/topGainers/summary`

급상승 (KR / 1w) — basePrice 가 1주 전 기준가, changeRate 가 기간 등락률

### `/responses/200/content/application/json/examples/emptyRankings/summary`

집계 데이터 없음 (빈 배열, rankedAt null)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/invalidType/summary`

지원하지 않는 type 값

### `/responses/400/content/application/json/examples/invalidCount/summary`

count 가 허용 범위(1~100)를 벗어남

### `/responses/400/content/application/json/examples/unsupportedRankingDuration/summary`

지원하지 않는 랭킹 기간 (TOP_GAINERS / TOP_LOSERS + realtime)

### 전체 연산 정의

````json
{
  "tags": [
    "Ranking"
  ],
  "summary": "주식 랭킹 조회",
  "description": "지정한 시장(`marketCountry`) · 기간(`duration`) · 기준(`type`)의 주식 랭킹을 조회합니다. 상위 100위까지 제공합니다.\n\n- `TOP_GAINERS` / `TOP_LOSERS` 는 `duration=realtime` 을 지원하지 않습니다 (400 `unsupported-ranking-duration`).\n- `tradingVolume` / `tradingAmount` 의 집계 기준은 `type` 이 결정합니다 — `TOSS_SECURITIES_*` 는 토스증권 체결 기준, 그 외(`MARKET_*` / `TOP_*`)는 시장 전체 기준.\n- `price.basePrice` 는 `TOP_GAINERS` / `TOP_LOSERS` 만 `duration` 시작 시점 기준가이며, 나머지 타입은 `duration` 과 무관하게 항상 전일 기준가입니다. `price.changeRate` 도 같은 의미를 따릅니다 (기간 등락률 vs 전일 대비 등락률).\n- 응답 항목 수는 `count` 보다 적을 수 있습니다 (시세 조회에 실패한 종목은 제외).\n- 랭킹이 집계되지 않은 조합은 에러가 아닌 빈 `rankings` 배열로 응답하며, 이때 `rankedAt` 은 null 입니다.\n\n**Rate Limits Group**: `RANKING`\n",
  "operationId": "getRankings",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "name": "type",
      "in": "query",
      "required": true,
      "description": "랭킹 종류. 이름에 포함된 지표가 랭킹 기준값입니다 — `*_TRADING_AMOUNT` → `tradingAmount`, `*_TRADING_VOLUME` → `tradingVolume`, `TOP_GAINERS` / `TOP_LOSERS` → `price.changeRate`.\n- `MARKET_TRADING_AMOUNT`: 시장 거래대금 상위\n- `MARKET_TRADING_VOLUME`: 시장 거래량 상위\n- `TOP_GAINERS`: 급상승 (등락률 상위) — `realtime` 미지원\n- `TOP_LOSERS`: 급하락 (등락률 하위) — `realtime` 미지원\n- `TOSS_SECURITIES_TRADING_AMOUNT`: 토스증권 거래대금 상위\n- `TOSS_SECURITIES_TRADING_VOLUME`: 토스증권 거래량 상위\n",
      "schema": {
        "type": "string",
        "enum": [
          "MARKET_TRADING_AMOUNT",
          "MARKET_TRADING_VOLUME",
          "TOP_GAINERS",
          "TOP_LOSERS",
          "TOSS_SECURITIES_TRADING_AMOUNT",
          "TOSS_SECURITIES_TRADING_VOLUME"
        ]
      }
    },
    {
      "name": "marketCountry",
      "in": "query",
      "required": true,
      "description": "조회 시장",
      "schema": {
        "$ref": "#/components/schemas/MarketCountry"
      }
    },
    {
      "name": "duration",
      "in": "query",
      "required": true,
      "description": "랭킹 산정 기간. 모든 기간은 거래일 기준입니다.\n- `realtime`: 실시간\n- `1d`: 1일\n- `1w`: 1주\n- `1mo`: 1개월\n- `3mo`: 3개월\n- `6mo`: 6개월\n- `1y`: 1년\n",
      "schema": {
        "type": "string",
        "enum": [
          "realtime",
          "1d",
          "1w",
          "1mo",
          "3mo",
          "6mo",
          "1y"
        ]
      }
    },
    {
      "name": "excludeInvestmentCaution",
      "in": "query",
      "required": false,
      "description": "투자 유의 종목 제외 여부",
      "schema": {
        "type": "boolean",
        "default": false
      }
    },
    {
      "name": "count",
      "in": "query",
      "required": false,
      "description": "조회 수 (최대 100). 응답 항목 수는 `count` 이하일 수 있습니다.",
      "schema": {
        "type": "integer",
        "default": 100,
        "minimum": 1,
        "maximum": 100
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
                    "$ref": "#/components/schemas/RankingResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "marketTradingAmount": {
              "summary": "시장 거래대금 상위 (KR / realtime)",
              "value": {
                "result": {
                  "rankedAt": "2026-06-10T14:30:00+09:00",
                  "rankings": [
                    {
                      "rank": 1,
                      "symbol": "005930",
                      "currency": "KRW",
                      "price": {
                        "lastPrice": "56500",
                        "basePrice": "55800",
                        "changeRate": "0.0125"
                      },
                      "tradingVolume": "18432100",
                      "tradingAmount": "1041436650000"
                    },
                    {
                      "rank": 2,
                      "symbol": "000660",
                      "currency": "KRW",
                      "price": {
                        "lastPrice": "192500",
                        "basePrice": "190000",
                        "changeRate": "0.0131"
                      },
                      "tradingVolume": "4821300",
                      "tradingAmount": "927910250000"
                    }
                  ]
                }
              }
            },
            "tossSecuritiesTradingVolume": {
              "summary": "토스증권 거래량 상위 (US / 1d) — trading* 값은 토스증권 체결 기준",
              "value": {
                "result": {
                  "rankedAt": "2026-06-10T14:30:00+09:00",
                  "rankings": [
                    {
                      "rank": 1,
                      "symbol": "NVDA",
                      "currency": "USD",
                      "price": {
                        "lastPrice": "131.38",
                        "basePrice": "128.45",
                        "changeRate": "0.0228"
                      },
                      "tradingVolume": "342100",
                      "tradingAmount": "44942580"
                    },
                    {
                      "rank": 2,
                      "symbol": "TSLA",
                      "currency": "USD",
                      "price": {
                        "lastPrice": "248.5",
                        "basePrice": "251.2",
                        "changeRate": "-0.0107"
                      },
                      "tradingVolume": "218500",
                      "tradingAmount": "54296250"
                    }
                  ]
                }
              }
            },
            "topGainers": {
              "summary": "급상승 (KR / 1w) — basePrice 가 1주 전 기준가, changeRate 가 기간 등락률",
              "value": {
                "result": {
                  "rankedAt": "2026-06-10T14:30:00+09:00",
                  "rankings": [
                    {
                      "rank": 1,
                      "symbol": "247540",
                      "currency": "KRW",
                      "price": {
                        "lastPrice": "87400",
                        "basePrice": "71200",
                        "changeRate": "0.2275"
                      },
                      "tradingVolume": "3241800",
                      "tradingAmount": "283333320000"
                    }
                  ]
                }
              }
            },
            "emptyRankings": {
              "summary": "집계 데이터 없음 (빈 배열, rankedAt null)",
              "value": {
                "result": {
                  "rankedAt": null,
                  "rankings": []
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
            "invalidType": {
              "summary": "지원하지 않는 type 값",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "요청이 올바르지 않습니다.",
                  "data": {
                    "field": "type",
                    "allowedValues": [
                      "MARKET_TRADING_AMOUNT",
                      "MARKET_TRADING_VOLUME",
                      "TOP_GAINERS",
                      "TOP_LOSERS",
                      "TOSS_SECURITIES_TRADING_AMOUNT",
                      "TOSS_SECURITIES_TRADING_VOLUME"
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
            },
            "unsupportedRankingDuration": {
              "summary": "지원하지 않는 랭킹 기간 (TOP_GAINERS / TOP_LOSERS + realtime)",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "unsupported-ranking-duration",
                  "message": "지원하지 않는 랭킹 기간입니다.",
                  "data": {
                    "field": "duration",
                    "allowedValues": [
                      "1d",
                      "1w",
                      "1mo",
                      "3mo",
                      "6mo",
                      "1y"
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
      "$ref": "#/components/responses/InternalErrorRanking"
    }
  }
}
````
