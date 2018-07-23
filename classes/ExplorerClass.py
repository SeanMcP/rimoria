import random
from utils.print import new_line
from utils.string import capitalize

class Explorer:
    def __init__(self, name='Link'):
        self.energy = 100
        # self.inventory = {
        #     'wood': 10,
        #     'fish': 10,
        #     'fire': 10,
        #     'ore': 10,
        #     'worm': 10,
        #     'rock': 10,
        #     'gem': 10,
        #     'stonefish': 10
        # }
        self.inventory = {}
        self.level = 1
        self.name = name
        self.status = 'alive'
        self.strength = 1
        self.xp = 0

    def checkup(self):
        print(f'''
Name:     {self.name}
Status:   {capitalize(self.status)}
Energy:   {self.energy}
Strength: {self.strength}
Level:    {self.level}
XP:       {self.xp}/100''')

    def collect(self, item, multiplier=1):
        if item not in self.inventory:
            self.inventory[item] = 1
        else:
            self.inventory[item] += 1
        self.gain(multiplier)
        return new_line(f'You collect one {item}!')

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
            new_line(f'** Alright! Your energy increased by {amount} **')
        else:
            new_line(f'** Ouch! Your energy decreased by {amount} **')
        self.status_check()

    def level_up(self, multiplier=1):
        self.level += 1 * multiplier
        new_line(f'** Power up! You are now level {self.level} **')
    
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
            return new_line('You die.')

        elif self.energy >= 1 and self.energy < 25:
            self.status = 'exhausted'
        elif self.energy >= 25 and self.energy < 50:
            self.status = 'tired'
        else:
            self.status = 'alive'
        if status != self.status:
            new_line(f'(( You are feeling {self.status} ))')
    
    def tire(self, multiplier=1):
        if self.status != 'alive':
            multiplier += 1
        self.energy -= (1.5 / self.strength) * multiplier
        self.status_check()