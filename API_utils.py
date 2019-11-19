import requests
import json

# def troll_info():
#     user = requests.get('https://hacker-news.firebaseio.com/v0/user/amichail.json')
#     user_stats = user.json()
#     print(user_stats)

def item_lookup(ItemId):
    item = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{ItemId}.json')
    item_stats = item.json()
    print(item_stats)

if __name__ == "__main__":
    # troll_info()
    item_lookup(1408)