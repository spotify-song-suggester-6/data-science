# pylint: disable=import-error
from flask import Blueprint
import os

home_route = Blueprint("home_route", __name__)

@home_route.route("/")
def index():
    return "Hello World"
