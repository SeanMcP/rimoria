import random

class Explorer:
    def __init__(self, name):
        self.energy = 100
        self.equipment = {}
        self.inventory = {}
        self.name = name
        self.status = 'alive'
        self.strength = 1
        self.xp = 0

    def collect(self, item, quantity):
        if item not in self.inventory:
            self.inventory[item] = quantity
        else:
            self.inventory[item] += quantity
        self.gain()
    
    def equip(self, item):
        if item not in self.equipment:
            self.equipment[item] = 1
        else:
            self.equipment += 1
        self.gain()

    def gain(self, multiplier=1):
        self.xp += 10 * multiplier
        if self.xp > 100:
            self.xp -= 100
            self.grow()
    
    def grow(self, multiplier=1):
        self.strength += 0.5 * multiplier
    
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