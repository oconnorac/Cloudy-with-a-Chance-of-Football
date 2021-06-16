#!/usr/bin/env python
# Pulls fantasy football player basic data from fantasydata.com

import requests
import pandas as pd

player_data_url = 'https://fly.sportsdata.io/api/nfl/fantasy/json/Players'

if __name__ == '__main__':
    api_key_fantasydata = input("Please enter your fantasydata.com API Key: ")
    player_data = requests.get(
        url = player_data_url,
        headers = {
            'Ocp-Apim-Subscription-Key': str(api_key_fantasydata)
        }
    )

    player_data = player_data.json()
    player_data_df = pd.json_normalize(player_data, max_level=1)

    player_data_df.to_csv('../fixtures/raw_data/player_data.csv')