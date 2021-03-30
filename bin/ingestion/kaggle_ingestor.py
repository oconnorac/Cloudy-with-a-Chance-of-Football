#!/usr/bin/env python

from urllib.request import urlretrieve as retrieve

positions = ['defense_stats_and_projections.csv', 'kicker_stats_and_projections.csv', 'qb_stats_and_projections.csv', 'rb_stats_and_projections.csv', 'te_stats_and_projections.csv', 'wr_stats_and_projections.csv']

for i in positions:
    url = 'https://www.kaggle.com/mur418/espn-2019-stats-and-2020-nfl-fantasy-projections?select='
    retrieve (url,i)
