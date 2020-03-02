import os
from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)

    return app