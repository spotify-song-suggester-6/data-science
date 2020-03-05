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


def basic_scatter(df):
    """A basic scatter plot. Flask functionality not yet added."""
    plot = px.scatter(df.iloc[:100], x='loudness',
                      y='energy', trendline='ols')
    return "We need to convert this plot into something"


def jsfy(df, songID):
    """Takes a data frame and song ID and outputs a Plotly graph converted to JSON"""
    features = [
        'acousticness',
        'danceability',
        'energy',
        'instrumentalness',
        'liveness',
        'speechiness']

    find_id = df['track_id'] == songID
    song_stats = df[find_id][features]
    print(song_stats)

    start = """{"data": [{"x":"""
    xs = list(song_stats.columns)
    middle = """, "y": """
    ys = list(song_stats.values[0])
    end = """, "type": "bar"}]}"""
    json = start + str(xs) + middle + str(ys) + end

    return json
