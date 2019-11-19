""" functions for pulling data from api """


import requests
import json
import random


def pull_data_new(item):
    """ default function for calling for new data """
    api_call = f"https://hacker-news.firebaseio.com/v0/item/{item}.json"
    result = requests.get(api_call).json()
    return result


def troll_troll_name(results):
    """ retrieve troll name from item """
    name = results['by']
    return name


def troll_date_created(results):
    """ get unix time posted """
    time = results['time']
    return time


def troll_salty_rank():
    """ create a random number to use for the "salty_rank" """
    return round(random.uniform(0, 10), 2)


def troll_salty_comments():
    """ Generate a number of total salty comments """
    return random.randint(100, 500)


def troll_comments_total():
    """ Generate a number of total comments """
    return random.randint(100, 1000)


def comment_uuid(results):
    """ get comment unique id """
    comment_id = results['id']
    return comment_id


def comment_troll_name(results):
    """ The same as troll_name """
    name = results['by']
    return name


def comment_is_salty():
    """ Randomize if comment is salty """
    value = random.randint(0, 1)
    return value


def comment_text(results):
    """ get comment text """
    text = results['text']
    return text


def comment_date_created(results):
    """ get date comement was made in unix time """
    datetime = results['time']
    return datetime


# this_varaible = (
#     f"this thing {x}" \
#     f"another one {y}"
# )
