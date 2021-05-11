# !/usr/bin/env python
# This script ingests weekly 2018 - 2020 fantasy data and projections from fantasydata.com
# Run this script and do not upload the csv to GitHub repo

from urllib.request import urlopen
import requests
import json
import pandas as pd

fantasy_data_list = []
fantasy_projections_list = []
df = pd.DataFrame()

if __name__ == 'main':
    api_key = input('Please enter the fantasydata API key: ')

    for x, y in [(x,y) for x in ['2018','2019','2020'] for y in range(1,18)]:
        fantasy_data_list.append('https://fly.sportsdata.io/api/nfl/fantasy/json/PlayerGameStatsByWeek/' + x + '/' + str(y))
        fantasy_projections_list.append('https://fly.sportsdata.io/api/nfl/fantasy/json/PlayerGameProjectionStatsByWeek/' + x + '/' + str(y))

    for n in url_list:
        r = requests.get(url = n, headers={'Ocp-Apim-Subscription-Key': api_key})
        r = r.json()
        df1 = pd.json_normalize(r, max_level=1)
        df = df.append(df1)

    df2.to_csv('../fixtures/raw_data/fantasy_data_projections.csv')
    df.to_csv('../fixtures/raw_data/fantasy_data.csv')