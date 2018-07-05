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
        if self.xp >= 100:
            self.xp -= 100
            self.grow()
            self.level_up()
    
    def grow(self, multiplier=1):
        self.strength += 0.5 * multiplier
    
    def heal(self, amount):
        self.energy += amount
        if self.energy > 100:
            self.energy = 100
        if amount > 0:
            print(f'''
** Alright! Your energy increased by {amount} **''')
        else:
            print(f'''
** Ouch! Your energy decreased by {amount} **''')
        self.status_check()

    def level_up(self, multiplier=1):
        self.level += 1 * multiplier
        print(f'''
** Power up; you are now level {self.level}! **''')
    
    def lose(self, item):
        if self.inventory[item] > 1:
            self.inventory[item] -= 1
        else:
            del self.inventory[item]
    
    def rest(self):
        self.energy += 10 * self.strength
        self.status_check()

    def status_check(self):
        status = self.status
        if self.energy < 1:
            self.status = 'dead'
            return print('''
You die of exhaustion.
''')
        elif self.energy >= 1 and self.energy < 25:
            self.status = 'exhausted'
        elif self.energy >= 25 and self.energy < 50:
            self.status = 'tired'
        else:
            self.status = 'alive'
        if status != self.status:
            print(f'''
(( You are feeling {self.status} ))''')
    
    def tire(self, multiplier=1):
        if self.status == 'tired':
            multiplier += 1
        elif self.status == 'exhausted':
            multiplier += 2
        self.energy -= (1 / self.strength) * multiplier
        self.status_check()

# player = Explorer('Sean')
# print('Equipment:', player.equipment)
# print('XP:', player.xp)
# player.equip('hammer')
# print('Equipment:', player.equipment)
# print('XP:', player.xp)