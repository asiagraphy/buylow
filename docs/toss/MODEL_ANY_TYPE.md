> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/openapi.json#/components/schemas/ApiError/properties/data
> 문서 버전: 1.2.17

# ApiError.data

공식 Markdown의 AnyType 링크는 HTTP 404입니다. 아래는 해당 필드의 OpenAPI 원본 정의입니다.

### `/description`

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
  "type": [
    "object",
    "null"
  ],
  "description": "에러 해결 힌트. 에러 코드별로 포함 여부와 키 구조가 다르며, 없는 경우 필드 자체가 생략됩니다.\n모든 표준 키가 항상 함께 내려가지 않으며, 각 에러 코드에 해당하는 서브셋만 포함됩니다.\n\n## 표준 키 (camelCase)\n\n| 키 | 타입 | 설명 |\n|---|---|---|\n| `field` | string | 검증 실패 원인 필드. 외부 API 에 노출된 이름 (request body JSON key 또는 query parameter name) 을 사용합니다. 복수 필드는 쉼표로 구분 (예: `\"quantity,orderAmount\"`). |\n| `allowedValues` | string[] | enum 후보 값 전체. |\n| `allowedConditions` | object | 조건부 허용 규칙 (`marketCountry` / `orderType` / `side` 등). |\n| `constraint` | object | 필드 제약 (`min` / `max` / `integerOnly` / `step`). |\n| `format` | string | 포맷 규칙명 (예: `decimal`). |\n| `pattern` | string | 정규식. |\n| `maxLength` | number | 문자열 길이 상한. |\n| `limits` | object | 금액 / 수량 한도 (`threshold` / `minimum` / `maximum` + `currency`). |\n| `retryAfterAt` | string | 절대 재시도 시각 (ISO 8601 offset, KST). |\n| `retryAfterSeconds` | number | 상대 재시도 시각 (초). |\n| `tickSize` | string | 호가 단위. |\n| `nearestPrices` | string[] | 근접 유효 가격 (`[lower, upper]`). |\n\n구체적인 에러 코드별 `data` 예시는 각 엔드포인트의 4xx / 5xx 응답 예시를 참고합니다.\n",
  "additionalProperties": true
}
````
