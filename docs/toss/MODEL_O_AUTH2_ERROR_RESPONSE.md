> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OAuth2ErrorResponse.md
> 문서 버전: 1.2.17

# OAuth2ErrorResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **error** | **String** | 에러 코드. | [default to null] |
| **error\_description** | **String** | 에러 상세 설명 (선택). 메시지에 non-ASCII 문자가 포함되는 경우 생략될 수 있습니다.  | [optional] [default to null] |
| **error\_uri** | **URI** | 에러 정보가 게시된 페이지 URI (선택). | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/description`

OAuth2 토큰 발급 실패 응답.
`/oauth2/token` 엔드포인트는 BFF 공통 `ErrorResponse` envelope 이 아닌 OAuth2 표준 포맷으로 응답합니다.
클라이언트는 `code` 가 아닌 `error` 필드로 에러를 식별해야 합니다.


### `/properties/error/description`

에러 코드.

### `/properties/error_description/description`

에러 상세 설명 (선택). 메시지에 non-ASCII 문자가 포함되는 경우 생략될 수 있습니다.


### `/properties/error_uri/description`

에러 정보가 게시된 페이지 URI (선택).

````json
{
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
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
