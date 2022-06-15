from src.etl.transform import transform_city_data,\
                            transform_status_data,\
                            transform_weather_data,\
                            utc_to_timestamp_string,\
                            transform_data
import pytest
from mock.mock_data import mock



@pytest.mark.parametrize("input_data, expected_data",[
                                                    (mock['raw_city_data'],
                                                    mock['clean_city_data'])])
def test_transform_city_data(input_data,expected_data):
    assert transform_city_data(input_data) == expected_data



@pytest.mark.parametrize("input_data, expected_data",[
                                                    (mock['raw_status_data'],
                                                    mock['clean_status_data'])])
def test_transform_status_data(input_data,expected_data):
    assert transform_status_data(input_data) == expected_data



@pytest.mark.parametrize("input_data, expected_data",[
                                                    (mock['raw_weather_data'],
                                                    mock['clean_weather_data'])])
def test_transform_weather_data(input_data,expected_data):
    out_data = transform_weather_data(input_data)
    assert out_data == expected_data
    


@pytest.mark.parametrize("input_data, expected_data",[
                                                    (mock['raw_data'],
                                                    mock['clean_data'])])
def test_transform_data(input_data,expected_data):
    assert transform_data(input_data) == expected_data
    


@pytest.mark.parametrize("input_data",[(mock['key_error_data'])])
def test_key_error_transform_data(input_data):
    assert transform_data(input_data) == KeyError



@pytest.mark.parametrize("input_data",[(mock['key_error_city_data'])])
def test_key_error_transform_city_data(input_data):
    with pytest.raises(KeyError):
        transform_city_data(input_data)
        
    

@pytest.mark.parametrize("input_data",[(mock['key_error_status_data'])])
def test_key_error_transform_status_data(input_data):
    with pytest.raises(KeyError):
        transform_status_data(input_data)
    

 
@pytest.mark.parametrize("input_data",[(mock['key_error_weather_data'])])
def test_key_error_transform_weather_data(input_data):
    with pytest.raises(KeyError):
        transform_weather_data(input_data)
    

 
@pytest.mark.parametrize("input_data",[(mock['value_error_data'])])
def test_value_error_transform_data(input_data):
    assert transform_data(input_data) == ValueError
    
    
 
@pytest.mark.parametrize("input_data",[(mock['value_error_weather_data'])])
def test_value_error_transform_weather_data(input_data):
    with pytest.raises(ValueError):
        transform_weather_data(input_data)
    
    

@pytest.mark.parametrize("input_data",[(mock['value_error_city_data'])])
def test_value_error_transform_city_data(input_data):
    with pytest.raises(ValueError):
        transform_city_data(input_data)
    

@pytest.mark.parametrize("input_data, expected_data",[
                                                    (1653379025,
                                                     "2022-05-24 14:57:05")])
def test_utc_to_timestamp_string(input_data,expected_data):
    assert utc_to_timestamp_string(input_data) == expected_data