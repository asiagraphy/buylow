> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/PaginatedConditionalOrderResponse.md
> 문서 버전: 1.2.17

# PaginatedConditionalOrderResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **conditionalOrders** | [**List**](MODEL_CONDITIONAL_ORDER_DETAIL_RESPONSE.md) |  | [default to null] |
| **nextCursor** | **String** | 다음 페이지 커서. 마지막 페이지면 null. | [optional] [default to null] |
| **hasNext** | **Boolean** | 다음 페이지 존재 여부 | [default to null] |




## OpenAPI 원본 스키마

### `/properties/nextCursor/description`

다음 페이지 커서. 마지막 페이지면 null.

### `/properties/hasNext/description`

다음 페이지 존재 여부

````json
{
  "type": "object",
  "required": [
    "conditionalOrders",
    "hasNext"
  ],
  "properties": {
    "conditionalOrders": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/ConditionalOrderDetailResponse"
      }
    },
    "nextCursor": {
      "type": [
        "string",
        "null"
      ],
      "description": "다음 페이지 커서. 마지막 페이지면 null."
    },
    "hasNext": {
      "type": "boolean",
      "description": "다음 페이지 존재 여부"
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
