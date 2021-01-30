import pytest

from datetime import date, time, datetime, timedelta

from suntime import suntime


def test_dates():
    """suntime.get_date functions return datetime.date objects"""
    assert isinstance(suntime.get_yesterday(), date)
    assert isinstance(suntime.get_today(), date)
    assert isinstance(suntime.get_tomorrow(), date)


def test_location(st):
    yesterday_sunset = st.yesterday['sunset']
    print(f"Yesterday's Sunset: {yesterday_sunset}")
    today_sunset = st.today['sunset']
    print(f"Today's Sunset: {today_sunset}")
    tomorrow_sunset = st.tomorrow['sunset']
    print(f"Tomorrow's Sunset: {tomorrow_sunset}")


def test_date_delta(st):
    """
    Tests that Suntime._date_delta() correclty adjusts for Suntime.
    """
    today = date.today()
    tomorrow = date.today() + timedelta(days=1)

    delta = st._date_delta(today, tomorrow)
    assert isinstance(delta, timedelta)
    assert delta == timedelta()


def test_sunset_delta(st):
    """
    Tests that Suntime can calculate the difference in suntime.
    """
    today = st.get_sun(date.today())
    tomorrow = st.get_sun(date.today() + timedelta(days=1))
    sd = st.sunset_delta(today, tomorrow)
    print(sd)
    assert isinstance(sd, timedelta)
    assert st.sunset_delta(today, today) == timedelta()


def test_sunrise_delta(st):
    """
    Tests that Suntime can calculate the difference in suntime.
    """
    today = st.get_sun(date.today())
    tomorrow = st.get_sun(date.today() + timedelta(days=1))
    sd = st.sunrise_delta(today, tomorrow)
    print(sd)
    assert isinstance(sd, timedelta)
    # assert st.sunrise_delta(today, today) == timedelta()


def test_diff_minutes(st):
    """Checks how many more or less minutes today is than yesterday."""
    yesterday = st.get_sun(date.today() + timedelta(days=-1))
    today = st.get_sun(date.today())
    tomorrow = st.get_sun(date.today() + timedelta(days=1))

    sunrise = st.sunrise_delta(yesterday, today)
    sunset = st.sunset_delta(yesterday, today)
    total = sunset + sunrise
    print(f'\nYesterday vs Today: {total}')

    sunrise = st.sunrise_delta(today, tomorrow)
    sunset = st.sunset_delta(today, tomorrow)
    total = sunset + sunrise
    print(f'Today vs Tomorrow: {total}')

    sunrise = st.sunrise_delta(yesterday, tomorrow)
    sunset = st.sunset_delta(yesterday, tomorrow)
    total = sunset + sunrise
    print(f'Yesterday vs Tomorrow: {total}')
