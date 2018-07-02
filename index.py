import random

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
    current_coordinates = location[0]
    x, y = current_coordinates[0], current_coordinates[1]

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
        new_location = {
            'terrain': terrains[random.randint(0, len(terrains) - 1)]
        }
        world_map[coordinate_string] = new_location

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

class Hero:
    def __init__(self, name, hitpoints=100, attackpoints=10, status='alive'):
        self.ap = attackpoints
        self.hp = hitpoints
        self.max_hp = hitpoints
        self.name = name
        self.status = status

    def damage(self, amount):
        print(f'You have been attacked!')
        if self.status is 'alive':
            self.hp -= amount
            if self.hp <= 0:
                self.status = 'unconscious'
                print('You\'re now unconscious')
        elif self.status is 'unconscious':
            lot = random.randint(0,3)
            if lot == 1:
                self.status = 'dead'
                print('You\'re dead!')
            elif lot == 2:
                self.status = 'alive'
                print('Somehow you recover!')
            else:
                print('Why hit someone while they\'re down?')

# hero_name = str(input('What is your name, hero? '))
# hero = Hero(hero_name)

# print(f'Welcome, {hero.name}, to the land of Rimoria!')