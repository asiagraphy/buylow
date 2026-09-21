> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/openapi.json#/components/schemas/OAuth2TokenRequest
> 문서 버전: 1.2.17

# OAuth2TokenRequest

### `/description`

OAuth2 Client Credentials Grant 토큰 발급 요청.
`application/x-www-form-urlencoded` 으로 전송합니다.


### `/properties/grant_type/description`

인증 방식. `client_credentials` 만 지원합니다.

### `/properties/client_id/description`

발급받은 클라이언트 ID

### `/properties/client_secret/description`

발급받은 클라이언트 시크릿. 노출되지 않도록 서버 측에서만 사용합니다.

````json
{
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
}
````
