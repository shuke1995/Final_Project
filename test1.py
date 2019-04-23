### read weather data

import pandas as pd
import numpy as np


#city_attributes = pd.read_csv('./historical-hourly-weather-data/city_attributes.csv')

Humiditiy = pd.read_csv('./historical-hourly-weather-data/humidity.csv')
Humiditiy['datetime'] = pd.to_datetime(Humiditiy['datetime'])
Humiditiy.head()

Pressure = pd.read_csv('./historical-hourly-weather-data/pressure.csv')

Temperature = pd.read_csv('./historical-hourly-weather-data/temperature.csv')

weather_description = pd.read_csv('./historical-hourly-weather-data/weather_description.csv')

wind_direction = pd.read_csv('./historical-hourly-weather-data/wind_direction.csv')

wind_speed = pd.read_csv('./historical-hourly-weather-data/wind_speed.csv')

chicago_crime = pd.read_csv('./Chicago_crime_2012-2017.csv')
chicago_crime=chicago_crime[chicago_crime.Date.str[6:10] !='2018']

airpollution = pd.read_csv('./pollution_us_2000_2016.csv')


airpollution.head()
list(airpollution.columns.values)

set(airpollution['City'])

#airpollution['Date Local']

list(chicago_crime.columns.values)
chicago_crime[['Primary Type', 'ID']].groupby(['Primary Type']).count()



#city_attributes.head()
Humiditiy.head()

#Humiditiy['datetime']

Pressure.head()
Temperature.head()
weather_description.head()
wind_direction.head()
wind_speed.head()


#Weather and crime

#Compute the crime every year each month
#print(chicago_crime.columns.values)

#print(chicago_crime.Date.str[3:10])
#chi_crime_per_month=chicago_crime.groupby(chicago_crime.Date.str[3:10]).count()
#print(chi_crime_per_month.head(10))

#check the type of the datetime in datasets
chi_humidity=Humiditiy[['datetime','Chicago']]
chi_temp=Temperature[['datetime','Chicago']]
#print(chi_temp.dtypes)
chi_pressure=Pressure[['datetime','Chicago']]
#print(chi_pressure.dtypes)
chi_wind_speed=wind_speed[['datetime','Chicago']]
#print(chi_wind_speed.dtypes)

chi_humidity=chi_humidity.astype({'datetime':'object','Chicago':'float64'})
#print(chi_humidity.dtypes)


#Compute the crime every year each month
chi_crime_per_month=chicago_crime.groupby(pd.to_datetime(chicago_crime['Date']).dt.to_period('M')).count()
chi_crime_per_month=chi_crime_per_month[['ID']].reset_index().rename(columns={'ID':'crime count','Date':'datetime'})
print(chi_crime_per_month.head(20))

#compute the average humidity each year each month
#chi_humidity=Humiditiy[['datetime','Chicago']]
print(chi_humidity.dtypes)
chi_humidity_per_month=chi_humidity.groupby(chi_humidity['datetime'].dt.to_period('M'))\
    ['Chicago'].agg(['mean']).reset_index().rename(columns={'mean':'Chi_humidity'})

print(chi_humidity_per_month.head())

#merge crime with humidity data
crime_humidity=pd.merge(chi_humidity_per_month,chi_crime_per_month, on='datetime',how='left')
print(crime_humidity.head(20))


#compute the average temperature


