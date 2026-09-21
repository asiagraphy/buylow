> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/AssetApi.md
> 문서 버전: 1.2.17

# AssetApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHoldings**](ASSET.md#getHoldings) | **GET** /api/v1/holdings | 보유 주식 조회 |


<a name="getHoldings"></a>
# **getHoldings**
> getHoldings_200_response getHoldings(X-Tossinvest-Account, symbol)

보유 주식 조회

    보유 주식 정보를 조회합니다. 국내(KR)·미국(US) 주식만 포함하며, 해외 옵션·채권은 제외합니다. 보유 종목이 없으면 요약 금액은 0이고 items는 빈 배열입니다.  **Rate Limits Group**: `ASSET` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **X-Tossinvest-Account** | **Long**| API 요청 시 사용할 계좌의 accountSeq. `GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.  | [default to null] |
| **symbol** | **String**| 종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 티커 (예: AAPL). 영문 대/소문자, 숫자, '.', '-' 만 허용한다. 제공 시 해당 종목만 필터링하여 반환하며, 요약 필드도 해당 종목 기준으로 재계산합니다. 미제공 시 전체 보유 종목을 반환합니다.  | [optional] [default to null] |

### Return type

[**getHoldings_200_response**](MODEL_GET_HOLDINGS_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## GET /api/v1/holdings

### `/summary`

보유 주식 조회

### `/description`

보유 주식 정보를 조회합니다.
국내(KR)·미국(US) 주식만 포함하며, 해외 옵션·채권은 제외합니다.
보유 종목이 없으면 요약 금액은 0이고 items는 빈 배열입니다.

**Rate Limits Group**: `ASSET`


### `/parameters/1/description`

종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 티커 (예: AAPL).
영문 대/소문자, 숫자, '.', '-' 만 허용한다.
제공 시 해당 종목만 필터링하여 반환하며, 요약 필드도 해당 종목 기준으로 재계산합니다.
미제공 시 전체 보유 종목을 반환합니다.


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/withHoldings/summary`

보유 종목 있음 (KR + US 혼합)

### `/responses/200/content/application/json/examples/withHoldings/description`

krw에는 KRW로 거래되는 국내 종목의 합만, usd에는 USD로 거래되는 해외 종목의 합만 포함됩니다. rate는 SDK가 제공하는 전체 자산 원화 환산 기준 손익률입니다.

### `/responses/200/content/application/json/examples/filteredBySymbol/summary`

symbol 필터 적용 (005930)

### `/responses/200/content/application/json/examples/filteredByUsSymbol/summary`

symbol 필터 적용 (AAPL, 해외 종목)

### `/responses/200/content/application/json/examples/filteredByUsSymbol/description`

해외 종목만 필터된 결과의 krw는 0(국내 종목 없음), usd만 합산됩니다. rate는 단일 통화(USD) 기준으로 재계산합니다.

### `/responses/200/content/application/json/examples/filteredBySymbolNotFound/summary`

symbol 필터 적용 — 해당 종목 미보유

### `/responses/200/content/application/json/examples/emptyHoldings/summary`

보유 종목 없음

### 전체 연산 정의

