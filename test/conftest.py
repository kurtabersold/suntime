import pytest

from suntime import suntime


@pytest.fixture
def st():
    """Retruns a suntime.Suntime()"""
    return suntime.Suntime()
