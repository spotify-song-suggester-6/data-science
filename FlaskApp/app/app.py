import os
from flask import Flask, jsonify, request

#from app.routes.home_routes import home_routes


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'