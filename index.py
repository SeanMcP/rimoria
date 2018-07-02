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

location = [[ 0, 0 ]]

def navigate(direction):
    global location
    current_loc = location[0]
    x, y = current_loc[0], current_loc[1]

    if direction == 'back':
        if len(location) > 1:
            location = location[1:]
            return print(location)
        else:
            return print('You cannot go back')
    elif direction == 'north':
        new_loc = [ x, y + 1 ]
    elif direction == 'south':
        new_loc = [ x, y - 1 ]
    elif direction == 'east':
        new_loc = [ x + 1, y ]
    elif direction == 'west':
        new_loc = [ x - 1, y ]
    
    location.insert(0, new_loc)
    location = location[:10]

    print(location)
    
# navigate('north')
# navigate('north')
# navigate('north')
# navigate('back')
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