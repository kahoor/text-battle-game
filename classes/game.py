import random
from . import magic

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
    def __init__(self,name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk-100
        self.atkh = atk+100
        self.df = df
        self.magic = magic
        self.items = items

        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(int(self.atkl), int(self.atkh))

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp <= 0 :
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp>self.maxhp:
            self.hp = self.maxhp

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


    # choos action
    def choose_action(self):
        i = 1
        print("    "+self.name)
        print(bcolors.BOLD+bcolors.HEADER+"    Actions"+bcolors.ENDC)
        for j in self.actions:
            print("        "+str(i)+". "+j)
            i += 1

    # chose magic
    def choose_magic(self):
        i = 1
        print("\n"+bcolors.BOLD+bcolors.HEADER+"    Magic"+bcolors.ENDC)
        for j in self.magic:
            print("        "+str(i)+". "+j.name+" (cost "+str(j.cost)+')')
            i += 1

    def choose_item(self):
        i = 1
        print("\n"+bcolors.BOLD + bcolors.HEADER + "    Items" + bcolors.ENDC)
        for j in self.items:
            print("        "+str(i) + ". " + j["item"].name + ": " + j["item"].description + " (x"+str(j["quantity"])+")")
            i += 1

    def choose_enemy(self, enemies):
        i = 1
        print("\n" + bcolors.BOLD + bcolors.HEADER + "    Enemies" + bcolors.ENDC)
        for j in enemies:
            print("        " + str(i) + ". " + j.name)
            i += 1

        choice = int(input("    Choose action:")) - 1
        return enemies[choice]

    def get_enemy_stats(self):
        hpbar = ""
        for _ in range(int((self.hp / self.maxhp) * 50)):
            hpbar += "█"

        while len(hpbar) < 50:
            hpbar += " "

        hpfln = str(self.hp) + "/" + str(self.maxhp)

        while len(hpfln) < 16:
            hpfln = " " + hpfln

        print(bcolors.BOLD + self.name + ":" + hpfln + bcolors.ENDC + " |" + bcolors.FAIL + hpbar + bcolors.ENDC + "|")

    def get_stats(self):
        hpbar = ""
        for _ in range(int((self.hp/self.maxhp)*25)):
            hpbar += "█"

        while len(hpbar)<25:
            hpbar += " "

        mpbar = ""
        for _ in range(int((self.mp / self.maxmp) * 10)):
            mpbar += "█"

        while len(mpbar) < 10:
            mpbar += " "

        hpfln = str(self.hp)+"/"+str(self.maxhp)

        while len(hpfln)<16:
            hpfln = " "+hpfln

        mpfln = str(self.mp) + "/" + str(self.maxmp)

        while len(mpfln) < 11:
            mpfln = " " + mpfln

        print(bcolors.BOLD + self.name + ":" + hpfln + bcolors.ENDC + " |" + bcolors.OKGREEN + hpbar + bcolors.ENDC + "|" + bcolors.BOLD + mpfln +bcolors.ENDC+" |"+bcolors.OKBLUE+ mpbar +bcolors.ENDC+"|")
