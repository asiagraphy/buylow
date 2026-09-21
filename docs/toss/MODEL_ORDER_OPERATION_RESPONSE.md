> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderOperationResponse.md
> 문서 버전: 1.2.17

# OrderOperationResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **orderId** | **String** | 정정/취소로 새로 발급된 주문 식별자. 원주문의 orderId 와 다릅니다.  | [default to null] |




## OpenAPI 원본 스키마

### `/properties/orderId/description`

정정/취소로 새로 발급된 주문 식별자. 원주문의 orderId 와 다릅니다.


````json
{
  "type": "object",
  "required": [
    "orderId"
  ],
  "properties": {
    "orderId": {
      "type": "string",
      "description": "정정/취소로 새로 발급된 주문 식별자. 원주문의 orderId 와 다릅니다.\n",
      "example": "5nfzdqmzfnAw3LFXWHPRy0UNi7y_WZlphJh5hRIsi25-NIfm_GtQgXima5QD2hUz"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
