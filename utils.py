#test utils

import requests
import json
import random

# def troll_info():
#     user = requests.get('https://hacker-news.firebaseio.com/v0/user/amichail.json')
#     user_stats = user.json()
#     print(user_stats)

def item_lookup(ItemId):
    item_stats_list = []
    item = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{ItemId}.json')
    item_stats = item.json()
    item_stats_list.append((item_stats["id"],(item_stats["by"],
    item_stats["time"], round(random.uniform(0,100), 2), item_stats["text"],random.randint(1,1001))))
    print(item_stats_list)
    return item_stats_list

if __name__ == "__main__":
    # troll_info()
    item_lookup(1408)