import random

class MapSquare:
    description = {
        'forest': 'A densely wooded area with a mixture of hard and soft wood, and evergreen trees.',
        'plain': 'Rolling hills of calf-length grass extend as far as the eye can see.',
        'mountain': 'A jagged mountain pass with large cracks, sharp corners, and steep ledges.',
        'cave': 'A dimly lit and cool cave with large stalactites and stalagmites.',
        'lake': 'Pebble beaches and cattails dot the shores of a clear and cold lake.'
    }
    resources = {
        'forest': 'wood',
        'plain': 'worms',
        'mountain': 'rocks',
        'cave': 'gems',
        'lake': 'fish'
    }
    terrains = ('forest', 'plain', 'mountain', 'cave', 'lake')

    def __init__(self, prev_terrain='plain'):
        # New terrain has a 50% chance of being the same
        # as preivous terrain
        self.type = prev_terrain if random.randint(0, 1) is 1 else self.terrains[random.randint(0, len(self.terrains) - 1)]
        self.resource_count = random.randint(0, 5) - 1
        self.resource_type = self.resources[self.type]
        self.square_description = self.description[self.type]
    
    def produce(self):
        if self.resource_count > 0:
            self.resource_count -= 1
            return self.resource_type
        return None

# square = MapSquare('plain')
# print(square.type)
# print(square.resource_count)
# print(square.produce())
# print(square.resource_count)
