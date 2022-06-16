import requests
from utilities import read_config


def get_location_current_weather_data(location):
    config = read_config()
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"q": location, "units": "metric"}
    headers = {
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
        "X-RapidAPI-Key": config['X-RapidAPI-Key']
    }
    print(f'Read data from {location}')
    response = requests.get(url, params=querystring, headers=headers)
    if response.ok:
        data_dic = response.json()
        return {"code": response.status_code,"data": data_dic}
    else :
        return {"code": response.status_code,"message": response.text}
