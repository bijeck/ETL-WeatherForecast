from src.api import get_location_current_weather_data
import pytest



@pytest.mark.parametrize("location, expected",[("hanoi",200),("Tan Uyen",404)])
def test_get_location_current_weather_data(location, expected):
    assert get_location_current_weather_data(location)["code"] == expected
