> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/Currency.md
> 문서 버전: 1.2.17

# Currency
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|




## OpenAPI 원본 스키마

### `/description`

통화 코드.
- KRW: 한국 원화
- USD: 미국 달러

클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.


````json
{
  "type": "string",
  "enum": [
    "KRW",
    "USD"
  ],
  "description": "통화 코드.\n- KRW: 한국 원화\n- USD: 미국 달러\n\n클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.\n"
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
