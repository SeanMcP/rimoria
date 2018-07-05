import random

class MapSquare:
    terrains = {
        'cave': {
            'description': 'A dimly lit and cool cave with large stalactites and stalagmites.',
            'resource': 'gems'
        },
        'forest': {
            'description': 'A densely forested area with a mixture of hard and soft wood, and evergreen trees.',
            'resource': 'wood'
        },
        'lake': {
            'description': 'Pebble beaches and cattails dot the shores of a clear and cold lake.',
            'resource': 'fish'
        },
        'mountain': {
            'description': 'A jagged mountain pass with large cracks, sharp corners, and steep ledges.',
            'resource': 'rocks'
        },
        'plain': {
            'description': 'Rolling hills of calf-length grass extend as far as the eye can see.',
            'resource': 'worms'
        }
    }

    def __init__(self, prev_terrain='plain'):
        # New terrain has a 50% chance of being the same
        # as preivous terrain
        self.type = prev_terrain if random.randint(0, 1) is 1 else [*self.terrains][random.randint(0, len([*self.terrains]) - 1)]
        self.resource_count = random.randint(0, 5) - 1
        self.resource_type = self.terrains[self.type]['resource']
        self.square_description = self.terrains[self.type]['description']
    
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
