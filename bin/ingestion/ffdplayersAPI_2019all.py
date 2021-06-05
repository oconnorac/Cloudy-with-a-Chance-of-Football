#!/usr/bin/env python

import numpy as np
import pandas as pd
import json
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

ffd_players_API = 'https://www.fantasyfootballdatapros.com/api/players/2019/all'

response = requests.get(ffd_players_API)
if response.status_code == 200:
    print(response)

r = requests.get(ffd_players_API)
files = r.json()
print(files)

# Turn json into actual dataframe format

ffd_players_API_df = pd.json_normalize(files, max_level=1)

ffd_players_API_df.to_csv('../../fixtures/raw_data/ffd_players_API.csv', index = False)