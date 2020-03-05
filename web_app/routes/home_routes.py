"""This module contains administrative and test routes for the app."""
# pylint: disable=import-error
import os
import psycopg2
from dotenv import load_dotenv
from flask import Blueprint, jsonify, request, render_template
from sqlalchemy_utils import database_exists
from web_app.plotting import basic_scatter, jsfy
from web_app.admin import check_db, load_environment_variables, load_from_db

load_dotenv()


home_route = Blueprint("home_route", __name__)


@home_route.route("/")
def index():
    """Base route: returns JSON for API/interface testing."""
    return jsonify({
  "id": "1a8b8863-a859-4d68-b63a-c466e554fd13",
  "name": "Ada Lovelace",
  "email": "ada@geemail.com",
  "bio": "First programmer. No big deal.",
  "age": 198,
  "avatar": "http://en.wikipedia.org/wiki/File:Ada_lovelace.jpg"
})


@home_route.route("/test_db")
def check_for_db():
    """Creates a route that runs successfully if app is connected to database."""
    db_user, db_pw, db_url, db_name = load_environment_variables()
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
        user=db_user, pw=db_pw, url=db_url, db=db_name)

    # if database_exists(DB_URL):
    connection = psycopg2.connect(
        database=db_name, user=db_user, password=db_pw, host=db_url)
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

    return("You have successfully connected to PostgreSQL.")


@home_route.route("/data_exists")
def db_check():
    """Checks for an empty database; populates data if empty.

    This route first checks if a specified database is empty. If it is not,
    it populates it from a csv within the repository. Based on the `check_db`
    function in `admin.py`.
    """
    check_db()
    return("Query executed successfully. Data should be present.")


@home_route.route('/test_predict')
def test_form():
    """The /test_predict methods are basic tests of the app receiving input."""
    return render_template('test_form.html')


@home_route.route('/test_predict', methods=['POST'])
def test_form_post():
     test_text = request.form["text"]
     return jsonify({'prediction': test_text})


@home_route.route("/plot")
def run_scatter():
    music_data = load_from_db()
    print(music_data.head())
    scatter = basic_scatter(music_data)
    return "Beautiful Plot"
