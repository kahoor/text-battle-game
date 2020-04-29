import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-100
        self.atkh = atk+100
        self.df = df
        self.magic = magic

        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(int(self.atkl), int(self.atkh))

    def generate_spell_dmg(self, i):
        return random.randrange(self.magic[i]["dmg"]-300, self.magic[i]["dmg"]+300)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0 :
            self.hp = 0
        return self.hp

    # get hp mp max mp maxhp
    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp
    # reduce mp
    def reduce_mp(self, cost):
        self.mp -= cost

    # get spell name
    def get_spell_name(self, i):
        return self.magic[i]["name"]
    # get spell mp cost
    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]
    # choos action
    def choose_action(self):
        i = 1
        print("Actions")
        for j in self.actions:
            print(str(i)+". "+j)
            i += 1

    # chose magic
    def choose_magic(self):
        i = 1
        print("Magics")
        print("You have", self.mp, "mp!")
        for j in self.magic:
            print(str(i)+". "+j["name"]+" cost "+str(j["cost"]))
            i += 1

