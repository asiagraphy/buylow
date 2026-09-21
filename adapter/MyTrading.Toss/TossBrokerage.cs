/*
 * TossBrokerage — 토스증권 LEAN 라이브 브로커리지 + 실시간 데이터큐.
 *
 * 역할: LEAN 라이브 엔진이 전략(①선별 + ②타이밍, 백테스트와 동일 코드)이 만든 주문을 이 클래스를 통해
 * 토스로 실제 전송하고, 체결/시세를 받아 LEAN에 되먹인다.
 *
 * 이 어댑터는 토스의 REST 폴링을 사용한다:
 *   - 체결통보: 웹소켓(KIS H0STCNI0) 대신 **주문 폴링**(getOrder)으로 체결을 확인한다. PlaceOrder가
 *     반환한 orderId를 추적 목록에 넣고, 백그라운드 폴러가 주기적으로 getOrder로 누적 체결수량을 보고
 *     증분만큼 OrderEvent(Fill)를 발생시킨다. 그래서 KIS와 달리 HTS ID가 필요 없다(체결통보 구독이 없음).
 *   - 실시간 시세: 웹소켓(KIS H0STCNT0) 대신 **현재가 폴링**(getPrices, ≤200종목/호출)으로 구독종목의
 *     가격을 주기적으로 받아 데이터피드(IDataQueueHandler)로 흘려보낸다.
 *
 * 무장(arming) 게이트는 없다(enabled면 바로 전송). 유일한 선택적 방벽은 max_order_amount(원>0)다.
 * 한 클래스가 IBrokerage와 IDataQueueHandler를 모두 구현 — 동일 토큰/세션 위에서 주문과 시세가 함께
 * 돌아간다(KIS 어댑터와 동일 패턴).
 */

using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Threading;
using QuantConnect;
using QuantConnect.Brokerages;
using QuantConnect.Configuration;
using QuantConnect.Data;
using QuantConnect.Data.Market;
using QuantConnect.Interfaces;
using QuantConnect.Logging;
using QuantConnect.Orders;
using QuantConnect.Orders.Fees;
using QuantConnect.Packets;
using QuantConnect.Securities;
using QuantConnect.Util;

namespace MyTrading.Toss
{
    public class TossBrokerage : Brokerage, IDataQueueHandler
    {
        static TossBrokerage()
        {
            try { Market.Add(TossConstants.KrxMarket, TossConstants.KrxMarketId); }
            catch { /* 이미 등록됨 */ }
        }

        private readonly IAlgorithm _algorithm;
        private readonly TossRestClient _rest;
        private readonly TossSymbolMapper _symbolMapper = new TossSymbolMapper();
        private readonly IDataAggregator _aggregator;
        private readonly decimal _maxOrderAmount;

        private bool _connected;
        private bool _orderStateUnknown;
        private CancellationTokenSource _cts;
        private Thread _fillPoller;
        private Thread _pricePoller;

        // 폴링 주기(체결/시세). 토스 레이트리밋(그룹별)을 넘지 않게 보수적으로.
        private static readonly TimeSpan FillPollInterval = TimeSpan.FromMilliseconds(1500);
        private static readonly TimeSpan PricePollInterval = TimeSpan.FromMilliseconds(2000);

        // 체결 폴링 추적: orderId(brokerId) → 누적 체결수량(직전 본 값). 증분만 OrderEvent로 발생.
        private readonly ConcurrentDictionary<string, TossOrderStatus> _trackedFilled = new ConcurrentDictionary<string, TossOrderStatus>();
        private readonly ConcurrentDictionary<int, string> _clientOrderIds = new ConcurrentDictionary<int, string>();
        private readonly ConcurrentDictionary<string, string> _replacements = new ConcurrentDictionary<string, string>();
        // 구독 종목(시세 폴링 대상).
        private readonly HashSet<string> _subscribed = new HashSet<string>();
        private readonly object _subLock = new object();

