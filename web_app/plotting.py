"""This module hosts functions used in home_routes.py"""
# pylint: disable=import-error
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


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

    # if database_exists(DB_URL):
    connection = psycopg2.connect(
        database=db_name, user=db_user, password=db_pw, host=db_url)
    music_data = pd.read_sql_query('SELECT * FROM song_database;', connection)
    print(music_data.shape)

    numeric_categories = ["acousticness", "danceability",
                          "energy", "instrumentalness", "liveness", "loudness",
                          "speechiness", "tempo", "valence", "duration_ms", "key",
                          "mode", "time_signature", "popularity"]
    for category in numeric_categories:
        music_data[category] = pd.to_numeric(music_data[category])

    # print(music_data.dtypes)
    # print(music_data.shape)
    #TODO add tests (assert?) to verify this is working.
    return music_data


def basic_scatter(df):
    plot = px.scatter(df.iloc[:100], x='loudness',
                      y='energy', trendline='ols')

    return "We need to convert this plot into something"
#
