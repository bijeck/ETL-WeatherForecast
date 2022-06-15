# ETL Project 

[![CI](https://github.com/bijeck/ETL-WeatherForecast/actions/workflows/python-app.yml/badge.svg)](https://github.com/bijeck/ETL-WeatherForecast/actions/workflows/python-app.yml)
![Code Coverage]()

## Requirements
Project uses a number of open source projects to work properly:
- [MySQL] - For run sql query and store data
- [Python] - Main programming language that lets project run effectively.
- [MySQL Workbench] - Manipulate with database, and show data
---

## Project Folder
- `mock`: contains mock data for testing
- `src` : contains source files
- `src/etl` : contains etl files
- `tests` : contains tests files
- `tests/etl` : contains etl tests files
- `config.json`: contains configuration for `MySQL` server
- `requirements.txt`: list python requirement packages
- `.github/workflows/python-app.yml`: file for run CI in github
- `database.sql`: database script
- `weather_schema.png`: database weather schema
---

## Create Enviroment

Be Sure you have Virtulenv installed if not running below:
```sh
>> pip install virtualenv
```

After unzip the project, create a virtual environment with the following:
```sh
>> cd ETL_SuMP
>> virtualenv venv
```

Then active the virtual environment and install the packages:
```sh
# For Mac or Linux
>> source venv/bin/activate

# For windows
>> venv\Scripts\activate.bat
```

---

## Installation 
Install python packages to run project effectively:
```sh
>> pip install -r requirements.txt
```
---
## Configuration
Configure your MySQL server in `config.json`:
| Key | Value |
| ------ | ------ |
| `host` | localhost |
| `user` | root|
| `password` | yourpassword |
| `database` | databasename|
---
## Run Project
Create database and table:
```sh
>> python src\db.py
```
Run project:
```sh
>> python src\main.py
```
Enter your location to fetch data:
```sh
>> Enter your location: london
```

Your location 's data will countinue get after 30 seconds.
You can terminate the project by press in your keyboard:
> Note: `You can terminate the project by press Ctrl + C`

---

## Run Test

Run test:
```sh
>> pytest -v
```

Run test with keywords( Examples: `get`,`extract`,`transform`,`error`):
```sh
>> pytest -k keywords -v
```

Run to see coverage results:
```sh
>> coverage report
```

Run to see coverage all project results:
```sh
>> pytest --cov=. tests/
```

---

## Slow Changing Dimensions

#### SCD Type 1
- Apply in `city_dim` table.
- Replace attribute from old record by new record with same `city_id`

#### SCD Type 2
- Apply in `weather_fact` table.
- Record have `current_flag` column to monitor the current weather of city.
- When new weather datas is inserted, its `current_flag` will be `Y` and old record will be `N`. So we can keep the historical weather data of a city.

---
## Note

You can use `database.sql` file to create database and it contains data for you.
> Note: Rename `database name` in the file with your prefer `name`.

---