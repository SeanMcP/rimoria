import json

def get_data(file):
    # Relative route from index.py
    with open(f'./json/{file}.json') as raw:
        return json.load(raw)

def get_items():
    return get_data('items')

def get_item(name):
    return get_items()[name]

def res(path):
    path_list = path.split('.')
    res_type, res_name = path_list[0], path_list[1]
    return get_data('responses')[res_type][res_name]