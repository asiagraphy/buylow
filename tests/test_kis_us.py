from datetime import date, datetime, timedelta, timezone

import pytest
import requests

from brokers.kis_us import BrokerError, KisUsClient, OrderUncertain, RequestPacer, limit_price
from market.us import session_for
from orchestrator.us_strategy import Stock, NEW_YORK


class Clock:
    value = 0.0

    def time(self):
        return self.value

    def sleep(self, duration):
        self.value += duration


class Response:
    def __init__(self, payload, status=200, more=""):
        self.payload, self.status_code = payload, status
        self.headers = {"tr_cont": more}

    def json(self):
        return self.payload


class Transport:
    def __init__(self, clock, replies):
        self.clock, self.replies, self.calls = clock, list(replies), []

    def request(self, method, url, **arguments):
        self.calls.append((self.clock.time(), method, url, arguments))
        if url.endswith("tokenP"):
            return Response({"access_token": "synthetic-token", "expires_in": 86400})
        result = self.replies.pop(0)
        if isinstance(result, Exception):
            raise result
        return result


def client(replies, mode="demo"):
    clock = Clock()
    transport = Transport(clock, replies)
    instance = KisUsClient("synthetic-key", "synthetic-secret", "50000000-01", mode,
                           session=transport, pacer=RequestPacer(clock=clock.time, sleep=clock.sleep))
    return instance, transport


def test_authentication_and_orders_share_strict_request_pacing():
    instance, transport = client([
        Response({"rt_cd": "0", "output": {"ODNO": "buy-1"}}),
        Response({"rt_cd": "0", "output": {"ODNO": "sell-1"}}),
    ])
    instance.place(Stock("AAPL"), "BUY", 1, 100.001)
    instance.place(Stock("AAPL"), "SELL", 1, 100.009)
    assert [call[0] for call in transport.calls] == [0, 1, 2]
    assert all("openapivts" in call[2] for call in transport.calls)
    buy, sell = [call[3] for call in transport.calls[1:]]
    assert buy["headers"]["tr_id"] == "VTTT1002U"
    assert sell["headers"]["tr_id"] == "VTTT1001U"
    assert buy["json"]["ORD_DVSN"] == sell["json"]["ORD_DVSN"] == "00"
    assert buy["json"]["OVRS_ORD_UNPR"] == "100.01"
    assert sell["json"]["OVRS_ORD_UNPR"] == "100.00"


def test_real_trading_is_a_separate_explicit_environment():
    instance, transport = client([Response({"rt_cd": "0", "output": {"ODNO": "one"}})], "real")
    instance.place(Stock("AAPL"), "SELL", 1, 100)
    assert transport.calls[-1][3]["headers"]["tr_id"] == "TTTT1006U"
    assert "openapi.koreainvestment.com" in transport.calls[-1][2]


def test_order_timeout_does_not_resubmit():
    instance, transport = client([requests.Timeout()])
    with pytest.raises(OrderUncertain):
        instance.place(Stock("AAPL"), "BUY", 1, 100)
    assert len(transport.calls) == 2


def test_explicit_rate_rejection_can_retry_without_hammering():
    instance, transport = client([
        Response({"rt_cd": "1", "msg_cd": "EGW00201"}, status=500),
        Response({"rt_cd": "0", "output": {"ODNO": "one"}}),
    ])
    assert instance.place(Stock("AAPL"), "BUY", 1, 100) == "one"
    assert all(right[0] - left[0] >= 1 for left, right in zip(transport.calls, transport.calls[1:]))


def test_demo_history_uses_supported_filters_and_continuation_header():
    instance, transport = client([
        Response({"rt_cd": "0", "output": [{"odno": "one"}],
                  "ctx_area_fk200": "filter", "ctx_area_nk200": "next"}, more="M"),
        Response({"rt_cd": "0", "output": [{"odno": "two"}]}),
    ])
    assert [row["odno"] for row in instance.orders(date(2026, 9, 21))] == ["one", "two"]
    request = transport.calls[-1][3]
    assert request["headers"]["tr_cont"] == "N"
    assert request["params"]["PDNO"] == request["params"]["OVRS_EXCG_CD"] == ""
    assert request["params"]["ODNO"] == ""
    assert request["params"]["SLL_BUY_DVSN"] == request["params"]["CCLD_NCCS_DVSN"] == "00"


def test_bad_pagination_is_not_a_successful_partial_account_snapshot():
    instance, _ = client([Response({"rt_cd": "0", "output": []}, more="M")])
    with pytest.raises(BrokerError, match="연속조회"):
        instance.orders(date(2026, 9, 21))


def test_market_calendar_observes_holidays_early_close_and_dst():
    assert session_for(date(2026, 7, 3)) is None
    assert session_for(date(2026, 11, 27)).close.hour == 13
    winter = session_for(date(2026, 1, 5)).open.astimezone(timezone.utc)
    summer = session_for(date(2026, 7, 6)).open.astimezone(timezone.utc)
    assert winter.hour == 14 and summer.hour == 13


def test_price_rounding_and_invalid_quantities():
    assert limit_price(99.999, "BUY") == "100.00"
    assert limit_price(99.999, "SELL") == "99.99"
    instance, transport = client([])
    with pytest.raises(ValueError):
        instance.place(Stock("AAPL"), "BUY", 0, 100)
    assert not transport.calls
