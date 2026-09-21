/*
 * 토스 어댑터 파싱/분류 로직 테스트 — REST 응답 파싱(계좌·잔고·주문상태), 주문 종료상태 분류, 상수.
 * 네트워크 없이 HttpMessageHandler 스텁으로 캔드 JSON을 먹여 TossRestClient를 검증한다.
 */

using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
using Xunit;
using MyTrading.Toss;

namespace MyTrading.Toss.Tests
{
    /// <summary>요청 경로(+메서드)별로 캔드 응답을 돌려주는 스텁 핸들러.</summary>
    public class StubHandler : HttpMessageHandler
    {
        // (method:path) → json. token은 path만으로 매칭.
        public readonly Dictionary<string, (HttpStatusCode code, string json)> Routes
            = new Dictionary<string, (HttpStatusCode, string)>();
        public readonly List<string> Seen = new List<string>();
        public readonly List<string> Bodies = new List<string>();
        public Func<HttpRequestMessage, HttpResponseMessage> Respond;

        private HttpResponseMessage Build(HttpRequestMessage request)
        {
            var path = request.RequestUri.AbsolutePath;
            var key = request.Method.Method + " " + path;
            Seen.Add(key);
            if (request.Content != null) Bodies.Add(request.Content.ReadAsStringAsync().GetAwaiter().GetResult());
            if (Respond != null && path.StartsWith("/api/v1/orders")) return Respond(request);
            (HttpStatusCode code, string json) hit;
            if (!Routes.TryGetValue(key, out hit) && !Routes.TryGetValue(path, out hit))
                hit = (HttpStatusCode.NotFound, "{}");
            return new HttpResponseMessage(hit.code) { Content = new StringContent(hit.json ?? "{}") };
        }

        protected override HttpResponseMessage Send(HttpRequestMessage request, CancellationToken ct)
            => Build(request);

