### read weather data

import pandas as pd
import numpy as np

Humiditiy = pd.read_csv('./historical-hourly-weather-data/humidity.csv')

Pressure = pd.read_csv('./historical-hourly-weather-data/pressure.csv')

Temperature = pd.read_csv('./historical-hourly-weather-data/temperature.csv')

weather_description = pd.read_csv('./historical-hourly-weather-data/weather_description.csv')

wind_direction = pd.read_csv('./historical-hourly-weather-data/wind_direction.csv')

wind_speed = pd.read_csv('./historical-hourly-weather-data/wind_speed.csv')



Humiditiy.head()
Pressure.head()
Temperature.head()
weather_description.head()
wind_direction.head()
wind_speed.head()
