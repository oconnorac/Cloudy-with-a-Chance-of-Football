# !/usr/bin/env python
# This script sets up the SQLite database structure for Cloudy With a Chance of Football
# The full description of the database schema can be seen in Deliverable 2

# Import sqlite3 to set up the database and pandas to assist with bringing tables and columns into the database
import sqlite3
import pandas as pd
import os

# Create a list of all table names
table_names = [
    'players',
    'positions',
    'player_dob',
    'injury_status',
    'player_age',
    'player_team',
    'days_since_last_game',
    'time_displacement_table',
    'weather',
    'opponents table',
    'stats_table',
    'week_table',
    'team_home_time_zone',
    'game_location',
    'performance'
]

# Create a list of lists for all column names for each table
column_names = [
    ['player_id','unique_id','player_name'],
    ['player_id','position'],
    ['player_id','dob'],
    ['player_id','week_id','injury_status'],
    ['player_id','week_id','age'],
    ['player_id','week_id','team_name'],
    ['team_name','week_id','days_since_last_game'],
    ['team_name','week_id','hours_displaced'],
    ['team_name','week_id','temperature_min','temperature_max','precipitation'],
    ['team_name','week_id','game_date','game_time','week_day','ARZ','ATL','BLT','BUF','CAR','CHI','CIN','CLV','DAL','DEN','DET','GB','HST','IND','JAX','KC','LV','LAC','LAR','MIA','MIN','NE','NO','NYG','NYJ','PHI','PIT','SF','SEA','TB','TEN','WAS'],
    ['team_name','week_id','PassingYds','PassingTD','Int','PassingAtt','Cmp','RushingAtt','RushingYds','RushingTD','Rec','Tgt','ReceivingYds','ReceivingTD','FL'],
    ['year','week','week_start','week_id'],
    ['team_name','week_id','time_zone'],
    ['week_id','team_name','location'],
    ['player_id','week_id','predicted','actual','performance']
]

# Create a list of lists for all data types
column_data_types = [
    ['INTEGER PRIMARY KEY AUTOINCREMENT','TEXT','TEXT'],
    ['INTEGER','TEXT'],
    ['INTEGER','TEXT'],
    ['INTEGER','TEXT','INTEGER'],
    ['INTEGER','TEXT','REAL'],
    ['INTEGER','TEXT','TEXT'],
    ['TEXT','TEXT','INTEGER'],
    ['TEXT','TEXT','INTEGER'],
    ['TEXT','TEXT','REAL','REAL','REAL'],
    ['TEXT','TEXT','TEXT','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER','INTEGER'],
    ['INTEGER','INTEGER','TEXT','TEXT'],
    ['TEXT','TEXT','INTEGER'],
    ['TEXT','TEXT','INTEGER'],
    ['INTEGER','TEXT','REAL','REAL','INTEGER']
]

# Read in the 3 lists above into a pandas dataframe
df = pd.DataFrame(list(
    zip(table_names, column_names, column_data_types)),
    columns = ['table_names','column_names','column_data_types'])

# Establish the path to and open a connection to the database
DBPATH = 'cloudy_with_a_chance_of_football.db'
conn = sqlite3.connect(DBPATH)


def create_tables(conn, dataframe):
    """
    Purpose: Translate a dataframe containing database table and column information into a database
    Input Type: Dataframe with 3 columns (table name, column names, column data types, and instructions)
    """
    cursor = conn.cursor()
    for row in range(len(dataframe)):
        sql = "CREATE TABLE IF NOT EXISTS " + dataframe.iloc[row,0]+" ("
        for n in range(len(dataframe)):
            if n < len(dataframe.iloc[row,1]):
                sql += dataframe.iloc[row, 1][n] + " " + dataframe.iloc[row, 2][n] + " NOT NULL, "
            elif n == len(dataframe.iloc[row,1]):
                sql += dataframe.iloc[row, 1][-1] + " NOT NULL" + dataframe.iloc[row, 2][-1] + ")"
            else:
                pass
        cursor.execute(sql)


if __name__ == "__main__":
    create_tables(conn, df)
    conn.close()
