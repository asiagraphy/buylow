> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderResponse.md
> 문서 버전: 1.2.17

# OrderResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **orderId** | **String** | 서버 생성 주문 식별자. 정정/취소 시 사용 | [default to null] |
| **clientOrderId** | **String** | 요청 시 전달한 값 그대로 반환. 미전달 시 `null`. | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/properties/orderId/description`

서버 생성 주문 식별자. 정정/취소 시 사용

### `/properties/clientOrderId/description`

요청 시 전달한 값 그대로 반환. 미전달 시 `null`.

````json
{
  "type": "object",
  "required": [
    "orderId"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "서버 생성 주문 식별자. 정정/취소 시 사용",
      "example": "0d5QIHjmtksbsmM-hBRAgP-ExI8iodGm9fAR5txelPfnMM8XQ_swoJdwL5RpGWMo"
    },
    "clientOrderId": {
      "type": [
        "string",
        "null"
      ],
      "description": "요청 시 전달한 값 그대로 반환. 미전달 시 `null`.",
      "example": "my-order-001"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
