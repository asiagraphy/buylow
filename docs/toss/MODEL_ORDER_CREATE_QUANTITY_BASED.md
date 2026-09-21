> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderCreateQuantityBased.md
> 문서 버전: 1.2.17

# OrderCreateQuantityBased
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **clientOrderId** | **String** | 클라이언트 지정 주문 식별자. 멱등성 키로 사용됩니다. - 미전달: 멱등성 미적용. 매 요청을 별개 주문으로 처리합니다. - 전달: 동일 값으로 재요청 시 이전 주문 결과를 그대로 재반환합니다. 서버는 자동 생성하지 않습니다. 최대 36자, 영숫자 및 `-`, `_` 허용. 멱등성 키는 10분간 유효하며, 이후 동일 값으로 재요청 시 새 주문으로 처리됩니다.  | [optional] [default to null] |
| **symbol** | **String** | 종목 심볼. KRX: 6자리 종목코드 (숫자 또는 영문·숫자 조합), US: 영문 티커 | [default to null] |
| **side** | **String** | 주문 방향 | [default to null] |
| **orderType** | **String** | 호가 유형. - `LIMIT`: 지정가 - `MARKET`: 시장가  | [default to null] |
| **timeInForce** | **String** | 주문 유효 조건 (Time In Force). 미전달 시 `DAY`. `orderType` 과 결합되어 주문 방식이 결정됩니다 (예: `LIMIT` + `CLS` = LOC). - `DAY`: 당일 유효 (Day). 정규장 종료까지 미체결분은 자동 취소됩니다. - `CLS`: 장 마감 주문 (At the Close). 현재 미국 주식 + `orderType=LIMIT` 조합만 지원합니다. - `OPG`: 장 개시 주문 (At the Opening, 국내 시가단일가). 현재 국내 주식 전용이며 `orderType` 은 `LIMIT`/`MARKET` 모두 지원합니다. 세션 시간(장전 사전접수) 외 접수는 원장에서 거절될 수 있습니다.  | [optional] [default to DAY] |
| **quantity** | **BigDecimal** | 주문 수량 (주 단위). 지정한 수량만큼 주문합니다. - 기본: 양의 정수만 가능합니다. - 소수점 수량: 미국 주식 시장가 매도(`orderType=MARKET` + `side=SELL`) 주문에만 허용됩니다.   그 외(매수/지정가/국내) 소수점 수량은 `400 invalid-request` 를 반환합니다.   소수점 매수는 `orderAmount` 를 사용하세요.   소수점 수량 매도는 정규장 시작부터 정규장 종료 1시간 전까지만 접수 가능하며, 그 외 시간 요청 시 `422 fractional-quantity-outside-regular-hours` 를 반환합니다.   소수점 수량은 소수점 6자리까지 지원하며, 초과 시 `400 invalid-request` (`fractional-quantity-scale-exceeded`) 를 반환합니다.  | [default to null] |
| **price** | **BigDecimal** | 주문 가격. `orderType`이 `LIMIT` 일 때만 사용합니다. - `LIMIT`: 필수. 미전달 시 `400 invalid-request`. - `MARKET`: 전달 불가. 전달 시 `400 invalid-request`. - KR: 정수 (원 단위). 호가 단위에 맞아야 합니다 (예: 50,000~200,000원 구간은 100원 단위). 맞지 않으면 `400 invalid-request` 에러와 함께 올바른 호가 단위가 `data`에 포함됩니다. - US: 소수점 (달러 단위).   - $1 미만: 소수점 넷째 자리까지 (그 이하 자릿수는 절삭).   - $1 이상: 소수점 둘째 자리까지 (그 이하 자릿수는 절삭).  | [optional] [default to null] |
| **confirmHighValueOrder** | **Boolean** | 착오주문 방지를 위한 주문 확인 플래그. 기본값 `false`. 1억원 이상의 주문 시 `true`가 아니면 `400 confirm-high-value-required` 에러를 반환합니다. 사용자가 해당 주문의 금액을 인지하고 있음을 표시하기 위한 필드입니다.  | [optional] [default to false] |



