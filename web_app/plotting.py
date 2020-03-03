#pylint: disable=import-error
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def load_from_db():
    user=os.getenv("POSTGRES_USER")
    pw=os.getenv("POSTGRES_PW")
    url=os.getenv("POSTGRES_URL")
    dbname=os.getenv("POSTGRES_DB")
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=user,pw=pw,url=url,db=dbname)
    # if database_exists(DB_URL):
    connection = psycopg2.connect(database = dbname, user=user, password=pw, host=url)
#    cur=connection.cursor()
    music_data = pd.read_sql_query('SELECT * FROM song_database;', connection)
    music_data = music_data.iloc[1:]
    numeric_categories = ["acousticness", "danceability",
        "energy", "instrumentalness", "liveness", "loudness",
        "speechiness", "tempo", "valence", "duration_ms", "key",
        "mode", "time_signature", "popularity"]
    for category in numeric_categories:
        music_data[category] = pd.to_numeric(music_data[category])
        print(music_data.dtypes)
        print(music_data.shape)
    return music_data

def basic_scatter(df):
    plot = px.scatter(df.iloc[:100], x='loudness', y='energy') #, trendline='ols')
    # Something about OLS is causing a typeerror between numpy and plotly.
    print(type(plot))
    return "We need to convert this plot into something"
# graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