        // 연결 판정은 REST 토큰 발급 기준(KIS 어댑터와 동일 — 데이터피드/폴러는 부가).
        public override bool IsConnected => _connected;

        public TossBrokerage(IAlgorithm algorithm, string clientId, string clientSecret,
                             decimal maxOrderAmount, string tokenCachePath)
            : base("TossBrokerage")
        {
            _algorithm = algorithm;
            _maxOrderAmount = maxOrderAmount;
            AccountBaseCurrency = TossConstants.KrwCurrency;
            _rest = new TossRestClient(clientId, clientSecret, tokenCachePath);
            _aggregator = Composer.Instance.GetExportedValueByTypeName<IDataAggregator>(
                Config.Get("data-aggregator", "QuantConnect.Lean.Engine.DataFeeds.AggregationManager"));
        }

        // ── 연결 ───────────────────────────────────────────────────────────
        public override void Connect()
        {
            if (_connected) return;
            _rest.AccessToken();      // 토큰 선발급(실패 시 즉시 예외)
            _rest.AccountSeq();       // accountSeq 선해석(없으면 즉시 예외)
            _cts = new CancellationTokenSource();
            _fillPoller = new Thread(() => PollLoop(PollFills, FillPollInterval)) { IsBackground = true, Name = "toss-fill-poller" };
            _pricePoller = new Thread(() => PollLoop(PollPrices, PricePollInterval)) { IsBackground = true, Name = "toss-price-poller" };
            _fillPoller.Start();
            _pricePoller.Start();
            _connected = true;
            Log.Trace($"TossBrokerage.Connect(): accountSeq={_rest.AccountSeq()}");
        }

        public override void Disconnect()
        {
            try { _cts?.Cancel(); } catch { }
            _connected = false;
        }

        private void PollLoop(Action tick, TimeSpan interval)
        {
            var token = _cts.Token;
            while (!token.IsCancellationRequested)
            {
                try { tick(); }
                catch (Exception e) { Log.Trace($"TossBrokerage 폴러 오류: {e.Message}"); }
                token.WaitHandle.WaitOne(interval);
            }
        }

        // ── 주문 ───────────────────────────────────────────────────────────
        public override bool PlaceOrder(Order order)
        {
            if (_orderStateUnknown) return false;
            var ticker = _symbolMapper.GetBrokerageSymbol(order.Symbol);
            var buy = order.Direction == OrderDirection.Buy;
            var isMarket = order.Type == OrderType.Market
                           || order.Type == OrderType.MarketOnOpen || order.Type == OrderType.MarketOnClose;
            var price = order.Type == OrderType.Limit && order is LimitOrder lo ? lo.LimitPrice
                        : (order.Price != 0 ? order.Price : _algorithm.Securities[order.Symbol].Price);

            if (!LimitCheck(order, price, out var reject))
            {
                OnOrderEvent(new OrderEvent(order, DateTime.UtcNow, OrderFee.Zero, reject) { Status = OrderStatus.Invalid });
                OnMessage(new BrokerageMessageEvent(BrokerageMessageType.Warning, "OrderBlocked", reject));
                return false;
            }

            try
            {
                // 멱등성 키: 같은 LEAN 주문의 전송 재시도가 토스에서 중복 주문이 되지 않게 한다.
                var clientOrderId = _clientOrderIds.GetOrAdd(order.Id, _ => Guid.NewGuid().ToString("N"));
                var res = _rest.CreateOrder(ticker, buy, (int)order.AbsoluteQuantity, price, isMarket, clientOrderId);
                if (!res.Ok || string.IsNullOrEmpty(res.OrderId))
                {
                    var msg = $"토스 주문거부 {res.Code} {res.Message}";
                    OnOrderEvent(new OrderEvent(order, DateTime.UtcNow, OrderFee.Zero, msg) { Status = OrderStatus.Invalid });
                    ReportOrderFailure(res, msg);
                    return false;
                }
                order.BrokerId.Add(res.OrderId);
                _trackedFilled[res.OrderId] = new TossOrderStatus();
                OnOrderEvent(new OrderEvent(order, DateTime.UtcNow, OrderFee.Zero) { Status = OrderStatus.Submitted });
                Log.Trace($"TossBrokerage.PlaceOrder(): {(buy ? "매수" : "매도")} {ticker} x{order.AbsoluteQuantity} orderId={res.OrderId}");
                return true;
            }
            catch (Exception e)
            {
                // Warning(Error 아님): 주문 1건의 예외가 LEAN RuntimeError로 라이브 전체를 종료시키면 안 된다.
                OnOrderEvent(new OrderEvent(order, DateTime.UtcNow, OrderFee.Zero, e.Message) { Status = OrderStatus.Invalid });
                OnMessage(new BrokerageMessageEvent(BrokerageMessageType.Warning, "OrderError", e.Message));
                return false;
            }
        }

