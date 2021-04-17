# This script sets up the SQLite database structure for Cloudy With a Chance of Football
# The full description of the database schema can be seen in Deliverable 2

# Import sqlite3 to set up the database and pandas to assist with bringing tables and columns into the database
import sqlite3
import pandas as pd

# Create a list of all table names
table_names = ['players',
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
'performance']

# Create a list of lists for all column names for each table
column_names = [['player_id','unique_id','player_name'],
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
['player_id','week_id','predicted','actual','performance']]

# Create a list of lists for all data types and instructions for each table
column_data_types_and_instructions = [['INTEGER PRIMARY KEY AUTOINCREMENT','TEXT NOT NULL','TEXT NOT NULL'],
['INTEGER NOT NULL','TEXT NOT NULL'],
['INTEGER NOT NULL','TEXT NOT NULL'],
['INTEGER NOT NULL','TEXT NOT NULL','INTEGER NOT NULL'],
['INTEGER NOT NULL','TEXT NOT NULL','REAL NOT NULL'],
['INTEGER NOT NULL','TEXT NOT NULL','TEXT NOT NULL'],
['TEXT NOT NULL','TEXT NOT NULL','INTEGER NOT NULL'],
['TEXT NOT NULL','TEXT NOT NULL','INTEGER NOT NULL'],
['TEXT NOT NULL','TEXT NOT NULL','REAL NOT NULL','REAL NOT NULL','REAL NOT NULL'],
['TEXT NOT NULL','TEXT NOT NULL','TEXT NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL','INTEGER NOT NULL'],
['INTEGER NOT NULL','INTEGER NOT NULL','TEXT NOT NULL','TEXT NOT NULL'],
['TEXT NOT NULL','TEXT NOT NULL','INTEGER NOT NULL'],
['TEXT NOT NULL','TEXT NOT NULL','INTEGER NOT NULL'],
['INTEGER NOT NULL','TEXT NOT NULL','REAL NOT NULL','REAL NOT NULL','INTEGER NOT NULL']]

# Read in the 3 lists above into a pandas dataframe
df = pd.DataFrame(list(
    zip(table_names, column_names, column_data_types_and_instructions)),
    columns = ['table_names','column_names','data_types_and instructions'])

# Establish the path to and open a connection to the database
DBPATH = 'cloud_with_a_chance_of_football.db'
conn = sqlite3.connect(DBPATH)

def create_tables(conn, dataframe): #bring this title for the function back when ready to add tables to database
#def create_tables(dataframe):
    """
    Purpose: Translate a dataframe containing database table and column information into a database
    Input Type: Dataframe with 3 columns (table name, column names, column data types and instructions)
    """
    cursor = conn.cursor() # Add the cursor back in once ready to add tables to databas
    for row in range(len(dataframe)):
        sql = "CREATE TABLE IF NOT EXISTS " + dataframe.iloc[row,0]+" ("
        for n in range(len(dataframe)):
            if n < len(dataframe.iloc[row,1]):
                sql += dataframe.iloc[row, 1][n] + " " + dataframe.iloc[row, 2][n] + ", "
            elif n == len(dataframe.iloc[row,1]):
                sql += dataframe.iloc[row, 1][-1] + " " + dataframe.iloc[row, 2][-1] + ")"
        cursor.execute(sql)

create_tables(conn, df)


def connect(path="people.db", syncdb=False):
    """
    Connects to the database and ensures there are tables.
    """
    
    if not os.path.exists(path):
        syncdb=True

    conn = sqlite3.connect(path)
    if syncdb:
        create_tables(conn)
    
    return conn


def insert(name, email, company, conn=None):
    if not conn: conn = connect()

    try: 
        cursor.execute("SELECT id FROM companies WHERE name=?", (company,))
        x = cursor.fetchone()
        company_id = x[0]
 
    except TypeError:
        create_tables(conn)
        sql = "INSERT INTO companies (name) VALUES (?)"
        cursor.execute(sql, (company,))
        conn.commit()
        cursor.execute("SELECT id FROM companies WHERE name=?", (company,))
        x = cursor.fetchone()
        company_id = x[0]
        
    sql = "INSERT INTO contacts (name, email, company_id) VALUES (?,?,?)"
    cursor.execute(sql, (name, email, company_id))
    conn.commit() 

if __name__ == "__main__":
    name    = input("Enter name: ")
    email   = input("Enter email: ")
    company = input("Enter company: ")
    
    conn = connect()
    insert(name, email, company, conn)
    
    company_id = cursor.execute("SELECT id FROM companies WHERE name=?", (company,)).fetchone()[0]
    contacts = len(cursor.execute("SELECT id FROM contacts WHERE company_id=?", (company_id,)).fetchall())
    print("The {0} now has {1} contacts.".format(company, contacts))

    conn.close()