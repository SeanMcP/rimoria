import random

# terrains = ('forest', 'plain', 'mountain', 'cave', 'lake')
# resources = {
#     'forest': 'wood',
#     'plain': 'worms',
#     'mountain': 'rocks',
#     'cave': 'gems',
#     'lake': 'fish'
# }

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
    
    def dig(self):
        if self.resource_count:
            self.resource_count -= 1
            return self.resource_type
        return None

# new_square = MapSquare('plain')
# print(new_square.type)
# print(new_square.resource_count)
# print(new_square.dig())
# print(new_square.resource_count)
