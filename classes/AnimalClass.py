import random
from utils.data import get_animal, find_animal_type
from utils.print import new_line

class Animal:

    def __init__(self, resource_type='plain'):
        self.type = find_animal_type(resource_type)
        self.data = get_animal(self.type)
        self.energy = self.data['energy']
        self.experience = self.data['experience']
        self.is_angry = False
        self.resource = self.data['resource']
        self.speed = self.data['speed']
        self.status = 'alive'
        self.strength = self.data['strength']
    
    def anger(self):
        if self.is_angry == False:
            self.is_angry = True
            new_line(f'The {self.type} is getting angry!')

    def attack(self):
        roll = random.randint(0, 20) + self.speed
        if roll < 10:
            new_line(f'The {self.type}\'s attack misses!')
            return None
        new_line(f'{self.type} attack hits!')
        return self.strength

    def calm(self):
        if self.is_angry == True:
            self.is_angry = False
            new_line(f'The {self.type} is calming down.')
    
    def damage(self, amount):
        self.energy -= amount
        new_line(f'** The {self.type} takes {amount} damage **')
        self.anger()
        self.status_check()

    def feed(self, amount):
        if amount > 5:
            self.energy += amount
            self.calm()
        else:
            self.anger()
    
    def run(self):
        roll = random.randint(0, 20) + self.speed
        if roll > 10:
            return True
        return False

    def status_check(self):
        if self.energy < 1:
            self.status = 'dead'
            return new_line(f'The {self.type} dies.')