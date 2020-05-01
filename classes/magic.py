import random

class Spell:
    def __init__(self, name, dmg, cost, type):
        self.name = name
        self. dmg = dmg
        self.cost = cost
        self.type = type

    def generate_spell_dmg(self):
        return random.randrange(self.dmg-300, self.dmg+300)
