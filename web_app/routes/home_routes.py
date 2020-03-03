# pylint: disable=import-error
from flask import Blueprint
import os
from sqlalchemy_utils import database_exists
import psycopg2
from dotenv import load_dotenv

load_dotenv()

home_route = Blueprint("home_route", __name__)

@home_route.route("/")
def index():
    return "Hello World"

@home_route.route("/test_db")
def check_for_db():
    user=os.getenv("POSTGRES_USER")
    pw=os.getenv("POSTGRES_PW")
    url=os.getenv("POSTGRES_URL")
    dbname=os.getenv("POSTGRES_DB")
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=user,pw=pw,url=url,db=dbname)
    # if database_exists(DB_URL):
    con = psycopg2.connect(database = dbname, user=user, password=pw, host=url)
    cur=con.cursor()
    print(cur)
    print("You've connected ot the database!")
    cur.close()
    return("You've connected to the database!")

#export = suggestSong(parseInput())

# return APP.response_class(
#            response= json.dumps( export),
#            status= 200,
#            mimetype= 'application/json'
# )

# export = suggestSong(parseInput())
