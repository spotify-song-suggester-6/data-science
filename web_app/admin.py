"""Module to hold administrative functions."""
#pylint: disable=import-error
import os
from dotenv import load_dotenv


def load_environment_variables():
    load_dotenv()
    db_user = os.getenv("POSTGRES_USER")
    db_pw = os.getenv("POSTGRES_PW")
    db_url = os.getenv("POSTGRES_URL")
    db_name = os.getenv("POSTGRES_DB")

    return(db_user, db_pw, db_url, db_name)
