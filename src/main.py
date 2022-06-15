from etl.extract import  extract_location_weather_data
from etl.transform import  transform_data
from etl.load import load
import schedule
from utilities import countdown
import os


def etl(location):
    data = extract_location_weather_data(location)
    while True:
        try:
            while data is None:
                print("Cannot find location. Please try again!")
                location = input('Enter your location: ')
                data = extract_location_weather_data(location)
            transformed_data = transform_data(data)
            load(transformed_data['city'], transformed_data['status'], transformed_data['weather'])
            print("API will continue be called after 30 seconds.(Press Ctrl+C to Shutdown)")
            break
        except ValueError as error:
            print("Cast value error in status transform "+ error)
            data = None
        except KeyError as error:
            print("Cannot find key in city transform "+ error)
            data = None


location = input('Enter your location: ')
etl(location)
schedule.every(30).seconds.do(etl,location)
while True:
    schedule.run_pending()
    countdown(30)
    os.system('cls' if os.name == 'nt' else 'clear')
