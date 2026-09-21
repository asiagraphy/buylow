> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OAuth2TokenResponse.md
> 문서 버전: 1.2.17

# OAuth2TokenResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **access\_token** | **String** | JWT 형식의 access token. 모든 API 요청의 `Authorization: Bearer` 헤더에 담습니다. | [default to null] |
| **token\_type** | **String** | 토큰 타입. 항상 `Bearer`. | [default to null] |
| **expires\_in** | **Long** | 토큰 만료까지 남은 초. | [default to null] |




## OpenAPI 원본 스키마

### `/description`

토큰 발급 성공 응답.
BFF 의 공통 `ApiResponse` envelope 을 사용하지 않고 OAuth2 표준 형식으로 응답합니다.


### `/properties/access_token/description`

JWT 형식의 access token. 모든 API 요청의 `Authorization: Bearer` 헤더에 담습니다.

### `/properties/token_type/description`

토큰 타입. 항상 `Bearer`.

### `/properties/expires_in/description`

토큰 만료까지 남은 초.

````json
{
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
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
