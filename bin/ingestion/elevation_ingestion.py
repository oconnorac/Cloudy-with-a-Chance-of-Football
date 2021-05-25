#!/usr/bin/env python
# Pull elevation data from Google Maps API

import pandas as pd
import simplejson
import urllib

API_KEY = input('Please enter your Google Maps API key: ')
path = path = input('Please enter the path to the dataframe you would like to use: ')
df = pd.read_csv(str(path))


def getElevation(path, API_KEY):
    """
    Grabs elevation data (in feet) from Google Maps API
    Input: path to dataframe with lat and long columns
    API_KEY: Google Maps API key
    """
    elevationArray = []
    ELEVATION_BASE_URL = 'https://maps.googleapis.com/maps/api/elevation/json?locations='
    for n in range(0,len(df)):
        response = simplejson.load(urllib.request.urlopen(
            ELEVATION_BASE_URL
            + str(df['latitude'][n])
            + ','
            + str(df['longitude'][n])
            + '&key='
            + API_KEY)
        )
    
        for n in response['results']:
            elevationArray.append((n['elevation'])*100)

    df['elevation'] = elevationArray


if __name__ == '__main__':
    getElevation(path, API_KEY)
    df.to_csv('../../fixtures/cleaned_data/stadium_elevations.csv', index = False)