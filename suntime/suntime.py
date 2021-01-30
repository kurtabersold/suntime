from datetime import date, datetime, timedelta
from astral import LocationInfo
from astral.sun import sun


# def get_time_delta(dt: date, days: int) -> date:
#     """Arbitrary time delta"""
#     return dt + timedelta(days=days)


def get_today():
    """Today"""
    return date.today()


def get_tomorrow():
    """Tomorrow"""
    return date.today() + timedelta(days=1)


def get_yesterday():
    """Yesterday"""
    return date.today() + timedelta(days=-1)


# def get_tz_for_loc():
#     """Returns timezone name for location"""
#     pass


def get_loc(name: str = 'Olympia', region: str = 'WA, USA', timezone: str = 'America/Los_Angeles',
            latitude: float = 47.037872, longitude: float = -122.900696):
    """Defines a location on Earth.

    # TODO: Does the timezone matter? What if we did all calculations in UTC?

    Latitude and longitude can be set either as a float or as a string. For strings they must
    be of the form

        degrees°minutes'seconds"[N|S|E|W] e.g. 51°31'N

    `minutes’` & `seconds”` are optional.

    Args:
        name:      Location name (can be any string)
        region:    Region location is in (can be any string)
        timezone:  The location's time zone (a list of time zone names can be obtained from
                      `pytz.all_timezones`)
        latitude:  Latitude - Northern latitudes should be positive
        longitude: Longitude - Eastern longitudes should be positive
    """
    return LocationInfo(name=name, region=region, timezone=timezone, latitude=latitude, longitude=longitude)


class Suntime:
    def __init__(self):
        self.loc: LocationInfo = get_loc()

        # Predetermined stats for common days.
        self.yesterday: sun = self.get_sun(get_yesterday())
        self.today: sun = self.get_sun(get_today())
        self.tomorrow: sun = self.get_sun(get_tomorrow())

    def get_sun(self, d: date) -> sun:
        """
        Returns a astral.sun object for a given date/LocationInfo.
        """
        return sun(self.loc.observer, date=d, tzinfo=self.loc.timezone)  # TODO: UTC???

    def _date_delta(self, first: date, last: date) -> timedelta:
        """
        Returns timedelta adjusted for difference between dates.
        TODO: future/past bug?
        """
        d = last - first
        return d + timedelta(days=-d.days)

    def _sun_delta(self, key: str, first: sun, last: sun) -> timedelta:
        """
        Returns a timedelta for a given key between two sun objects.
        """
        return self._date_delta(first.get(key), last.get(key))

    def sunset_delta(self, first: sun, last: sun) -> timedelta:
        """Returns a timedelta for sunset between two sun objects"""
        return self._sun_delta('sunset', first, last)

    def sunrise_delta(self, first: sun, last: sun) -> timedelta:
        """Returns a timedelta for sunrise between two sun objects"""
        return self._sun_delta('sunrise', first=last, last=first)
