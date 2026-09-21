> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/MarketInfoApi.md
> 문서 버전: 1.2.17

# MarketInfoApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getExchangeRate**](MARKET_INFO.md#getExchangeRate) | **GET** /api/v1/exchange-rate | 환율 조회 |
| [**getKrMarketCalendar**](MARKET_INFO.md#getKrMarketCalendar) | **GET** /api/v1/market-calendar/KR | 국내 장 운영 정보 조회 |
| [**getUsMarketCalendar**](MARKET_INFO.md#getUsMarketCalendar) | **GET** /api/v1/market-calendar/US | 해외 장 운영 정보 조회 |


<a name="getExchangeRate"></a>
# **getExchangeRate**
> getExchangeRate_200_response getExchangeRate(baseCurrency, quoteCurrency, dateTime)

환율 조회

    KRW ↔ USD 환율 정보를 조회합니다.  - **갱신 주기 1분**, 참고용 표시 환율. 실제 주문 시 적용되는 거래 환율과 다를 수 있습니다. - `dateTime` 미지정 시 **현재 시점의 유효 환율**이 응답됩니다. - 응답의 `validFrom` ~ `validUntil` 은 해당 환율의 **유효 시간 윈도** (보통 1분) 입니다.  **Rate Limits Group**: `MARKET_INFO` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **baseCurrency** | [**Currency**](MODEL_CURRENCY.md)| 기준 통화 | [default to null] [enum: KRW, USD] |
| **quoteCurrency** | [**Currency**](MODEL_CURRENCY.md)| 표시 통화 (quote currency) | [default to null] [enum: KRW, USD] |
| **dateTime** | **Date**| 조회할 환율 시각. 특정 시점의 환율을 조회할 수 있습니다. | [optional] [default to null] |

### Return type

[**getExchangeRate_200_response**](MODEL_GET_EXCHANGE_RATE_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getKrMarketCalendar"></a>
# **getKrMarketCalendar**
> getKrMarketCalendar_200_response getKrMarketCalendar(date)

국내 장 운영 정보 조회

    국내 시장의 거래 가능 시간을 조회합니다. 통합 모드 (KRX+NXT) 기준이며, 장전/장후 시간외종가는 제외됩니다. 전일/당일/익일 3영업일 정보를 반환합니다. 모든 시간은 KST(+09:00) 기준.  **Rate Limits Group**: `MARKET_INFO` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **date** | **date**| 조회 기준일 (YYYY-MM-DD) | [optional] [default to null] |

### Return type

[**getKrMarketCalendar_200_response**](MODEL_GET_KR_MARKET_CALENDAR_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getUsMarketCalendar"></a>
# **getUsMarketCalendar**
> getUsMarketCalendar_200_response getUsMarketCalendar(date)

해외 장 운영 정보 조회

    미국 시장의 장 운영 시간을 조회합니다. 4 세션(`dayMarket`, `preMarket`, `regularMarket`, `afterMarket`) 별로 nullable. 휴장 시 4 세션 모두 null. 전일/당일/익일 3영업일 정보를 반환합니다. 모든 시간은 KST(+09:00) 기준.  **Rate Limits Group**: `MARKET_INFO` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **date** | **date**| 조회 기준일 (YYYY-MM-DD, 미국 현지 날짜) | [optional] [default to null] |

### Return type

[**getUsMarketCalendar_200_response**](MODEL_GET_US_MARKET_CALENDAR_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## GET /api/v1/exchange-rate

### `/summary`

환율 조회

### `/description`

KRW ↔ USD 환율 정보를 조회합니다.

- **갱신 주기 1분**, 참고용 표시 환율. 실제 주문 시 적용되는 거래 환율과 다를 수 있습니다.
- `dateTime` 미지정 시 **현재 시점의 유효 환율**이 응답됩니다.
- 응답의 `validFrom` ~ `validUntil` 은 해당 환율의 **유효 시간 윈도** (보통 1분) 입니다.

**Rate Limits Group**: `MARKET_INFO`


### `/parameters/0/description`

조회할 환율 시각. 특정 시점의 환율을 조회할 수 있습니다.

### `/parameters/1/description`

기준 통화

### `/parameters/2/description`

표시 통화 (quote currency)

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/usdToKrwUp/summary`

USD→KRW 환율 (상승)

### `/responses/200/content/application/json/examples/usdToKrwDown/summary`

USD→KRW 환율 (하락)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedCurrency/summary`

지원하지 않는 통화

### `/responses/400/content/application/json/examples/sameCurrency/summary`

기준 통화와 상대 통화가 같음

### `/responses/404/description`

환율 정보 없음

### `/responses/404/content/application/json/examples/exchangeRateNotFound/summary`

요청한 시점의 환율 정보 없음

### 전체 연산 정의

````json
{
  "tags": [
    "Market Info"
  ],
  "summary": "환율 조회",
  "description": "KRW ↔ USD 환율 정보를 조회합니다.\n\n- **갱신 주기 1분**, 참고용 표시 환율. 실제 주문 시 적용되는 거래 환율과 다를 수 있습니다.\n- `dateTime` 미지정 시 **현재 시점의 유효 환율**이 응답됩니다.\n- 응답의 `validFrom` ~ `validUntil` 은 해당 환율의 **유효 시간 윈도** (보통 1분) 입니다.\n\n**Rate Limits Group**: `MARKET_INFO`\n",
  "operationId": "getExchangeRate",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "name": "dateTime",
      "in": "query",
      "required": false,
      "description": "조회할 환율 시각. 특정 시점의 환율을 조회할 수 있습니다.",
      "schema": {
        "type": "string",
        "format": "date-time"
      },
      "example": "2026-03-25T09:30:00+09:00"
    },
    {
      "name": "baseCurrency",
      "in": "query",
      "required": true,
      "description": "기준 통화",
      "schema": {
        "$ref": "#/components/schemas/Currency"
      },
      "example": "USD"
    },
    {
      "name": "quoteCurrency",
      "in": "query",
      "required": true,
      "description": "표시 통화 (quote currency)",
      "schema": {
        "$ref": "#/components/schemas/Currency"
      },
      "example": "KRW"
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
                    "$ref": "#/components/schemas/ExchangeRateResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "usdToKrwUp": {
              "summary": "USD→KRW 환율 (상승)",
              "value": {
                "result": {
                  "baseCurrency": "USD",
                  "quoteCurrency": "KRW",
                  "rate": "1380.5",
                  "midRate": "1375",
                  "basisPoint": "40",
                  "rateChangeType": "UP",
                  "validFrom": "2026-03-25T09:30:00+09:00",
                  "validUntil": "2026-03-25T09:31:00+09:00"
                }
              }
            },
            "usdToKrwDown": {
              "summary": "USD→KRW 환율 (하락)",
              "value": {
                "result": {
                  "baseCurrency": "USD",
                  "quoteCurrency": "KRW",
                  "rate": "1372.3",
                  "midRate": "1375",
                  "basisPoint": "-19.6",
                  "rateChangeType": "DOWN",
                  "validFrom": "2026-03-25T09:30:00+09:00",
                  "validUntil": "2026-03-25T09:31:00+09:00"
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
                    "field": "baseCurrency",
                    "allowedValues": [
                      "KRW",
                      "USD"
                    ]
                  }
                }
              }
            },
            "sameCurrency": {
              "summary": "기준 통화와 상대 통화가 같음",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-request",
                  "message": "기준 통화와 상대 통화가 같을 수 없습니다.",
                  "data": {
                    "field": "baseCurrency,quoteCurrency"
                  }
                }
              }
            }
          }
        }
      }
    },
    "404": {
      "description": "환율 정보 없음",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "exchangeRateNotFound": {
              "summary": "요청한 시점의 환율 정보 없음",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "exchange-rate-not-found",
                  "message": "요청한 시점의 환율 정보가 없습니다."
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
      "$ref": "#/components/responses/InternalErrorMarketInfo"
    }
  }
}
````