````json
{
  "tags": [
    "Asset"
  ],
  "summary": "보유 주식 조회",
  "description": "보유 주식 정보를 조회합니다.\n국내(KR)·미국(US) 주식만 포함하며, 해외 옵션·채권은 제외합니다.\n보유 종목이 없으면 요약 금액은 0이고 items는 빈 배열입니다.\n\n**Rate Limits Group**: `ASSET`\n",
  "operationId": "getHoldings",
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
      "name": "symbol",
      "in": "query",
      "required": false,
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9.\\-]+$"
      },
      "description": "종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 티커 (예: AAPL).\n영문 대/소문자, 숫자, '.', '-' 만 허용한다.\n제공 시 해당 종목만 필터링하여 반환하며, 요약 필드도 해당 종목 기준으로 재계산합니다.\n미제공 시 전체 보유 종목을 반환합니다.\n",
      "example": "005930"
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
                    "$ref": "#/components/schemas/HoldingsOverview"
                  }
                }
              }
            ]
          },
          "examples": {
            "withHoldings": {
              "summary": "보유 종목 있음 (KR + US 혼합)",
              "description": "krw에는 KRW로 거래되는 국내 종목의 합만, usd에는 USD로 거래되는 해외 종목의 합만 포함됩니다. rate는 SDK가 제공하는 전체 자산 원화 환산 기준 손익률입니다.",
              "value": {
                "result": {
                  "totalPurchaseAmount": {
                    "krw": "6500000",
                    "usd": "1553"
                  },
                  "marketValue": {
                    "amount": {
                      "krw": "7200000",
                      "usd": "1785"
                    },
                    "amountAfterCost": {
                      "krw": "7050000",
                      "usd": "1771.43"
                    }
                  },
                  "profitLoss": {
                    "amount": {
                      "krw": "700000",
                      "usd": "232"
                    },
                    "amountAfterCost": {
                      "krw": "550000",
                      "usd": "218.43"
                    },
                    "rate": "0.1179",
                    "rateAfterCost": "0.0983"
                  },
                  "dailyProfitLoss": {
                    "amount": {
                      "krw": "100000",
                      "usd": "25"
                    },
                    "rate": "0.0141"
                  },
                  "items": [
                    {
                      "symbol": "005930",
                      "name": "삼성전자",
                      "marketCountry": "KR",
                      "currency": "KRW",
                      "quantity": "100",
                      "lastPrice": "72000",
                      "averagePurchasePrice": "65000",
                      "marketValue": {
                        "purchaseAmount": "6500000",
                        "amount": "7200000",
                        "amountAfterCost": "7050000"
                      },
                      "profitLoss": {
                        "amount": "700000",
                        "amountAfterCost": "550000",
                        "rate": "0.1077",
                        "rateAfterCost": "0.0846"
                      },
                      "dailyProfitLoss": {
                        "amount": "100000",
                        "rate": "0.0141"
                      },
                      "cost": {
                        "commission": "14400",
                        "tax": "135600"
                      }
                    },
                    {
                      "symbol": "AAPL",
                      "name": "Apple Inc.",
                      "marketCountry": "US",
                      "currency": "USD",
                      "quantity": "10",
                      "lastPrice": "178.5",
                      "averagePurchasePrice": "155.3",
                      "marketValue": {
                        "purchaseAmount": "1553",
                        "amount": "1785",
                        "amountAfterCost": "1771.43"
                      },
                      "profitLoss": {
                        "amount": "232",
                        "amountAfterCost": "218.43",
                        "rate": "0.1494",
                        "rateAfterCost": "0.1406"
                      },
                      "dailyProfitLoss": {
                        "amount": "25",
                        "rate": "0.0142"
                      },
                      "cost": {
                        "commission": "3.57",
                        "tax": "10"
                      }
                    }
                  ]
                }
              }
            },
            "filteredBySymbol": {
              "summary": "symbol 필터 적용 (005930)",
              "value": {
                "result": {
                  "totalPurchaseAmount": {
                    "krw": "6500000",
                    "usd": null
                  },
                  "marketValue": {
                    "amount": {
                      "krw": "7200000",
                      "usd": null
                    },
                    "amountAfterCost": {
                      "krw": "7050000",
                      "usd": null
                    }
                  },
                  "profitLoss": {
                    "amount": {
                      "krw": "700000",
                      "usd": null
                    },
                    "amountAfterCost": {
                      "krw": "550000",
                      "usd": null
                    },
                    "rate": "0.1077",
                    "rateAfterCost": "0.0846"
                  },
                  "dailyProfitLoss": {
                    "amount": {
                      "krw": "100000",
                      "usd": null
                    },
                    "rate": "0.0141"
                  },
                  "items": [
                    {
                      "symbol": "005930",
                      "name": "삼성전자",
                      "marketCountry": "KR",
                      "currency": "KRW",
                      "quantity": "100",
                      "lastPrice": "72000",
                      "averagePurchasePrice": "65000",
                      "marketValue": {
                        "purchaseAmount": "6500000",
                        "amount": "7200000",
                        "amountAfterCost": "7050000"
                      },
                      "profitLoss": {
                        "amount": "700000",
                        "amountAfterCost": "550000",
                        "rate": "0.1077",
                        "rateAfterCost": "0.0846"
                      },
                      "dailyProfitLoss": {
                        "amount": "100000",
                        "rate": "0.0141"
                      },
                      "cost": {
                        "commission": "14400",
                        "tax": "135600"
                      }
                    }
                  ]
                }
              }
            },
            "filteredByUsSymbol": {
              "summary": "symbol 필터 적용 (AAPL, 해외 종목)",
              "description": "해외 종목만 필터된 결과의 krw는 0(국내 종목 없음), usd만 합산됩니다. rate는 단일 통화(USD) 기준으로 재계산합니다.",
              "value": {
                "result": {
                  "totalPurchaseAmount": {
                    "krw": "0",
                    "usd": "1500.00"
                  },
                  "marketValue": {
                    "amount": {
                      "krw": "0",
                      "usd": "1700.00"
                    },
                    "amountAfterCost": {
                      "krw": "0",
                      "usd": "1650.00"
                    }
                  },
                  "profitLoss": {
                    "amount": {
                      "krw": "0",
                      "usd": "200.00"
                    },
                    "amountAfterCost": {
                      "krw": "0",
                      "usd": "150.00"
                    },
                    "rate": "0.1333",
                    "rateAfterCost": "0.1000"
                  },
                  "dailyProfitLoss": {
                    "amount": {
                      "krw": "0",
                      "usd": "20.00"
                    },
                    "rate": "0.0119"
                  },
                  "items": [
                    {
                      "symbol": "AAPL",
                      "name": "Apple Inc.",
                      "marketCountry": "US",
                      "currency": "USD",
                      "quantity": "10",
                      "lastPrice": "170.00",
                      "averagePurchasePrice": "150.00",
                      "marketValue": {
                        "purchaseAmount": "1500.00",
                        "amount": "1700.00",
                        "amountAfterCost": "1650.00"
                      },
                      "profitLoss": {
                        "amount": "200.00",
                        "amountAfterCost": "150.00",
                        "rate": "0.1333",
                        "rateAfterCost": "0.10"
                      },
                      "dailyProfitLoss": {
                        "amount": "20.00",
                        "rate": "0.012"
                      },
                      "cost": {
                        "commission": "2.15",
                        "tax": null
                      }
                    }
                  ]
                }
              }
            },
            "filteredBySymbolNotFound": {
              "summary": "symbol 필터 적용 — 해당 종목 미보유",
              "value": {
                "result": {
                  "totalPurchaseAmount": {
                    "krw": "0",
                    "usd": null
                  },
                  "marketValue": {
                    "amount": {
                      "krw": "0",
                      "usd": null
                    },
                    "amountAfterCost": {
                      "krw": "0",
                      "usd": null
                    }
                  },
                  "profitLoss": {
                    "amount": {
                      "krw": "0",
                      "usd": null
                    },
                    "amountAfterCost": {
                      "krw": "0",
                      "usd": null
                    },
                    "rate": "0",
                    "rateAfterCost": "0"
                  },
                  "dailyProfitLoss": {
                    "amount": {
                      "krw": "0",
                      "usd": null
                    },
                    "rate": "0"
                  },
                  "items": []
                }
              }
            },
            "emptyHoldings": {
              "summary": "보유 종목 없음",
              "value": {
                "result": {
                  "totalPurchaseAmount": {
                    "krw": "0",
                    "usd": null
                  },
                  "marketValue": {
                    "amount": {
                      "krw": "0",
                      "usd": null
                    },
                    "amountAfterCost": {
                      "krw": "0",
                      "usd": null
                    }
                  },
                  "profitLoss": {
                    "amount": {
                      "krw": "0",
                      "usd": null
                    },
                    "amountAfterCost": {
                      "krw": "0",
                      "usd": null
                    },
                    "rate": "0",
                    "rateAfterCost": "0"
                  },
                  "dailyProfitLoss": {
                    "amount": {
                      "krw": "0",
                      "usd": null
                    },
                    "rate": "0"
                  },
                  "items": []
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
      "$ref": "#/components/responses/NotFound"
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    },
    "500": {
      "$ref": "#/components/responses/InternalErrorAsset"
    }
  }
}
````
