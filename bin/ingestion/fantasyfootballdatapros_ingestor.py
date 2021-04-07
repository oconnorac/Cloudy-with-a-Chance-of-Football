#!/usr/bin/env python

#Using urllib, programmatically download/ingest CSV data.
#Be aware your IP address may get flagged after multiple uses in a short period of time
from urllib.request import urlretrieve as retrieve
url = 'https://www.fantasyfootballdatapros.com/static/files/2019projections.csv'
retrieve(url,'datapros_2019.csv')

