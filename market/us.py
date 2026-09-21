"""미국 현물 정규장 달력. 일광절약시간과 조기폐장은 거래소 달력에서 읽는다."""

from dataclasses import dataclass
from datetime import date, datetime
from functools import lru_cache

import exchange_calendars

from orchestrator.us_strategy import NEW_YORK


@dataclass(frozen=True)
class Session:
    day: date
    open: datetime
    close: datetime


@lru_cache(maxsize=366)
def session_for(day: date) -> Session | None:
    calendar = exchange_calendars.get_calendar("XNYS")
    label = day.isoformat()
    if not calendar.is_session(label):
        return None
    return Session(day, calendar.session_open(label).to_pydatetime().astimezone(NEW_YORK),
                   calendar.session_close(label).to_pydatetime().astimezone(NEW_YORK))
