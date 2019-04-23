import pandas as pd
import numpy as np




def read_indata(path):
    '''

    :param path: a string of path saved the dataset
    :return: pandas datarame
    '''
    data = pd.read_csv(path)
    return data




## generate new column year for every data

def generate_year(df, colname):
    '''

    :param df: dataframe we want to add column year and month
    :param colname: a stirng column name in the dataframe saved the dateandtime
    :return: dataframe after adding the column
    '''
    df['year'] = pd.DatetimeIndex(df[colname]).year
    df['month'] = pd.DatetimeIndex(df[colname]).month
    return df






#### Soluruib

if __name__ == "__main__":

    city_attributes = read_indata('./historical-hourly-weather-data/city_attributes.csv')
    Humiditiy = read_indata('./historical-hourly-weather-data/humidity.csv')
    Pressure = read_indata('./historical-hourly-weather-data/pressure.csv')
    Temperature = read_indata('./historical-hourly-weather-data/temperature.csv')
    weather_description = read_indata('./historical-hourly-weather-data/weather_description.csv')
    wind_direction = read_indata('./historical-hourly-weather-data/wind_direction.csv')
    wind_speed = read_indata('./historical-hourly-weather-data/wind_speed.csv')
    chicago_crime = read_indata('./Chicago_crime_2012-2017.csv')
    airpollution = read_indata('./pollution_us_2000_2016.csv')


    ### ADD YEAR AND MONTH COLUMN TO DATA
    df_list = [Humiditiy, Pressure, Temperature, weather_description, wind_direction,
               wind_speed]
    for data in df_list:
        data = generate_year_month(data, 'datetime')

    airpollution = generate_year_month(airpollution, 'Date Local')
