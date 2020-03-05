"""This module contains the routes for the flask app."""
#TODO: create another routes file
# pylint: disable=import-error
from flask import Blueprint, jsonify, request, render_template
import os
from sqlalchemy_utils import database_exists
import psycopg2
from dotenv import load_dotenv
from web_app.plotting import basic_scatter, jsfy
from web_app.admin import check_db, load_environment_variables, load_from_db
load_dotenv()


home_route = Blueprint("home_route", __name__)


@home_route.route("/")
def index():
    return jsonify({
  "id": "1a8b8863-a859-4d68-b63a-c466e554fd13",
  "name": "Ada Lovelace",
  "email": "ada@geemail.com",
  "bio": "First programmer. No big deal.",
  "age": 198,
  "avatar": "http://en.wikipedia.org/wiki/File:Ada_lovelace.jpg"
})

@home_route.route("/plotly")
def get_song_id():
    """Receives text from user using an HTML template. Must receive valid song id."""

    return render_template('test_form.html')

@home_route.route('/plotly', methods=['POST'])
def plot_to_json():
    music_data = load_from_db()
    song_name = request.form["text"]
    return jsfy(music_data, song_name)

@home_route.route("/test_db")
def check_for_db():
    user=os.getenv("POSTGRES_USER")
    pw=os.getenv("POSTGRES_PW")
    url=os.getenv("POSTGRES_URL")
    dbname=os.getenv("POSTGRES_DB")
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=user,pw=pw,url=url,db=dbname)
    # if database_exists(DB_URL):
    connection = psycopg2.connect(database = dbname, user=user, password=pw, host=url)
    cur=connection.cursor()
    print (connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cur.execute("SELECT version();")
    record = cur.fetchone()
    print("You are connected to - ", record,"\n")
    if(connection):
        cur.close()
        connection.close()
        print("PostgreSQL connection is closed")
    return("fortyseven")

@home_route.route("/plot")
def run_scatter():
    music_data = load_from_db()
    print(music_data.head())
    scatter = basic_scatter(music_data)
    return "Beautiful Plot"

@home_route.route("/data_exists")
def db_check():
    check_db()
    return("Squery executed successfuly")

# return APP.response_class(
#            response= json.dumps( export),
#            status= 200,
#            mimetype= 'application/json'
# )

@home_route.route('/test_predict')
def test_form():
    return render_template('test_form.html')

@home_route.route('/test_predict', methods=['POST'])
def test_form_post():
     test_text = request.form["text"]
     return jsonify({'prediction': test_text})
