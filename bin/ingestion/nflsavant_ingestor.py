#!/usr/bin/env python

#Using urllib, programmatically download/ingest CSV data.
#Be aware your IP address may get flagged after multiple uses in a short period of time
from urllib.request import urlretrieve as retrieve
url = 'http://nflsavant.com/pbp_data.php?year=2019'
retrieve(url,'nflsavant_201920-players.csv')

