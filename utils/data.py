import json

def get_data(file):
    # Relative route from index.py
    with open(f'./json/{file}.json') as raw:
        return json.load(raw)

def get_items():
    return get_data('items')

def get_item(name):
    items = get_items()
    if name in items:
        return items[name]
    return None

def get_animals():
    return get_data('animals')

def get_animal(name):
    animals = get_animals()
    if name in animals:
        return animals[name]
    return None

def get_terrains():
    return get_data('terrains')

def get_terrain(name):
    terrains = get_terrains()
    if name in terrains:
        return terrains[name]
    return None

def res(path):
    path_list = path.split('.')
    res_type, res_name = path_list[0], path_list[1]
    return get_data('responses')[res_type][res_name]