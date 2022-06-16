from src.api import get_location_current_weather_data
from unittest import mock

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.ok = True

        def json(self):
            return self.json_data
    if kwargs['params']['q'] == 'hanoi':
        return MockResponse({"data": "value1"}, 200)
    return MockResponse(None, 404)


@mock.patch('requests.get', side_effect=mocked_requests_get)
def test_success_get_location_current_weather_data(mock_get):
    code = get_location_current_weather_data('hanoi')['code']
    assert code == 200


@mock.patch('requests.get', side_effect=mocked_requests_get)
def test_fail_get_location_current_weather_data(mock_get):
    code = get_location_current_weather_data('tan uyen')['code']
    assert code == 404
