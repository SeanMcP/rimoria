import json

def get_items():
    # Relative route from index.py
    with open('./json/items.json') as raw:
        return json.load(raw)

def get_item(name):
    return get_items()[name]