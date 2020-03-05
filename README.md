# Data Science with Spotify

## App Description

This app loads Spotify song data into an external PostgreSQL database, then queries that data to generate graphs and predict the 10 most similar songs based on user input.

It is a Flask app that is deployed via Heroku. It is formatted to output JSON data to its Heroku endpoints for further web processing.

## Running Flask App

Begin by cloning this repository to your desktop. You must then have a valid PostgreSQL database to connect to -- create a .env file that contains data in the following format, filled in with your database's specific information.

```
POSTGRES_USER=
POSTGRES_PW=
POSTGRES_URL=
POSTGRES_DB=
```

Then run the Flask app with:
```
set FLASK_APP=web_app
flask run
```

## Interacting with Database

Flask should deploy to your local IP address; all of the following specified routes are relative to that file path.

From the home_routes folder, "/test_db" will test your connection to the database. "/data_exists" will check to see if the database has any elements in it; if not, it will populate the database with the raw data from the Spotify .csv included in the repository.

Other routes in the home_routes folder are test elements to ensure, among other things, that the app can take in and respond to data.

## Generating Predictions

The data_routes folder contains routes that interact with the database to generate predictions based on user input.

The "/plotly" route takes in a valid song ID and outputs a Plotly graph, formatted in JSON per the Plotly API schema.

The "/model" route takes in a valid song name and outputs a JSON object containing the name and features of the 10 most similar songs in the database.

## Notes

This app is deployed to Heroku with the base html <http://spotify-ds-app.herokuapp.com/>. This app is currently set up to interact with external web development resources; changes to output format are recommended if deployed as a stand-alone app.
