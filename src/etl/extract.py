try:
    from api import get_location_current_weather_data
except ImportError:
    from src.api import get_location_current_weather_data



def extract_location_weather_data(location: str):
    try:
        response = get_location_current_weather_data(location)
        if response["code"] == 200:
            return response["data"]
        else:
            return None
    except TypeError:
        print("TypeError occur when extract data")
    except ValueError:
        print("ValueError occur when extract data")

