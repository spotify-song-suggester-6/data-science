"""Module to hold administrative functions."""

#pylint: disable=import-error
import csv
import os
import pandas as pd
from dotenv import load_dotenv
import psycopg2
import requests
from sqlalchemy import create_engine
from sqlalchemy import event
import io

def load_environment_variables():
    load_dotenv()
    db_user = os.getenv("POSTGRES_USER")
    db_pw = os.getenv("POSTGRES_PW")
    db_url = os.getenv("POSTGRES_URL")
    db_name = os.getenv("POSTGRES_DB")


    return(db_user, db_pw, db_url, db_name)

#how to pass arguments as a tuple
#TODO: import this function and use it where authentication is used
# throughout the package

def check_db():
    """Check if there are songs in Postgres DB"""
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
    return("query executed successfully")

def populate_db():
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
