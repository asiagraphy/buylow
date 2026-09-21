> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ApiResponse.md
> 문서 버전: 1.2.17

# ApiResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **result** | **Object** | 성공 응답의 페이로드. 엔드포인트별 타입이 다르며, 각 엔드포인트 스펙에서 `allOf` 로 구체 타입을 명시합니다.  | [default to null] |




## OpenAPI 원본 스키마

### `/description`

성공 응답 envelope. 200 응답에 사용됩니다.
각 엔드포인트의 성공 응답 스키마는 `allOf` 로 본 스키마를 상속하며 `result` 를 구체 타입으로 specialize 합니다.
실패 응답은 별도의 `ErrorResponse` 스키마를 사용합니다 (4xx/5xx). `result` 와 `error` 는 동시에 나타나지 않습니다.


### `/properties/result/description`

성공 응답의 페이로드. 엔드포인트별 타입이 다르며, 각 엔드포인트 스펙에서 `allOf` 로 구체 타입을 명시합니다.


````json
{
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
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
