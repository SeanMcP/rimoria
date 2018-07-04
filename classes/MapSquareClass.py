import random

class MapSquare:
    terrains = ('forest', 'plain', 'mountain', 'cave', 'lake')
    resources = {
        'forest': 'wood',
        'plain': 'worms',
        'mountain': 'rocks',
        'cave': 'gems',
        'lake': 'fish'
    }

    def __init__(self, prev_terrain='plain'):
        # New terrain has a 50% chance of being the same
        # as preivous terrain
        self.type = prev_terrain if random.randint(0, 1) is 1 else self.terrains[random.randint(0, len(self.terrains) - 1)]
        self.resource_count = random.randint(0, 5)
        self.resource_type = self.resources[self.type]
    
    def produce(self):
        if self.resource_count:
            self.resource_count -= 1
            return self.resource_type
        return None

# square = MapSquare('plain')
# print(square.type)
# print(square.resource_count)
# print(square.produce())
# print(square.resource_count)
