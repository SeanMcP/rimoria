import random
from classes.ExplorerClass import Explorer
from classes.MapSquareClass import MapSquare

world_map = { '0,0': MapSquare() }
location = ['0,0']
RES = {
    'UNKNOWN': 'I do not understand'
}

def print_location():
        print(location[0], world_map[location[0]].type)

def navigate(player, direction):
    global location, world_map
    current_location = location[0].split(',')
    x, y = int(current_location[0]), int(current_location[1])

    def print_navigate():
        print(f'''
You head {direction} and find a {world_map[location[0]].type}.''')

    if direction == 'back':
        if len(location) > 1:
            location = location[1:]
            player.tire()
            return print_navigate()
        else:
            return print('You cannot go back')
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
    player.tire()

    print_navigate()
    
def forage(player):
    square = world_map[location[0]]
    multiplier = 1

    if square.type is 'cave' and 'hammers' not in player.inventory:
        return print('You need a hammer to forage here')
    if square.type is 'lake' and 'worms' not in player.inventory:
        return print('You need a worm to forage here')
    
    if square.type is 'cave' or square.type is 'mountain' or square.type is 'lake':
        player.tire(2)
        multiplier = 2
    else:
        player.tire()
    product = square.produce()
    if product is not None:
        print(f'You found one {product}.')
        if square.type == 'cave':
            player.lose('hammers')
        if square.type == 'lake':
            player.lose('worms')
        return player.collect(product, multiplier)
    return print('You found nothing.')

# print('''                                                                            
#      ***** ***                                                               
#   ******  * **  *                                            *               
#  **   *  *  ** ***                                          ***              
# *    *  *   **  *                                            *               
#     *  *    *                          ****   ***  ****                      
#    ** **   *  ***   *** **** ****     * ***  * **** **** * ***       ****    
#    ** **  *    ***   *** **** ***  * *   ****   **   ****   ***     * ***  * 
#    ** ****      **    **  **** **** **    **    **           **    *   ****  
#    ** **  ***   **    **   **   **  **    **    **           **   **    **   
#    ** **    **  **    **   **   **  **    **    **           **   **    **   
#    *  **    **  **    **   **   **  **    **    **           **   **    **   
#       *     **  **    **   **   **  **    **    **           **   **    **   
#   ****      *** **    **   **   **   ******     ***          **   **    **   
#  *  ****    **  *** * ***  ***  ***   ****       ***         *** * ***** **  
# *    **     *    ***   ***  ***  ***                          ***   ***   ** 
# *                                                                            
#  **                 A text-based adventure game in Python                 
# ''')

player_name = str(input('What is your name, explorer? '))
player = Explorer(player_name)
print(f'''
Welcome, {player.name}, to the land of Rimoria!''')

# player = Explorer()

def status_check():
    global player
    while player.status == 'alive':
        print(' ')
        play()

def play():
    action = str(input('''What do you want to do: navigate, forage, look, or check?
''')).lower()
    if action == 'navigate':
        action_navigate(player)
    elif action == 'forage':
        forage(player)
    elif action == 'look':
        action_look()
    elif action == 'check':
        action_check()
    else:
        print(RES['UNKNOWN'])

def action_check():
    check = str(input('''What do you want to check: location, inventory, or status?
''')).lower()
    if check == 'inventory':
        return print(player.inventory)
    elif check == 'location':
        return print(f'''
You are standing in a {world_map[location[0]].type} at {location[0]}.''')
    elif check == 'status':
        return player.checkup()
    else:
        print(RES['UNKNOWN'])

def action_look():
    print(f'''
{world_map[location[0]].square_description}''')

def action_navigate(player):
    direction = str(input('''Which direction: north, east, south, west, or back?
''')).lower()
    options = ('north', 'east', 'south', 'west', 'back')
    if direction not in options:
        print(RES['UNKNOWN'])
    else:
        navigate(player, direction)

status_check()