        /// <summary>주문금액 한도 검사. 통과 시 true. 한도(>0) 초과 시에만 거부(0=비활성).</summary>
        private bool LimitCheck(Order order, decimal price, out string reason)
        {
            if (_maxOrderAmount > 0)
            {
                if (price <= 0)
                {
                    reason = "주문금액 한도 확인에 필요한 가격이 없습니다.";
                    return false;
                }
                var amount = order.AbsoluteQuantity * (price > 0 ? price : 0m);
                if (amount > _maxOrderAmount)
                {
                    reason = $"주문금액 {amount:N0}원 > 한도 {_maxOrderAmount:N0}원 — 차단.";
                    return false;
                }
            }
            reason = null;
            return true;
        }

        public override bool UpdateOrder(Order order)
        {
            if (_orderStateUnknown) return false;
            var orderId = order.BrokerId.LastOrDefault();
            if (string.IsNullOrEmpty(orderId)) return false;
            try
            {
                var isMarket = order.Type == OrderType.Market;
                var price = order is LimitOrder lo ? lo.LimitPrice : order.Price;
                if (!LimitCheck(order, price, out var reason))
                {
                    OnMessage(new BrokerageMessageEvent(BrokerageMessageType.Warning, "OrderBlocked", reason));
                    return false;
                }
                var res = _rest.ModifyOrder(orderId, (int)order.AbsoluteQuantity, price, isMarket);
                if (!res.Ok) ReportOrderFailure(res, res.Message);
                if (res.Ok)
                {
                    // 정정 응답은 새 주문번호다. 원주문의 마지막 체결도 종결될 때까지 추적한다.
                    _replacements[orderId] = res.OrderId;
                    order.BrokerId.Add(res.OrderId);
                    _trackedFilled[res.OrderId] = new TossOrderStatus();
                    OnOrderEvent(new OrderEvent(order, DateTime.UtcNow, OrderFee.Zero) { Status = OrderStatus.UpdateSubmitted });
                }
                return res.Ok;
            }
            catch (Exception e)
            {
                OnMessage(new BrokerageMessageEvent(BrokerageMessageType.Warning, "UpdateError", e.Message));
                return false;
            }
        }

        public override bool CancelOrder(Order order)
        {
            if (_orderStateUnknown) return false;
            var orderId = order.BrokerId.LastOrDefault();
            if (string.IsNullOrEmpty(orderId)) return false;
            try
            {
                var res = _rest.CancelOrder(orderId);
                if (!res.Ok) ReportOrderFailure(res, res.Message);
                if (res.Ok)
                {
                    // HTTP 접수 성공과 취소 완료는 다르다. 원주문의 최종 상태와 잔여 체결을 계속 확인한다.
                    OnOrderEvent(new OrderEvent(order, DateTime.UtcNow, OrderFee.Zero) { Status = OrderStatus.CancelPending });
                }
                return res.Ok;
            }
            catch (Exception e)
            {
                OnMessage(new BrokerageMessageEvent(BrokerageMessageType.Warning, "CancelError", e.Message));
                return false;
            }
        }

