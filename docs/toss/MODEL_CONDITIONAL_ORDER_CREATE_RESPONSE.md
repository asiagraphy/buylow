> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ConditionalOrderCreateResponse.md
> 문서 버전: 1.2.17

# ConditionalOrderCreateResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **conditionalOrderId** | **String** | 서버가 생성한 조건주문 식별자. 이후 조회·수정·취소에 사용합니다. | [default to null] |
| **clientOrderId** | **String** | 요청에 사용한 멱등키(`clientOrderId`)를 그대로 반환합니다. 요청에 없었으면 null. | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/description`

조건주문 생성 응답.

### `/properties/conditionalOrderId/description`

서버가 생성한 조건주문 식별자. 이후 조회·수정·취소에 사용합니다.

### `/properties/clientOrderId/description`

요청에 사용한 멱등키(`clientOrderId`)를 그대로 반환합니다. 요청에 없었으면 null.

````json
{
  "type": "object",
  "required": [
    "conditionalOrderId"
  ],
  "description": "조건주문 생성 응답.",
  "properties": {
    "conditionalOrderId": {
      "type": "string",
      "description": "서버가 생성한 조건주문 식별자. 이후 조회·수정·취소에 사용합니다.",
      "example": "gaZIG-dYMWil8AAXyPmlRg"
    },
    "clientOrderId": {
      "type": [
        "string",
        "null"
      ],
      "description": "요청에 사용한 멱등키(`clientOrderId`)를 그대로 반환합니다. 요청에 없었으면 null.",
      "example": "my-order-001"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
