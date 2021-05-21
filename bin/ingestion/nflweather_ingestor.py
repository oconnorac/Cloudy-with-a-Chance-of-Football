#!/usr/bin/env python
# This script ingests weather data from NFLWeather.com

import urllib.request
from bs4 import BeautifulSoup
import requests
import pandas as pd

# From investigation of the data, I know that pulling data from the
# URL format following this structure
# (http://www.nflweather.com/en/game/YYYY/week-W/away-at-home)
# structure and the <p> html tags provide a list of data
# (from the start of the game).
# The 3rd position shows the general weather detail,
# the 4th position shows the temperature,
# the 6th position shows the wind,
# the 7th position shows the humidity,
# the 11th position shows the cloud couver,
# and the 12th position shows the precipitation.

def weatherListSorter(soup):
    """
    This function takes html soup and pulls relevant data into pre-defined lists
    Input: html soup
    """
    detail.append(soup.find_all('p')[3].text.strip())
    temp.append(soup.find_all('p')[4].text.strip())
    wind.append(soup.find_all('p')[6].text.strip())
    humidity.append(soup.find_all('p')[7].text.strip())
    cloud_cover.append(soup.find_all('p')[11].text.strip())
    precipitation.append(soup.find_all('p')[12].text.strip())

if __name__ == 'main':

    # Make a series of lists for the data pulled below to feed into
    detail = []
    temp = []
    wind = []
    humidity = []
    cloud_cover = []
    precipitation = []

    df = pd.read_csv('../../fixtures/raw_data/spreadspoke_scores.csv')

    # Make two lambda functions that make away and home team lower case
    f = lambda x: x['team_away'].split()[-1].lower()
    f1 = lambda x: x['team_home'].split()[-1].lower()

    # Apply the two lambda functions above to the team_away_home and team_away_last functions
    df['team_away_last'] = df.apply(f, axis =1)
    df['team_home_last'] = df.apply(f1, axis = 1)

    # Make another dataframe column to make a URL from the format above for each game
    df['weather_url'] = df['schedule_season'] + '/week-' + df['schedule_week'] + '/' + df['team_away_last'] + '-at-' + df['team_home_last']
    
    for n in df['weather_url']:
    
        try:
        
            source = urllib.request.urlopen('http://www.nflweather.com/en/game/' + n).read()
            soup = BeautifulSoup(source, 'html.parser')
            
        except Exception:
            
            try:
                
                source = urllib.request.urlopen('http://www.nflweather.com/en/game/' + (n.replace('team','redskins'))).read()
                soup = BeautifulSoup(source, 'html.parser')

                weatherListSorter(soup)
            
            except Exception:
                
                try:
                
                    source = urllib.request.urlopen('http://www.nflweather.com/en/game/' + (n.replace('team','football%20team'))).read()
                    soup = BeautifulSoup(source, 'html.parser')

                    weatherListSorter(soup)
                    
                except Exception:
                
                    try:

                        source = urllib.request.urlopen('http://www.nflweather.com/en/game/' + (n.replace('team','washington'))).read()
                        soup = BeautifulSoup(source, 'html.parser')

                        weatherListSorter(soup)
                    
                    except Exception:
                        print(f'Error with url http://www.nflweather.com/en/game/{n}')

    df1 = pd.DataFrame()

    # Make new dataframe columns for all of the new lists
    df1['detail'] = detail
    df1['temp'] = temp
    df1['wind'] = wind
    df1['humidity'] = humidity
    df1['cloud_cover'] = cloud_cover
    df1['precipitation'] = precipitation

    df1.to_csv('../../fixtures/raw_data/weather_data_filler.csv')