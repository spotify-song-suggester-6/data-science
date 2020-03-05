"""This module contains the routes that analyze the data"""
# pylint: disable=import-error
import os
import psycopg2
from flask import Blueprint, jsonify, request, render_template
from sqlalchemy_utils import database_exists
from dotenv import load_dotenv
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
    pass

@data_route.route('/model', methods=['POST'])
def model_data(song):
    # use song input to grab features
    # convert features to 2d array
    # drop unnecessary columns
    # run model
    # return jsonified output
    pass
