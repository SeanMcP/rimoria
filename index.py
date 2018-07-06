import random
from classes.ExplorerClass import Explorer
from classes.MapSquareClass import MapSquare
from utils.print import new_line

world_map = { '0,0': MapSquare() }
location = ['0,0']
RES = {
    'FAIL': {
        'ASSEMBLE': 'You cannot assemble those items.'
    },
    'UNKNOWN': 'I do not understand.'
}

def print_location():
    print(location[0], world_map[location[0]].type)

def navigate(direction):
    global location, world_map
    current_location = location[0].split(',')
    x, y = int(current_location[0]), int(current_location[1])

    def print_navigate():
        new_line(f'You head {direction} and find a {world_map[location[0]].type}.')

    if direction == 'back':
        if len(location) > 1:
            location = location[1:]
            player.tire()
            return print_navigate()
        else:
            return new_line('You cannot go back')
    elif direction == 'north':
        new_coordinates = f'{x},{y + 1}'
    elif direction == 'south':
        new_coordinates = f'{x},{y - 1}'
    elif direction == 'east':
        new_coordinates = f'{x + 1},{y}'
    elif direction == 'west':
        new_coordinates = f'{x - 1},{y}'

    if new_coordinates not in world_map:
        world_map[new_coordinates] = MapSquare(world_map[location[0]].type)

    location.insert(0, new_coordinates)
    location = location[:10]
    print_navigate()

    player.tire()
    
def forage(player):
    square = world_map[location[0]]
    multiplier = 1

    if square.type is 'cave' and 'hammers' not in player.inventory:
        return new_line('You need a hammer to forage here.')
    if square.type is 'lake' and 'worms' not in player.inventory:
        return new_line('You need a worm to forage here.')
    
    product = square.produce()
    if product is not None:
        new_line(f'You find one {product}.')
        if square.type == 'cave':
            player.lose('hammers')
        if square.type == 'lake':
            player.lose('worms')
        player.collect(product, multiplier)
    else:
        new_line('You find nothing.')
    if square.type is 'cave' or square.type is 'mountain' or square.type is 'lake':
        player.tire(2)
        multiplier = 2
    else:
        player.tire()

def print_logo():
    print('''                                                                            
    ***** ***                                                               
******  * **  *                                            *               
**   *  *  ** ***                                          ***              
*    *  *   **  *                                            *               
    *  *    *                          ****   ***  ****                      
** **   *  ***   *** **** ****     * ***  * **** **** * ***       ****    
** **  *    ***   *** **** ***  * *   ****   **   ****   ***     * ***  * 
** ****      **    **  **** **** **    **    **           **    *   ****  
** **  ***   **    **   **   **  **    **    **           **   **    **   
** **    **  **    **   **   **  **    **    **           **   **    **   
*  **    **  **    **   **   **  **    **    **           **   **    **   
    *     **  **    **   **   **  **    **    **           **   **    **   
****      *** **    **   **   **   ******     ***          **   **    **   
*  ****    **  *** * ***  ***  ***   ****       ***         *** * ***** **  
*    **     *    ***   ***  ***  ***                          ***   ***   ** 
*                                                                            
**                 A text-based adventure game in Python                 
''')

player_name = str(input('''
What is your name, explorer?
>> '''))
player = Explorer(player_name)
new_line(f'Welcome, {player.name}, to the land of Rimoria!')

# player = Explorer()

def status_check():
    global player
    while player.status != 'dead':
        print(' ')
        play()
    print('Game over')

def play():
    action_input = str(input('''What do you want to do: look, navigate, forage, check, eat, or assemble?
>> ''')).lower()
    action_list = action_input.split(' ')
    action = action_list[0]
    extra = action_list[1] if len(action_list) > 1 else None
    if action == 'navigate':
        action_navigate(extra)
    elif action == 'forage':
        forage(player)
    elif action == 'look':
        action_look()
    elif action == 'check':
        action_check(extra)
    elif action == 'eat':
        action_eat()
    elif action == 'assemble':
        action_assemble()
    else:
        new_line(RES['UNKNOWN'])

def action_assemble():
    if len(player.inventory) < 1:
        return new_line('You don\'t have anything to assemble.')
    new_line(f'''Inventory: {player.inventory}
''')
    options = list(player.inventory)
    component_1 = str(input('Component 1: >> ')).lower()
    if component_1 not in options:
        return new_line(RES['UNKNOWN'])
    component_2 = str(input('Component 2: >> ')).lower()
    if component_2 not in options:
        return new_line(RES['UNKNOWN'])
    components = [ component_1, component_2 ]
    if component_1 == component_2:
        if player.inventory[component_1] < 2:
            return new_line(f'You don\'t have enough {component_1}.')
    if 'wood' in components and 'rocks' in components:
        lose_components(components)
        player.collect('hammers', 2)
        new_line('You have assembled 1 hammer!')
    elif 'wood' in components and component_1 == component_2:
        lose_components(components)
        player.collect('fire', 2)
        new_line('You have assembled 1 fire!')
    elif 'wood' in components and 'worms' in components:
        lose_components(components)
        player.collect('wormwood', 1)
        new_line('You have assembled 1 wormwood!')
    elif 'wood' in components and 'fish' in components:
        lose_components(components)
        player.collect('fishsticks', 1)
        new_line('You have assembled 1 fishstick!')
    else:
        return new_line(RES['FAIL']['ASSEMBLE'])

def lose_components(components):
    for component in components:
        player.lose(component)

def action_check(check):
    if not check:
        check = str(input('''
What do you want to check: location, inventory, or status?
>> ''')).lower()
    if check == 'inventory':
        return new_line(f'Inventory: {player.inventory}' if len(player.inventory) > 0 else 'You have nothing in your inventory.')
    elif check == 'location':
        return new_line(f'You are standing in a {world_map[location[0]].type} at {location[0]}.')
    elif check == 'status':
        return player.checkup()
    else:
        print(RES['UNKNOWN'])

def action_eat():
    options = list(player.inventory)
    if len(options) < 1:
        return new_line('You have nothing to eat.')
    options_string = ', '.join(options) + ', or nothing'
    food = str(input(f'''
What would you like to eat: {options_string}?
>> '''))
    if food in options:
        player.lose(food)
    if food == 'worms':
        new_line('It\'s better than nothing.')
        player.heal(1)
    elif food == 'fish':
        new_line('Mmmm; looks good!')
        player.heal(25)
    elif food in options:
        new_line('You may regret this.')
        player.heal(-10)
    elif food == 'nothing':
        new_line('Best to save your food for later.')
    else:
        return print(RES['UNKNOWN'])

def action_look():
    new_line(f'{world_map[location[0]].square_description}')

def action_navigate(direction):
    options = ('north', 'east', 'south', 'west', 'back')
    if not direction:
        direction = str(input('''
Which direction: north, east, south, west, or back?
>> ''')).lower()
    if direction not in options:
        print(RES['UNKNOWN'])
    else:
        navigate(direction)

status_check()