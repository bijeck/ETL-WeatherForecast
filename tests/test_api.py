from src.api import get_location_current_weather_data
import pytest



@pytest.mark.parametrize("location, expected",[("Tan Uyen",404)])
def test_get_location_current_weather_data(location, expected):
    code = get_location_current_weather_data(location)["code"]
    if code == 429:
        assert code == 429
    else:
        assert code == expected
