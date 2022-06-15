import requests



def get_location_current_weather_data(location):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"q": location, "units": "metric"}
    headers = {
        "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
        "X-RapidAPI-Key": "9584fc7ed9msh08fbaba91774455p1f2820jsn892312893eef"
    }
    print(f'Read data from {location}')
    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    if response.ok:
        data_dic = response.json()
        return {"code": response.status_code,"data": data_dic}
    else :
        return {"code": response.status_code,"message": response.text}