        // ── 잔고/예수금/주문 ──────────────────────────────────────────────
        public override List<Order> GetOpenOrders()
        {
            var orders = new List<Order>();
            foreach (var pending in _rest.GetOpenOrders())
            {
                if (pending.Currency != "KRW") continue;
                var remaining = pending.Quantity - pending.FilledQty;
                if (remaining <= 0) continue;
                var symbol = _symbolMapper.GetLeanSymbol(pending.Symbol, SecurityType.Equity, TossConstants.KrxMarket);
                var quantity = pending.Buy ? remaining : -remaining;
                Order order;
                if (pending.OrderType == "LIMIT")
                    order = new LimitOrder(symbol, quantity, pending.Price, pending.OrderedAt);
                else if (pending.OrderType == "MARKET")
                    order = new MarketOrder(symbol, quantity, pending.OrderedAt);
                else throw new TossException("지원하지 않는 미체결 주문 유형입니다.");
                order.BrokerId.Add(pending.OrderId);
                order.Status = OrderStatus.Submitted;
                _trackedFilled.TryAdd(pending.OrderId, pending);
                orders.Add(order);
            }
            return orders;
        }

        private void ReportOrderFailure(TossOrderResult result, string message)
        {
            _orderStateUnknown |= result.Code == "ORDER_STATE_UNKNOWN";
            OnMessage(new BrokerageMessageEvent(
                _orderStateUnknown ? BrokerageMessageType.Error : BrokerageMessageType.Warning,
                result.Code ?? "OrderRejected", message));
            if (_orderStateUnknown) Log.Error("ORDER_STATE_UNKNOWN: 자동매매 중지, 주문내역 확인 필요");
        }

        public override List<Holding> GetAccountHoldings()
        {
            var balance = _rest.GetBalance();
            return balance.Holdings.Select(h => new Holding
            {
                Symbol = _symbolMapper.GetLeanSymbol(h.Ticker, SecurityType.Equity, TossConstants.KrxMarket),
                Quantity = h.Quantity,
                AveragePrice = h.AveragePrice,
                MarketPrice = h.CurrentPrice,
                MarketValue = h.EvalAmount,
                UnrealizedPnL = h.ProfitLoss,
                CurrencySymbol = "₩",
            }).ToList();
        }

        public override List<CashAmount> GetCashBalance()
        {
            var bp = _rest.GetBuyingPower("KRW");
            return new List<CashAmount> { new CashAmount(bp, TossConstants.KrwCurrency) };
        }

        // ── 체결 폴링 → OrderEvent ────────────────────────────────────────
        private void PollFills()
        {
            // 추적 중인 주문들을 스냅샷해 순회(폴링 중 PlaceOrder가 추가해도 다음 틱에 반영).
            foreach (var orderId in _trackedFilled.Keys.ToArray())
            {
                var st = _rest.GetOrder(orderId);
                if (!st.Found) continue;
                var orders = _algorithm.Transactions.GetOrdersByBrokerageId(orderId);
                if (orders == null || orders.Count == 0) continue;
                if (!_trackedFilled.TryGetValue(orderId, out var previous)) continue;
                var delta = st.FilledQty - previous.FilledQty;
                var filledStatus = st.Status != null && st.Status.ToUpperInvariant() == "FILLED";
                foreach (var order in orders)
                {
                    // 누적 체결금액·수량·수수료의 증분만 반영한다.
                    if (delta > 0)
                    {
                        var fee = new OrderFee(new CashAmount(
                            Math.Max(0, st.Commission + st.Tax - previous.Commission - previous.Tax),
                            TossConstants.KrwCurrency));
                        OnOrderEvent(new OrderEvent(order, DateTime.UtcNow, fee)
                        {
                            Status = filledStatus ? OrderStatus.Filled : OrderStatus.PartiallyFilled,
                            FillQuantity = st.Buy ? delta : -delta,
                            FillPrice = st.FillPriceSince(previous),
                            FillPriceCurrency = TossConstants.KrwCurrency,
                        });
                    }
                    // 종료 상태인데 위 fill로 종결 통지가 안 된 경우를 보정(폴링 특성상 상태 전이를 놓치지 않게):
                    //  - 취소/거부/만료(부분체결 후 취소 포함) → Canceled
                    //  - FILLED인데 새 증분이 없던 케이스(원자적 업데이트가 어긋난 드문 경우) → 0수량 Filled로 종결
                    if (st.IsTerminal())
                    {
                        var finalFee = delta > 0 ? OrderFee.Zero : new OrderFee(new CashAmount(
                            Math.Max(0, st.Commission + st.Tax - previous.Commission - previous.Tax),
                            TossConstants.KrwCurrency));
                        if (!filledStatus && !(st.Status == "REPLACED" && _replacements.ContainsKey(orderId)))
                            OnOrderEvent(new OrderEvent(order, DateTime.UtcNow, finalFee,
                                $"토스 주문 종료: {st.Status}") { Status = OrderStatus.Canceled });
                        else if (filledStatus && delta <= 0)
                            OnOrderEvent(new OrderEvent(order, DateTime.UtcNow, finalFee)
                            { Status = OrderStatus.Filled, FillPriceCurrency = TossConstants.KrwCurrency });
                    }
                }
                _trackedFilled[orderId] = st;
                if (st.IsTerminal())
                {
                    _trackedFilled.TryRemove(orderId, out _);
                    _replacements.TryRemove(orderId, out _);
                }
            }
        }

