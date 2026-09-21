> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/PaginatedOrderResponse.md
> 문서 버전: 1.2.17

# PaginatedOrderResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **orders** | [**List**](MODEL_ORDER.md) | 주문 목록 | [default to null] |
| **nextCursor** | **String** | 다음 페이지 커서. 다음 페이지가 없으면 null | [default to null] |
| **hasNext** | **Boolean** | 다음 페이지 존재 여부 | [default to null] |




## OpenAPI 원본 스키마

### `/description`

주문 목록 페이징 응답.
- `status=OPEN`: 모든 대기 중 주문을 반환합니다. `nextCursor`는 항상 `null`, `hasNext`는 항상 `false`.
- `status=CLOSED`: `limit` 단위로 페이징합니다. 다음 페이지가 있으면 `nextCursor`에 커서가, `hasNext`에 `true`가 내려옵니다.


### `/properties/orders/description`

주문 목록

### `/properties/nextCursor/description`

다음 페이지 커서. 다음 페이지가 없으면 null

### `/properties/hasNext/description`

다음 페이지 존재 여부

````json
{
  "type": "object",
  "required": [
    "orders",
    "nextCursor",
    "hasNext"
  ],
  "description": "주문 목록 페이징 응답.\n- `status=OPEN`: 모든 대기 중 주문을 반환합니다. `nextCursor`는 항상 `null`, `hasNext`는 항상 `false`.\n- `status=CLOSED`: `limit` 단위로 페이징합니다. 다음 페이지가 있으면 `nextCursor`에 커서가, `hasNext`에 `true`가 내려옵니다.\n",
  "properties": {
    "orders": {
      "type": "array",
      "items": {
        "$ref": "#/components/schemas/Order"
      },
      "description": "주문 목록"
    },
    "nextCursor": {
      "type": [
        "string",
        "null"
      ],
      "description": "다음 페이지 커서. 다음 페이지가 없으면 null",
      "example": null
    },
    "hasNext": {
      "type": "boolean",
      "description": "다음 페이지 존재 여부",
      "example": false
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
