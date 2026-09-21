> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Apis/AccountApi.md
> 문서 버전: 1.2.17

# AccountApi

All URIs are relative to *https://openapi.tossinvest.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccounts**](ACCOUNT.md#getAccounts) | **GET** /api/v1/accounts | 계좌 목록 조회 |


<a name="getAccounts"></a>
# **getAccounts**
> getAccounts_200_response getAccounts()

계좌 목록 조회

    사용자의 계좌 목록을 조회합니다.  - 현재는 **종합매매 (`BROKERAGE`) 계좌만 반환**하며, 계좌가 없으면 빈 배열. 자녀계좌는 사용할 수 없습니다. - 응답의 `accountSeq` 는 **다른 모든 사용자 컨텍스트 API** (보유 주식, 주문, 매수가능금액 등) 의 `X-Tossinvest-Account` 헤더에 사용합니다. - `accountType` enum 은 `BROKERAGE` / `OVERSEAS_DERIVATIVES` / `PENSION_SAVINGS` / `RESHORING_INVESTMENT` 가 정의되어 있으나 본 API 에서는 현재 `BROKERAGE` 만 노출됩니다. enum 의미는 `Account.accountType` schema 참조.  **Rate Limits Group**: `ACCOUNT` 

### Parameters
This endpoint does not need any parameter.

### Return type

[**getAccounts_200_response**](MODEL_GET_ACCOUNTS_200_RESPONSE.md)

### Authorization

[oauth2ClientCredentials](API_REFERENCE.md#oauth2ClientCredentials)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


# OpenAPI 원본 연산 정의

[공통 보안·서버·전체 명세](OPENAPI_SPEC.md) · [공통 정의와 스키마](REST_DEFINITIONS.md)

## GET /api/v1/accounts

### `/summary`

계좌 목록 조회

### `/description`

사용자의 계좌 목록을 조회합니다.

- 현재는 **종합매매 (`BROKERAGE`) 계좌만 반환**하며, 계좌가 없으면 빈 배열. 자녀계좌는 사용할 수 없습니다.
- 응답의 `accountSeq` 는 **다른 모든 사용자 컨텍스트 API** (보유 주식, 주문, 매수가능금액 등) 의 `X-Tossinvest-Account` 헤더에 사용합니다.
- `accountType` enum 은 `BROKERAGE` / `OVERSEAS_DERIVATIVES` / `PENSION_SAVINGS` / `RESHORING_INVESTMENT` 가 정의되어 있으나 본 API 에서는 현재 `BROKERAGE` 만 노출됩니다. enum 의미는 `Account.accountType` schema 참조.

**Rate Limits Group**: `ACCOUNT`


### `/responses/200/description`

성공

### `/responses/200/content/application/json/examples/brokerageAccount/summary`

종합매매 계좌

### `/responses/200/content/application/json/examples/emptyAccounts/summary`

계좌 없음

### 전체 연산 정의

````json
{
  "tags": [
    "Account"
  ],
  "summary": "계좌 목록 조회",
  "description": "사용자의 계좌 목록을 조회합니다.\n\n- 현재는 **종합매매 (`BROKERAGE`) 계좌만 반환**하며, 계좌가 없으면 빈 배열. 자녀계좌는 사용할 수 없습니다.\n- 응답의 `accountSeq` 는 **다른 모든 사용자 컨텍스트 API** (보유 주식, 주문, 매수가능금액 등) 의 `X-Tossinvest-Account` 헤더에 사용합니다.\n- `accountType` enum 은 `BROKERAGE` / `OVERSEAS_DERIVATIVES` / `PENSION_SAVINGS` / `RESHORING_INVESTMENT` 가 정의되어 있으나 본 API 에서는 현재 `BROKERAGE` 만 노출됩니다. enum 의미는 `Account.accountType` schema 참조.\n\n**Rate Limits Group**: `ACCOUNT`\n",
  "operationId": "getAccounts",
  "security": [
    {
      "oauth2ClientCredentials": []
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
                      "$ref": "#/components/schemas/Account"
                    }
                  }
                }
              }
            ]
          },
          "examples": {
            "brokerageAccount": {
              "summary": "종합매매 계좌",
              "value": {
                "result": [
                  {
                    "accountNo": "12345678901",
                    "accountSeq": 1,
                    "accountType": "BROKERAGE"
                  }
                ]
              }
            },
            "emptyAccounts": {
              "summary": "계좌 없음",
              "value": {
                "result": []
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
      "$ref": "#/components/responses/ServiceUnavailable"
    }
  }
}
````
