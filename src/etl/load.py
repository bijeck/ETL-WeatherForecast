from db import create_connection, insert_data


def load(city_data, status_data, weather_data):
    conn = create_connection()
    insert_data(conn, weather_data, status_data, city_data)
    print('Add new record successfully!')
