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

world_map = { '0,0': { 'terrain': 'plain' } }
location = [[0,0]]
terrains = ['plain', 'forest', 'mountain', 'cave']

def navigate(direction):
    global location
    current_location = location[0]
    x, y = current_location[0], current_location[1]

    if direction == 'back':
        if len(location) > 1:
            location = location[1:]
            return print(location)
        else:
            return print('You cannot go back')
    elif direction == 'north':
        new_coordinates = [ x, y + 1 ]
    elif direction == 'south':
        new_coordinates = [ x, y - 1 ]
    elif direction == 'east':
        new_coordinates = [ x + 1, y ]
    elif direction == 'west':
        new_coordinates = [ x - 1, y ]
    
    coordinate_string = ','.join(map(str, new_coordinates))

    global world_map
    if coordinate_string not in world_map:
        world_map[coordinate_string] = {
            'terrain': terrains[random.randint(0, len(terrains) - 1)]
        }

    location.insert(0, new_coordinates)
    location = location[:10]

    print(location)
    print(world_map)
    
navigate('north')
# navigate('north')
# navigate('north')
navigate('back')
# navigate('back')
# navigate('back')
# navigate('back')

player_name = str(input('What is your name, explorer? '))
player = Explorer(player_name)

print(f'Welcome, {player.name}, to the land of Rimoria!')