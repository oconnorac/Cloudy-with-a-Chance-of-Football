#!/usr/bin/env python

#Using urllib, programmatically download/ingest CSV data.
#Be aware that script can only be used a limited number of times before IP address flagged.
from urllib.request import urlretrieve as retrieve
url = 'http://nflsavant.com/pbp_data.php?year=2019'
retrieve(url,'nflsavant_201920-players.csv')

