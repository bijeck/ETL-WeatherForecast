import pytest
from src.etl.extract import extract_location_weather_data


# @pytest.mark.parametrize("location, expected",[("hanoi", True), ("Tan Uyen",False)])
# def test_extract_location_weather_data(location,expected):
#     assert isinstance(extract_location_weather_data(location),dict) is expected


@pytest.mark.parametrize("location, resp, expected",[
                                                    ("hanoi", {'code':200,'data':{'location':'hanoi','id':1}}, True),
                                                    ("Tan Uyen", {'code':404,'message':'Wrong Location'}, False)])
def test_extract_location_weather_data(location,resp,expected,mocker):
    mocker.patch("src.etl.extract.get_location_current_weather_data",return_value=resp)
    assert isinstance(extract_location_weather_data(location),dict) is expected

