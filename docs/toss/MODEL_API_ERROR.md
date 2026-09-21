> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/ApiError.md
> 문서 버전: 1.2.17

# ApiError
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **requestId** | **String** | 요청을 식별하는 고유 ID. 응답 헤더 `X-Request-Id` 와 동일한 값입니다. 토스증권 CS 문의 시 첨부를 권장합니다.  | [default to null] |
| **code** | **String** | 에러 코드. flat string 식별자. 도메인 에러는 이유를 직접 표현하는 단일 식별자 (예: `invalid-request`, `order-not-found`) 를 사용합니다. 클라이언트는 unknown code 를 허용하도록 구현해야 합니다.  | [default to null] |
| **message** | **String** | 사용자에게 노출 가능한 에러 메시지. 내부 정책상 노출이 제한되는 경우 빈 문자열로 내려갈 수 있으므로 클라이언트는 `code` 기반으로 메시지를 자체 매핑할 것을 권장합니다.  | [default to null] |
| **data** | [**Map**](MODEL_ANY_TYPE.md) | 에러 해결 힌트. 에러 코드별로 포함 여부와 키 구조가 다르며, 없는 경우 필드 자체가 생략됩니다. 모든 표준 키가 항상 함께 내려가지 않으며, 각 에러 코드에 해당하는 서브셋만 포함됩니다.  ## 표준 키 (camelCase)  | 키 | 타입 | 설명 | |---|---|---| | `field` | string | 검증 실패 원인 필드. 외부 API 에 노출된 이름 (request body JSON key 또는 query parameter name) 을 사용합니다. 복수 필드는 쉼표로 구분 (예: `\"quantity,orderAmount\"`). | | `allowedValues` | string[] | enum 후보 값 전체. | | `allowedConditions` | object | 조건부 허용 규칙 (`marketCountry` / `orderType` / `side` 등). | | `constraint` | object | 필드 제약 (`min` / `max` / `integerOnly` / `step`). | | `format` | string | 포맷 규칙명 (예: `decimal`). | | `pattern` | string | 정규식. | | `maxLength` | number | 문자열 길이 상한. | | `limits` | object | 금액 / 수량 한도 (`threshold` / `minimum` / `maximum` + `currency`). | | `retryAfterAt` | string | 절대 재시도 시각 (ISO 8601 offset, KST). | | `retryAfterSeconds` | number | 상대 재시도 시각 (초). | | `tickSize` | string | 호가 단위. | | `nearestPrices` | string[] | 근접 유효 가격 (`[lower, upper]`). |  구체적인 에러 코드별 `data` 예시는 각 엔드포인트의 4xx / 5xx 응답 예시를 참고합니다.  | [optional] [default to null] |




## OpenAPI 원본 스키마

### `/description`

에러 객체. 에러 식별에 필요한 최소 정보(`requestId`, `code`, `message`)와
필요 시 해결 힌트(`data`)를 포함합니다.


### `/properties/requestId/description`

요청을 식별하는 고유 ID. 응답 헤더 `X-Request-Id` 와 동일한 값입니다.
토스증권 CS 문의 시 첨부를 권장합니다.


### `/properties/code/description`

에러 코드. flat string 식별자.
도메인 에러는 이유를 직접 표현하는 단일 식별자 (예: `invalid-request`, `order-not-found`) 를 사용합니다.
클라이언트는 unknown code 를 허용하도록 구현해야 합니다.


### `/properties/message/description`

사용자에게 노출 가능한 에러 메시지. 내부 정책상 노출이 제한되는 경우 빈 문자열로 내려갈 수 있으므로
클라이언트는 `code` 기반으로 메시지를 자체 매핑할 것을 권장합니다.


### `/properties/data/description`

에러 해결 힌트. 에러 코드별로 포함 여부와 키 구조가 다르며, 없는 경우 필드 자체가 생략됩니다.
모든 표준 키가 항상 함께 내려가지 않으며, 각 에러 코드에 해당하는 서브셋만 포함됩니다.

## 표준 키 (camelCase)

