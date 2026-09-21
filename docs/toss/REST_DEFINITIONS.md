> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/openapi.json#/components
> 문서 버전: 1.2.17

# REST 공통 정의


````json
{
  "securitySchemes": {
    "oauth2ClientCredentials": {
      "type": "oauth2",
      "description": "OAuth 2.0 Client Credentials Grant. `POST /oauth2/token` 으로 발급받은 access token 을\n모든 요청의 `Authorization: Bearer {access_token}` 헤더로 전달합니다.\n",
      "flows": {
        "clientCredentials": {
          "tokenUrl": "/oauth2/token",
          "scopes": {}
        }
      }
    }
  },
  "headers": {
    "XRequestId": {
      "description": "요청 식별자. 모든 응답(성공·실패) 에 포함되며, 본문 `error.requestId` 와 동일한 값입니다.\nCS 문의 시 첨부를 권장합니다.\n",
      "schema": {
        "type": "string"
      },
      "example": "01HXYZABCDEFG123456789"
    },
    "WWWAuthenticate": {
      "description": "OAuth 2.0 Bearer 토큰 챌린지.\n401 응답에 포함됩니다. 메시지에 non-ASCII 문자가 포함되는 경우 `error_description` 파라미터는 생략됩니다.\n",
      "schema": {
        "type": "string"
      },
      "example": "Bearer realm=\"openapi\", error=\"invalid_token\", error_description=\"Token has expired\""
    }
  },
  "parameters": {
    "Symbol": {
      "name": "symbol",
      "in": "path",
      "required": true,
      "description": "종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL). 영문 대/소문자, 숫자, '.', '-' 만 허용한다.",
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9.\\-]+$"
      },
      "examples": {
        "krx": {
          "summary": "삼성전자",
          "value": "005930"
        },
        "us": {
          "summary": "Apple",
          "value": "AAPL"
        }
      }
    },
    "SymbolQuery": {
      "name": "symbol",
      "in": "query",
      "required": true,
      "description": "종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL). 영문 대/소문자, 숫자, '.', '-' 만 허용한다.",
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9.\\-]+$"
      },
      "examples": {
        "krx": {
          "summary": "삼성전자",
          "value": "005930"
        },
        "us": {
          "summary": "Apple",
          "value": "AAPL"
        }
      }
    },
    "AccountSeq": {
      "name": "X-Tossinvest-Account",
      "in": "header",
      "required": true,
      "description": "API 요청 시 사용할 계좌의 accountSeq.\n`GET /api/v1/accounts` 응답의 `accountSeq` 값을 사용합니다.\n",
      "schema": {
        "type": "integer",
        "format": "int64"
      },
      "example": 1
    },
    "OrderId": {
      "name": "orderId",
      "in": "path",
      "required": true,
      "description": "주문 식별자.\n서버에서 발급한 opaque token 입니다.\n",
      "schema": {
        "type": "string"
      },
      "example": "0d5QIHjmtksbsmM-hBRAgP-ExI8iodGm9fAR5txelPfnMM8XQ_swoJdwL5RpGWMo"
    },
    "KrSymbol": {
      "name": "symbol",
      "in": "path",
      "required": true,
      "description": "국내(KR) 종목 심볼. KRX 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0).",
      "schema": {
        "type": "string",
        "pattern": "^[A-Za-z0-9.\\-]+$"
      },
      "examples": {
        "krx": {
          "summary": "삼성전자",
          "value": "005930"
        }
      }
    }
  },
  "responses": {
    "Unauthorized": {
      "description": "인증 실패. `WWW-Authenticate: Bearer ...` 헤더가 함께 내려갑니다.\n",
      "headers": {
        "WWW-Authenticate": {
          "description": "OAuth 2.0 Bearer 토큰 챌린지. 메시지에 non-ASCII 문자가 포함되는 경우\n`error_description` 파라미터는 생략됩니다.\n",
          "schema": {
            "type": "string"
          },
          "example": "Bearer realm=\"openapi\", error=\"invalid_token\", error_description=\"Token has expired\""
        }
      },
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "examples": {
            "invalidToken": {
              "summary": "유효하지 않은 토큰",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "invalid-token",
                  "message": "유효하지 않은 토큰입니다."
                }
              }
            },
            "expiredToken": {
              "summary": "만료된 토큰",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "expired-token",
                  "message": "토큰이 만료되었습니다."
                }
              }
            },
            "tokenRevoked": {
              "summary": "재발급으로 무효화된 토큰",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "token-revoked",
                  "message": "새로 발급된 토큰으로 대체되어 더 이상 유효하지 않은 토큰입니다. 최신 토큰으로 다시 시도해 주세요."
                }
              }
            },
            "loginUserNotFound": {
              "summary": "로그인 정보 없음",
              "value": {
                "error": {
                  "requestId": "01HXYZABCDEFG123456789",
                  "code": "login-user-not-found",
                  "message": "로그인 정보를 찾을 수 없습니다."
                }
              }
            }
          }
        }
      }
    },
    "Forbidden": {
      "description": "권한 부족",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "forbidden",
              "message": "요청에 필요한 권한이 부족합니다."
            }
          }
        }
      }
    },
    "NotFound": {
      "description": "종목을 찾을 수 없음",
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
    "RateLimitExceeded": {
      "description": "요청 한도 초과. 포함 헤더의 의미는 아래 `headers` 정의를 참조합니다.",
      "headers": {
        "X-RateLimit-Limit": {
          "description": "현재 허용된 초당 요청 수 (burst capacity)",
          "schema": {
            "type": "integer"
          },
          "example": 10
        },
        "X-RateLimit-Remaining": {
          "description": "현재 버킷에 남은 토큰 수. 429 시 0.",
          "schema": {
            "type": "integer"
          },
          "example": 0
        },
        "X-RateLimit-Reset": {
          "description": "토큰 1 개가 재충전될 때까지 예상 초",
          "schema": {
            "type": "integer"
          },
          "example": 1
        },
        "Retry-After": {
          "description": "재시도 권장 초",
          "schema": {
            "type": "integer"
          },
          "example": 1
        }
      },
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "rate-limit-exceeded",
              "message": "요청 한도를 초과했습니다. 잠시 후 다시 시도해 주세요."
            }
          }
        }
      }
    },
    "ServiceUnavailable": {
      "description": "서비스 일시 불가",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "internal-error",
              "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
            }
          }
        }
      }
    },
    "OrderNotFound": {
      "description": "주문을 찾을 수 없음",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "order-not-found",
              "message": "주문을 찾을 수 없습니다."
            }
          }
        }
      }
    },
    "OrderInfoAccountNotFound": {
      "description": "조회 가능한 계좌가 없음",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "account-not-found",
              "message": "계좌를 찾을 수 없습니다."
            }
          }
        }
      }
    },
    "InternalErrorMarketData": {
      "description": "시세 조회 중 일시적 오류",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "internal-error",
              "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
            }
          }
        }
      }
    },
    "InternalErrorMarketInfo": {
      "description": "시장 정보 조회 중 일시적 오류",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "internal-error",
              "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
            }
          }
        }
      }
    },
    "InternalErrorOrderInfo": {
      "description": "거래 가능 정보 조회 중 일시적 오류",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "internal-error",
              "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
            }
          }
        }
      }
    },
    "InternalErrorAsset": {
      "description": "보유 자산 조회 중 일시적 오류",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "internal-error",
              "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
            }
          }
        }
      }
    },
    "InternalErrorStock": {
      "description": "종목 정보 조회 중 일시적 오류",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "internal-error",
              "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
            }
          }
        }
      }
    },
    "InternalErrorOrder": {
      "description": "주문 처리 중 일시적 오류",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "internal-error",
              "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
            }
          }
        }
      }
    },
    "InternalErrorOrderHistory": {
      "description": "주문 조회 중 일시적 오류",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "internal-error",
              "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
            }
          }
        }
      }
    },
    "InternalErrorRanking": {
      "description": "랭킹 조회 중 일시적 오류"
    },
    "InternalErrorMarketIndicators": {
      "description": "시장 지표 조회 중 일시적 오류",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "internal-error",
              "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
            }
          }
        }
      }
    },
    "InternalErrorTradingTrend": {
      "description": "수급·투자자 동향 조회 중 일시적 오류",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "internal-error",
              "message": "처리 중 문제가 생겼어요. 잠시 후 다시 시도해주세요."
            }
          }
        }
      }
    },
    "AccountHeaderRequired": {
      "description": "X-Tossinvest-Account 헤더 누락",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/ErrorResponse"
          },
          "example": {
            "error": {
              "requestId": "01HXYZABCDEFG123456789",
              "code": "account-header-required",
              "message": "x-tossinvest-account 헤더가 필요합니다."
            }
          }
        }
      }
    }
  },
  "schemas": {
    "ApiResponse": {
      "type": "object",
      "description": "성공 응답 envelope. 200 응답에 사용됩니다.\n각 엔드포인트의 성공 응답 스키마는 `allOf` 로 본 스키마를 상속하며 `result` 를 구체 타입으로 specialize 합니다.\n실패 응답은 별도의 `ErrorResponse` 스키마를 사용합니다 (4xx/5xx). `result` 와 `error` 는 동시에 나타나지 않습니다.\n",
      "required": [
        "result"
      ],
      "properties": {
        "result": {
          "description": "성공 응답의 페이로드. 엔드포인트별 타입이 다르며, 각 엔드포인트 스펙에서 `allOf` 로 구체 타입을 명시합니다.\n"
        }
      }
    },
    "ErrorResponse": {
      "type": "object",
      "description": "에러 응답 envelope. 4xx/5xx 응답에 사용됩니다. 성공 응답은 별도의 `ApiResponse` 스키마를 사용합니다.\n",
      "required": [
        "error"
      ],
      "properties": {
        "error": {
          "$ref": "#/components/schemas/ApiError"
        }
      }
    },
    "ApiError": {
      "type": "object",
      "description": "에러 객체. 에러 식별에 필요한 최소 정보(`requestId`, `code`, `message`)와\n필요 시 해결 힌트(`data`)를 포함합니다.\n",
      "required": [
        "requestId",
        "code",
        "message"
      ],
      "properties": {
        "requestId": {
          "type": "string",
          "description": "요청을 식별하는 고유 ID. 응답 헤더 `X-Request-Id` 와 동일한 값입니다.\n토스증권 CS 문의 시 첨부를 권장합니다.\n",
          "example": "01HXYZABCDEFG123456789"
        },
        "code": {
          "type": "string",
          "description": "에러 코드. flat string 식별자.\n도메인 에러는 이유를 직접 표현하는 단일 식별자 (예: `invalid-request`, `order-not-found`) 를 사용합니다.\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n",
          "example": "order-not-found"
        },
        "message": {
          "type": "string",
          "description": "사용자에게 노출 가능한 에러 메시지. 내부 정책상 노출이 제한되는 경우 빈 문자열로 내려갈 수 있으므로\n클라이언트는 `code` 기반으로 메시지를 자체 매핑할 것을 권장합니다.\n",
          "example": "주문 방향이 올바르지 않습니다."
        },
        "data": {
          "type": [
            "object",
            "null"
          ],
          "description": "에러 해결 힌트. 에러 코드별로 포함 여부와 키 구조가 다르며, 없는 경우 필드 자체가 생략됩니다.\n모든 표준 키가 항상 함께 내려가지 않으며, 각 에러 코드에 해당하는 서브셋만 포함됩니다.\n\n## 표준 키 (camelCase)\n\n| 키 | 타입 | 설명 |\n|---|---|---|\n| `field` | string | 검증 실패 원인 필드. 외부 API 에 노출된 이름 (request body JSON key 또는 query parameter name) 을 사용합니다. 복수 필드는 쉼표로 구분 (예: `\"quantity,orderAmount\"`). |\n| `allowedValues` | string[] | enum 후보 값 전체. |\n| `allowedConditions` | object | 조건부 허용 규칙 (`marketCountry` / `orderType` / `side` 등). |\n| `constraint` | object | 필드 제약 (`min` / `max` / `integerOnly` / `step`). |\n| `format` | string | 포맷 규칙명 (예: `decimal`). |\n| `pattern` | string | 정규식. |\n| `maxLength` | number | 문자열 길이 상한. |\n| `limits` | object | 금액 / 수량 한도 (`threshold` / `minimum` / `maximum` + `currency`). |\n| `retryAfterAt` | string | 절대 재시도 시각 (ISO 8601 offset, KST). |\n| `retryAfterSeconds` | number | 상대 재시도 시각 (초). |\n| `tickSize` | string | 호가 단위. |\n| `nearestPrices` | string[] | 근접 유효 가격 (`[lower, upper]`). |\n\n구체적인 에러 코드별 `data` 예시는 각 엔드포인트의 4xx / 5xx 응답 예시를 참고합니다.\n",
          "additionalProperties": true
        }
      }
    },
    "Currency": {
      "type": "string",
      "enum": [
        "KRW",
        "USD"
      ],
      "description": "통화 코드.\n- KRW: 한국 원화\n- USD: 미국 달러\n\n클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.\n"
    },
    "MarketCountry": {
      "type": "string",
      "enum": [
        "KR",
        "US"
      ],
      "description": "시장 국가 구분.\n- KR: 국내 주식 (KRX)\n- US: 미국 주식 (NYSE, NASDAQ 등)\n\n클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.\n"
    },
    "OAuth2TokenRequest": {
      "type": "object",
      "description": "OAuth2 Client Credentials Grant 토큰 발급 요청.\n`application/x-www-form-urlencoded` 으로 전송합니다.\n",
      "required": [
        "grant_type",
        "client_id",
        "client_secret"
      ],
      "properties": {
        "grant_type": {
          "type": "string",
          "enum": [
            "client_credentials"
          ],
          "description": "인증 방식. `client_credentials` 만 지원합니다."
        },
        "client_id": {
          "type": "string",
          "description": "발급받은 클라이언트 ID",
          "example": "c_01HXYZABCDEFG123456789"
        },
        "client_secret": {
          "type": "string",
          "format": "password",
          "description": "발급받은 클라이언트 시크릿. 노출되지 않도록 서버 측에서만 사용합니다."
        }
      }
    },
    "OAuth2TokenResponse": {
      "type": "object",
      "description": "토큰 발급 성공 응답.\nBFF 의 공통 `ApiResponse` envelope 을 사용하지 않고 OAuth2 표준 형식으로 응답합니다.\n",
      "required": [
        "access_token",
        "token_type",
        "expires_in"
      ],
      "properties": {
        "access_token": {
          "type": "string",
          "description": "JWT 형식의 access token. 모든 API 요청의 `Authorization: Bearer` 헤더에 담습니다.",
          "example": "eyJraWQiOiIyMDI2LTA0LTAxLWtleSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjXzAxSFhZWiJ9..."
        },
        "token_type": {
          "type": "string",
          "enum": [
            "Bearer"
          ],
          "description": "토큰 타입. 항상 `Bearer`.",
          "example": "Bearer"
        },
        "expires_in": {
          "type": "integer",
          "format": "int64",
          "description": "토큰 만료까지 남은 초.",
          "example": 86400
        }
      }
    },
    "OAuth2ErrorResponse": {
      "type": "object",
      "description": "OAuth2 토큰 발급 실패 응답.\n`/oauth2/token` 엔드포인트는 BFF 공통 `ErrorResponse` envelope 이 아닌 OAuth2 표준 포맷으로 응답합니다.\n클라이언트는 `code` 가 아닌 `error` 필드로 에러를 식별해야 합니다.\n",
      "required": [
        "error"
      ],
      "properties": {
        "error": {
          "type": "string",
          "description": "에러 코드.",
          "enum": [
            "invalid_request",
            "invalid_client",
            "invalid_grant",
            "unauthorized_client",
            "unsupported_grant_type",
            "access_denied"
          ]
        },
        "error_description": {
          "type": "string",
          "description": "에러 상세 설명 (선택). 메시지에 non-ASCII 문자가 포함되는 경우 생략될 수 있습니다.\n",
          "example": "Client authentication failed."
        },
        "error_uri": {
          "type": "string",
          "format": "uri",
          "description": "에러 정보가 게시된 페이지 URI (선택)."
        }
      }
    },
    "OrderbookEntry": {
      "type": "object",
      "required": [
        "price",
        "volume"
      ],
      "properties": {
        "price": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "호가",
          "example": "72100"
        },
        "volume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "잔량",
          "example": "8500"
        }
      }
    },
    "OrderbookResponse": {
      "type": "object",
      "required": [
        "currency",
        "asks",
        "bids"
      ],
      "properties": {
        "timestamp": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time",
          "description": "데이터 시각. 데이터 미제공 시 null",
          "example": "2026-03-25T09:30:00.123+09:00"
        },
        "currency": {
          "$ref": "#/components/schemas/Currency"
        },
        "asks": {
          "type": "array",
          "description": "매도호가 목록 (낮은 가격순)",
          "items": {
            "$ref": "#/components/schemas/OrderbookEntry"
          }
        },
        "bids": {
          "type": "array",
          "description": "매수호가 목록 (높은 가격순)",
          "items": {
            "$ref": "#/components/schemas/OrderbookEntry"
          }
        }
      }
    },
    "PriceResponse": {
      "type": "object",
      "required": [
        "symbol",
        "lastPrice",
        "currency"
      ],
      "properties": {
        "symbol": {
          "type": "string",
          "description": "종목 심볼",
          "example": "005930"
        },
        "timestamp": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time",
          "description": "데이터 시각. 체결 미발생 등으로 시각이 없을 경우 null",
          "example": "2026-03-25T09:30:00.123+09:00"
        },
        "lastPrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "현재가",
          "example": "72000"
        },
        "currency": {
          "$ref": "#/components/schemas/Currency"
        }
      }
    },
    "Trade": {
      "type": "object",
      "required": [
        "price",
        "volume",
        "timestamp",
        "currency"
      ],
      "properties": {
        "price": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "체결가",
          "example": "72000"
        },
        "volume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "체결 수량",
          "example": "120"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time",
          "description": "체결 시각",
          "example": "2026-03-25T09:30:42.000+09:00"
        },
        "currency": {
          "$ref": "#/components/schemas/Currency"
        }
      }
    },
    "PriceLimitResponse": {
      "type": "object",
      "required": [
        "timestamp",
        "currency"
      ],
      "properties": {
        "timestamp": {
          "type": "string",
          "format": "date-time",
          "description": "데이터 시각",
          "example": "2026-03-25T09:30:00.123+09:00"
        },
        "upperLimitPrice": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "상한가. 미국 주식 등 가격제한이 없는 시장에서는 null",
          "example": "93000"
        },
        "lowerLimitPrice": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "하한가. 미국 주식 등 가격제한이 없는 시장에서는 null",
          "example": "50400"
        },
        "currency": {
          "$ref": "#/components/schemas/Currency"
        }
      }
    },
    "CandlePageResponse": {
      "type": "object",
      "required": [
        "candles"
      ],
      "properties": {
        "candles": {
          "type": "array",
          "description": "캔들 목록. 최신순(`timestamp` 내림차순) 정렬 — 배열 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다.",
          "items": {
            "$ref": "#/components/schemas/Candle"
          }
        },
        "nextBefore": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time",
          "description": "다음 페이지 조회 시 `before` 쿼리 파라미터에 그대로 전달. 마지막 페이지면 null."
        }
      }
    },
    "Candle": {
      "type": "object",
      "required": [
        "timestamp",
        "openPrice",
        "highPrice",
        "lowPrice",
        "closePrice",
        "volume",
        "currency"
      ],
      "properties": {
        "timestamp": {
          "type": "string",
          "format": "date-time",
          "description": "봉 기준 시각\n- `1m`: 봉 종료 시각. 해당 봉은 `[timestamp - 1분, timestamp)` 구간의 체결을 집계합니다.\n- `1d`: 해당 거래일 (시각은 현지 자정 고정)\n",
          "example": "2026-03-25T09:00:00+09:00"
        },
        "openPrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "시가",
          "example": "71600"
        },
        "highPrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "고가",
          "example": "72300"
        },
        "lowPrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "저가",
          "example": "71500"
        },
        "closePrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "종가",
          "example": "72000"
        },
        "volume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "거래량",
          "example": "3521000"
        },
        "currency": {
          "$ref": "#/components/schemas/Currency"
        }
      }
    },
    "StockInfo": {
      "type": "object",
      "required": [
        "symbol",
        "name",
        "englishName",
        "isinCode",
        "market",
        "securityType",
        "isCommonShare",
        "status",
        "currency",
        "sharesOutstanding"
      ],
      "properties": {
        "symbol": {
          "type": "string",
          "description": "종목 심볼.",
          "example": "005930"
        },
        "name": {
          "type": "string",
          "description": "종목명 (한글)",
          "example": "삼성전자"
        },
        "englishName": {
          "type": "string",
          "description": "영문 종목명",
          "example": "SamsungElec"
        },
        "isinCode": {
          "type": "string",
          "description": "국제증권식별번호 (ISO 6166)",
          "example": "KR7005930003"
        },
        "market": {
          "type": "string",
          "description": "상장 시장. warnings API의 exchange(거래소 단위)와 달리 시장 세그먼트 단위로 구분",
          "enum": [
            "KOSPI",
            "KOSDAQ",
            "NYSE",
            "NASDAQ",
            "AMEX",
            "KR_ETC",
            "US_ETC"
          ],
          "example": "KOSPI"
        },
        "securityType": {
          "type": "string",
          "description": "종목 유형",
          "enum": [
            "STOCK",
            "FOREIGN_STOCK",
            "DEPOSITARY_RECEIPT",
            "INFRASTRUCTURE_FUND",
            "REIT",
            "ETF",
            "FOREIGN_ETF",
            "ETN",
            "STOCK_WARRANTS"
          ],
          "example": "STOCK"
        },
        "isCommonShare": {
          "type": "boolean",
          "description": "보통주 여부. 우선주인 경우 false",
          "example": true
        },
        "status": {
          "type": "string",
          "description": "상장 상태",
          "enum": [
            "SCHEDULED",
            "ACTIVE",
            "DELISTED"
          ],
          "example": "ACTIVE"
        },
        "currency": {
          "$ref": "#/components/schemas/Currency"
        },
        "listDate": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "상장일 (YYYY-MM-DD, KST 기준). 정보 미제공 시 null",
          "example": "1975-06-11"
        },
        "delistDate": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "상장폐지일 (YYYY-MM-DD, KST 기준). 활성 종목은 null",
          "example": null
        },
        "sharesOutstanding": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "발행주식수",
          "example": "5919637922"
        },
        "leverageFactor": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "레버리지 배수. ETF/ETN에만 적용 (1.0, 2.0, -1.0 등). 일반 주식 등 해당 없는 종목은 null",
          "example": null
        },
        "koreanMarketDetail": {
          "description": "국내 시장 상세 정보. 국내 종목(KOSPI, KOSDAQ, KR_ETC)에만 제공되며, 해외 종목은 null",
          "oneOf": [
            {
              "$ref": "#/components/schemas/KrMarketDetail"
            },
            {
              "type": "null"
            }
          ]
        }
      }
    },
    "KrMarketDetail": {
      "type": "object",
      "required": [
        "liquidationTrading",
        "nxtSupported",
        "krxTradingSuspended"
      ],
      "properties": {
        "liquidationTrading": {
          "type": "boolean",
          "description": "정리매매 여부 (상장폐지 절차 진행 중).",
          "example": false
        },
        "nxtSupported": {
          "type": "boolean",
          "description": "NXT 대체거래소 지원 여부",
          "example": true
        },
        "krxTradingSuspended": {
          "type": "boolean",
          "description": "KRX 거래정지 여부",
          "example": false
        },
        "nxtTradingSuspended": {
          "type": [
            "boolean",
            "null"
          ],
          "description": "NXT 거래정지 여부. NXT 미지원 종목(nxtSupported=false)은 null",
          "example": false
        }
      }
    },
    "StockWarning": {
      "type": "object",
      "required": [
        "warningType"
      ],
      "properties": {
        "warningType": {
          "type": "string",
          "description": "유의사항 유형.\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n\n| 값 | 의미 |\n|------|------|\n| `LIQUIDATION_TRADING` | 정리매매 (상장폐지 절차 진행 중) |\n| `OVERHEATED` | 단기과열종목 지정 |\n| `INVESTMENT_WARNING` | 투자경고종목 지정 |\n| `INVESTMENT_RISK` | 투자위험종목 지정 |\n| `VI_STATIC_AND_DYNAMIC` | 변동성 완화장치(VI) 정적 + 동적 동시 발동 |\n| `VI_STATIC` | 변동성 완화장치(VI) 정적 발동 |\n| `VI_DYNAMIC` | 변동성 완화장치(VI) 동적 발동 |\n| `STOCK_WARRANTS` | 신주인수권증서/증권 |\n",
          "enum": [
            "LIQUIDATION_TRADING",
            "OVERHEATED",
            "INVESTMENT_WARNING",
            "INVESTMENT_RISK",
            "VI_STATIC_AND_DYNAMIC",
            "VI_STATIC",
            "VI_DYNAMIC",
            "STOCK_WARRANTS"
          ],
          "example": "VI_STATIC"
        },
        "exchange": {
          "type": [
            "string",
            "null"
          ],
          "description": "거래소 코드 (KRX, NXT 등 물리적 거래소 단위). stocks API의 market(상장 시장 단위)과 추상화 수준이 다름. 거래소 무관 경고는 null",
          "example": "KRX"
        },
        "startDate": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "적용 시작일 (inclusive, YYYY-MM-DD, KST 기준). 시작일 미정 시 null",
          "example": "2026-03-26"
        },
        "endDate": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "적용 종료일 (inclusive, YYYY-MM-DD, KST 기준). 진행 중이거나 미정 시 null",
          "example": "2026-03-27"
        }
      }
    },
    "ListedStock": {
      "type": "object",
      "required": [
        "symbol",
        "name",
        "securityType",
        "isCommonShare",
        "isinCode"
      ],
      "properties": {
        "symbol": {
          "type": "string",
          "description": "종목 심볼.",
          "example": "005930"
        },
        "name": {
          "type": "string",
          "description": "종목명 (한글)",
          "example": "삼성전자"
        },
        "securityType": {
          "type": "string",
          "description": "종목 유형",
          "enum": [
            "STOCK",
            "FOREIGN_STOCK",
            "DEPOSITARY_RECEIPT",
            "INFRASTRUCTURE_FUND",
            "REIT",
            "ETF",
            "FOREIGN_ETF",
            "ETN",
            "STOCK_WARRANTS"
          ],
          "example": "STOCK"
        },
        "isCommonShare": {
          "type": "boolean",
          "description": "보통주 여부",
          "example": true
        },
        "isinCode": {
          "type": "string",
          "description": "ISIN 코드",
          "example": "KR7005930003"
        }
      }
    },
    "StockInvestorTradingResponse": {
      "type": "object",
      "required": [
        "records"
      ],
      "properties": {
        "nextUntil": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "다음 페이지 조회 기준일. 다음 페이지 조회 시 `until` 쿼리 파라미터에 그대로 전달. 더 이상 데이터가 없으면 null",
          "example": "2026-07-15"
        },
        "records": {
          "type": "array",
          "description": "일별 투자자 매매동향 기록 목록 (최신순). 데이터가 없으면 빈 배열",
          "items": {
            "$ref": "#/components/schemas/StockInvestorTradingRecord"
          }
        }
      }
    },
    "StockInvestorTradingRecord": {
      "type": "object",
      "required": [
        "date",
        "updatedAt",
        "foreigner",
        "institution"
      ],
      "properties": {
        "date": {
          "type": "string",
          "format": "date",
          "description": "매매 기준일",
          "example": "2026-07-16"
        },
        "updatedAt": {
          "type": "string",
          "format": "date-time",
          "description": "기록 전체의 마지막 갱신 시각 (투자자별 매매동향과 `foreignerHolding`·`cfd` 반영 포함).\n당일 기록은 장중 잠정치로 계속 갱신되며, `cfd` 반영(T+1)과 외국인 보유 확정 갱신으로\n다음 영업일에도 갱신될 수 있습니다.\n",
          "example": "2026-07-16T17:29:12+09:00"
        },
        "individual": {
          "description": "개인. 당일 잠정 기록에는 개인 잠정치가 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다",
          "oneOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingVolume"
            },
            {
              "type": "null"
            }
          ]
        },
        "foreigner": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingVolume"
            }
          ],
          "description": "등록외국인. 미등록 외국인은 포함하지 않으며, 시장 지표의 투자자별 매매대금\n(`GET /api/v1/market-indicators/{symbol}/investor-trading`)의 `foreigner`(등록·미등록 합계)와 기준이 다릅니다\n"
        },
        "institution": {
          "allOf": [
            {
              "$ref": "#/components/schemas/StockInstitutionTradingVolume"
            }
          ],
          "description": "기관 합계"
        },
        "otherCorporation": {
          "description": "기타법인. 당일 잠정 기록에는 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다",
          "oneOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingVolume"
            },
            {
              "type": "null"
            }
          ]
        },
        "foreignerHolding": {
          "description": "외국인 보유 현황. 해당 일자의 보유 데이터가 아직 반영되지 않았으면 null (당일 저녁 반영, 다음 영업일 오전 확정 갱신될 수 있음)",
          "oneOf": [
            {
              "$ref": "#/components/schemas/ForeignerHolding"
            },
            {
              "type": "null"
            }
          ]
        },
        "cfd": {
          "description": "CFD(차액결제거래) 잔고 현황. 해당 일자의 잔고 데이터가 아직 반영되지 않았으면 null (다음 영업일 새벽 반영, T+1)",
          "oneOf": [
            {
              "$ref": "#/components/schemas/CfdBalance"
            },
            {
              "type": "null"
            }
          ]
        }
      }
    },
    "InvestorTradingVolume": {
      "type": "object",
      "required": [
        "buyVolume",
        "sellVolume",
        "netBuyVolume"
      ],
      "properties": {
        "buyVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "매수 거래량 (주, 정수)",
          "example": "8412300"
        },
        "sellVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "매도 거래량 (주, 정수)",
          "example": "8120450"
        },
        "netBuyVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "순매수 거래량 (주, 정수). 매수 거래량 − 매도 거래량, 음수면 순매도",
          "example": "291850"
        }
      }
    },
    "StockInstitutionTradingVolume": {
      "type": "object",
      "required": [
        "buyVolume",
        "sellVolume",
        "netBuyVolume"
      ],
      "properties": {
        "buyVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "기관 합계 매수 거래량 (주, 정수). `breakdown` 7개 항목의 `buyVolume` 합과 일치",
          "example": "1953200"
        },
        "sellVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "기관 합계 매도 거래량 (주, 정수). `breakdown` 7개 항목의 `sellVolume` 합과 일치",
          "example": "1915300"
        },
        "netBuyVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "기관 합계 순매수 거래량 (주, 정수). 매수 − 매도, 음수면 순매도. `breakdown` 7개 항목의 `netBuyVolume` 합과 일치",
          "example": "37900"
        },
        "breakdown": {
          "description": "기관 세부 7개 분류별 거래량. 당일 잠정 기록에는 제공되지 않아 null 이며, 확정치가 반영되는 당일 저녁부터 값이 채워집니다",
          "oneOf": [
            {
              "$ref": "#/components/schemas/StockInstitutionTradingBreakdown"
            },
            {
              "type": "null"
            }
          ]
        }
      }
    },
    "StockInstitutionTradingBreakdown": {
      "type": "object",
      "description": "기관 세부 7개 분류별 매매 거래량",
      "required": [
        "financialInvestment",
        "insurance",
        "trust",
        "privateEquityFund",
        "bank",
        "otherFinancialInstitution",
        "pensionFund"
      ],
      "properties": {
        "financialInvestment": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingVolume"
            }
          ],
          "description": "금융투자"
        },
        "insurance": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingVolume"
            }
          ],
          "description": "보험"
        },
        "trust": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingVolume"
            }
          ],
          "description": "투신"
        },
        "privateEquityFund": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingVolume"
            }
          ],
          "description": "사모펀드"
        },
        "bank": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingVolume"
            }
          ],
          "description": "은행"
        },
        "otherFinancialInstitution": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingVolume"
            }
          ],
          "description": "기타금융"
        },
        "pensionFund": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingVolume"
            }
          ],
          "description": "연기금"
        }
      }
    },
    "ForeignerHolding": {
      "type": "object",
      "required": [
        "holdingQuantity",
        "limitQuantity",
        "holdingRate"
      ],
      "properties": {
        "holdingQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "외국인 보유 주식 수 (주, 정수)",
          "example": "3012456789"
        },
        "limitQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "외국인 보유 한도 주식 수 (주, 정수)",
          "example": "5919637922"
        },
        "holdingRate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "외국인 보유 비율 (소수 비율). 상장주식수 대비 보유 주식 수. 예: `0.5089` = 50.89%",
          "example": "0.5089"
        }
      }
    },
    "CfdBalance": {
      "type": "object",
      "required": [
        "buyBalanceQuantity",
        "buyBalanceRate",
        "sellBalanceQuantity",
        "sellBalanceRate"
      ],
      "properties": {
        "buyBalanceQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "CFD 매수 잔고 수량 (주, 정수)",
          "example": "1250000"
        },
        "buyBalanceRate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "CFD 매수 잔고 비율 (소수 비율). 상장주식수 대비 매수 잔고 수량. 예: `0.0002` = 0.02%",
          "example": "0.0002"
        },
        "sellBalanceQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "CFD 매도 잔고 수량 (주, 정수)",
          "example": "890000"
        },
        "sellBalanceRate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "CFD 매도 잔고 비율 (소수 비율). 상장주식수 대비 매도 잔고 수량. 예: `0.0001` = 0.01%",
          "example": "0.0001"
        }
      }
    },
    "ProgramTradesResponse": {
      "type": "object",
      "required": [
        "records"
      ],
      "properties": {
        "nextUntil": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "다음 페이지 조회 기준일. 다음 페이지 조회 시 `until` 쿼리 파라미터에 그대로 전달. 더 이상 데이터가 없으면 null",
          "example": "2026-07-15"
        },
        "records": {
          "type": "array",
          "description": "일별 프로그램매매 기록 목록 (최신순). 데이터가 없으면 빈 배열",
          "items": {
            "$ref": "#/components/schemas/ProgramTradeRecord"
          }
        }
      }
    },
    "ProgramTradeRecord": {
      "type": "object",
      "required": [
        "date",
        "arbitrage",
        "nonArbitrage"
      ],
      "properties": {
        "date": {
          "type": "string",
          "format": "date",
          "description": "매매 기준일",
          "example": "2026-07-17"
        },
        "arbitrage": {
          "allOf": [
            {
              "$ref": "#/components/schemas/ProgramTradingVolume"
            }
          ],
          "description": "차익거래"
        },
        "nonArbitrage": {
          "allOf": [
            {
              "$ref": "#/components/schemas/ProgramTradingVolume"
            }
          ],
          "description": "비차익거래"
        }
      }
    },
    "ProgramTradingVolume": {
      "type": "object",
      "required": [
        "buyVolume",
        "sellVolume",
        "netBuyVolume"
      ],
      "properties": {
        "buyVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "프로그램 매수 거래량 (주, 정수)",
          "example": "152300"
        },
        "sellVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "프로그램 매도 거래량 (주, 정수)",
          "example": "183400"
        },
        "netBuyVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "프로그램 순매수 거래량 (주, 정수). 매수 − 매도, 음수면 순매도",
          "example": "-31100"
        }
      }
    },
    "ShortSellingResponse": {
      "type": "object",
      "required": [
        "records"
      ],
      "properties": {
        "nextUntil": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "다음 페이지 조회 기준일. 다음 페이지 조회 시 `until` 쿼리 파라미터에 그대로 전달. 더 이상 데이터가 없으면 null",
          "example": "2026-07-15"
        },
        "records": {
          "type": "array",
          "description": "일별 공매도 기록 목록 (최신순). 데이터가 없으면 빈 배열",
          "items": {
            "$ref": "#/components/schemas/ShortSellingRecord"
          }
        }
      }
    },
    "ShortSellingRecord": {
      "type": "object",
      "required": [
        "date",
        "updatedAt",
        "shortSellingVolume",
        "shortSellingAmount"
      ],
      "properties": {
        "date": {
          "type": "string",
          "format": "date",
          "description": "매매 기준일",
          "example": "2026-07-16"
        },
        "updatedAt": {
          "type": "string",
          "format": "date-time",
          "description": "해당 기록의 마지막 갱신 시각",
          "example": "2026-07-16T17:25:43+09:00"
        },
        "shortSellingVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "공매도 거래량 (주, 정수)",
          "example": "512300"
        },
        "shortSellingAmount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "공매도 거래대금 (KRW, 정수)",
          "example": "41250000000"
        },
        "shortSellingVolumeRate": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "공매도 거래량 비중 (소수 비율, 소수 다섯째 자리까지). 해당 일자 전체 거래량 대비 공매도 거래량.\n분모인 전체 거래량은 정규장 외 세션(장전·장후 시간외종가, 애프터마켓)을 포함한 당일 누적입니다.\n기준 거래량 데이터가 없는 날짜는 null, 기준 거래량이 0 이면 `0`. 예: `0.03215` = 3.215%\n",
          "example": "0.03215"
        },
        "shortSellingAmountRate": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "공매도 거래대금 비중 (소수 비율, 소수 넷째 자리까지). 해당 일자 전체 거래대금 대비 공매도 거래대금.\n분모인 전체 거래대금은 정규장 외 세션(장전·장후 시간외종가, 애프터마켓)을 포함한 당일 누적입니다.\n기준 거래대금 데이터가 없는 날짜는 null, 기준 거래대금이 0 이면 `0`. 예: `0.0318` = 3.18%\n",
          "example": "0.0318"
        }
      }
    },
    "CreditTradesResponse": {
      "type": "object",
      "required": [
        "records"
      ],
      "properties": {
        "nextUntil": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "다음 페이지 조회 기준일. 다음 페이지 조회 시 `until` 쿼리 파라미터에 그대로 전달. 더 이상 데이터가 없으면 null",
          "example": "2026-07-14"
        },
        "records": {
          "type": "array",
          "description": "일별 신용거래 기록 목록 (최신순). 데이터가 없으면 빈 배열",
          "items": {
            "$ref": "#/components/schemas/CreditTradeRecord"
          }
        }
      }
    },
    "CreditTradeRecord": {
      "type": "object",
      "required": [
        "date",
        "updatedAt"
      ],
      "properties": {
        "date": {
          "type": "string",
          "format": "date",
          "description": "매매 기준일",
          "example": "2026-07-16"
        },
        "updatedAt": {
          "type": "string",
          "format": "date-time",
          "description": "해당 기록의 마지막 갱신 시각",
          "example": "2026-07-17T02:35:00+09:00"
        },
        "marginLoan": {
          "description": "신용융자 (돈을 빌려 매수하는 신용거래). 해당 일자의 융자 데이터가 없으면 null",
          "oneOf": [
            {
              "$ref": "#/components/schemas/CreditTradeDetail"
            },
            {
              "type": "null"
            }
          ]
        },
        "stockLoan": {
          "description": "신용대주 (주식을 빌려 매도하는 개인 신용거래). 기관 간 대차거래\n(`GET /api/v1/stocks/{symbol}/securities-lending`)와는 다른 데이터입니다.\n해당 일자의 대주 데이터가 없으면 null\n",
          "oneOf": [
            {
              "$ref": "#/components/schemas/CreditTradeDetail"
            },
            {
              "type": "null"
            }
          ]
        }
      }
    },
    "CreditTradeDetail": {
      "type": "object",
      "required": [
        "newQuantity",
        "returnQuantity",
        "balanceQuantity",
        "balanceRate",
        "tradingRate"
      ],
      "properties": {
        "newQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "신규 수량 (주, 정수)",
          "example": "125300"
        },
        "returnQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "상환 수량 (주, 정수)",
          "example": "98200"
        },
        "balanceQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "잔고 수량 (주, 정수)",
          "example": "2513400"
        },
        "balanceRate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "잔고 비율 (소수 비율). 상장주식수 대비 잔고 수량. 예: `0.0042` = 0.42%",
          "example": "0.0042"
        },
        "tradingRate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "공여율 (소수 비율). 매매일의 종목 전체 거래량 중 해당 신용거래 유형의 거래량 비율. 예: `0.09` = 9%",
          "example": "0.09"
        }
      }
    },
    "SecuritiesLendingResponse": {
      "type": "object",
      "required": [
        "records"
      ],
      "properties": {
        "nextUntil": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "다음 페이지 조회 기준일. 다음 페이지 조회 시 `until` 쿼리 파라미터에 그대로 전달. 더 이상 데이터가 없으면 null",
          "example": "2026-07-15"
        },
        "records": {
          "type": "array",
          "description": "일별 대차거래 기록 목록 (최신순). 데이터가 없으면 빈 배열",
          "items": {
            "$ref": "#/components/schemas/SecuritiesLendingRecord"
          }
        }
      }
    },
    "SecuritiesLendingRecord": {
      "type": "object",
      "required": [
        "date",
        "updatedAt",
        "executionQuantity",
        "repaymentQuantity",
        "balanceQuantity",
        "balanceAmount"
      ],
      "properties": {
        "date": {
          "type": "string",
          "format": "date",
          "description": "매매 기준일",
          "example": "2026-07-17"
        },
        "updatedAt": {
          "type": "string",
          "format": "date-time",
          "description": "해당 기록의 마지막 갱신 시각",
          "example": "2026-07-17T19:03:21+09:00"
        },
        "executionQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "대차 체결 수량 (주, 정수)",
          "example": "210500"
        },
        "repaymentQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "대차 상환 수량 (주, 정수)",
          "example": "185300"
        },
        "balanceQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "대차 잔고 수량 (주, 정수)",
          "example": "15234000"
        },
        "balanceAmount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "대차 잔고 금액 (KRW, 정수)",
          "example": "1218720000000"
        }
      }
    },
    "ExchangeRateResponse": {
      "type": "object",
      "required": [
        "baseCurrency",
        "quoteCurrency",
        "rate",
        "midRate",
        "basisPoint",
        "rateChangeType",
        "validFrom",
        "validUntil"
      ],
      "properties": {
        "baseCurrency": {
          "$ref": "#/components/schemas/Currency",
          "description": "기준 통화",
          "example": "USD"
        },
        "quoteCurrency": {
          "$ref": "#/components/schemas/Currency",
          "description": "표시 통화 (quote currency)",
          "example": "KRW"
        },
        "rate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "매수 환율 (1 baseCurrency = ? quoteCurrency)",
          "example": "1380.5"
        },
        "midRate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "매매기준율 (은행간 mid rate)",
          "example": "1375"
        },
        "basisPoint": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "매매기준율(midRate) 대비 basis points. (rate - midRate) / midRate * 10000",
          "example": "40"
        },
        "rateChangeType": {
          "type": "string",
          "description": "등락 구분",
          "enum": [
            "UP",
            "EQUAL",
            "DOWN"
          ],
          "example": "UP"
        },
        "validFrom": {
          "type": "string",
          "format": "date-time",
          "description": "환율 유효 시작 시각",
          "example": "2026-03-25T09:30:00+09:00"
        },
        "validUntil": {
          "type": "string",
          "format": "date-time",
          "description": "환율 유효 종료 시각",
          "example": "2026-03-25T09:31:00+09:00"
        }
      }
    },
    "KrMarketCalendarResponse": {
      "type": "object",
      "required": [
        "today",
        "previousBusinessDay",
        "nextBusinessDay"
      ],
      "properties": {
        "today": {
          "$ref": "#/components/schemas/KrMarketDay"
        },
        "previousBusinessDay": {
          "$ref": "#/components/schemas/KrMarketDay"
        },
        "nextBusinessDay": {
          "$ref": "#/components/schemas/KrMarketDay"
        }
      }
    },
    "KrMarketDay": {
      "type": "object",
      "required": [
        "date"
      ],
      "properties": {
        "date": {
          "type": "string",
          "format": "date",
          "description": "영업일 (KST 기준)",
          "example": "2026-03-25"
        },
        "integrated": {
          "description": "거래 가능 시간 (통합 모드 (KRX+NXT) 기준). 둘 다 휴장이면 null",
          "oneOf": [
            {
              "$ref": "#/components/schemas/IntegratedHour"
            },
            {
              "type": "null"
            }
          ]
        }
      }
    },
    "IntegratedHour": {
      "type": "object",
      "description": "거래 가능 시간. 장전/장후 시간외종가 제외, 통합 모드 (KRX+NXT) 기준.\n세 세션(`preMarket`, `regularMarket`, `afterMarket`) 각각 nullable. 해당 세션이 KRX·NXT 모두 휴장이면 null,\n세 세션 모두 null 이면 상위 `integrated` 자체가 null.\n",
      "properties": {
        "preMarket": {
          "description": "프리마켓 (NXT 접속매매). NXT 프리마켓이 휴장이면 null",
          "oneOf": [
            {
              "$ref": "#/components/schemas/PreMarketSession"
            },
            {
              "type": "null"
            }
          ]
        },
        "regularMarket": {
          "description": "정규장. KRX·NXT 정규장의 합집합. 둘 다 휴장이면 null",
          "oneOf": [
            {
              "$ref": "#/components/schemas/RegularMarketSession"
            },
            {
              "type": "null"
            }
          ]
        },
        "afterMarket": {
          "description": "애프터마켓. KRX·NXT 애프터마켓의 합집합. 둘 다 휴장이면 null",
          "oneOf": [
            {
              "$ref": "#/components/schemas/AfterMarketSession"
            },
            {
              "type": "null"
            }
          ]
        }
      }
    },
    "PreMarketSession": {
      "type": "object",
      "description": "프리마켓 세션",
      "required": [
        "startTime",
        "endTime"
      ],
      "properties": {
        "startTime": {
          "type": "string",
          "format": "date-time",
          "description": "프리마켓 시작",
          "example": "2026-03-25T08:00:00+09:00"
        },
        "singlePriceAuctionStartTime": {
          "description": "프리마켓 내 시가단일가 구간 시작 (NXT 프리마켓 접속매매 종료). 단일가 정보 결손 시 null",
          "example": "2026-03-25T08:50:00+09:00",
          "oneOf": [
            {
              "type": "string",
              "format": "date-time"
            },
            {
              "type": "null"
            }
          ]
        },
        "endTime": {
          "type": "string",
          "format": "date-time",
          "description": "프리마켓 종료 (시가단일가 종료)",
          "example": "2026-03-25T09:00:00+09:00"
        }
      }
    },
    "RegularMarketSession": {
      "type": "object",
      "description": "정규장 세션. KRX·NXT 정규장의 합집합(가장 이른 시작 ~ 가장 늦은 종료). 종가단일가 구간을 포함",
      "required": [
        "startTime",
        "endTime"
      ],
      "properties": {
        "startTime": {
          "type": "string",
          "format": "date-time",
          "description": "정규장 시작. 가장 이른 KRX/NXT 정규장 시작 시각",
          "example": "2026-03-25T09:00:00+09:00"
        },
        "singlePriceAuctionStartTime": {
          "description": "정규장 내 종가단일가 구간 시작 (KRX 기준). KRX 휴장이면 null",
          "example": "2026-03-25T15:20:00+09:00",
          "oneOf": [
            {
              "type": "string",
              "format": "date-time"
            },
            {
              "type": "null"
            }
          ]
        },
        "endTime": {
          "type": "string",
          "format": "date-time",
          "description": "정규장 종료 (종가단일가 종료)",
          "example": "2026-03-25T15:30:00+09:00"
        }
      }
    },
    "AfterMarketSession": {
      "type": "object",
      "description": "애프터마켓 세션. KRX·NXT 애프터마켓의 합집합(가장 이른 시작 ~ 가장 늦은 종료)",
      "required": [
        "startTime",
        "endTime"
      ],
      "properties": {
        "startTime": {
          "type": "string",
          "format": "date-time",
          "description": "애프터마켓 시작. 가장 이른 KRX/NXT 애프터마켓 시작 시각",
          "example": "2026-03-25T15:30:00+09:00"
        },
        "singlePriceAuctionEndTime": {
          "description": "애프터마켓 내 시가단일가 구간 종료 (NXT 기준). NXT 애프터마켓이 휴장이면 null",
          "example": "2026-03-25T15:40:00+09:00",
          "oneOf": [
            {
              "type": "string",
              "format": "date-time"
            },
            {
              "type": "null"
            }
          ]
        },
        "endTime": {
          "type": "string",
          "format": "date-time",
          "description": "애프터마켓 전체 종료. 가장 늦은 KRX/NXT 애프터마켓 종료 시각",
          "example": "2026-03-25T20:00:00+09:00"
        }
      }
    },
    "UsMarketCalendarResponse": {
      "type": "object",
      "required": [
        "today",
        "previousBusinessDay",
        "nextBusinessDay"
      ],
      "properties": {
        "today": {
          "$ref": "#/components/schemas/UsMarketDay"
        },
        "previousBusinessDay": {
          "$ref": "#/components/schemas/UsMarketDay"
        },
        "nextBusinessDay": {
          "$ref": "#/components/schemas/UsMarketDay"
        }
      }
    },
    "UsMarketDay": {
      "type": "object",
      "description": "미국 시장 영업일 정보. 4 세션(`dayMarket`, `preMarket`, `regularMarket`, `afterMarket`) 각각 nullable.\n휴장일이면 4 세션 모두 null.\n",
      "required": [
        "date"
      ],
      "properties": {
        "date": {
          "type": "string",
          "format": "date",
          "description": "영업일 (미국 현지 기준)",
          "example": "2026-03-25"
        },
        "dayMarket": {
          "description": "데이마켓 세션 (토스증권). 휴장이면 null",
          "oneOf": [
            {
              "$ref": "#/components/schemas/UsDayMarketSession"
            },
            {
              "type": "null"
            }
          ]
        },
        "preMarket": {
          "description": "프리마켓 세션. 휴장이면 null",
          "oneOf": [
            {
              "$ref": "#/components/schemas/UsPreMarketSession"
            },
            {
              "type": "null"
            }
          ]
        },
        "regularMarket": {
          "description": "정규장 세션. 휴장이면 null",
          "oneOf": [
            {
              "$ref": "#/components/schemas/UsRegularMarketSession"
            },
            {
              "type": "null"
            }
          ]
        },
        "afterMarket": {
          "description": "애프터마켓 세션. 휴장이면 null",
          "oneOf": [
            {
              "$ref": "#/components/schemas/UsAfterMarketSession"
            },
            {
              "type": "null"
            }
          ]
        }
      }
    },
    "UsDayMarketSession": {
      "type": "object",
      "description": "데이마켓 세션 (토스증권)",
      "required": [
        "startTime",
        "endTime"
      ],
      "properties": {
        "startTime": {
          "type": "string",
          "format": "date-time",
          "description": "데이마켓 시작",
          "example": "2026-03-25T09:00:00+09:00"
        },
        "endTime": {
          "type": "string",
          "format": "date-time",
          "description": "데이마켓 종료",
          "example": "2026-03-25T16:50:00+09:00"
        }
      }
    },
    "UsPreMarketSession": {
      "type": "object",
      "description": "프리마켓 세션",
      "required": [
        "startTime",
        "endTime"
      ],
      "properties": {
        "startTime": {
          "type": "string",
          "format": "date-time",
          "description": "프리마켓 시작",
          "example": "2026-03-25T17:00:00+09:00"
        },
        "endTime": {
          "type": "string",
          "format": "date-time",
          "description": "프리마켓 종료",
          "example": "2026-03-25T22:30:00+09:00"
        }
      }
    },
    "UsRegularMarketSession": {
      "type": "object",
      "description": "정규장 세션",
      "required": [
        "startTime",
        "endTime"
      ],
      "properties": {
        "startTime": {
          "type": "string",
          "format": "date-time",
          "description": "정규장 시작",
          "example": "2026-03-25T22:30:00+09:00"
        },
        "endTime": {
          "type": "string",
          "format": "date-time",
          "description": "정규장 종료",
          "example": "2026-03-26T05:00:00+09:00"
        }
      }
    },
    "UsAfterMarketSession": {
      "type": "object",
      "description": "애프터마켓 세션",
      "required": [
        "startTime",
        "endTime"
      ],
      "properties": {
        "startTime": {
          "type": "string",
          "format": "date-time",
          "description": "애프터마켓 시작",
          "example": "2026-03-26T05:00:00+09:00"
        },
        "endTime": {
          "type": "string",
          "format": "date-time",
          "description": "애프터마켓 종료",
          "example": "2026-03-26T07:00:00+09:00"
        }
      }
    },
    "RankingResponse": {
      "type": "object",
      "required": [
        "rankings"
      ],
      "properties": {
        "rankedAt": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time",
          "description": "랭킹 집계 기준 시각. `rankings` 가 빈 배열이면 null",
          "example": "2026-06-10T14:30:00+09:00"
        },
        "rankings": {
          "type": "array",
          "description": "랭킹 종목 목록 (순위 오름차순). 집계 데이터가 없으면 빈 배열. 항목 수는 `count` 이하일 수 있습니다.",
          "items": {
            "$ref": "#/components/schemas/RankingItem"
          }
        }
      }
    },
    "RankingItem": {
      "type": "object",
      "required": [
        "rank",
        "symbol",
        "currency",
        "price",
        "tradingVolume",
        "tradingAmount"
      ],
      "properties": {
        "rank": {
          "type": "integer",
          "description": "순위. 1부터 시작",
          "example": 1
        },
        "symbol": {
          "type": "string",
          "description": "종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합; 예: 005930, 0101N0), US: 영문 티커 (예: AAPL)",
          "example": "005930"
        },
        "currency": {
          "$ref": "#/components/schemas/Currency"
        },
        "price": {
          "$ref": "#/components/schemas/RankingPrice"
        },
        "tradingVolume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "거래량 (`duration` 누적). 집계 기준은 `type` 이 결정합니다 —\n`TOSS_SECURITIES_*` 는 토스증권 체결 기준, 그 외(`MARKET_*` / `TOP_*`)는 시장 전체 기준.\n",
          "example": "18432100"
        },
        "tradingAmount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "거래대금 (`duration` 누적). 집계 기준은 `tradingVolume` 과 동일합니다.",
          "example": "1041436650000"
        }
      }
    },
    "RankingPrice": {
      "type": "object",
      "required": [
        "lastPrice",
        "basePrice"
      ],
      "properties": {
        "lastPrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "현재가",
          "example": "56500"
        },
        "basePrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "기준가. `TOP_GAINERS` / `TOP_LOSERS` 는 `duration` 시작 시점 기준가,\n나머지 타입은 `duration` 과 무관하게 항상 전일 기준가.\n",
          "example": "55800"
        },
        "changeRate": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "등락률, 소수비율 (`0.0125` = 1.25%). `(lastPrice - basePrice) / basePrice`.\n`basePrice` 가 0 이면 null.\n`basePrice` 의 의미를 따라 `TOP_GAINERS` / `TOP_LOSERS` 는 기간 등락률,\n나머지 타입은 전일 대비 등락률입니다.\n",
          "example": "0.0125"
        }
      }
    },
    "MarketIndicatorPriceResponse": {
      "type": "object",
      "required": [
        "symbol",
        "lastPrice"
      ],
      "properties": {
        "symbol": {
          "type": "string",
          "description": "시장 지표 심볼. `GET /api/v1/market-indicators/prices` 의 심볼 카탈로그 참조",
          "example": "KOSPI"
        },
        "timestamp": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time",
          "description": "데이터 시각. 데이터 미제공 시 null",
          "example": "2026-06-11T15:30:00+09:00"
        },
        "lastPrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "현재가. 시장 호가 그대로이며, 통화·단위는 심볼 카탈로그를 따릅니다",
          "example": "2812.45"
        }
      }
    },
    "MarketIndicatorCandlePageResponse": {
      "type": "object",
      "required": [
        "candles"
      ],
      "properties": {
        "candles": {
          "type": "array",
          "description": "캔들 목록. 최신순(`timestamp` 내림차순) 정렬 — 배열 첫 요소가 가장 최근 봉, 마지막 요소가 가장 오래된 봉입니다.",
          "items": {
            "$ref": "#/components/schemas/MarketIndicatorCandle"
          }
        },
        "nextBefore": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time",
          "description": "다음 페이지 조회 시 `before` 쿼리 파라미터에 그대로 전달. 마지막 페이지면 null."
        }
      }
    },
    "MarketIndicatorCandle": {
      "type": "object",
      "required": [
        "timestamp",
        "openPrice",
        "highPrice",
        "lowPrice",
        "closePrice",
        "volume"
      ],
      "properties": {
        "timestamp": {
          "type": "string",
          "format": "date-time",
          "description": "봉 시작 시각",
          "example": "2026-06-11T09:00:00+09:00"
        },
        "openPrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "시가",
          "example": "2798.32"
        },
        "highPrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "고가",
          "example": "2820.15"
        },
        "lowPrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "저가",
          "example": "2790.1"
        },
        "closePrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "종가",
          "example": "2812.45"
        },
        "volume": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "거래량",
          "example": "542000000"
        }
      }
    },
    "InvestorTradingResponse": {
      "type": "object",
      "required": [
        "records"
      ],
      "properties": {
        "nextUntil": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "다음 페이지 조회 기준일. 다음 페이지 조회 시 `until` 쿼리 파라미터에 그대로 전달. 더 이상 데이터가 없으면 null",
          "example": "2026-06-09"
        },
        "records": {
          "type": "array",
          "description": "집계 기간별 매매대금 기록 목록 (최신순). 데이터가 없으면 빈 배열",
          "items": {
            "$ref": "#/components/schemas/InvestorTradingRecord"
          }
        }
      }
    },
    "InvestorTradingRecord": {
      "type": "object",
      "required": [
        "date",
        "updatedAt",
        "individual",
        "foreigner",
        "institution",
        "otherCorporation"
      ],
      "properties": {
        "date": {
          "type": "string",
          "format": "date",
          "description": "집계 기준일. `interval` 이 나타내는 집계 기간의 대표 일자",
          "example": "2026-06-11"
        },
        "updatedAt": {
          "type": "string",
          "format": "date-time",
          "description": "해당 기록의 마지막 갱신 시각. 당일 기록은 장 종료 전까지 갱신될 수 있으므로,\n이 값으로 확정치·잠정치 여부를 판단할 수 있습니다.\n",
          "example": "2026-06-11T18:10:00+09:00"
        },
        "individual": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingAmount"
            }
          ],
          "description": "개인"
        },
        "foreigner": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingAmount"
            }
          ],
          "description": "외국인 합계 (등록·미등록 외국인 포함)"
        },
        "institution": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InstitutionTradingAmount"
            }
          ],
          "description": "기관 합계. `buyAmount`/`sellAmount` 는 `breakdown` 7개 항목의 합과 일치합니다"
        },
        "otherCorporation": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingAmount"
            }
          ],
          "description": "기타법인"
        }
      }
    },
    "InvestorTradingAmount": {
      "type": "object",
      "required": [
        "buyAmount",
        "sellAmount"
      ],
      "properties": {
        "buyAmount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "매수 거래대금 (KRW, 정수)",
          "example": "5200000000000"
        },
        "sellAmount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "매도 거래대금 (KRW, 정수)",
          "example": "5350000000000"
        }
      }
    },
    "InstitutionTradingAmount": {
      "type": "object",
      "required": [
        "buyAmount",
        "sellAmount",
        "breakdown"
      ],
      "properties": {
        "buyAmount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "기관 합계 매수 거래대금 (KRW, 정수). `breakdown` 7개 항목의 `buyAmount` 합과 일치",
          "example": "2100000000000"
        },
        "sellAmount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "기관 합계 매도 거래대금 (KRW, 정수). `breakdown` 7개 항목의 `sellAmount` 합과 일치",
          "example": "2180000000000"
        },
        "breakdown": {
          "$ref": "#/components/schemas/InstitutionTradingBreakdown"
        }
      }
    },
    "InstitutionTradingBreakdown": {
      "type": "object",
      "description": "기관 세부 7개 분류별 매매대금",
      "required": [
        "financialInvestment",
        "insurance",
        "trust",
        "privateEquityFund",
        "bank",
        "otherFinancialInstitution",
        "pensionFund"
      ],
      "properties": {
        "financialInvestment": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingAmount"
            }
          ],
          "description": "금융투자"
        },
        "insurance": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingAmount"
            }
          ],
          "description": "보험"
        },
        "trust": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingAmount"
            }
          ],
          "description": "투신"
        },
        "privateEquityFund": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingAmount"
            }
          ],
          "description": "사모펀드"
        },
        "bank": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingAmount"
            }
          ],
          "description": "은행"
        },
        "otherFinancialInstitution": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingAmount"
            }
          ],
          "description": "기타금융"
        },
        "pensionFund": {
          "allOf": [
            {
              "$ref": "#/components/schemas/InvestorTradingAmount"
            }
          ],
          "description": "연기금"
        }
      }
    },
    "Account": {
      "type": "object",
      "required": [
        "accountNo",
        "accountSeq",
        "accountType"
      ],
      "properties": {
        "accountNo": {
          "type": "string",
          "description": "계좌번호",
          "example": "12345678901"
        },
        "accountSeq": {
          "type": "integer",
          "format": "int64",
          "description": "계좌 식별 키. 주문 등 API 호출 시 이 값을 사용",
          "example": 1
        },
        "accountType": {
          "type": "string",
          "enum": [
            "BROKERAGE",
            "OVERSEAS_DERIVATIVES",
            "PENSION_SAVINGS",
            "RESHORING_INVESTMENT"
          ],
          "description": "계좌 유형. 현재는 BROKERAGE 만 지원합니다.\n- BROKERAGE: 종합매매. 국내·해외 주식 통합 매매 계좌\n- OVERSEAS_DERIVATIVES: 해외파생. 해외 파생상품 거래 계좌\n- PENSION_SAVINGS: 연금저축. 세제혜택 연금저축 계좌\n- RESHORING_INVESTMENT: RIA 계좌\n\n클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.\n",
          "example": "BROKERAGE"
        }
      }
    },
    "HoldingsOverview": {
      "type": "object",
      "required": [
        "totalPurchaseAmount",
        "marketValue",
        "profitLoss",
        "dailyProfitLoss",
        "items"
      ],
      "properties": {
        "totalPurchaseAmount": {
          "description": "투자원금. 전체 보유 종목의 통화별 합산",
          "allOf": [
            {
              "$ref": "#/components/schemas/Price"
            }
          ]
        },
        "marketValue": {
          "$ref": "#/components/schemas/OverviewMarketValue"
        },
        "profitLoss": {
          "$ref": "#/components/schemas/OverviewProfitLoss"
        },
        "dailyProfitLoss": {
          "$ref": "#/components/schemas/OverviewDailyProfitLoss"
        },
        "items": {
          "type": "array",
          "description": "보유 종목 목록. 보유 종목이 없으면 빈 배열",
          "items": {
            "$ref": "#/components/schemas/HoldingsItem"
          }
        }
      }
    },
    "HoldingsItem": {
      "type": "object",
      "required": [
        "symbol",
        "name",
        "marketCountry",
        "currency",
        "quantity",
        "lastPrice",
        "averagePurchasePrice",
        "marketValue",
        "profitLoss",
        "dailyProfitLoss",
        "cost"
      ],
      "properties": {
        "symbol": {
          "type": "string",
          "description": "종목 심볼. KR: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 티커",
          "example": "005930"
        },
        "name": {
          "type": "string",
          "description": "종목명",
          "example": "삼성전자"
        },
        "marketCountry": {
          "$ref": "#/components/schemas/MarketCountry"
        },
        "currency": {
          "$ref": "#/components/schemas/Currency"
        },
        "quantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "보유 수량",
          "example": "100"
        },
        "lastPrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "현재가. 거래 통화(currency) 기준",
          "example": "72000"
        },
        "averagePurchasePrice": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "매수 평균가. 거래 통화(currency) 기준",
          "example": "65000"
        },
        "marketValue": {
          "$ref": "#/components/schemas/MarketValue"
        },
        "profitLoss": {
          "$ref": "#/components/schemas/ProfitLoss"
        },
        "dailyProfitLoss": {
          "$ref": "#/components/schemas/DailyProfitLoss"
        },
        "cost": {
          "$ref": "#/components/schemas/Cost"
        }
      }
    },
    "Price": {
      "type": "object",
      "description": "통화별 합산 금액. 각 통화 필드는 해당 통화로 거래된 종목의 합만 포함합니다 (환율 환산을 통한 통화 간 합산 미포함).",
      "required": [
        "krw"
      ],
      "properties": {
        "krw": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "KRW로 거래되는 국내 종목의 합산 금액. 국내 종목이 없으면 0"
        },
        "usd": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "USD로 거래되는 해외 종목의 합산 금액. 해외 종목이 없으면 null"
        }
      }
    },
    "OverviewMarketValue": {
      "type": "object",
      "description": "시장 평가금액. 전체 보유 종목의 통화별 합산",
      "required": [
        "amount",
        "amountAfterCost"
      ],
      "properties": {
        "amount": {
          "description": "시장 평가금액",
          "allOf": [
            {
              "$ref": "#/components/schemas/Price"
            }
          ]
        },
        "amountAfterCost": {
          "description": "세금/수수료 공제 후 평가금액",
          "allOf": [
            {
              "$ref": "#/components/schemas/Price"
            }
          ]
        }
      }
    },
    "OverviewProfitLoss": {
      "type": "object",
      "description": "손익. 전체 보유 종목의 통화별 합산",
      "required": [
        "amount",
        "amountAfterCost",
        "rate",
        "rateAfterCost"
      ],
      "properties": {
        "amount": {
          "description": "손익금액",
          "allOf": [
            {
              "$ref": "#/components/schemas/Price"
            }
          ]
        },
        "amountAfterCost": {
          "description": "세금/수수료 공제 후 손익금액",
          "allOf": [
            {
              "$ref": "#/components/schemas/Price"
            }
          ]
        },
        "rate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.1516 = 15.16%",
          "example": "0.1516"
        },
        "rateAfterCost": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "세금/수수료 공제 후 손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.1406 = 14.06%",
          "example": "0.1406"
        }
      }
    },
    "OverviewDailyProfitLoss": {
      "type": "object",
      "description": "일간 손익. 전체 보유 종목의 통화별 합산",
      "required": [
        "amount",
        "rate"
      ],
      "properties": {
        "amount": {
          "description": "일간 손익금액",
          "allOf": [
            {
              "$ref": "#/components/schemas/Price"
            }
          ]
        },
        "rate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "일간 손익률 (소수비율). 전체 자산을 현재 환율로 원화 환산한 기준. 0.0185 = 1.85%",
          "example": "0.0185"
        }
      }
    },
    "MarketValue": {
      "type": "object",
      "description": "시장 평가. 거래 통화(currency) 기준",
      "required": [
        "purchaseAmount",
        "amount",
        "amountAfterCost"
      ],
      "properties": {
        "purchaseAmount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "매입금액",
          "example": "6500000"
        },
        "amount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "시장 평가금액",
          "example": "7200000"
        },
        "amountAfterCost": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "세금/수수료 공제 후 평가금액",
          "example": "7050000"
        }
      }
    },
    "ProfitLoss": {
      "type": "object",
      "description": "손익. 거래 통화(currency) 기준",
      "required": [
        "amount",
        "amountAfterCost",
        "rate",
        "rateAfterCost"
      ],
      "properties": {
        "amount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "손익금액",
          "example": "700000"
        },
        "amountAfterCost": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "세금/수수료 공제 후 손익금액",
          "example": "550000"
        },
        "rate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "손익률. 소수비율 (0.1077 = 10.77%)",
          "example": "0.1077"
        },
        "rateAfterCost": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "세금/수수료 공제 후 손익률. 소수비율 (0.0846 = 8.46%)",
          "example": "0.0846"
        }
      }
    },
    "DailyProfitLoss": {
      "type": "object",
      "description": "일간 손익. 거래 통화(currency) 기준",
      "required": [
        "amount",
        "rate"
      ],
      "properties": {
        "amount": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "일간 손익금액",
          "example": "100000"
        },
        "rate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "일간 손익률. 소수비율 (0.0141 = 1.41%)",
          "example": "0.0141"
        }
      }
    },
    "Cost": {
      "type": "object",
      "description": "비용. 거래 통화(currency) 기준",
      "required": [
        "commission"
      ],
      "properties": {
        "commission": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "수수료",
          "example": "14400"
        },
        "tax": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "세금. 세금이 없는 경우 null",
          "example": "135600"
        }
      }
    },
    "OrderCreateRequest": {
      "oneOf": [
        {
          "title": "OrderCreateQuantityBased",
          "description": "수량 기반 주문. quantity 로 주문 수량을 지정.",
          "type": "object",
          "required": [
            "symbol",
            "side",
            "orderType",
            "quantity"
          ],
          "properties": {
            "clientOrderId": {
              "type": "string",
              "maxLength": 36,
              "pattern": "^[a-zA-Z0-9\\-_]+$",
              "description": "클라이언트 지정 주문 식별자. 멱등성 키로 사용됩니다.\n- 미전달: 멱등성 미적용. 매 요청을 별개 주문으로 처리합니다.\n- 전달: 동일 값으로 재요청 시 이전 주문 결과를 그대로 재반환합니다.\n서버는 자동 생성하지 않습니다.\n최대 36자, 영숫자 및 `-`, `_` 허용.\n멱등성 키는 10분간 유효하며, 이후 동일 값으로 재요청 시 새 주문으로 처리됩니다.\n",
              "example": "my-order-001"
            },
            "symbol": {
              "type": "string",
              "description": "종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커",
              "example": "005930"
            },
            "side": {
              "type": "string",
              "enum": [
                "BUY",
                "SELL"
              ],
              "description": "주문 방향",
              "example": "BUY"
            },
            "orderType": {
              "type": "string",
              "enum": [
                "LIMIT",
                "MARKET"
              ],
              "description": "호가 유형.\n- `LIMIT`: 지정가\n- `MARKET`: 시장가\n",
              "example": "LIMIT"
            },
            "timeInForce": {
              "type": "string",
              "enum": [
                "DAY",
                "CLS",
                "OPG"
              ],
              "description": "주문 유효 조건 (Time In Force). 미전달 시 `DAY`. `orderType` 과 결합되어 주문 방식이 결정됩니다 (예: `LIMIT` + `CLS` = LOC).\n- `DAY`: 당일 유효 (Day). 정규장 종료까지 미체결분은 자동 취소됩니다.\n- `CLS`: 장 마감 주문 (At the Close). 현재 미국 주식 + `orderType=LIMIT` 조합만 지원합니다.\n- `OPG`: 장 개시 주문 (At the Opening, 국내 시가단일가). 현재 국내 주식 전용이며 `orderType` 은 `LIMIT`/`MARKET` 모두 지원합니다. 세션 시간(장전 사전접수) 외 접수는 원장에서 거절될 수 있습니다.\n",
              "default": "DAY",
              "example": "DAY"
            },
            "quantity": {
              "type": "string",
              "format": "decimal",
              "pattern": "^\\d+(\\.\\d+)?$",
              "maxLength": 30,
              "description": "주문 수량 (주 단위). 지정한 수량만큼 주문합니다.\n- 기본: 양의 정수만 가능합니다.\n- 소수점 수량: 미국 주식 시장가 매도(`orderType=MARKET` + `side=SELL`) 주문에만 허용됩니다.\n  그 외(매수/지정가/국내) 소수점 수량은 `400 invalid-request` 를 반환합니다.\n  소수점 매수는 `orderAmount` 를 사용하세요.\n  소수점 수량 매도는 정규장 시작부터 정규장 종료 1시간 전까지만 접수 가능하며, 그 외 시간 요청 시 `422 fractional-quantity-outside-regular-hours` 를 반환합니다.\n  소수점 수량은 소수점 6자리까지 지원하며, 초과 시 `400 invalid-request` (`fractional-quantity-scale-exceeded`) 를 반환합니다.\n",
              "example": "10"
            },
            "price": {
              "type": "string",
              "format": "decimal",
              "pattern": "^\\d+(\\.\\d+)?$",
              "maxLength": 30,
              "description": "주문 가격. `orderType`이 `LIMIT` 일 때만 사용합니다.\n- `LIMIT`: 필수. 미전달 시 `400 invalid-request`.\n- `MARKET`: 전달 불가. 전달 시 `400 invalid-request`.\n- KR: 정수 (원 단위). 호가 단위에 맞아야 합니다 (예: 50,000~200,000원 구간은 100원 단위). 맞지 않으면 `400 invalid-request` 에러와 함께 올바른 호가 단위가 `data`에 포함됩니다.\n- US: 소수점 (달러 단위).\n  - $1 미만: 소수점 넷째 자리까지 (그 이하 자릿수는 절삭).\n  - $1 이상: 소수점 둘째 자리까지 (그 이하 자릿수는 절삭).\n",
              "example": "70000"
            },
            "confirmHighValueOrder": {
              "type": "boolean",
              "description": "착오주문 방지를 위한 주문 확인 플래그. 기본값 `false`.\n1억원 이상의 주문 시 `true`가 아니면 `400 confirm-high-value-required` 에러를 반환합니다.\n사용자가 해당 주문의 금액을 인지하고 있음을 표시하기 위한 필드입니다.\n",
              "default": false,
              "example": false
            }
          }
        },
        {
          "title": "OrderCreateAmountBased",
          "description": "금액 기반 주문 (US MARKET 전용). orderAmount 로 주문 금액을 지정.",
          "type": "object",
          "required": [
            "symbol",
            "side",
            "orderType",
            "orderAmount"
          ],
          "properties": {
            "clientOrderId": {
              "type": "string",
              "maxLength": 36,
              "pattern": "^[a-zA-Z0-9\\-_]+$",
              "description": "클라이언트 지정 주문 식별자. 멱등성 키로 사용됩니다.\n- 미전달: 멱등성 미적용. 매 요청을 별개 주문으로 처리합니다.\n- 전달: 동일 값으로 재요청 시 이전 주문 결과를 그대로 재반환합니다.\n서버는 자동 생성하지 않습니다.\n최대 36자, 영숫자 및 `-`, `_` 허용.\n멱등성 키는 10분간 유효하며, 이후 동일 값으로 재요청 시 새 주문으로 처리됩니다.\n",
              "example": "my-order-001"
            },
            "symbol": {
              "type": "string",
              "description": "US 종목 심볼 (영문 티커). 금액 기반 주문은 US MARKET 전용입니다.",
              "example": "AAPL"
            },
            "side": {
              "type": "string",
              "enum": [
                "BUY",
                "SELL"
              ],
              "description": "주문 방향",
              "example": "BUY"
            },
            "orderType": {
              "type": "string",
              "enum": [
                "MARKET"
              ],
              "description": "호가 유형. 금액 기반 주문은 `MARKET` 만 허용합니다.",
              "example": "MARKET"
            },
            "orderAmount": {
              "type": "string",
              "format": "decimal",
              "pattern": "^\\d+(\\.\\d+)?$",
              "maxLength": 30,
              "description": "주문 금액 (달러). 지정한 금액만큼 주문합니다.\n체결 수량은 체결 시점의 시장가에 따라 결정됩니다.\n\nQuantity-based 와의 차이: quantity 는 수량을 확정하고 비용이 변동하며,\norderAmount 는 금액을 확정하고 수량이 변동합니다.\n\n정규장 시작부터 정규장 종료 1시간 전까지만 접수 가능합니다.\n그 외 시간 요청 시 `422 amount-order-outside-regular-hours` 에러를 반환합니다.\n",
              "example": "100.5"
            },
            "confirmHighValueOrder": {
              "type": "boolean",
              "description": "착오주문 방지를 위한 주문 확인 플래그. 기본값 `false`.\n1억원 이상의 주문 시 `true`가 아니면 `400 confirm-high-value-required` 에러를 반환합니다.\n사용자가 해당 주문의 금액을 인지하고 있음을 표시하기 위한 필드입니다.\n",
              "default": false,
              "example": false
            }
          }
        }
      ]
    },
    "OrderModifyRequest": {
      "type": "object",
      "required": [
        "orderType"
      ],
      "properties": {
        "orderType": {
          "type": "string",
          "enum": [
            "LIMIT",
            "MARKET"
          ],
          "description": "변경할 호가 유형.\n- `LIMIT`: 지정가\n- `MARKET`: 시장가\n",
          "example": "LIMIT"
        },
        "quantity": {
          "type": "string",
          "format": "decimal",
          "pattern": "^\\d+$",
          "maxLength": 30,
          "description": "변경할 수량.\n**KR 주식: 필수.** 양의 정수만 허용합니다 (미전달/0/음수/소수점은 `400 invalid-request`).\nUS 주식: 전달 불가. 제공 시 `400 us-modify-quantity-not-supported` 에러.\n",
          "example": "15"
        },
        "price": {
          "type": "string",
          "format": "decimal",
          "pattern": "^\\d+(\\.\\d+)?$",
          "maxLength": 30,
          "description": "변경할 가격. `orderType`이 `LIMIT` 일 때만 사용합니다.\n- `LIMIT`: 필수. 미전달 시 `400 invalid-request`.\n- `MARKET`: 전달 불가. 전달 시 `400 invalid-request`.\n- KR: 정수 (원 단위). 호가 단위에 맞아야 합니다. 맞지 않으면 `400 invalid-request` 에러.\n- US: 소수점 (달러 단위).\n  - $1 미만: 소수점 넷째 자리까지 (그 이하 자릿수는 절삭).\n  - $1 이상: 소수점 둘째 자리까지 (그 이하 자릿수는 절삭).\n",
          "example": "71000"
        },
        "confirmHighValueOrder": {
          "type": "boolean",
          "description": "착오주문 방지를 위한 주문 확인 플래그. 기본값 `false`.\n1억원 이상의 주문 시 `true`가 아니면 `400 confirm-high-value-required` 에러를 반환합니다.\n사용자가 해당 주문의 금액을 인지하고 있음을 표시하기 위한 필드입니다.\n30억원 이상의 주문은 본 플래그와 무관하게 `422 max-order-amount-exceeded` 에러를 반환합니다.\n",
          "default": false,
          "example": false
        }
      }
    },
    "OrderResponse": {
      "type": "object",
      "required": [
        "orderId"
      ],
      "properties": {
        "orderId": {
          "type": "string",
          "description": "서버 생성 주문 식별자. 정정/취소 시 사용",
          "example": "0d5QIHjmtksbsmM-hBRAgP-ExI8iodGm9fAR5txelPfnMM8XQ_swoJdwL5RpGWMo"
        },
        "clientOrderId": {
          "type": [
            "string",
            "null"
          ],
          "description": "요청 시 전달한 값 그대로 반환. 미전달 시 `null`.",
          "example": "my-order-001"
        }
      }
    },
    "OrderOperationResponse": {
      "type": "object",
      "required": [
        "orderId"
      ],
      "properties": {
        "orderId": {
          "type": "string",
          "description": "정정/취소로 새로 발급된 주문 식별자. 원주문의 orderId 와 다릅니다.\n",
          "example": "5nfzdqmzfnAw3LFXWHPRy0UNi7y_WZlphJh5hRIsi25-NIfm_GtQgXima5QD2hUz"
        }
      }
    },
    "ConditionalOrderCreateRequest": {
      "type": "object",
      "required": [
        "symbol",
        "type",
        "quantity",
        "orderType",
        "expireDate",
        "first"
      ],
      "properties": {
        "symbol": {
          "type": "string",
          "description": "종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커",
          "example": "005930"
        },
        "type": {
          "type": "string",
          "enum": [
            "SINGLE",
            "OCO",
            "OTO"
          ],
          "description": "조건주문 타입 (조건의 개수와 관계).\n- `SINGLE`: 한 조건만 감시\n- `OCO` (One-Cancels-the-Other): 두 조건을 동시에 감시, 하나의 조건 충족 시 나머지 조건 자동 취소\n- `OTO` (One-Triggers-the-Other): `first` 조건 체결 후 `second` 조건 감시 시작\n",
          "example": "OCO"
        },
        "quantity": {
          "type": "string",
          "format": "decimal",
          "pattern": "^\\d+(\\.\\d+)?$",
          "maxLength": 30,
          "description": "매매 수량 (주 단위). 조건주문 그룹 공통값 — OCO/OTO 는 동일 포지션이라 first/second 가 같은 수량을 씁니다.",
          "example": "100"
        },
        "orderType": {
          "type": "string",
          "enum": [
            "LIMIT",
            "MARKET"
          ],
          "description": "호가유형 (그룹 공통). `LIMIT`(지정가) 이면 각 조건의 `orderPrice` 가 필수이고, `MARKET`(시장가) 이면 `orderPrice` 를 지정할 수 없습니다.\nOCO/OTO 는 지정가(`LIMIT`)만 지원합니다.\n",
          "example": "LIMIT"
        },
        "clientOrderId": {
          "type": "string",
          "maxLength": 36,
          "pattern": "^[a-zA-Z0-9\\-_]+$",
          "description": "멱등키 (선택) — 주문 생성 API 와 동일. 동일한 값으로 재요청 시 중복 생성을 방지합니다.",
          "example": "my-order-001"
        },
        "expireDate": {
          "type": "string",
          "format": "date",
          "description": "조건주문 만료일 (YYYY-MM-DD, 필수). 만료일까지 조건이 충족되지 않으면 자동 만료됩니다.",
          "example": "2026-09-10"
        },
        "first": {
          "allOf": [
            {
              "$ref": "#/components/schemas/ConditionRequest"
            }
          ],
          "description": "첫번째 감시 조건 (필수). OTO 는 먼저 감시할 부모 조건입니다."
        },
        "second": {
          "allOf": [
            {
              "$ref": "#/components/schemas/ConditionRequest"
            }
          ],
          "description": "두번째 감시 조건. SINGLE 은 생략(설정하지 않음), OCO/OTO 는 필수. 그 외 구조·규칙은 first 와 동일합니다.",
          "nullable": true
        },
        "confirmHighValueOrder": {
          "type": "boolean",
          "default": false,
          "description": "1억원 이상 주문 동의 여부"
        }
      },
      "description": "조건주문 생성 요청. \"이 가격(triggerPrice)에 닿으면 매수/매도(orderSide) 주문\" 만 입력하면 됩니다.\n가격이 감시가(triggerPrice)에 닿으면 트리거됩니다.\n타입은 `type`(SINGLE/OCO/OTO)으로 지정합니다.\n"
    },
    "ConditionalOrderModifyRequest": {
      "type": "object",
      "required": [
        "type",
        "quantity",
        "orderType",
        "expireDate",
        "first"
      ],
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "SINGLE",
            "OCO",
            "OTO"
          ],
          "description": "변경 결과 타입. 수정 시 타입 전환(예: SINGLE→OCO)이 허용됩니다.\n",
          "example": "OCO"
        },
        "quantity": {
          "type": "string",
          "format": "decimal",
          "pattern": "^\\d+(\\.\\d+)?$",
          "maxLength": 30,
          "description": "매매 수량 (주 단위, 그룹 공통).",
          "example": "100"
        },
        "orderType": {
          "type": "string",
          "enum": [
            "LIMIT",
            "MARKET"
          ],
          "description": "호가유형 (그룹 공통). LIMIT(지정가)/MARKET(시장가). OCO/OTO 는 지정가만 지원합니다.",
          "example": "LIMIT"
        },
        "expireDate": {
          "type": "string",
          "format": "date",
          "description": "조건주문 만료일 (수정 시 필수)",
          "example": "2026-09-10"
        },
        "first": {
          "allOf": [
            {
              "$ref": "#/components/schemas/ConditionRequest"
            }
          ],
          "description": "첫번째 감시 조건 (필수). OTO 는 먼저 감시할 부모 조건입니다."
        },
        "second": {
          "allOf": [
            {
              "$ref": "#/components/schemas/ConditionRequest"
            }
          ],
          "description": "두번째 감시 조건. SINGLE 은 생략(설정하지 않음), OCO/OTO 는 필수. 그 외 구조·규칙은 first 와 동일합니다.",
          "nullable": true
        },
        "confirmHighValueOrder": {
          "type": "boolean",
          "default": false,
          "description": "1억원 이상 주문 동의 여부"
        }
      },
      "description": "조건주문 수정 요청. 등록과 동일하게 \"이 가격에 닿으면 매매\" 만 입력하며,\n조건주문 전체를 재설정하므로 유지할 조건도 함께 전달해야 합니다.\n종목은 `conditionalOrderId` 로 식별되므로 수정 요청에는 `symbol` 이 필요 없습니다.\n"
    },
    "ConditionRequest": {
      "type": "object",
      "required": [
        "orderSide",
        "triggerPrice"
      ],
      "description": "감시 조건 (leg). 가격이 `triggerPrice` 에 닿으면 `orderSide`(매수/매도) 주문을 냅니다.\n수량(`quantity`)·호가유형(`orderType`)은 그룹 공통이라 상위 요청에 있습니다.\n호가유형이 `LIMIT` 이면 `orderPrice` 가 필수이고, `MARKET` 이면 `orderPrice` 를 보내면 안 됩니다.\n`orderPrice` 는 호가 단위에 맞아야 하며, 맞지 않으면 `400 invalid-request` 에러와 함께 올바른 호가 단위가 `data`에 포함됩니다.\n",
      "properties": {
        "orderSide": {
          "type": "string",
          "enum": [
            "BUY",
            "SELL"
          ],
          "description": "매매 유형 (매수/매도)",
          "example": "SELL"
        },
        "triggerPrice": {
          "type": "string",
          "format": "decimal",
          "pattern": "^\\d+(\\.\\d+)?$",
          "maxLength": 30,
          "description": "감시 가격. 현재가가 이 값에 닿으면 주문을 생성합니다.",
          "example": "305"
        },
        "orderPrice": {
          "type": "string",
          "format": "decimal",
          "pattern": "^\\d+(\\.\\d+)?$",
          "maxLength": 30,
          "description": "[orderType=LIMIT] 주문 가격(지정가). 트리거 시 이 가격의 지정가 주문을 생성합니다. MARKET 이면 보내지 않습니다.\n- KR: 정수 (원 단위). 호가 단위에 맞아야 합니다 (예: 50,000~200,000원 구간은 100원 단위).\n- US: 소수점 (달러 단위). 호가 단위에 맞아야 합니다 ($1 미만은 0.0001, $1 이상은 0.01 단위).\n\n호가 단위에 맞지 않으면 `400 invalid-request` 에러와 함께 올바른 호가 단위가 `data`에 포함됩니다.\n",
          "example": "305"
        }
      }
    },
    "ConditionalOrderResponse": {
      "type": "object",
      "required": [
        "conditionalOrderId"
      ],
      "description": "조건주문 수정·취소 응답. 대상 조건주문 식별자만 반환합니다.",
      "properties": {
        "conditionalOrderId": {
          "type": "string",
          "description": "조건주문 식별자",
          "example": "gaZIG-dYMWil8AAXyPmlRg"
        }
      }
    },
    "PaginatedConditionalOrderResponse": {
      "type": "object",
      "required": [
        "conditionalOrders",
        "hasNext"
      ],
      "properties": {
        "conditionalOrders": {
          "type": "array",
          "items": {
            "$ref": "#/components/schemas/ConditionalOrderDetailResponse"
          }
        },
        "nextCursor": {
          "type": [
            "string",
            "null"
          ],
          "description": "다음 페이지 커서. 마지막 페이지면 null."
        },
        "hasNext": {
          "type": "boolean",
          "description": "다음 페이지 존재 여부"
        }
      }
    },
    "ConditionalOrderDetailResponse": {
      "type": "object",
      "required": [
        "conditionalOrderId",
        "type",
        "status",
        "symbol",
        "market",
        "quantity",
        "orderType",
        "first",
        "createdAt"
      ],
      "description": "조건주문 조회 응답 (목록 항목 / 상세 공용). 모든 타입을 단일 스키마로 표현하며,\n감시 조건은 `first`/`second` 로 내려갑니다 (SINGLE 은 `first` 만, OCO/OTO 는 `second` 도 존재).\n",
      "properties": {
        "conditionalOrderId": {
          "type": "string",
          "description": "조건주문 식별자. 상세 조회·수정·취소에 사용합니다.\n",
          "example": "gaZIG-dYMWil8AAXyPmlRg"
        },
        "type": {
          "type": "string",
          "enum": [
            "SINGLE",
            "OCO",
            "OTO"
          ],
          "description": "조건주문 타입.\n- `SINGLE`: 한 조건만 감시\n- `OCO` (One-Cancels-the-Other): 두 조건을 동시에 감시, 하나의 조건 충족 시 나머지 조건 자동 취소\n- `OTO` (One-Triggers-the-Other): `first` 조건 체결 후 `second` 조건 감시 시작\n",
          "example": "OCO"
        },
        "status": {
          "type": "string",
          "enum": [
            "WATCHING",
            "PAUSED",
            "ORDERING",
            "ORDERED",
            "COMPLETED",
            "EXPIRED"
          ],
          "description": "조건주문(그룹) 상태 — 살아있는 조건(leg)의 상태를 대표로 따릅니다.\nleg 전용 상태인 `HOLDING`·`CANCELED` 는 최상위 status 로는 내려오지 않습니다 (조건별 상태 `first.status`/`second.status` 에서만 노출).\n- `WATCHING`: 조건 감시 중\n- `PAUSED`: 일시중지\n- `ORDERING`: 조건 충족 — 주문 생성 진행 중\n- `ORDERED`: 주문 생성됨\n- `COMPLETED`: 완료\n- `EXPIRED`: 만료\n",
          "example": "WATCHING"
        },
        "symbol": {
          "type": "string",
          "description": "종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커",
          "example": "005930"
        },
        "market": {
          "type": "string",
          "enum": [
            "KR",
            "US"
          ],
          "description": "시장 구분",
          "example": "KR"
        },
        "quantity": {
          "type": "string",
          "format": "decimal",
          "description": "매매 수량 (주 단위, 그룹 공통).",
          "example": "100"
        },
        "orderType": {
          "type": "string",
          "enum": [
            "LIMIT",
            "MARKET"
          ],
          "description": "호가유형 (그룹 공통). LIMIT(지정가)/MARKET(시장가).",
          "example": "LIMIT"
        },
        "expireDate": {
          "type": "string",
          "format": "date",
          "description": "조건주문 만료일 (조건주문 1건의 모든 감시 조건이 공유). 이 날짜까지 미충족 시 자동 만료됩니다.",
          "example": "2026-09-10"
        },
        "first": {
          "allOf": [
            {
              "$ref": "#/components/schemas/ConditionalOrderCondition"
            }
          ],
          "description": "첫번째 감시 조건 (OTO 는 부모)"
        },
        "second": {
          "allOf": [
            {
              "$ref": "#/components/schemas/ConditionalOrderCondition"
            }
          ],
          "description": "두번째 감시 조건. OCO/OTO 만 존재하며 단일(SINGLE)은 null.",
          "nullable": true
        },
        "createdAt": {
          "type": "string",
          "format": "date-time",
          "description": "조건주문 등록 시각 (KST)",
          "example": "2026-06-12T09:00:00+09:00"
        }
      }
    },
    "ConditionalOrderCondition": {
      "type": "object",
      "required": [
        "type",
        "status"
      ],
      "properties": {
        "type": {
          "type": "string",
          "enum": [
            "STOP",
            "PROFIT_RATE"
          ],
          "description": "감시 조건 세부 타입 (그룹 타입을 구성하는 단위).\n- `STOP`: 가격 트리거\n- `PROFIT_RATE`: 목표 수익률(%) 트리거\n\n그룹(OCO/OTO)의 `first` 와 `second` 는 항상 동일한 타입입니다.\n",
          "example": "STOP"
        },
        "status": {
          "type": "string",
          "enum": [
            "WATCHING",
            "HOLDING",
            "PAUSED",
            "ORDERING",
            "ORDERED",
            "COMPLETED",
            "EXPIRED",
            "CANCELED"
          ],
          "description": "조건(leg) 단위 상태. 최상위 조건주문 `status` 와 달리 leg 전용인 `HOLDING`·`CANCELED` 를 포함합니다.\n- `HOLDING`: 선행 조건(OTO first) 체결 전 대기 (leg 전용)\n- `CANCELED`: 취소됨 (완료된 OCO 에서 자동취소된 반대편 조건)\n",
          "example": "WATCHING"
        },
        "triggerPrice": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "description": "이 가격에 닿으면 트리거됩니다.\n현재 지원 조건은 항상 값이 존재하나, 향후 수익률(PROFIT_RATE)·추종형 조건은 고정 트리거가가 없어 null 일 수 있습니다.\n",
          "example": "295"
        },
        "targetProfitRate": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "description": "[PROFIT_RATE 전용] 감시 수익률. **퍼센트(%) 단위**입니다 (예: `10.5` = +10.5%).\nPROFIT_RATE 이 아닌 조건이면 null.\n",
          "example": "10.5"
        },
        "orderPrice": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "description": "주문 가격(지정가). 그룹 호가유형(orderType)이 LIMIT 이면 값이 있고, MARKET 이면 null.",
          "example": "294.5"
        },
        "triggeredOrderId": {
          "type": [
            "string",
            "null"
          ],
          "description": "조건 충족으로 생성된 주문의 ID. 일반 주문 API(`GET /orders/{orderId}` 등)에 그대로 사용할 수 있습니다. 주문 생성 전이면 null.\n"
        }
      }
    },
    "PaginatedOrderResponse": {
      "type": "object",
      "required": [
        "orders",
        "nextCursor",
        "hasNext"
      ],
      "description": "주문 목록 페이징 응답.\n- `status=OPEN`: 모든 대기 중 주문을 반환합니다. `nextCursor`는 항상 `null`, `hasNext`는 항상 `false`.\n- `status=CLOSED`: `limit` 단위로 페이징합니다. 다음 페이지가 있으면 `nextCursor`에 커서가, `hasNext`에 `true`가 내려옵니다.\n",
      "properties": {
        "orders": {
          "type": "array",
          "items": {
            "$ref": "#/components/schemas/Order"
          },
          "description": "주문 목록"
        },
        "nextCursor": {
          "type": [
            "string",
            "null"
          ],
          "description": "다음 페이지 커서. 다음 페이지가 없으면 null",
          "example": null
        },
        "hasNext": {
          "type": "boolean",
          "description": "다음 페이지 존재 여부",
          "example": false
        }
      }
    },
    "Order": {
      "type": "object",
      "required": [
        "orderId",
        "symbol",
        "side",
        "orderType",
        "timeInForce",
        "status",
        "quantity",
        "currency",
        "orderedAt",
        "execution"
      ],
      "properties": {
        "orderId": {
          "type": "string",
          "description": "주문 식별자",
          "example": "bAGzNvMOOTa5Uy0xVzYNbxDJ3Qpobwau4jDF3hyZZGWbpHm7wha8CFZc7aXVOWAl"
        },
        "symbol": {
          "type": "string",
          "description": "종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커",
          "example": "005930"
        },
        "side": {
          "type": "string",
          "enum": [
            "BUY",
            "SELL"
          ],
          "description": "주문 방향",
          "example": "BUY"
        },
        "orderType": {
          "type": "string",
          "enum": [
            "LIMIT",
            "MARKET"
          ],
          "description": "호가 유형.\n- `LIMIT`: 지정가\n- `MARKET`: 시장가\n\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n",
          "example": "LIMIT"
        },
        "timeInForce": {
          "type": "string",
          "enum": [
            "DAY",
            "CLS",
            "OPG"
          ],
          "description": "주문 유효 조건 (Time In Force). `orderType` 과 결합되어 주문 방식이 결정됩니다 (예: `LIMIT` + `CLS` = LOC).\n- `DAY`: 당일 유효 (Day)\n- `CLS`: 장 마감 주문 (At the Close)\n- `OPG`: 장 개시 주문 (At the Opening, 국내 시가단일가)\n\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n",
          "example": "DAY"
        },
        "status": {
          "$ref": "#/components/schemas/OrderStatus"
        },
        "price": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "주문 가격 (native currency). MARKET 주문 시 null",
          "example": "70000"
        },
        "quantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "주문 수량",
          "example": "10"
        },
        "orderAmount": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "주문 금액 (USD). 금액 기반 US 시장가 매수 주문에만 해당. 그 외 null",
          "example": null
        },
        "currency": {
          "$ref": "#/components/schemas/Currency",
          "example": "KRW"
        },
        "orderedAt": {
          "type": "string",
          "format": "date-time",
          "description": "주문 시간 (ISO 8601, KST)",
          "example": "2026-03-29T09:30:00.000+09:00"
        },
        "canceledAt": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time",
          "description": "취소 시간 (ISO 8601, KST). 해당 없으면 null",
          "example": null
        },
        "execution": {
          "type": "object",
          "description": "체결 결과. 체결 내역이 없으면 filledQuantity=0",
          "allOf": [
            {
              "$ref": "#/components/schemas/OrderExecution"
            }
          ]
        }
      }
    },
    "OrderExecution": {
      "type": "object",
      "required": [
        "filledQuantity",
        "averageFilledPrice",
        "filledAmount",
        "commission",
        "tax",
        "filledAt",
        "settlementDate"
      ],
      "properties": {
        "filledQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "체결 수량",
          "example": "10"
        },
        "averageFilledPrice": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "평균 체결 가격 (native currency). 부분 체결 시 체결된 건의 평균, 미체결 시 null",
          "example": "70000"
        },
        "filledAmount": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "총 체결 금액 (native currency)",
          "example": "700000"
        },
        "commission": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "총 체결 수수료 (native currency)",
          "example": "1400"
        },
        "tax": {
          "type": [
            "string",
            "null"
          ],
          "format": "decimal",
          "maxLength": 30,
          "description": "총 체결 세금 (native currency)",
          "example": "0"
        },
        "filledAt": {
          "type": [
            "string",
            "null"
          ],
          "format": "date-time",
          "description": "최종 체결 시간 (ISO 8601, KST)",
          "example": "2026-03-28T09:31:15.000+09:00"
        },
        "settlementDate": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "결제 예정일 (YYYY-MM-DD, KST 기준). 미결제 시 null",
          "example": "2026-03-30"
        }
      }
    },
    "OrderStatus": {
      "type": "string",
      "enum": [
        "PENDING",
        "PENDING_CANCEL",
        "PENDING_REPLACE",
        "PARTIAL_FILLED",
        "FILLED",
        "CANCELED",
        "REJECTED",
        "CANCEL_REJECTED",
        "REPLACE_REJECTED",
        "REPLACED"
      ],
      "description": "주문 상태.\n- `PENDING`: 체결 대기. 주문이 접수되어 체결을 대기 중인 상태\n- `PENDING_CANCEL`: 취소 대기. 취소 요청이 접수되어 브로커 응답을 대기 중인 상태\n- `PENDING_REPLACE`: 정정 대기. 정정 요청이 접수되어 브로커 응답을 대기 중인 상태\n- `PARTIAL_FILLED`: 부분 체결. 주문 수량 중 일부만 체결된 상태\n- `FILLED`: 체결 완료. 주문 수량이 전량 체결된 상태\n- `CANCELED`: 취소 완료. execution.filledQuantity를 통해 부분 체결 여부를 확인할 수 있음\n- `REJECTED`: 거부됨. 브로커가 주문을 거부한 상태. execution.filledQuantity를 통해 부분 체결 여부를 확인할 수 있음\n- `CANCEL_REJECTED`: 취소 거부. 브로커가 취소 요청을 거부한 경우 별도 주문 레코드로 생성됨. 원주문은 이전 상태로 복귀함\n- `REPLACE_REJECTED`: 정정 거부. 브로커가 정정 요청을 거부한 경우 별도 주문 레코드로 생성됨. 원주문은 이전 상태로 복귀함\n- `REPLACED`: 정정됨. 정정 요청이 수락되어 원주문이 대체된 상태. execution.filledQuantity를 통해 부분 체결 여부를 확인할 수 있음\n\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n",
      "example": "FILLED"
    },
    "BuyingPowerResponse": {
      "type": "object",
      "required": [
        "currency",
        "cashBuyingPower"
      ],
      "properties": {
        "currency": {
          "$ref": "#/components/schemas/Currency"
        },
        "cashBuyingPower": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "현금 기반 매수 가능 금액 (미수 미발생 기준).\n순수 현금으로 매수할 수 있는 금액.\nKRW: 정수 (원 단위). USD: 소수점 포함 (달러 단위).\n",
          "example": "5000000"
        }
      }
    },
    "SellableQuantityResponse": {
      "type": "object",
      "required": [
        "sellableQuantity"
      ],
      "properties": {
        "sellableQuantity": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "판매 가능 수량.\nKR: 정수 (주 단위). US: 소수점 포함 가능 (주 단위).\n",
          "example": "100"
        }
      }
    },
    "Commission": {
      "type": "object",
      "required": [
        "marketCountry",
        "commissionRate"
      ],
      "properties": {
        "marketCountry": {
          "$ref": "#/components/schemas/MarketCountry"
        },
        "commissionRate": {
          "type": "string",
          "format": "decimal",
          "maxLength": 30,
          "description": "매매 수수료율 (소수 비율). 예: `0.00015` = 0.015%",
          "example": "0.00015"
        },
        "startDate": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "수수료 적용 시작일 (YYYY-MM-DD, KST 기준). 해외주식은 null",
          "example": "2026-01-01"
        },
        "endDate": {
          "type": [
            "string",
            "null"
          ],
          "format": "date",
          "description": "수수료 적용 종료일 (YYYY-MM-DD, KST 기준). 무기한 적용 시 null",
          "example": "2026-12-31"
        }
      }
    },
    "ConditionalOrderCreateResponse": {
      "type": "object",
      "required": [
        "conditionalOrderId"
      ],
      "description": "조건주문 생성 응답.",
      "properties": {
        "conditionalOrderId": {
          "type": "string",
          "description": "서버가 생성한 조건주문 식별자. 이후 조회·수정·취소에 사용합니다.",
          "example": "gaZIG-dYMWil8AAXyPmlRg"
        },
        "clientOrderId": {
          "type": [
            "string",
            "null"
          ],
          "description": "요청에 사용한 멱등키(`clientOrderId`)를 그대로 반환합니다. 요청에 없었으면 null.",
          "example": "my-order-001"
        }
      }
    }
  }
}
````