        // ── 시세 폴링 → 데이터피드 ────────────────────────────────────────
        private void PollPrices()
        {
            string[] symbols;
            lock (_subLock) { symbols = _subscribed.ToArray(); }
            if (symbols.Length == 0) return;
            // 토스 현재가는 ≤200종목/호출. 유니버스가 200을 넘으면 끊어 호출.
            for (var i = 0; i < symbols.Length; i += 200)
            {
                var batch = symbols.Skip(i).Take(200);
                foreach (var p in _rest.GetPrices(batch))
                {
                    if (p.LastPrice <= 0) continue;
                    var symbol = _symbolMapper.GetLeanSymbol(p.Symbol, SecurityType.Equity, TossConstants.KrxMarket);
                    var time = DateTime.UtcNow.AddHours(9);  // KRX는 Asia/Seoul(UTC+9 근사)
                    var tick = new Tick(time, symbol, "", "KRX", 0m, p.LastPrice) { TickType = TickType.Trade };
                    _aggregator.Update(tick);
                }
            }
        }

        // ── IDataQueueHandler ──────────────────────────────────────────────
        public IEnumerator<BaseData> Subscribe(SubscriptionDataConfig dataConfig, EventHandler newDataAvailableHandler)
        {
            if (!CanSubscribe(dataConfig.Symbol) || dataConfig.TickType == TickType.OpenInterest)
                return null;
            var enumerator = _aggregator.Add(dataConfig, newDataAvailableHandler);
            lock (_subLock) { _subscribed.Add(_symbolMapper.GetBrokerageSymbol(dataConfig.Symbol)); }
            return enumerator;
        }

        public void Unsubscribe(SubscriptionDataConfig dataConfig)
        {
            if (!CanSubscribe(dataConfig.Symbol)) return;
            lock (_subLock) { _subscribed.Remove(_symbolMapper.GetBrokerageSymbol(dataConfig.Symbol)); }
            _aggregator.Remove(dataConfig);
        }

        public void SetJob(LiveNodePacket job) { /* 생성자에서 모두 주입 */ }

        private static bool CanSubscribe(Symbol symbol)
        {
            return symbol != null
                && !symbol.Value.Contains("universe", StringComparison.OrdinalIgnoreCase)
                && symbol.SecurityType == SecurityType.Equity
                && symbol.ID.Market == TossConstants.KrxMarket;
        }

        public override void Dispose()
        {
            try { _cts?.Cancel(); } catch { }
            _aggregator?.Dispose();
        }
    }
}
