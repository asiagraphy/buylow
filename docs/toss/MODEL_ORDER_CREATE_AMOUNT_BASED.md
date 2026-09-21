> 원본 URL: https://openapi.tossinvest.com/openapi-docs/latest/api-reference/Models/OrderCreateAmountBased.md
> 문서 버전: 1.2.17

# OrderCreateAmountBased
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **clientOrderId** | **String** | 클라이언트 지정 주문 식별자. 멱등성 키로 사용됩니다. - 미전달: 멱등성 미적용. 매 요청을 별개 주문으로 처리합니다. - 전달: 동일 값으로 재요청 시 이전 주문 결과를 그대로 재반환합니다. 서버는 자동 생성하지 않습니다. 최대 36자, 영숫자 및 `-`, `_` 허용. 멱등성 키는 10분간 유효하며, 이후 동일 값으로 재요청 시 새 주문으로 처리됩니다.  | [optional] [default to null] |
| **symbol** | **String** | US 종목 심볼 (영문 티커). 금액 기반 주문은 US MARKET 전용입니다. | [default to null] |
| **side** | **String** | 주문 방향 | [default to null] |
| **orderType** | **String** | 호가 유형. 금액 기반 주문은 `MARKET` 만 허용합니다. | [default to null] |
| **orderAmount** | **BigDecimal** | 주문 금액 (달러). 지정한 금액만큼 주문합니다. 체결 수량은 체결 시점의 시장가에 따라 결정됩니다.  Quantity-based 와의 차이: quantity 는 수량을 확정하고 비용이 변동하며, orderAmount 는 금액을 확정하고 수량이 변동합니다.  정규장 시작부터 정규장 종료 1시간 전까지만 접수 가능합니다. 그 외 시간 요청 시 `422 amount-order-outside-regular-hours` 에러를 반환합니다.  | [default to null] |
| **confirmHighValueOrder** | **Boolean** | 착오주문 방지를 위한 주문 확인 플래그. 기본값 `false`. 1억원 이상의 주문 시 `true`가 아니면 `400 confirm-high-value-required` 에러를 반환합니다. 사용자가 해당 주문의 금액을 인지하고 있음을 표시하기 위한 필드입니다.  | [optional] [default to false] |



