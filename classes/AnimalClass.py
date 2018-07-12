import random
from utils.data import get_animal
from utils.print import new_line

class Animal:

    def __init__(self, animal_type='buffalo'):
        self.data = get_animal(animal_type)
        self.type = animal_type
        self.energy = self.data['energy']
        self.experience = self.data['experience']
        self.resource = self.data['resource']
        self.speed = self.data['speed']
        self.status = 'alive'
        self.strength = self.data['strength']
    
    def attack(self):
        roll = random.randint(0, 20) + self.speed
        if roll < 10:
            new_line(f'The {self.type}\'s attack misses!')
            return None
        new_line(f'{self.type} attack hits!')
        return self.strength
    
    def damage(self, amount):
        self.energy -= amount
        new_line(f'** The {self.type} takes {amount} damage **')
        self.status_check()
    
    def run(self):
        roll = random.randint(0, 20) + self.speed
        if roll > 10:
            return True
        return False

    def status_check(self):
        if self.energy < 1:
            self.status = 'dead'
            return new_line(f'The {self.type} dies.')
