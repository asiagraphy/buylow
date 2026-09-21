> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderResponse.md
> 문서 버전: 1.2.17

# ConditionalOrderResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **conditionalOrderId** | **String** | 조건주문 식별자 | [default to null] |




## OpenAPI 원본 스키마

### `/description`

조건주문 수정·취소 응답. 대상 조건주문 식별자만 반환합니다.

### `/properties/conditionalOrderId/description`

조건주문 식별자

````json
{
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
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
