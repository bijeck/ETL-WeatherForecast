from asyncio import set_event_loop
import mysql.connector
from mysql.connector import Error
import json
import os

from requests import patch


def read_config():
    path = os.path.abspath(".\config.json")
    with open(path) as f:
        config = json.load(f)
    return config


def create_connection():
    try:
        config = read_config()
        conn = mysql.connector.connect(host=config['host'],
                                       database=config['database'],
                                       user=config['user'],
                                       password=config['password'])
        if conn.is_connected():
            return conn
    except Error as e:
        print("Error while connecting to MySQL", e)


def create_database():
    try:
        config = read_config()
        conn = mysql.connector.connect(host=config['host'],
                                       user=config['user'],
                                       password=config['password'])
        if conn.is_connected():
            cursor = conn.cursor()
            sql = f"CREATE DATABASE {config['database']}"
            cursor.execute(sql)
            conn.commit()
            print(f"Created {config['database']} database!")
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def create_table(conn):
    try:
        create_citydim_table_query = """CREATE TABLE IF NOT EXISTS CITY_DIM ( 
                                 CITY_ID INT NOT NULL,
                                 NAME VARCHAR(30) NOT NULL,
                                 COUNTRY_NAME VARCHAR(15) NOT NULL,
                                 TIMEZONE INT NOT NULL,
                                 LAT FLOAT NOT NULL,
                                 LON FLOAT NOT NULL,
                                 PRIMARY KEY (CITY_ID)) """
        create_weatherfact_table_query = """CREATE TABLE IF NOT EXISTS WEATHER_FACT ( 
                                         CITY_ID INT NOT NULL,
                                         STATUS_ID INT NOT NULL,
                                         DT DATETIME NOT NULL,
                                         TEMP FLOAT NOT NULL,
                                         REAL_TEMP FLOAT NOT NULL,
                                         TEMP_MIN FLOAT NOT NULL,
                                         TEMP_MAX FLOAT NOT NULL,
                                         PRESSURE FLOAT DEFAULT 0,
                                         HUMIDITY FLOAT DEFAULT 0,
                                         SEA_LEVEL FLOAT DEFAULT 0,
                                         GRND_LEVEL FLOAT DEFAULT 0,
                                         VISIBILITY FLOAT DEFAULT 0,
                                         CLOUD FLOAT DEFAULT 0,
                                         RAIN FLOAT DEFAULT 0,
                                         WIND_SPEED FLOAT DEFAULT 0,
                                         WIND_DEG FLOAT DEFAULT 0,
                                         WIND_GUST FLOAT DEFAULT 0,
                                         SUNRISE DATETIME NOT NULL,
                                         SUNSET DATETIME NOT NULL,
                                         CURRENT_FLAG VARCHAR(1) NOT NULL,
                                         PRIMARY KEY (CITY_ID,STATUS_ID),
                                         FOREIGN KEY (CITY_ID) REFERENCES CITY_DIM(CITY_ID),
                                         FOREIGN KEY (STATUS_ID) REFERENCES STATUS_DIM(STATUS_ID)) """
        create_statusdim_table_query = """CREATE TABLE IF NOT EXISTS STATUS_DIM ( 
                                         STATUS_ID INT NOT NULL AUTO_INCREMENT,
                                         TITLE VARCHAR(30) NOT NULL,
                                         ICON VARCHAR(15) NOT NULL,
                                         DESCRIPTION VARCHAR(100) NOT NULL,
                                         PRIMARY KEY (STATUS_ID))"""

        cursor = conn.cursor()
        cursor.execute(create_citydim_table_query)
        cursor.execute(create_statusdim_table_query)
        cursor.execute(create_weatherfact_table_query)
        print("Tables created successfully!")
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def insert_with_update_city(conn, value):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM CITY_DIM WHERE CITY_ID = %s", (value['city_id'],))
        if cursor.fetchone():
            update_records(conn, value)
        else:
            insert_city_query = ("INSERT INTO CITY_DIM "
                                 "(CITY_ID, NAME, COUNTRY_NAME, TIMEZONE, LAT, LON) "
                                 "VALUES (%(city_id)s, %(name)s,"
                                 "%(country_name)s, %(timezone)s, %(lat)s, %(lon)s)")
            cursor.execute(insert_city_query, value)
            conn.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record in MySQL: {}".format(error))


