mock = {'raw_city_data' : {
    "coord": {
            "lon": 100.5167,
            "lat": 13.75
        },
    "sys": {
            "country": "TH"
        },
    "timezone": 25200,
        "id": 1609350,
        "name": "Bangkok",
        "cod": 200
},

'raw_weather_data' :{
    "main": {
            "temp": 89.51,
            "feels_like": 101.97,
            "temp_min": 88.92,
            "temp_max": 93.92,
            "pressure": 1006,
            "humidity": 66,
            "sea_level": 1006,
            "grnd_level": 1005
        },
        "visibility": 10000,
        "wind": {
            "speed": 10.4,
            "deg": 207,
            "gust": 14.97
        },
        "clouds": {
            "all": 100
        },
        "dt": 1653379025,"sys": {
            "type": 2,
            "id": 2032756,
            "country": "TH",
            "sunrise": 1653346199,
            "sunset": 1653392388
        }
},

'raw_status_data' :{
    "weather": [
            {
                "id": 804,
                "main": "Clouds",
                "description": "overcast clouds",
                "icon": "04d"
            }
        ]
},

'raw_data' : {
    "coord": {
            "lon": 100.5167,
            "lat": 13.75
        },
        "weather": [
            {
                "id": 804,
                "main": "Clouds",
                "description": "overcast clouds",
                "icon": "04d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 89.51,
            "feels_like": 101.97,
            "temp_min": 88.92,
            "temp_max": 93.92,
            "pressure": 1006,
            "humidity": 66,
            "sea_level": 1006,
            "grnd_level": 1005
        },
        "visibility": 10000,
        "wind": {
            "speed": 10.4,
            "deg": 207,
            "gust": 14.97
        },
        "clouds": {
            "all": 100
        },
        "dt": 1653379025,
        "sys": {
            "type": 2,
            "id": 2032756,
            "country": "TH",
            "sunrise": 1653346199,
            "sunset": 1653392388
        },
        "timezone": 25200,
        "id": 1609350,
        "name": "Bangkok",
        "cod": 200
},
'key_error_data' : {
        "lon": 100.5167,
        "lat": 13.75,
        "weather": [
            {
                "id": 804,
                "main": "Clouds",
                "icon": "04d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 89.51,
            "feels_like": 101.97,
            "temp_min": 88.92,
            "pressure": 1006,
            "humidity": 66,
            "grnd_level": 1005
        },
        "visibility": 10000,
        "wind": {
            "speed": 10.4,
            "deg": 207,
            "gust": 14.97
        },
        "clouds": {
            "all": 100
        },
        "dt": 1653379025,
        "sys": {
            "type": 2,
            "id": 2032756,
            "country": "TH",
            "sunset": 1653392388
        },
        "timezone": 25200,
        "id": 1609350,
        "cod": 200
},

'key_error_city_data' : {

            "lon": 100.5167,
            "lat": 13.75,

    "sys": {
            "country": "TH"
        },
    "timezone": 25200,
        "id": 1609350,
        "name": "Bangkok",
        "cod": 200
},
'key_error_weather_data' :{
    "main": {
            "temp": 89.51,
            "feels_like": 101.97,
            "temp_min": 88.92,
            "temp_max": 93.92,
            "pressure": 1006,
            "humidity": 66,
            "sea_level": 1006,
            "grnd_level": 1005
        },
        "wind": {
            "speed": 10.4,
            "deg": 207,
            "gust": 14.97
        },
        "clouds": {
            "all": 100
        },
        "dt": 1653379025
},
'key_error_status_data' :{
    "weather": [
            {
                "id": 804,
                "description": "overcast clouds",
                "icon": "04d"
            }
        ]
},
'value_error_data' : {
    "coord": {
            "lon": 100.5167,
            "lat": 13.75
        },
        "weather": [
            {
                "id": 804,
                "main": "Clouds",
                "description": "overcast clouds",
                "icon": "04d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 89.51,
            "feels_like": 101.97,
            "temp_min": 88.92,
            "temp_max": 93.92,
            "pressure": 1006,
            "humidity": 66,
            "sea_level": 1006,
            "grnd_level": "high"
        },
        "visibility": 10000,
        "wind": {
            "speed": 10.4,
            "deg": 207,
            "gust": 14.97
        },
        "clouds": {
            "all": 100
        },
        "dt": 1653379025,
        "sys": {
            "type": 2,
            "id": 2032756,
            "country": "TH",
            "sunrise": 1653346199,
            "sunset": 1653392388
        },
        "timezone": 25200,
        "id": 1609350,
        "name": "Bangkok",
        "cod": 200
},
'value_error_weather_data' :{
    "main": {
            "temp": 89.51,
            "feels_like": 101.97,
            "temp_min": 88.92,
            "temp_max": 93.92,
            "pressure": 1006,
            "humidity": 66,
            "sea_level": 1006,
            "grnd_level": 1005
        },
        "visibility": 'hello',
        "wind": {
            "speed": 10.4,
            "deg": 207,
            "gust": 14.97
        },
        "clouds": {
            "all": 100
        },
        "dt": 1653379025
},
'value_error_city_data' : {
    "coord": {
            "lon": 100.5167,
            "lat": 13.75
        },
    "sys": {
            "country": "TH"
        },
    "timezone": 25200,
        "id": '1609350adv',
        "name": "Bangkok",
        "cod": 200
},


'clean_city_data' : {
        "city_id": 1609350,
        "name": "Bangkok",
        "country_name": "TH",
        "timezone": 25200,
        "lat": 13.75,
        "lon": 100.5167
    },

'clean_status_data' : {
        "title": "Clouds",
        "icon": "04d",
        "description": "overcast clouds"
    },

'clean_weather_data' : {
        "dt": "2022-05-24 14:57:05",
        "temp": 89.51,
        "real_temp": 101.97,
        "temp_min": 88.92,
        "temp_max": 93.92,
        "pressure": 1006.0,
        "humidity": 66.0,
        "sea_level": 1006.0,
        "grnd_level": 1005.0,
        "visibility": 10000.0,
        "cloud": 100.0,
        "rain": 0,
        "wind_speed": 10.4,
        "wind_deg": 207.0,
        "wind_gust": 14.97,
        "sunrise": "2022-05-24 05:49:59",
        "sunset": "2022-05-24 18:39:48",
        "current_flag": "Y"
    },

'clean_data' : {
    'city': {
        "city_id": 1609350,
        "name": "Bangkok",
        "country_name": "TH",
        "timezone": 25200,
        "lat": 13.75,
        "lon": 100.5167
    },
    'status': {
        "title": "Clouds",
        "icon": "04d",
        "description": "overcast clouds"
    },
    'weather': {
        "dt": "2022-05-24 14:57:05",
        "temp": 89.51,
        "real_temp": 101.97,
        "temp_min": 88.92,
        "temp_max": 93.92,
        "pressure": 1006.0,
        "humidity": 66.0,
        "sea_level": 1006.0,
        "grnd_level": 1005.0,
        "visibility": 10000.0,
        "cloud": 100.0,
        "rain": 0,
        "wind_speed": 10.4,
        "wind_deg": 207.0,
        "wind_gust": 14.97,
        "sunrise": "2022-05-24 05:49:59",
        "sunset": "2022-05-24 18:39:48",
        "current_flag": "Y"
    }
}
}