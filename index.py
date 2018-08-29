import random
from classes.AnimalClass import Animal
from classes.ExplorerClass import Explorer
from classes.TerrainClass import Terrain
from utils.data import get_item, get_items, res
from utils.print import gameover_results, new_line, new_line_input, print_map

animals = { '0,0': None }
location = ['0,0']
mode = 'explore'
world_map = { '0,0': Terrain() }

def navigate(direction):
    global animals, location, mode, world_map
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
        world_map[new_coordinates] = Terrain(world_map[location[0]].type)
        # roll = 1
        roll = random.randint(1, 10)
        if roll == 1:
            animals[new_coordinates] = Animal(world_map[new_coordinates].type)

    location.insert(0, new_coordinates)
    location = location[:10]

    if new_coordinates in animals and animals[new_coordinates]:
        mode = 'encounter'
        new_line(f'You encounter a wild {animals[new_coordinates].type}!')
    else:
        print_navigate()

    player.tire(world_map[new_coordinates].difficulty)
    
def action_forage(player):
    square = world_map[location[0]]

    requirement = square.requirement
    if requirement and requirement not in player.inventory:
        return new_line(f'You need one {requirement} to forage here.')
    
    product = square.produce()
    if product is not None:
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
        options = {
            'encounter': encounter,
            'explore': explore
        }
        options[mode]()
    gameover_results(player, world_map)

def encounter():
    action_input = new_line_input('What do you want to do: look, run, feed, or attack?').lower()
    action_list = action_input.split(' ')
    action = action_list[0]
    # extra = action_list[1] if len(action_list) > 1 else None
    if action == 'run':
        action_run()
    elif action == 'look':
        animal = animals[location[0]]
        new_line(f'{animal.description} It looks {"angry!" if animal.is_angry else "calm."}')
    elif action == 'feed':
        action_feed()
    elif action == 'attack':
        action_attack()
    else:
        new_line(res('fail.unknown'))

def action_attack():
    global animals, mode
    animal = animals[location[0]]
    player_roll = random.randint(1, 20)
    animal_roll = random.randint(1, 20)
    if player_roll + player.strength > animal_roll + animal.speed:
        animal.damage(player.strength)
        if not animal.is_alive:
            mode = 'explore'
            animals[location[0]] = None
            return player.collect(animal.resource, animal.speed)
    else:
        new_line('You miss!')
    animal_decide()

def animal_decide():
    global mode
    animal = animals[location[0]]
    roll = random.randint(1, 5)
    if roll > 1:
        damage = animal.attack()
        if damage:
            player.heal(-damage)
    else:
        run = animal.run()
        if run:
            new_line(f'The {animal.type} ran away.')
            animals[location[0]] = None
            mode = 'explore'

def action_run():
    global mode
    animal = animals[location[0]]
    player_roll = random.randint(1, 20) + player.strength
    animal_roll = random.randint(1, 20) + animal.speed
    if animal.is_angry and player_roll < animal_roll:
        new_line(res('fail.run'))
        player.tire()
        animal_decide()
    else:
        new_line(res('success.run'))
        directions = ['n', 'e', 's', 'w']
        mode = 'explore'
        action_navigate(directions[random.randint(0, len(directions) - 1)])

def action_feed():
    global mode
    options = list(player.inventory)
    animal = animals[location[0]]

    if len(options) < 1:
        return new_line('You have nothing to feed animal.')

    options_string = ', '.join(options) + ', or nothing'
    selection = new_line_input(f'What would you like to feed the animal: {options_string}?')

    if selection in options:
        player.lose(selection)
        new_line(f'You try feeding it one {selection}.')
        animal_leaves = animal.feed(selection)
        if animal_leaves:
            if not animal.is_alive:
                player.collect(animal.resource)
            mode = 'explore'
            animals[location[0]] = None
    elif selection == 'nothing':
        return new_line('Best to save your food for later.')
    else:
        return new_line(res('fail.unknown'))

def explore():
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
        return print_map(location[0], world_map, animals)
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
    elif selection == 'nothing':
        return new_line('Best to keep moving.')
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
    else:
        new_line(res('fail.assemble'))
    player.tire()

status_check()