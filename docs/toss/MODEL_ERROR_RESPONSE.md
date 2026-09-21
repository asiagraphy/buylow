> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ErrorResponse.md
> 문서 버전: 1.2.17

# ErrorResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **error** | [**ApiError**](MODEL_API_ERROR.md) |  | [default to null] |




## OpenAPI 원본 스키마

### `/description`

에러 응답 envelope. 4xx/5xx 응답에 사용됩니다. 성공 응답은 별도의 `ApiResponse` 스키마를 사용합니다.


````json
{
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
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
