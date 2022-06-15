from datetime import datetime
from sorcery import dict_of
import pytz


def utc_to_timestamp_string(utc: int):
    date = datetime.fromtimestamp(utc)
    tz = pytz.timezone("Asia/Saigon")
    return date.astimezone(tz=tz).strftime('%Y-%m-%d %H:%M:%S')


def transform_city_data(data: dict):
    city_id = int(data['id'])
    name = str(data['name'])
    country_name = str(data['sys']['country'])
    timezone = int(data['timezone'])
    lat = float(data['coord']['lat'])
    lon = float(data['coord']['lon'])
    city_data = dict_of(city_id, name, country_name, timezone, lat, lon)
    return city_data

def transform_weather_data(data: dict):
    dt = utc_to_timestamp_string(int(data['dt']))
    temp = float(data['main']['temp'])
    real_temp = float(data['main']['feels_like'])
    temp_min = float(data['main']['temp_min'])
    temp_max = float(data['main']['temp_max'])
    pressure = float(data['main']['pressure'])
    humidity = float(data['main']['humidity'])
    sea_level = float(data['main'].get('sea_level', 0))
    grnd_level = float(data['main'].get('grnd_level', 0))
    visibility = float(data.get('visibility', 0))

    cloud_data = data.get('clouds', None)
    if cloud_data:
        cloud = float(cloud_data.get('all', 0))
    else:
        cloud = 0

    rain_data = data.get('rain', None)
    if rain_data:
        rain = float(rain_data.get(list(data.get('rain').keys())[0], 0))
    else:
        rain = 0

    wind_data = data.get('wind', None)
    if wind_data:
        wind_speed = float(wind_data.get('speed', 0))
        wind_deg = float(wind_data.get('deg', 0))
        wind_gust = float(wind_data.get('gust', 0))
    else:
        wind_speed = 0
        wind_deg = 0
        wind_gust = 0
    sunrise = utc_to_timestamp_string(int(data['sys']['sunrise']))
    sunset = utc_to_timestamp_string(int(data['sys']['sunset']))
    current_flag = "Y"
    weather_data = dict_of(dt,
                            temp,
                            real_temp,
                            temp_min,
                            temp_max,
                            pressure,
                            humidity,
                            sea_level,
                            grnd_level,
                            visibility,
                            cloud,
                            rain,
                            wind_speed,
                            wind_deg,
                            wind_gust,
                            sunrise,
                            sunset,
                            current_flag)
    return weather_data


def transform_status_data(data: dict):
    weather_list_value = data['weather']
    weather_data = weather_list_value[0]
    title = str(weather_data['main'])
    icon = str(weather_data['icon'])
    description = str(weather_data['description'])
    status_data = dict_of(title, icon, description)
    return status_data


def transform_data(data: dict):
    try:
        city = transform_city_data(data)
        weather = transform_weather_data(data)
        status = transform_status_data(data)
        return dict_of(city, weather, status)
    except KeyError:
        return KeyError
    except ValueError:
        return ValueError
    


# def transform_list_data(list_data: list):
#     list_transform_data = []
#     for data in list_data:
#         city = transform_city_data(data)
#         weather = transform_weather_data(data)
#         status = transform_status_data(data)
#         list_transform_data.append([city, weather, status])
#     return list_transform_data
