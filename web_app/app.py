# pylint: disable=import-error
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from web_app.models import db, migrate
from web_app.routes.home_routes import home_route


load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_pw = os.getenv("POSTGRES_PW")
db_url = os.getenv("POSTGRES_URL")
db_name = os.getenv("POSTGRES_DB")

app = Flask(__name__)


def create_app():
    """This function creates a Flask app to interact with Spotify data.

    Returns:
        Flask app - returns an object of class Flask from the flask module.


    This function uses psycopg2 to connect to a postgresql database containing
    data from Spotify about the auditory properties of their songs. To use,
    a user must have the appropriate database password and details properly
    configured within their Flask environment.
    """
    app = Flask(__name__)

    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{dbname}'.format(
        user=db_user, pw=db_pw, url=db_url, dbname=db_name)

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    # silence the deprecation warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_route)
    return app


if __name__ == "__main__":
    app.run()
