import random
from utils.data import get_animal, get_item, find_animal_type
from utils.print import new_line

class Animal:

    def __init__(self, resource_type='plain'):
        self.type = find_animal_type(resource_type)
        self.data = get_animal(self.type)
        self.description = self.data['description']
        self.energy = self.data['energy']
        self.experience = self.data['experience']
        self.is_alive = True
        self.is_angry = False
        self.resource = self.data['resource']
        self.speed = self.data['speed']
        self.strength = self.data['strength']
    
    def anger(self):
        if self.is_angry == False:
            self.is_angry = True
            new_line(f'The {self.type} is getting angry!')

    def attack(self):
        roll = random.randint(1, 20) + self.speed
        if roll < 10:
            return None
        new_line(f'The {self.type} attacks!')
        return self.strength

    def calm(self):
        if self.is_angry == True:
            self.is_angry = False
            new_line(f'The {self.type} is calming down.')
    
    def damage(self, amount):
        self.energy -= amount
        new_line(f'** The {self.type} takes {amount} damage **')
        alive = self.status_check()
        if alive:
            self.anger()

    def feed(self, item_name):
        item = get_item(item_name)
        amount = item['energy']
        self.energy += amount
        if amount > 5:
            if self.is_angry:
                self.calm()
            else:
                new_line(f'The {self.type} takes the offering and happily goes on its way.')
                return True
        else:
            is_alive = self.status_check()
            if is_alive:
                self.anger()
            else:
                return True
        return False
    
    def run(self):
        roll = random.randint(0, 20) + self.speed
        if roll > 10:
            return True
        return False

    def status_check(self):
        if self.energy < 1:
            self.is_alive = False
            new_line(f'The {self.type} dies.')
            return None
        else:
            return True