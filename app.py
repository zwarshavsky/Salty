"""Salty Hacker / JSON Output """
from flask import Flask, jsonify
from models import DB, troll, comments


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackernews.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

DB.init_app(APP)

@APP.route('/')
def root():
    """Base view."""
    return "YES"

@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    return "Updated!"

