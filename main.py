from classes.game import Person, bcolors
from classes.magic import Spell


# dark magic initialize
toop = Spell("Toop", 800, 11, "dark")
tank = Spell("Tank", 600, 9, "dark")
feshfeshe = Spell("Feshfeshe", 700, 10, "dark")

# white magic initialize
cure = Spell("Cure", 1500, 9, "white")
cura = Spell("Cura", 3000, 14, "white")

player_magic=[toop, tank, feshfeshe, cure, cura]

player = Person(10000, 50, 480, 40, player_magic)
enemy = Person(10000, 50, 480, 40, player_magic)

running = True

print(bcolors.FAIL+bcolors.UNDERLINE+bcolors.BOLD+"THE BEST TEXT BATTLE GAME EVER!"+bcolors.ENDC)

while running:
    print("+++++++++++++++++++++++++++++++++++")
    player.choose_action()
    choice = int(input("Choose action:"))-1
    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_dmg(dmg)
        print("You attacked for "+ str(dmg)+" points of damage.")

    elif choice == 1:
        player.choose_magic()
        index = int(input("Choose magic:"))-1
        spell = player.magic[index]
        cost = spell.cost
        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL+bcolors.BOLD, "Not enough MP", bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        dmg = spell.generate_spell_dmg()
        if spell.type == "dark":
            enemy.take_dmg(dmg)
            print(bcolors.OKBLUE+ spell.name+ " deals " + str(dmg) + " points of damage.", bcolors.ENDC)
        else:
            player.heal(dmg)
            print(bcolors.OKBLUE + spell.name + " deals " + str(dmg) + " points of HP.", bcolors.ENDC)



    enemy_choice = 0

    dmg = enemy.generate_damage()
    player.take_dmg(dmg)
    print("Enemy attacked for " + str(dmg) + " points of damage.")

    print("---------------------------------")
    print("Enemy HP:", bcolors.OKBLUE, enemy.get_hp(), '/', enemy.get_maxhp(), bcolors.ENDC, '\n')
    print("Your HP:", bcolors.OKGREEN, player.get_hp(), '/', player.get_maxhp(), bcolors.ENDC, '\n')

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN, "YOU WIN!",bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL, "YOU LOST!", bcolors.ENDC)
        running = False
