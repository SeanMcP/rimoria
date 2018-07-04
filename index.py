import random
from classes.ExplorerClass import Explorer
from classes.MapSquareClass import MapSquare

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

world_map = { '0,0': MapSquare() }
location = ['0,0']

def print_location():
        print(location[0], world_map[location[0]].type)

# print_location()

def navigate(direction):
    global location, world_map
    current_location = location[0].split(',')
    x, y = int(current_location[0]), int(current_location[1])

    # def print_location():
    #     print(location[0], world_map[location[0]].type)

    if direction == 'back':
        if len(location) > 1:
            location = location[1:]
            return print_location()
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

    print_location()
    
def search(player):
    print('Searching for resources')
    square = world_map[location[0]]
    multiplier = 1
    if square.type is 'cave' or square.type is 'mountain' or square.type is 'lake':
        player.tire(2)
        multiplier = 2
    else:
        player.tire()
    product = square.produce()
    if product is not None:
        print(f'You found one {product}')
        return player.collect(product, multiplier)
    return print('You found nothing')

player = Explorer('Sean')
player.checkup()
search(player)
print(player.inventory)
player.checkup()

# navigate('north')
# navigate('back')
# navigate('east')
# navigate('east')
# navigate('east')
# navigate('east')
# navigate('back')
# navigate('back')
# navigate('back')
# navigate('back')

# player_name = str(input('What is your name, explorer? '))
# player = Explorer(player_name)

# print(f'Welcome, {player.name}, to the land of Rimoria!')