#!/usr/bin/env python

from urllib.request import urlretrieve as retrieve
url = 'http://nflsavant.com/pbp_data.php?year=2019'
retrieve (url,'nflsavant_2018-19-players.csv.')

