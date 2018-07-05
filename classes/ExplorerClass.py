import random

class Explorer:
    def __init__(self, name='Link'):
        self.energy = 100
        self.inventory = {}
        self.level = 1
        self.name = name
        self.status = 'alive'
        self.strength = 1
        self.xp = 0

    def checkup(self):
        print(f'''
Explorer:  {self.name}
Status:    {self.status}
Energy:    {self.energy}
Strength:  {self.strength}
Level:     {self.level}
XP:        {self.xp}/100
Inventory: {self.inventory}
''')

    def collect(self, item, multiplier=1):
        if item not in self.inventory:
            self.inventory[item] = 1
        else:
            self.inventory[item] += 1
        self.gain(multiplier)

    def gain(self, multiplier=1):
        self.xp += 10 * multiplier
        if self.xp > 100:
            self.xp -= 100
            self.grow()
            self.level_up()
    
    def grow(self, multiplier=1):
        self.strength += 0.5 * multiplier

    def level_up(self, multiplier=1):
        self.level += 1 * multiplier
    
    def lose(self, item):
        if self.inventory[item] > 1:
            self.inventory[item] -= 1
        else:
            del self.inventory[item]
    
    def rest(self):
        self.energy += 10 * self.strength
    
    def tire(self, multiplier=1):
        self.energy -= (1 / self.strength) * multiplier

# player = Explorer('Sean')
# print('Equipment:', player.equipment)
# print('XP:', player.xp)
# player.equip('hammer')
# print('Equipment:', player.equipment)
# print('XP:', player.xp)