- [ApiResponse](MODEL_API_RESPONSE.md)
- [ErrorResponse](MODEL_ERROR_RESPONSE.md)
- [ApiError](MODEL_API_ERROR.md)
- [Currency](MODEL_CURRENCY.md)
- [MarketCountry](MODEL_MARKET_COUNTRY.md)
- OAuth2TokenRequest
- [OAuth2TokenResponse](MODEL_O_AUTH2_TOKEN_RESPONSE.md)
- [OAuth2ErrorResponse](MODEL_O_AUTH2_ERROR_RESPONSE.md)
- [OrderbookEntry](MODEL_ORDERBOOK_ENTRY.md)
- [OrderbookResponse](MODEL_ORDERBOOK_RESPONSE.md)
- [PriceResponse](MODEL_PRICE_RESPONSE.md)
- [Trade](MODEL_TRADE.md)
- [PriceLimitResponse](MODEL_PRICE_LIMIT_RESPONSE.md)
- [CandlePageResponse](MODEL_CANDLE_PAGE_RESPONSE.md)
- [Candle](MODEL_CANDLE.md)
- [StockInfo](MODEL_STOCK_INFO.md)
- [KrMarketDetail](MODEL_KR_MARKET_DETAIL.md)
- [StockWarning](MODEL_STOCK_WARNING.md)
- [ListedStock](MODEL_LISTED_STOCK.md)
- [StockInvestorTradingResponse](MODEL_STOCK_INVESTOR_TRADING_RESPONSE.md)
- [StockInvestorTradingRecord](MODEL_STOCK_INVESTOR_TRADING_RECORD.md)
- [InvestorTradingVolume](MODEL_INVESTOR_TRADING_VOLUME.md)
- [StockInstitutionTradingVolume](MODEL_STOCK_INSTITUTION_TRADING_VOLUME.md)
- [StockInstitutionTradingBreakdown](MODEL_STOCK_INSTITUTION_TRADING_BREAKDOWN.md)
- [ForeignerHolding](MODEL_FOREIGNER_HOLDING.md)
- [CfdBalance](MODEL_CFD_BALANCE.md)
- [ProgramTradesResponse](MODEL_PROGRAM_TRADES_RESPONSE.md)
- [ProgramTradeRecord](MODEL_PROGRAM_TRADE_RECORD.md)
- [ProgramTradingVolume](MODEL_PROGRAM_TRADING_VOLUME.md)
- [ShortSellingResponse](MODEL_SHORT_SELLING_RESPONSE.md)
- [ShortSellingRecord](MODEL_SHORT_SELLING_RECORD.md)
- [CreditTradesResponse](MODEL_CREDIT_TRADES_RESPONSE.md)
- [CreditTradeRecord](MODEL_CREDIT_TRADE_RECORD.md)
- [CreditTradeDetail](MODEL_CREDIT_TRADE_DETAIL.md)
- [SecuritiesLendingResponse](MODEL_SECURITIES_LENDING_RESPONSE.md)
- [SecuritiesLendingRecord](MODEL_SECURITIES_LENDING_RECORD.md)
- [ExchangeRateResponse](MODEL_EXCHANGE_RATE_RESPONSE.md)
- [KrMarketCalendarResponse](MODEL_KR_MARKET_CALENDAR_RESPONSE.md)
- [KrMarketDay](MODEL_KR_MARKET_DAY.md)
- [IntegratedHour](MODEL_INTEGRATED_HOUR.md)
- [PreMarketSession](MODEL_PRE_MARKET_SESSION.md)
- [RegularMarketSession](MODEL_REGULAR_MARKET_SESSION.md)
- [AfterMarketSession](MODEL_AFTER_MARKET_SESSION.md)
- [UsMarketCalendarResponse](MODEL_US_MARKET_CALENDAR_RESPONSE.md)
- [UsMarketDay](MODEL_US_MARKET_DAY.md)
- [UsDayMarketSession](MODEL_US_DAY_MARKET_SESSION.md)
- [UsPreMarketSession](MODEL_US_PRE_MARKET_SESSION.md)
- [UsRegularMarketSession](MODEL_US_REGULAR_MARKET_SESSION.md)
- [UsAfterMarketSession](MODEL_US_AFTER_MARKET_SESSION.md)
- [RankingResponse](MODEL_RANKING_RESPONSE.md)
- [RankingItem](MODEL_RANKING_ITEM.md)
- [RankingPrice](MODEL_RANKING_PRICE.md)
- [MarketIndicatorPriceResponse](MODEL_MARKET_INDICATOR_PRICE_RESPONSE.md)
- [MarketIndicatorCandlePageResponse](MODEL_MARKET_INDICATOR_CANDLE_PAGE_RESPONSE.md)
- [MarketIndicatorCandle](MODEL_MARKET_INDICATOR_CANDLE.md)
- [InvestorTradingResponse](MODEL_INVESTOR_TRADING_RESPONSE.md)
- [InvestorTradingRecord](MODEL_INVESTOR_TRADING_RECORD.md)
- [InvestorTradingAmount](MODEL_INVESTOR_TRADING_AMOUNT.md)
- [InstitutionTradingAmount](MODEL_INSTITUTION_TRADING_AMOUNT.md)
- [InstitutionTradingBreakdown](MODEL_INSTITUTION_TRADING_BREAKDOWN.md)
- [Account](MODEL_ACCOUNT.md)
- [HoldingsOverview](MODEL_HOLDINGS_OVERVIEW.md)
- [HoldingsItem](MODEL_HOLDINGS_ITEM.md)
- [Price](MODEL_PRICE.md)
- [OverviewMarketValue](MODEL_OVERVIEW_MARKET_VALUE.md)
- [OverviewProfitLoss](MODEL_OVERVIEW_PROFIT_LOSS.md)
- [OverviewDailyProfitLoss](MODEL_OVERVIEW_DAILY_PROFIT_LOSS.md)
- [MarketValue](MODEL_MARKET_VALUE.md)
- [ProfitLoss](MODEL_PROFIT_LOSS.md)
- [DailyProfitLoss](MODEL_DAILY_PROFIT_LOSS.md)
- [Cost](MODEL_COST.md)
- [OrderCreateRequest](MODEL_ORDER_CREATE_REQUEST.md)
- [OrderModifyRequest](MODEL_ORDER_MODIFY_REQUEST.md)
- [OrderResponse](MODEL_ORDER_RESPONSE.md)
- [OrderOperationResponse](MODEL_ORDER_OPERATION_RESPONSE.md)
- [ConditionalOrderCreateRequest](MODEL_CONDITIONAL_ORDER_CREATE_REQUEST.md)
- [ConditionalOrderModifyRequest](MODEL_CONDITIONAL_ORDER_MODIFY_REQUEST.md)
- [ConditionRequest](MODEL_CONDITION_REQUEST.md)
- [ConditionalOrderResponse](MODEL_CONDITIONAL_ORDER_RESPONSE.md)
- [PaginatedConditionalOrderResponse](MODEL_PAGINATED_CONDITIONAL_ORDER_RESPONSE.md)
- [ConditionalOrderDetailResponse](MODEL_CONDITIONAL_ORDER_DETAIL_RESPONSE.md)
- [ConditionalOrderCondition](MODEL_CONDITIONAL_ORDER_CONDITION.md)
- [PaginatedOrderResponse](MODEL_PAGINATED_ORDER_RESPONSE.md)
- [Order](MODEL_ORDER.md)
- [OrderExecution](MODEL_ORDER_EXECUTION.md)
- [OrderStatus](MODEL_ORDER_STATUS.md)
- [BuyingPowerResponse](MODEL_BUYING_POWER_RESPONSE.md)
- [SellableQuantityResponse](MODEL_SELLABLE_QUANTITY_RESPONSE.md)
- [Commission](MODEL_COMMISSION.md)
- [ConditionalOrderCreateResponse](MODEL_CONDITIONAL_ORDER_CREATE_RESPONSE.md)
- [OAuth2TokenRequest](MODEL_O_AUTH2_TOKEN_REQUEST.md)
