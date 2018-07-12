import random
from utils.data import get_terrains

class Terrain:
    terrains = get_terrains()

    def __init__(self, prev_terrain='plain'):
        # New terrain has a 50% chance of being
        # the same as preivous terrain
        self.type = prev_terrain if random.randint(0, 1) is 1 else [*self.terrains][random.randint(0, len([*self.terrains]) - 1)]
        self.description = self.terrains[self.type]['description']
        self.difficulty = self.terrains[self.type]['difficulty']
        self.resource_count = random.randint(0, 5) - 1
        self.resource_type = self.terrains[self.type]['resource']
        self.requirement = self.terrains[self.type]['requirement']
    
    def produce(self):
        if self.resource_count > 0:
            self.resource_count -= 1
            return self.resource_type
        return None