| 키 | 타입 | 설명 |
|---|---|---|
| `field` | string | 검증 실패 원인 필드. 외부 API 에 노출된 이름 (request body JSON key 또는 query parameter name) 을 사용합니다. 복수 필드는 쉼표로 구분 (예: `"quantity,orderAmount"`). |
| `allowedValues` | string[] | enum 후보 값 전체. |
| `allowedConditions` | object | 조건부 허용 규칙 (`marketCountry` / `orderType` / `side` 등). |
| `constraint` | object | 필드 제약 (`min` / `max` / `integerOnly` / `step`). |
| `format` | string | 포맷 규칙명 (예: `decimal`). |
| `pattern` | string | 정규식. |
| `maxLength` | number | 문자열 길이 상한. |
| `limits` | object | 금액 / 수량 한도 (`threshold` / `minimum` / `maximum` + `currency`). |
| `retryAfterAt` | string | 절대 재시도 시각 (ISO 8601 offset, KST). |
| `retryAfterSeconds` | number | 상대 재시도 시각 (초). |
| `tickSize` | string | 호가 단위. |
| `nearestPrices` | string[] | 근접 유효 가격 (`[lower, upper]`). |

구체적인 에러 코드별 `data` 예시는 각 엔드포인트의 4xx / 5xx 응답 예시를 참고합니다.


````json
{
  "type": "object",
  "description": "에러 객체. 에러 식별에 필요한 최소 정보(`requestId`, `code`, `message`)와\n필요 시 해결 힌트(`data`)를 포함합니다.\n",
  "required": [
    "requestId",
    "code",
    "message"
  ],
  "properties": {
    "requestId": {
      "type": "string",
      "description": "요청을 식별하는 고유 ID. 응답 헤더 `X-Request-Id` 와 동일한 값입니다.\n토스증권 CS 문의 시 첨부를 권장합니다.\n",
      "example": "01HXYZABCDEFG123456789"
    },
    "code": {
      "type": "string",
      "description": "에러 코드. flat string 식별자.\n도메인 에러는 이유를 직접 표현하는 단일 식별자 (예: `invalid-request`, `order-not-found`) 를 사용합니다.\n클라이언트는 unknown code 를 허용하도록 구현해야 합니다.\n",
      "example": "order-not-found"
    },
    "message": {
      "type": "string",
      "description": "사용자에게 노출 가능한 에러 메시지. 내부 정책상 노출이 제한되는 경우 빈 문자열로 내려갈 수 있으므로\n클라이언트는 `code` 기반으로 메시지를 자체 매핑할 것을 권장합니다.\n",
      "example": "주문 방향이 올바르지 않습니다."
    },
    "data": {
      "type": [
        "object",
        "null"
      ],
      "description": "에러 해결 힌트. 에러 코드별로 포함 여부와 키 구조가 다르며, 없는 경우 필드 자체가 생략됩니다.\n모든 표준 키가 항상 함께 내려가지 않으며, 각 에러 코드에 해당하는 서브셋만 포함됩니다.\n\n## 표준 키 (camelCase)\n\n| 키 | 타입 | 설명 |\n|---|---|---|\n| `field` | string | 검증 실패 원인 필드. 외부 API 에 노출된 이름 (request body JSON key 또는 query parameter name) 을 사용합니다. 복수 필드는 쉼표로 구분 (예: `\"quantity,orderAmount\"`). |\n| `allowedValues` | string[] | enum 후보 값 전체. |\n| `allowedConditions` | object | 조건부 허용 규칙 (`marketCountry` / `orderType` / `side` 등). |\n| `constraint` | object | 필드 제약 (`min` / `max` / `integerOnly` / `step`). |\n| `format` | string | 포맷 규칙명 (예: `decimal`). |\n| `pattern` | string | 정규식. |\n| `maxLength` | number | 문자열 길이 상한. |\n| `limits` | object | 금액 / 수량 한도 (`threshold` / `minimum` / `maximum` + `currency`). |\n| `retryAfterAt` | string | 절대 재시도 시각 (ISO 8601 offset, KST). |\n| `retryAfterSeconds` | number | 상대 재시도 시각 (초). |\n| `tickSize` | string | 호가 단위. |\n| `nearestPrices` | string[] | 근접 유효 가격 (`[lower, upper]`). |\n\n구체적인 에러 코드별 `data` 예시는 각 엔드포인트의 4xx / 5xx 응답 예시를 참고합니다.\n",
      "additionalProperties": true
    }
  }
}
````

[공통 정의와 참조 대상](REST_DEFINITIONS.md)
