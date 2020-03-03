import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv
from web_app.models import db, migrate
from web_app.routes.home_routes import home_route


load_dotenv()
user=os.getenv("POSTGRES_USER")
pw=os.getenv("POSTGRES_PW")
url=os.getenv("POSTGRES_URL")
dbname=os.getenv("POSTGRES_DB")
app = Flask(__name__)

def create_app():
    app = Flask(__name__)
    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=user,pw=pw,url=url,db=dbname)

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_route)
    return app


if __name__ == "__main__":
    app.run()
