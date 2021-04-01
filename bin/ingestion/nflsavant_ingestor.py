#!/usr/bin/env python

#Using urllib, programmatically download/ingest CSV data.
from urllib.request import urlretrieve as retrieve
url = 'http://nflsavant.com/pbp_data.php?year=2019'
retrieve(url,'nflsavant_201920-players.csv')