        protected override Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken ct)
            => Task.FromResult(Build(request));
    }

    public class TossConstantsTests
    {
        [Fact]
        public void Order_paths_embed_orderId()
        {
            Assert.Equal("/api/v1/orders/OID", TossConstants.PathOrder("OID"));
            Assert.Equal("/api/v1/orders/OID/modify", TossConstants.PathOrderModify("OID"));
            Assert.Equal("/api/v1/orders/OID/cancel", TossConstants.PathOrderCancel("OID"));
            Assert.Equal("krx", TossConstants.KrxMarket);
            Assert.Equal(50, TossConstants.KrxMarketId);
        }
    }

    public class TossOrderStatusTests
    {
        [Theory]
        [InlineData("FILLED", true)]
        [InlineData("CANCELED", true)]
        [InlineData("REJECTED", true)]
        [InlineData("EXPIRED", true)]
        [InlineData("PENDING", false)]
        [InlineData("PARTIAL_FILLED", false)]
        [InlineData("PENDING_CANCEL", false)]
        public void IsTerminal_classifies_lifecycle(string status, bool terminal)
        {
            Assert.Equal(terminal, new TossOrderStatus { Status = status }.IsTerminal());
        }

        [Fact]
        public void Partial_fill_price_uses_incremental_amount()
        {
            var previous = new TossOrderStatus { FilledQty = 2, FilledAmount = 200, AvgPrice = 100 };
            var current = new TossOrderStatus { FilledQty = 5, FilledAmount = 560, AvgPrice = 112 };
            Assert.Equal(120m, current.FillPriceSince(previous));
            Assert.Equal(0m, current.FillPriceSince(current));
        }
    }

    public class TossRestParsingTests
    {
        private static TossRestClient Client(StubHandler h)
        {
            h.Routes["/oauth2/token"] = (HttpStatusCode.OK, "{\"access_token\":\"TOK\",\"expires_in\":86400}");
            return new TossRestClient("client_id_xyz", "secret", null, new HttpClient(h));
        }

        private static readonly string Accounts =
            "{\"result\":[{\"accountNo\":\"999\",\"accountSeq\":3,\"accountType\":\"PENSION_SAVINGS\"}," +
            "{\"accountNo\":\"12345678901\",\"accountSeq\":7,\"accountType\":\"BROKERAGE\"}]}";

        [Fact]
        public void AccountSeq_picks_brokerage()
        {
            var h = new StubHandler();
            h.Routes["GET /api/v1/accounts"] = (HttpStatusCode.OK, Accounts);
            var c = Client(h);
            Assert.Equal(7, c.AccountSeq());
            Assert.Equal("12345678901", c.AccountNo());
        }

        [Fact]
        public void GetBalance_normalizes_kr_only()
        {
            var h = new StubHandler();
            h.Routes["GET /api/v1/accounts"] = (HttpStatusCode.OK, Accounts);
            h.Routes["GET /api/v1/holdings"] = (HttpStatusCode.OK,
                "{\"result\":{\"marketValue\":{\"amount\":{\"krw\":\"7200000\"}},\"items\":[" +
                "{\"symbol\":\"005930\",\"name\":\"삼성전자\",\"marketCountry\":\"KR\",\"quantity\":\"100\"," +
                "\"lastPrice\":\"72000\",\"averagePurchasePrice\":\"65000\"," +
                "\"marketValue\":{\"amount\":\"7200000\"},\"profitLoss\":{\"amount\":\"700000\"}}," +
                "{\"symbol\":\"AAPL\",\"marketCountry\":\"US\",\"quantity\":\"10\",\"lastPrice\":\"178\"," +
                "\"averagePurchasePrice\":\"155\",\"marketValue\":{\"amount\":\"1780\"},\"profitLoss\":{\"amount\":\"230\"}}]}}");
            h.Routes["GET /api/v1/buying-power"] = (HttpStatusCode.OK, "{\"result\":{\"cashBuyingPower\":\"5000000\"}}");
            var c = Client(h);
            var bal = c.GetBalance();
            Assert.Single(bal.Holdings);                  // 국내만(AAPL 제외)
            Assert.Equal("005930", bal.Holdings[0].Ticker);
            Assert.Equal(100m, bal.Holdings[0].Quantity);
            Assert.Equal(65000m, bal.Holdings[0].AveragePrice);
            Assert.Equal(5000000m, bal.BuyingPower);
            Assert.Equal(7200000m, bal.TotalEval);
        }

        [Fact]
        public void GetOrder_parses_execution()
        {
            var h = new StubHandler();
            h.Routes["GET /api/v1/accounts"] = (HttpStatusCode.OK, Accounts);
            h.Routes["GET /api/v1/orders/OID1"] = (HttpStatusCode.OK,
                "{\"result\":{\"orderId\":\"OID1\",\"symbol\":\"005930\",\"side\":\"BUY\",\"status\":\"FILLED\"," +
                "\"execution\":{\"filledQuantity\":\"10\",\"averageFilledPrice\":\"70000\",\"commission\":\"105\",\"tax\":\"0\"}}}");
            var c = Client(h);
            var st = c.GetOrder("OID1");
            Assert.True(st.Found && st.Buy);
            Assert.Equal("FILLED", st.Status);
            Assert.True(st.IsTerminal());
            Assert.Equal(10m, st.FilledQty);
            Assert.Equal(70000m, st.AvgPrice);
            Assert.Equal(105m, st.Commission);
        }

        [Fact]
        public void CreateOrder_returns_orderId_on_success()
        {
            var h = new StubHandler();
            h.Routes["GET /api/v1/accounts"] = (HttpStatusCode.OK, Accounts);
            h.Routes["POST /api/v1/orders"] = (HttpStatusCode.OK, "{\"result\":{\"orderId\":\"NEWID\"}}");
            var c = Client(h);
            var res = c.CreateOrder("005930", true, 10, 70000m, false, "buylow-1");
            Assert.True(res.Ok);
            Assert.Equal("NEWID", res.OrderId);
        }

        [Fact]
        public void CreateOrder_failure_returns_not_ok_without_throwing()
        {
            var h = new StubHandler();
            h.Routes["GET /api/v1/accounts"] = (HttpStatusCode.OK, Accounts);
            h.Routes["POST /api/v1/orders"] = (HttpStatusCode.UnprocessableEntity,
                "{\"error\":{\"code\":\"insufficient-cash\",\"message\":\"잔고 부족\"}}");
            var c = Client(h);
            var res = c.CreateOrder("005930", true, 10, 70000m, false, "buylow-2");
            Assert.False(res.Ok);
            Assert.Equal("insufficient-cash", res.Code);   // 422는 즉시 반환(재시도 안 함)
            Assert.Contains("잔고", res.Message);
        }

        [Fact]
        public void CreateOrder_retries_http_429_with_string_error_code()
        {
            var handler = new StubHandler();
            handler.Routes["GET /api/v1/accounts"] = (HttpStatusCode.OK, Accounts);
            var attempts = 0;
            handler.Respond = request => new HttpResponseMessage(++attempts == 1
                ? HttpStatusCode.TooManyRequests : HttpStatusCode.OK)
            {
                Content = new StringContent(attempts == 1
                    ? "{\"error\":{\"code\":\"rate-limit-exceeded\"}}"
                    : "{\"result\":{\"orderId\":\"created\"}}"),
            };
            var result = Client(handler).CreateOrder("005930", true, 1, 70000, false, "stable-key");
            Assert.True(result.Ok);
            Assert.Equal(2, attempts);
            Assert.Equal(handler.Bodies[1], handler.Bodies[2]);
        }

        [Fact]
        public void ModifyOrder_does_not_retry_ambiguous_transport_failure()
        {
            var handler = new StubHandler();
            handler.Routes["GET /api/v1/accounts"] = (HttpStatusCode.OK, Accounts);
            var attempts = 0;
            handler.Respond = request => { attempts++; throw new HttpRequestException("response lost"); };
            var result = Client(handler).ModifyOrder("original", 1, 70000, false);
            Assert.False(result.Ok);
            Assert.Equal("ORDER_STATE_UNKNOWN", result.Code);
            Assert.Equal(1, attempts);
        }

        [Fact]
        public void CreateOrder_reuses_idempotency_key_after_transport_failure()
        {
            var handler = new StubHandler();
            handler.Routes["GET /api/v1/accounts"] = (HttpStatusCode.OK, Accounts);
            var attempts = 0;
            handler.Respond = request =>
            {
                if (++attempts == 1) throw new HttpRequestException("response lost");
                return new HttpResponseMessage(HttpStatusCode.OK)
                { Content = new StringContent("{\"result\":{\"orderId\":\"same-order\"}}") };
            };
            var result = Client(handler).CreateOrder("005930", true, 1, 70000, false, "stable-key");
            Assert.True(result.Ok);
            Assert.Equal(2, attempts);
            Assert.Equal(handler.Bodies[1], handler.Bodies[2]);
        }

        [Fact]
        public void GetOpenOrders_preserves_partial_fill_baseline()
        {
            var handler = new StubHandler();
            handler.Routes["GET /api/v1/accounts"] = (HttpStatusCode.OK, Accounts);
            handler.Routes["GET /api/v1/orders"] = (HttpStatusCode.OK,
                "{\"result\":{\"orders\":[{\"orderId\":\"pending\",\"symbol\":\"005930\"," +
                "\"currency\":\"KRW\",\"side\":\"BUY\",\"orderType\":\"LIMIT\",\"status\":\"PARTIAL_FILLED\"," +
                "\"quantity\":\"10\",\"price\":\"70000\",\"orderedAt\":\"2026-06-01T09:00:00+09:00\"," +
                "\"execution\":{\"filledQuantity\":\"3\",\"filledAmount\":\"210000\",\"averageFilledPrice\":\"70000\"}}]}}");
            var pending = Assert.Single(Client(handler).GetOpenOrders());
            Assert.Equal(7m, pending.Quantity - pending.FilledQty);
            Assert.Equal(210000m, pending.FilledAmount);
            Assert.Equal("pending", pending.OrderId);
        }

        [Fact]
        public void GetOpenOrders_does_not_treat_missing_response_as_empty_account()
        {
            var handler = new StubHandler();
            handler.Routes["GET /api/v1/accounts"] = (HttpStatusCode.OK, Accounts);
            handler.Routes["GET /api/v1/orders"] = (HttpStatusCode.OK, "{\"result\":{}}");
            Assert.Throws<TossException>(() => Client(handler).GetOpenOrders());
        }
    }
}
