> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/MarketCountry.md
> 문서 버전: 1.2.17

# MarketCountry
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|




## OpenAPI 원본 스키마

### `/description`

시장 국가 구분.
- KR: 국내 주식 (KRX)
- US: 미국 주식 (NYSE, NASDAQ 등)

클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.


````json
{
  "type": "string",
  "enum": [
    "KR",
    "US"
  ],
  "description": "시장 국가 구분.\n- KR: 국내 주식 (KRX)\n- US: 미국 주식 (NYSE, NASDAQ 등)\n\n클라이언트는 unknown enum 값을 허용하도록 구현해야 합니다.\n"
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
