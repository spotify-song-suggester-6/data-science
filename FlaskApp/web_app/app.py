#import os
from flask import Flask, jsonify, request

app = Flask(__name__)

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'
    
    return app


if __name__ == "__main__":
    app.run()