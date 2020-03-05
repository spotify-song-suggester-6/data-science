"""This module contains the routes that analyze the data"""
# pylint: disable=import-error
import os
import psycopg2
import pandas as pd
from flask import Blueprint, jsonify, request, render_template
from sqlalchemy_utils import database_exists
from dotenv import load_dotenv
from web_app.load_model import kayDeeSuggestsThis, FILENAME
from web_app.plotting import basic_scatter, jsfy
from web_app.admin import check_db, load_environment_variables, load_from_db


load_dotenv()
data_route = Blueprint("data_route", __name__)


@data_route.route("/plotly")
def get_song_id():
    return render_template('test_form.html')

@data_route.route('/plotly', methods=['POST'])
def plot_to_json():
    music_data = load_from_db()
    song_name = request.form["text"]
    return jsfy(music_data, song_name)

@data_route.route('/model')
def get_data():
    return render_template('test_form.html')

@data_route.route('/model', methods=['POST'])
def model_data():
    song_name = request.form['text']
    music_data = load_from_db()
    features = music_data.columns.drop(["id", "track_id", "track_name",
        "artist_name", "duration_ms"])
    find_id = music_data['track_name'] == song_name
    song_stats = music_data[find_id][features]
    print(song_stats.shape)
    print(song_stats)
#    song_array = np.array(song_stats)
    rec_songs = kayDeeSuggestsThis(FILENAME, song_stats, music_data)
    songs_json = rec_songs.to_json()
    return songs_json
