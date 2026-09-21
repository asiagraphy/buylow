> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/AuthApi.md
> 문서 버전: 1.2.17

# AuthApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**issueOAuth2Token**](AUTH.md#issueOAuth2Token) | **POST** /oauth2/token | OAuth2 액세스 토큰 발급 |


<a name="issueOAuth2Token"></a>
# **issueOAuth2Token**
> OAuth2TokenResponse issueOAuth2Token(grant\_type, client\_id, client\_secret)

OAuth2 액세스 토큰 발급

    OAuth 2.0 Client Credentials Grant 로 access token 을 발급합니다.  - 요청 본문은 `application/x-www-form-urlencoded` 으로 전송합니다. - 발급된 token 은 다른 모든 API 의 `Authorization: Bearer {access_token}` 헤더에 사용합니다. - 응답 형식은 BFF 공통 envelope 이 아닌 OAuth2 표준 형식을 따릅니다. - refresh token 은 제공되지 않습니다. 만료 시 동일 엔드포인트로 재발급합니다. - client 당 유효한 access token 은 1 개입니다. 재발급 시 이전에 발급된 token 은 즉시 무효화됩니다.  **Rate Limits Group**: `AUTH` 

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **grant\_type** | **String**| 인증 방식. `client_credentials` 만 지원합니다. | [default to null] [enum: client_credentials] |
| **client\_id** | **String**| 발급받은 클라이언트 ID | [default to null] |
| **client\_secret** | **String**| 발급받은 클라이언트 시크릿. 노출되지 않도록 서버 측에서만 사용합니다. | [default to null] |

### Return type

[**OAuth2TokenResponse**](MODEL_O_AUTH2_TOKEN_RESPONSE.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## POST /oauth2/token

### `/summary`

OAuth2 액세스 토큰 발급

### `/description`

OAuth 2.0 Client Credentials Grant 로 access token 을 발급합니다.

- 요청 본문은 `application/x-www-form-urlencoded` 으로 전송합니다.
- 발급된 token 은 다른 모든 API 의 `Authorization: Bearer {access_token}` 헤더에 사용합니다.
- 응답 형식은 BFF 공통 envelope 이 아닌 OAuth2 표준 형식을 따릅니다.
- refresh token 은 제공되지 않습니다. 만료 시 동일 엔드포인트로 재발급합니다.
- client 당 유효한 access token 은 1 개입니다. 재발급 시 이전에 발급된 token 은 즉시 무효화됩니다.

**Rate Limits Group**: `AUTH`


### `/responses/200/description`

토큰 발급 성공

### `/responses/400/description`

잘못된 요청.
필수 파라미터 누락, 지원하지 않는 grant_type 등.


### `/responses/400/content/application/json/examples/invalidRequest/summary`

필수 파라미터 누락 / 형식 오류

### `/responses/400/content/application/json/examples/unsupportedGrantType/summary`

지원하지 않는 grant_type

### `/responses/401/description`

클라이언트 인증 실패.
`client_id` / `client_secret` 가 잘못되었거나 클라이언트가 비활성 상태인 경우.


### `/responses/401/headers/WWW-Authenticate/description`

Basic 인증 챌린지. 토큰 엔드포인트는 `Basic realm="openapi"` 로 응답합니다.


### `/responses/403/description`

허용되지 않은 IP 에서의 요청.
클라이언트에 등록된 허용 IP 목록에 없는 IP 에서 호출한 경우 차단됩니다.
토스증권 WTS 설정 > Open API > 허용 IP 관리 에서 호출을 허용할 IP 를 등록할 수 있습니다.


### 전체 연산 정의

````json
{
  "tags": [
    "Auth"
  ],
  "summary": "OAuth2 액세스 토큰 발급",
  "description": "OAuth 2.0 Client Credentials Grant 로 access token 을 발급합니다.\n\n- 요청 본문은 `application/x-www-form-urlencoded` 으로 전송합니다.\n- 발급된 token 은 다른 모든 API 의 `Authorization: Bearer {access_token}` 헤더에 사용합니다.\n- 응답 형식은 BFF 공통 envelope 이 아닌 OAuth2 표준 형식을 따릅니다.\n- refresh token 은 제공되지 않습니다. 만료 시 동일 엔드포인트로 재발급합니다.\n- client 당 유효한 access token 은 1 개입니다. 재발급 시 이전에 발급된 token 은 즉시 무효화됩니다.\n\n**Rate Limits Group**: `AUTH`\n",
  "operationId": "issueOAuth2Token",
  "security": [],
  "requestBody": {
    "required": true,
    "content": {
      "application/x-www-form-urlencoded": {
        "schema": {
          "$ref": "#/components/schemas/OAuth2TokenRequest"
        },
        "example": {
          "grant_type": "client_credentials",
          "client_id": "c_01HXYZABCDEFG123456789",
          "client_secret": "s_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        }
      }
    }
  },
  "responses": {
    "200": {
      "description": "토큰 발급 성공",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/OAuth2TokenResponse"
          },
          "example": {
            "access_token": "eyJraWQiOiIyMDI2LTA0LTAxLWtleSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjXzAxSFhZWiJ9...",
            "token_type": "Bearer",
            "expires_in": 86400
          }
        }
      }
    },
    "400": {
      "description": "잘못된 요청.\n필수 파라미터 누락, 지원하지 않는 grant_type 등.\n",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/OAuth2ErrorResponse"
          },
          "examples": {
            "invalidRequest": {
              "summary": "필수 파라미터 누락 / 형식 오류",
              "value": {
                "error": "invalid_request",
                "error_description": "Required parameter is missing."
              }
            },
            "unsupportedGrantType": {
              "summary": "지원하지 않는 grant_type",
              "value": {
                "error": "unsupported_grant_type",
                "error_description": "Only client_credentials grant type is supported."
              }
            }
          }
        }
      }
    },
    "401": {
      "description": "클라이언트 인증 실패.\n`client_id` / `client_secret` 가 잘못되었거나 클라이언트가 비활성 상태인 경우.\n",
      "headers": {
        "WWW-Authenticate": {
          "description": "Basic 인증 챌린지. 토큰 엔드포인트는 `Basic realm=\"openapi\"` 로 응답합니다.\n",
          "schema": {
            "type": "string"
          },
          "example": "Basic realm=\"openapi\""
        }
      },
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/OAuth2ErrorResponse"
          },
          "example": {
            "error": "invalid_client",
            "error_description": "Client authentication failed."
          }
        }
      }
    },
    "403": {
      "description": "허용되지 않은 IP 에서의 요청.\n클라이언트에 등록된 허용 IP 목록에 없는 IP 에서 호출한 경우 차단됩니다.\n토스증권 WTS 설정 > Open API > 허용 IP 관리 에서 호출을 허용할 IP 를 등록할 수 있습니다.\n",
      "content": {
        "application/json": {
          "schema": {
            "$ref": "#/components/schemas/OAuth2ErrorResponse"
          },
          "example": {
            "error": "access_denied",
            "error_description": "IP address not allowed"
          }
        }
      }
    },
    "429": {
      "$ref": "#/components/responses/RateLimitExceeded"
    }
  }
}
````
