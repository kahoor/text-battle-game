from classes.game import Person, bcolors


magic = [{"name": "Toop", "cost": 10, "dmg": 800},
         {"name": "Tank", "cost": 10, "dmg": 600},
         {"name": "Feshfeshe", "cost": 10, "dmg": 700}]

player = Person(10000, 50, 480, 40, magic)
enemy = Person(10000, 50, 480, 40, magic)
print(player.get_hp())

running = True

print(bcolors.FAIL+bcolors.UNDERLINE+ "THE BEST TEXT BATTLE GAME EVER!"+bcolors.ENDC)

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
        cost = magic[index]["cost"]
        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL+bcolors.bold, "Not enough MP", bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        dmg = player.generate_spell_dmg(index)
        enemy.take_dmg(dmg)
        print(bcolors.OKBLUE+ magic[index]["name"]+ " deals " + str(dmg) + " points of damage.", bcolors.ENDC)


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