def update_records(conn, value):
    try:
        update_city_query = ("UPDATE CITY_DIM "
                             "SET name = %(name)s, country_name = %(country_name)s, timezone=%(timezone)s,"
                             "lat = %(lat)s, lon = %(lon)s "
                             "WHERE city_id = %(city_id)s")
        cursor = conn.cursor()
        cursor.execute(update_city_query, value)
        conn.commit()
    except mysql.connector.Error as error:
        print("Failed to update record in MySQL: {}".format(error))


def insert_to_weather_table(conn, sql, value: tuple):
    try:
        cursor = conn.cursor()
        update_records(conn, {'city_id': value['city_id']})
        cursor.execute(sql, value)
        conn.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record in MySQL: {}".format(error))

def set_safe_update(conn,number:int):
    try:
        set_query = ("SET SQL_SAFE_UPDATES = %s")
        cursor = conn.cursor()
        cursor.execute(set_query, (number,))
        conn.commit()
    except mysql.connector.Error as error:
        print("Failed to set_safe_update in MySQL: {}".format(error))
def update_records(conn, value):
    try:
        set_safe_update(conn,0)
        update_city_query = ("UPDATE WEATHER_FACT "
                             "SET CURRENT_FLAG = \"N\" "
                             "WHERE CURRENT_FLAG = \"Y\" AND CITY_ID = %(city_id)s")
        cursor = conn.cursor()
        cursor.execute(update_city_query, value)
        conn.commit()
        set_safe_update(conn,1)
    except mysql.connector.Error as error:
        print("Failed to update record in MySQL: {}".format(error))


def insert_to_table_get_id_back(conn, sql, value: tuple):
    try:
        cursor = conn.cursor()
        cursor.execute(sql, value)
        conn.commit()
        return cursor.lastrowid
    except mysql.connector.Error as error:
        print("Failed to insert record in MySQL: {}".format(error))


def insert_data(conn, weather_data, status_data, city_data):
    try:
        insert_with_update_city(conn, city_data)
        insert_status_query = ("INSERT INTO STATUS_DIM "
                               "(TITLE, ICON, DESCRIPTION) "
                               "VALUES (%(title)s, %(icon)s, %(description)s)")
        status_id = insert_to_table_get_id_back(
            conn, insert_status_query, status_data)

        weather_data.update(
            {"city_id": city_data["city_id"], "status_id": status_id})
        insert_weather_query = ("INSERT INTO WEATHER_FACT "
                                "(CITY_ID, STATUS_ID, DT,TEMP,REAL_TEMP,TEMP_MIN,TEMP_MAX,PRESSURE,"
                                "HUMIDITY,SEA_LEVEL,GRND_LEVEL,VISIBILITY,CLOUD,RAIN,WIND_SPEED,"
                                "WIND_DEG,WIND_GUST,SUNRISE,SUNSET,CURRENT_FLAG) "
                                "VALUES (%(city_id)s, %(status_id)s, %(dt)s, %(temp)s, %(real_temp)s,"
                                "%(temp_min)s, %(temp_max)s, %(pressure)s, %(humidity)s, %(sea_level)s,"
                                "%(grnd_level)s, %(visibility)s, %(cloud)s, %(rain)s, %(wind_speed)s,"
                                "%(wind_deg)s, %(wind_gust)s, %(sunrise)s, %(sunset)s,%(current_flag)s)")
        insert_to_weather_table(conn, insert_weather_query, weather_data)
    except mysql.connector.Error as error:
        print("Failed to insert record in MySQL: {}".format(error))


if __name__ == "__main__":
    create_database()
    conn = create_connection()
    create_table(conn)