## GET /api/v1/market-calendar/KR

### `/summary`

국내 장 운영 정보 조회

### `/description`

국내 시장의 거래 가능 시간을 조회합니다. 통합 모드 (KRX+NXT) 기준이며, 장전/장후 시간외종가는 제외됩니다. 전일/당일/익일 3영업일 정보를 반환합니다. 모든 시간은 KST(+09:00) 기준.

**Rate Limits Group**: `MARKET_INFO`


### `/parameters/0/description`

조회 기준일 (YYYY-MM-DD)

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/businessDay/summary`

영업일 (KRX+NXT 정상 운영)

### `/responses/200/content/application/json/examples/holidayToday/summary`

휴장일 (today 만 휴장, integrated null)

### `/responses/200/content/application/json/examples/nxtPreMarketHoliday/summary`

부분 휴장 (NXT 프리마켓만 휴장, 정규장·애프터마켓은 운영)

### `/responses/400/description`

잘못된 요청

### `/responses/400/content/application/json/examples/unsupportedDate/summary`

지원하지 않는 조회 일자

### 전체 연산 정의

````json
{
  "tags": [
    "Market Info"
  ],
  "summary": "국내 장 운영 정보 조회",
  "description": "국내 시장의 거래 가능 시간을 조회합니다. 통합 모드 (KRX+NXT) 기준이며, 장전/장후 시간외종가는 제외됩니다. 전일/당일/익일 3영업일 정보를 반환합니다. 모든 시간은 KST(+09:00) 기준.\n\n**Rate Limits Group**: `MARKET_INFO`\n",
  "operationId": "getKrMarketCalendar",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "name": "date",
      "in": "query",
      "required": false,
      "description": "조회 기준일 (YYYY-MM-DD)",
      "schema": {
        "type": "string",
        "format": "date"
      },
      "example": "2026-03-25"
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
                    "$ref": "#/components/schemas/KrMarketCalendarResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "businessDay": {
              "summary": "영업일 (KRX+NXT 정상 운영)",
              "value": {
                "result": {
                  "today": {
                    "date": "2026-03-25",
                    "integrated": {
                      "preMarket": {
                        "startTime": "2026-03-25T08:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-25T08:50:00+09:00",
                        "endTime": "2026-03-25T09:00:00+09:00"
                      },
                      "regularMarket": {
                        "startTime": "2026-03-25T09:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-25T15:20:00+09:00",
                        "endTime": "2026-03-25T15:30:00+09:00"
                      },
                      "afterMarket": {
                        "startTime": "2026-03-25T15:30:00+09:00",
                        "singlePriceAuctionEndTime": "2026-03-25T15:40:00+09:00",
                        "endTime": "2026-03-25T20:00:00+09:00"
                      }
                    }
                  },
                  "previousBusinessDay": {
                    "date": "2026-03-24",
                    "integrated": {
                      "preMarket": {
                        "startTime": "2026-03-24T08:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-24T08:50:00+09:00",
                        "endTime": "2026-03-24T09:00:00+09:00"
                      },
                      "regularMarket": {
                        "startTime": "2026-03-24T09:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-24T15:20:00+09:00",
                        "endTime": "2026-03-24T15:30:00+09:00"
                      },
                      "afterMarket": {
                        "startTime": "2026-03-24T15:30:00+09:00",
                        "singlePriceAuctionEndTime": "2026-03-24T15:40:00+09:00",
                        "endTime": "2026-03-24T20:00:00+09:00"
                      }
                    }
                  },
                  "nextBusinessDay": {
                    "date": "2026-03-26",
                    "integrated": {
                      "preMarket": {
                        "startTime": "2026-03-26T08:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-26T08:50:00+09:00",
                        "endTime": "2026-03-26T09:00:00+09:00"
                      },
                      "regularMarket": {
                        "startTime": "2026-03-26T09:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-26T15:20:00+09:00",
                        "endTime": "2026-03-26T15:30:00+09:00"
                      },
                      "afterMarket": {
                        "startTime": "2026-03-26T15:30:00+09:00",
                        "singlePriceAuctionEndTime": "2026-03-26T15:40:00+09:00",
                        "endTime": "2026-03-26T20:00:00+09:00"
                      }
                    }
                  }
                }
              }
            },
            "holidayToday": {
              "summary": "휴장일 (today 만 휴장, integrated null)",
              "value": {
                "result": {
                  "today": {
                    "date": "2026-05-05",
                    "integrated": null
                  },
                  "previousBusinessDay": {
                    "date": "2026-05-04",
                    "integrated": {
                      "preMarket": {
                        "startTime": "2026-05-04T08:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-05-04T08:50:00+09:00",
                        "endTime": "2026-05-04T09:00:00+09:00"
                      },
                      "regularMarket": {
                        "startTime": "2026-05-04T09:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-05-04T15:20:00+09:00",
                        "endTime": "2026-05-04T15:30:00+09:00"
                      },
                      "afterMarket": {
                        "startTime": "2026-05-04T15:30:00+09:00",
                        "singlePriceAuctionEndTime": "2026-05-04T15:40:00+09:00",
                        "endTime": "2026-05-04T20:00:00+09:00"
                      }
                    }
                  },
                  "nextBusinessDay": {
                    "date": "2026-05-06",
                    "integrated": {
                      "preMarket": {
                        "startTime": "2026-05-06T08:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-05-06T08:50:00+09:00",
                        "endTime": "2026-05-06T09:00:00+09:00"
                      },
                      "regularMarket": {
                        "startTime": "2026-05-06T09:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-05-06T15:20:00+09:00",
                        "endTime": "2026-05-06T15:30:00+09:00"
                      },
                      "afterMarket": {
                        "startTime": "2026-05-06T15:30:00+09:00",
                        "singlePriceAuctionEndTime": "2026-05-06T15:40:00+09:00",
                        "endTime": "2026-05-06T20:00:00+09:00"
                      }
                    }
                  }
                }
              }
            },
            "nxtPreMarketHoliday": {
              "summary": "부분 휴장 (NXT 프리마켓만 휴장, 정규장·애프터마켓은 운영)",
              "value": {
                "result": {
                  "today": {
                    "date": "2026-03-25",
                    "integrated": {
                      "preMarket": null,
                      "regularMarket": {
                        "startTime": "2026-03-25T09:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-25T15:20:00+09:00",
                        "endTime": "2026-03-25T15:30:00+09:00"
                      },
                      "afterMarket": {
                        "startTime": "2026-03-25T15:30:00+09:00",
                        "singlePriceAuctionEndTime": "2026-03-25T15:40:00+09:00",
                        "endTime": "2026-03-25T20:00:00+09:00"
                      }
                    }
                  },
                  "previousBusinessDay": {
                    "date": "2026-03-24",
                    "integrated": {
                      "preMarket": {
                        "startTime": "2026-03-24T08:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-24T08:50:00+09:00",
                        "endTime": "2026-03-24T09:00:00+09:00"
                      },
                      "regularMarket": {
                        "startTime": "2026-03-24T09:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-24T15:20:00+09:00",
                        "endTime": "2026-03-24T15:30:00+09:00"
                      },
                      "afterMarket": {
                        "startTime": "2026-03-24T15:30:00+09:00",
                        "singlePriceAuctionEndTime": "2026-03-24T15:40:00+09:00",
                        "endTime": "2026-03-24T20:00:00+09:00"
                      }
                    }
                  },
                  "nextBusinessDay": {
                    "date": "2026-03-26",
                    "integrated": {
                      "preMarket": {
                        "startTime": "2026-03-26T08:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-26T08:50:00+09:00",
                        "endTime": "2026-03-26T09:00:00+09:00"
                      },
                      "regularMarket": {
                        "startTime": "2026-03-26T09:00:00+09:00",
                        "singlePriceAuctionStartTime": "2026-03-26T15:20:00+09:00",
                        "endTime": "2026-03-26T15:30:00+09:00"
                      },
                      "afterMarket": {
                        "startTime": "2026-03-26T15:30:00+09:00",
                        "singlePriceAuctionEndTime": "2026-03-26T15:40:00+09:00",
                        "endTime": "2026-03-26T20:00:00+09:00"
                      }
                    }
                  }
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
            "unsupportedDate": {
              "summary": "지원하지 않는 조회 일자",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "unsupported-date",
                  "message": "요청한 조회 일자를 지원하지 않습니다.",
                  "data": {
                    "field": "date"
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
      "$ref": "#/components/responses/InternalErrorMarketInfo"
    }
  }
}
````

## GET /api/v1/market-calendar/US

### `/summary`

해외 장 운영 정보 조회

### `/description`

미국 시장의 장 운영 시간을 조회합니다. 4 세션(`dayMarket`, `preMarket`, `regularMarket`, `afterMarket`) 별로 nullable. 휴장 시 4 세션 모두 null. 전일/당일/익일 3영업일 정보를 반환합니다. 모든 시간은 KST(+09:00) 기준.

**Rate Limits Group**: `MARKET_INFO`


### `/parameters/0/description`

조회 기준일 (YYYY-MM-DD, 미국 현지 날짜)

### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/businessDay/summary`

