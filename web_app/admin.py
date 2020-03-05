"""Module to hold administrative functions."""

#pylint: disable=import-error
import csv
import io
import os
import pandas as pd
import psycopg2
import requests
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import event

#TODO: better approach to organizing module-level constants and login info.

def load_environment_variables():
    """This function returns the necessary database login credentials."""
    load_dotenv()
    db_user = os.getenv("POSTGRES_USER")
    db_pw = os.getenv("POSTGRES_PW")
    db_url = os.getenv("POSTGRES_URL")
    db_name = os.getenv("POSTGRES_DB")

    return(db_user, db_pw, db_url, db_name)

#how to pass arguments as a tuple
#TODO: import this function and use it where authentication is used
# throughout the package

def load_from_db():
    """This function loads and minimally processes the Spotify data.

    Returns:
        music_data - a pandas Data Frame

    This app connects to a specified postgresql database of Spotify songs
     through psycopg2. It then reads the data in and converts it to a data
     frame. Finally, it casts all numeric categories as proper types.
    """
    db_user = os.getenv("POSTGRES_USER")
    db_pw = os.getenv("POSTGRES_PW")
    db_url = os.getenv("POSTGRES_URL")
    db_name = os.getenv("POSTGRES_DB")
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=db_user, pw=db_pw, url=db_url, db=db_name)

    connection = psycopg2.connect(
        database=db_name, user=db_user, password=db_pw, host=db_url)
    music_data = pd.read_sql_query('SELECT * FROM song_database;', connection)
    print(music_data.shape)

    #Reformat any variables that may be cast as strings due to database quirks.
    numeric_categories = ["acousticness", "danceability",
                          "energy", "instrumentalness", "liveness", "loudness",
                          "speechiness", "tempo", "valence", "duration_ms", "key",
                          "mode", "time_signature", "popularity"]
    for category in numeric_categories:
        music_data[category] = pd.to_numeric(music_data[category])

    #TODO: add tests that ensure data loaded correctly.

    return music_data

def check_db():
    """Populate postgres database

    This function connects to your desired song database. It checks whether
    any records exist in that database. If they do, it prints the first row
    and returns a text string showing it ran to completion.

    If no records exist, it runs the populate_db() function to insert records
    from the .csv file in this repository and returns the same text string.
    """
    user=os.getenv("POSTGRES_USER")
    pw=os.getenv("POSTGRES_PW")
    url=os.getenv("POSTGRES_URL")
    dbname=os.getenv("POSTGRES_DB")
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=user,pw=pw,url=url,db=dbname)

    # if database_exists(DB_URL):
    connection = psycopg2.connect(database = dbname, user=user, password=pw, host=url)
    cur = connection.cursor()
    cur.execute("SELECT * FROM song_database")
    record = cur.fetchone()

    if record is None:
        populate_db()

    record = cur.fetchone()
    print(record)

    #Q_drop_if_exists = """DROP TABLE IF EXISTS song_database"""
    #Q_create_table = """"""
    if(connection):
        cur.close()
        connection.close()
        print("PostgreSQL connection is closed")

    return("Database has rows.")

def populate_db():
    """This function connects to an empty database and populates it from a csv.

    """
    user=os.getenv("POSTGRES_USER")
    pw=os.getenv("POSTGRES_PW")
    url=os.getenv("POSTGRES_URL")
    dbname=os.getenv("POSTGRES_DB")
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=user,pw=pw,url=url,db=dbname)

    CSV_URL = "rawData/SpotifyAudioFeaturesApril2019.csv"
    df = pd.read_csv(CSV_URL)
    engine = create_engine(DB_URL, executemany_mode='values', executemany_values_page_size=10000, executemany_batch_page_size=500)
    df.head(0).to_sql('song_database', engine, if_exists='replace',index=False) #truncates the table
    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    cur.copy_from(output, 'song_database', null="") # null values become ''
    conn.commit()
    return("success")
