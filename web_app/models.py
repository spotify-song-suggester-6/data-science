"""This module constructs the classes that SQLAlchemy uses to interact with
the Spotify database.
"""
#pylint: disable=import-error
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Song(db.Model):
    track_id = db.Column(db.String(128), primary_key=True)
    artist_name =  db.Column(db.String(128))
    track_name =  db.Column(db.String(128))
    acousticness = db.Column(db.Float)
    danceability = db.Column(db.Float)
    energy = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    liveness = db.Column(db.Float)
    loudness = db.Column(db.Float)
    speechiness = db.Column(db.Float)
    tempo = db.Column(db.Float)
    valence = db.Column(db.Float)
    duration_ms = db.Column(db.Float)
    key = db.Column(db.Float)
    mode = db.Column(db.Float)
    time_signature = db.Column(db.Float)
    popularity = db.Column(db.Float)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spotify_id = db.Column(db.String(200), unique=False, nullable=True)
    spotify_token = db.Column(db.String(200), unique=False, nullable=True)