영업일 (데이마켓 포함, 4 세션 nested)

### `/responses/200/content/application/json/examples/holidayToday/summary`

휴장일 (today 만 휴장, 4 세션 모두 null)

### 전체 연산 정의

````json
{
  "tags": [
    "Market Info"
  ],
  "summary": "해외 장 운영 정보 조회",
  "description": "미국 시장의 장 운영 시간을 조회합니다. 4 세션(`dayMarket`, `preMarket`, `regularMarket`, `afterMarket`) 별로 nullable. 휴장 시 4 세션 모두 null. 전일/당일/익일 3영업일 정보를 반환합니다. 모든 시간은 KST(+09:00) 기준.\n\n**Rate Limits Group**: `MARKET_INFO`\n",
  "operationId": "getUsMarketCalendar",
  "security": [
    {
      "oauth2ClientCredentials": []
    }
  ],
  "parameters": [
    {
      "name": "date",
      "in": "query",
      "required": false,
      "description": "조회 기준일 (YYYY-MM-DD, 미국 현지 날짜)",
      "schema": {
        "type": "string",
        "format": "date"
      },
      "example": "2026-03-25"
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
                    "$ref": "#/components/schemas/UsMarketCalendarResponse"
                  }
                }
              }
            ]
          },
          "examples": {
            "businessDay": {
              "summary": "영업일 (데이마켓 포함, 4 세션 nested)",
              "value": {
                "result": {
                  "today": {
                    "date": "2026-03-25",
                    "dayMarket": {
                      "startTime": "2026-03-25T09:00:00+09:00",
                      "endTime": "2026-03-25T16:50:00+09:00"
                    },
                    "preMarket": {
                      "startTime": "2026-03-25T17:00:00+09:00",
                      "endTime": "2026-03-25T22:30:00+09:00"
                    },
                    "regularMarket": {
                      "startTime": "2026-03-25T22:30:00+09:00",
                      "endTime": "2026-03-26T05:00:00+09:00"
                    },
                    "afterMarket": {
                      "startTime": "2026-03-26T05:00:00+09:00",
                      "endTime": "2026-03-26T07:00:00+09:00"
                    }
                  },
                  "previousBusinessDay": {
                    "date": "2026-03-24",
                    "dayMarket": {
                      "startTime": "2026-03-24T09:00:00+09:00",
                      "endTime": "2026-03-24T16:50:00+09:00"
                    },
                    "preMarket": {
                      "startTime": "2026-03-24T17:00:00+09:00",
                      "endTime": "2026-03-24T22:30:00+09:00"
                    },
                    "regularMarket": {
                      "startTime": "2026-03-24T22:30:00+09:00",
                      "endTime": "2026-03-25T05:00:00+09:00"
                    },
                    "afterMarket": {
                      "startTime": "2026-03-25T05:00:00+09:00",
                      "endTime": "2026-03-25T07:00:00+09:00"
                    }
                  },
                  "nextBusinessDay": {
                    "date": "2026-03-26",
                    "dayMarket": {
                      "startTime": "2026-03-26T09:00:00+09:00",
                      "endTime": "2026-03-26T16:50:00+09:00"
                    },
                    "preMarket": {
                      "startTime": "2026-03-26T17:00:00+09:00",
                      "endTime": "2026-03-26T22:30:00+09:00"
                    },
                    "regularMarket": {
                      "startTime": "2026-03-26T22:30:00+09:00",
                      "endTime": "2026-03-27T05:00:00+09:00"
                    },
                    "afterMarket": {
                      "startTime": "2026-03-27T05:00:00+09:00",
                      "endTime": "2026-03-27T07:00:00+09:00"
                    }
                  }
                }
              }
            },
            "holidayToday": {
              "summary": "휴장일 (today 만 휴장, 4 세션 모두 null)",
              "value": {
                "result": {
                  "today": {
                    "date": "2026-07-03",
                    "dayMarket": null,
                    "preMarket": null,
                    "regularMarket": null,
                    "afterMarket": null
                  },
                  "previousBusinessDay": {
                    "date": "2026-07-02",
                    "dayMarket": {
                      "startTime": "2026-07-02T09:00:00+09:00",
                      "endTime": "2026-07-02T16:50:00+09:00"
                    },
                    "preMarket": {
                      "startTime": "2026-07-02T17:00:00+09:00",
                      "endTime": "2026-07-02T22:30:00+09:00"
                    },
                    "regularMarket": {
                      "startTime": "2026-07-02T22:30:00+09:00",
                      "endTime": "2026-07-03T05:00:00+09:00"
                    },
                    "afterMarket": {
                      "startTime": "2026-07-03T05:00:00+09:00",
                      "endTime": "2026-07-03T07:00:00+09:00"
                    }
                  },
                  "nextBusinessDay": {
                    "date": "2026-07-06",
                    "dayMarket": {
                      "startTime": "2026-07-06T09:00:00+09:00",
                      "endTime": "2026-07-06T16:50:00+09:00"
                    },
                    "preMarket": {
                      "startTime": "2026-07-06T17:00:00+09:00",
                      "endTime": "2026-07-06T22:30:00+09:00"
                    },
                    "regularMarket": {
                      "startTime": "2026-07-06T22:30:00+09:00",
                      "endTime": "2026-07-07T05:00:00+09:00"
                    },
                    "afterMarket": {
                      "startTime": "2026-07-07T05:00:00+09:00",
                      "endTime": "2026-07-07T07:00:00+09:00"
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
      "$ref": "#/components/responses/InternalErrorMarketInfo"
    }
  }
}
````
