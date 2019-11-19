"""Salty Hacker / JSON Output """
from flask import Flask, jsonify
from models import DB, Troll, Comments
import requests
import json
from pull_data import *


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hackernews.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

DB.init_app(APP)

@APP.route('/')
def root():
    """Base view."""
    return "YES"

# @APP.route('/refresh')
# def refresh():
#     """Pull fresh data replace existing data."""
#     DB.drop_all()
#     DB.create_all()
#     return "Updated!"

@APP.route('/newpull/<int:item>', methods=['GET'])
def newpull(item):
    """ Make request to hacker news API for new data """
    results = pull_data_new(item)
    troll = Troll(
        troll_name=troll_troll_name(results),
        date_created=troll_date_created(results),
        salty_rank=troll_salty_rank(),
        salty_comments=troll_salty_comments(),
        comments_total=troll_comments_total()
    )
    comment = Comments(
        comment_uuid=comment_uuid(results),
        troll_name=comment_troll_name(results),
        is_salty=comment_is_salty(),
        text=comment_text(results),
        date_created=comment_date_created(results)
    )
    DB.session.add(troll)
    DB.session.add(comment)
    DB.session.commit()
    return "Success"


@APP.route('/request/<troll_name>', methods=['GET'])
def request(troll_name):
    troll_query = [Troll.query.filter_by(troll_name=troll_name).first()]
    troll = [troll.serialize_troll() for troll in troll_query]
    comments_query = Comments.query.filter_by(troll_name=troll_name).all()
    comments = [comment.serialize_comments() for comment in comments_query]
    return jsonify([troll, comments])
    # user = Troll.query.filter_by(troll_name=troll_name).first()


