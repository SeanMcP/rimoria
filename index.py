import random
from classes.ExplorerClass import Explorer
from classes.MapSquareClass import MapSquare
from utils.data import get_item, get_items, res
from utils.print import new_line, new_line_input, print_map

world_map = { '0,0': MapSquare() }
location = ['0,0']

def navigate(direction):
    global location, world_map
    current_location = location[0].split(',')
    x, y = int(current_location[0]), int(current_location[1])

    def print_navigate():
        new_line(f'You head {direction if len(direction) > 1 else direction.upper()} and find a {world_map[location[0]].type}.')

    if direction in ['back', 'b']:
        if len(location) > 1:
            location = location[1:]
            player.tire()
            return print_navigate()
        else:
            return new_line('You cannot go back')
    elif direction in ['north', 'n']:
        new_coordinates = f'{x},{y + 1}'
    elif direction in ['south', 's']:
        new_coordinates = f'{x},{y - 1}'
    elif direction in ['east', 'e']:
        new_coordinates = f'{x + 1},{y}'
    elif direction in ['west', 'w']:
        new_coordinates = f'{x - 1},{y}'

    if new_coordinates not in world_map:
        world_map[new_coordinates] = MapSquare(world_map[location[0]].type)

    location.insert(0, new_coordinates)
    location = location[:10]
    print_navigate()

    player.tire()
    
def action_forage(player):
    square = world_map[location[0]]

    requirement = square.requirement
    if requirement and requirement not in player.inventory:
        return new_line(f'You need one {requirement} to forage here.')
    
    product = square.produce()
    if product is not None:
        new_line(f'You find one {product}.')
        if requirement:
            player.lose(requirement)
        player.collect(product, square.difficulty)
    else:
        new_line('You find nothing.')

    player.tire(square.difficulty)

player_name = new_line_input('What is your name, explorer?')
player = Explorer(player_name)
new_line(f'Welcome, {player.name}, to the land of Rimoria!')

def status_check():
    global player
    while player.status != 'dead':
        play()
    new_line('Game over')

def play():
    action_input = new_line_input('What do you want to do: look, navigate, forage, check, eat, inspect, or assemble?').lower()
    action_list = action_input.split(' ')
    action = action_list[0]
    extra = action_list[1] if len(action_list) > 1 else None
    if action in ['navigate', 'go']:
        action_navigate(extra)
    elif action == 'forage':
        action_forage(player)
    elif action == 'look':
        action_look()
    elif action == 'check':
        action_check(extra)
    elif action == 'eat':
        action_eat()
    elif action == 'inspect':
        action_inspect()
    elif action == 'assemble':
        action_assemble()
    else:
        new_line(res('fail.unknown'))

def action_assemble():
    if len(player.inventory) < 1:
        return new_line('You don\'t have anything to assemble.')

    new_line(f'''Inventory: {player.inventory}
''')
    options = list(player.inventory)

    component_1 = str(input('Component 1: >> ')).lower()
    if component_1 not in options:
        return new_line(res('fail.unknown'))

    component_2 = str(input('Component 2: >> ')).lower()
    if component_2 not in options:
        return new_line(res('fail.unknown'))

    if component_1 == component_2:
        if player.inventory[component_1] < 2:
            return new_line(f'You don\'t have enough {component_1}.')

    return assemble([component_1, component_2])

def lose_components(components):
    for component in components:
        player.lose(component)

def action_check(check):
    if not check:
        check = new_line_input('What do you want to check: location, map, inventory, or status?').lower()
    if check == 'inventory':
        return new_line(f'Inventory: {player.inventory}' if len(player.inventory) > 0 else 'You have nothing in your inventory.')
    elif check == 'location':
        return new_line(f'You are standing in a {world_map[location[0]].type} at {location[0]}.')
    elif check == 'status':
        return player.checkup()
    elif check == 'map':
        return print_map(location[0], world_map)
    else:
        print(res('fail.unknown'))

def action_eat():
    options = list(player.inventory)

    if len(options) < 1:
        return new_line('You have nothing to eat.')

    options_string = f'{", ".join(options)}, or nothing'
    food = new_line_input(f'What would you like to eat: {options_string}?')

    if food == 'nothing':
        return new_line('Best to save your food for later.')

    item = get_item(food)
    if not item:
        return new_line(res('fail.unknown'))
    
    energy = item['energy']
    if not energy:
        return new_line(res('fail.eat'))
    if energy >= 20:
        new_line('Mmmm; looks good!')
    elif energy > 0:
        new_line('Something is better than nothing.')
    elif energy < 0:
        new_line('You may regret this.')
    else:
        return print(res('fail.unknown'))
    player.lose(food)
    player.heal(energy)

def action_inspect():
    options = list(player.inventory)

    if len(options) < 1:
        return new_line('You have nothing to inspect.')

    options_string = ', '.join(options) + ', or nothing'
    selection = new_line_input(f'What would you like to inspect: {options_string}?')

    if selection in options:
        return new_line(get_item(selection)['description'])
    else:
        return new_line(res('fail.unknown'))

def action_look():
    new_line(world_map[location[0]].description)

def action_navigate(direction):
    options = ('north', 'n', 'east', 'e', 'south', 's', 'west', 'w', 'back', 'b')
    if not direction:
        direction = new_line_input('Which direction: north, east, south, west, or back?').lower()
    if direction not in options:
        print(res('fail.unknown'))
    else:
        navigate(direction)

def assemble(components):
    components.sort()
    key_string = '+'.join(components)
    items = get_items()
    product = None
    for item in items:
        if items[item]['source'] == key_string:
            product = item
    if product:
        lose_components(components)
        player.collect(product, items[product]['experience'])
        new_line(f'You have assembled one {product}!')
    else:
        new_line(res('fail.assemble'))
    player.tire()

status_check()