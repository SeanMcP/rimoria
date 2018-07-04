import random

class Explorer:
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
