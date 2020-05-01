from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


# dark magic initialize
toop = Spell("Toop", 1500, 11, "dark")
tank = Spell("Tank", 1300, 9, "dark")
feshfeshe = Spell("Feshfeshe", 1400, 10, "dark")

# white magic initialize
cure = Spell("Cure", 2000, 9, "white")
cura = Spell("Cura", 4000, 14, "white")

# Create some Items
potion = Item("Potion", "potion", "Heals 700 HP", 700)
hipotion = Item("Hi-Potion", "potion", "Heals 1500 HP", 1500)
superpotion = Item("Super Potion", "potion", "Heals 3700 HP", 3700)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 1700 damage", 1700)


player_spells = [toop, tank, feshfeshe, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer, "quantity": 5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity": 5}]


player1 = Person("Kahoor", 13000, 50, 780, 40, player_spells, player_items)
player2 = Person("Omid  ", 11000, 50, 560, 40, player_spells, player_items)
player3 = Person("Shayan", 9000, 50, 900, 40, player_spells, player_items)

players = [player1, player2, player3]

enemy1 = Person("fboy  ", 100000, 60, 480, 40, [], [])
enemy2 = Person("minboy", 6000, 60, 980, 40, [], [])
enemy3 = Person("litgrl", 8000, 60, 700, 40, [], [])

enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.FAIL+bcolors.UNDERLINE+bcolors.BOLD+"THE BEST TEXT BATTLE GAME EVER!"+bcolors.ENDC)

while running:
    print("+++++++++++++++++++++++++++++++++++")
    print("name                     HP                                     MP")

    for player in players:
        player.get_stats()
    print("\n")

    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = int(input("    Choose action:"))-1
        if choice == 0:
            dmg = player.generate_damage()
            enemy = player.choose_enemy(enemies)
            enemy.take_dmg(dmg)
            print(bcolors.FAIL+  "You attacked for " + str(dmg) + " points of damage.", bcolors.ENDC)
            if enemy.get_hp() == 0:
                print(bcolors.FAIL+ "You killed " + enemy.name, bcolors.ENDC)
                enemies.remove(enemy)

        elif choice == 1:
            player.choose_magic()
            index = int(input("    Choose magic:"))-1
            if index == -1:
                continue
            spell = player.magic[index]
            cost = spell.cost
            current_mp = player.get_mp()

            if cost > current_mp:
                print(bcolors.FAIL+bcolors.BOLD, "Not enough MP", bcolors.ENDC)
                continue

            player.reduce_mp(cost)
            dmg = spell.generate_spell_dmg()
            if spell.type == "dark":
                enemy = player.choose_enemy(enemies)
                enemy.take_dmg(dmg)
                print(bcolors.FAIL+ spell.name+ " deals " + str(dmg) + " points of damage.", bcolors.ENDC)
                if enemy.get_hp() == 0:
                    print(bcolors.FAIL + "You killed " + enemy.name, bcolors.ENDC)
                    enemies.remove(enemy)

            else:
                player.heal(dmg)
                print(bcolors.OKBLUE + item.name + " heals for " + str(item.prop) + " HP.", bcolors.ENDC)

        elif choice == 2:
            player.choose_item()
            index = int(input("    Choose item:")) - 1
            if index == -1:
                continue

            item = player_items[index]["item"]

            if player_items[index]["quantity"] == 0:
                print(bcolors.FAIL + bcolors.BOLD, "None left...", bcolors.ENDC)
                continue

            player_items[index]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKBLUE + item.name + " heals for " + str(item.prop) + " HP.", bcolors.ENDC)

            elif item.type == "elixer":
                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    print(bcolors.OKBLUE + item.name + " fully restores party's HP/MP ", bcolors.ENDC)

                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.OKBLUE + item.name + " fully restores your HP/MP ", bcolors.ENDC)

            elif item.type == "attack":
                enemy = player.choose_enemy(enemies)
                enemy.take_dmg(item.prop)
                print(bcolors.FAIL + item.name + " deals " + str(item.prop) + " points of damage.", bcolors.ENDC)
                if enemy.get_hp() == 0:
                    print(bcolors.FAIL + "You killed " + enemy.name, bcolors.ENDC)
                    enemies.remove(enemy)

    for enemy in enemies:
        dmg = enemy.generate_damage()
        target = random.randrange(0, len(players))
        players[target].take_dmg(dmg)
        print("Enemy attacked "+players[target].name+" for " + str(dmg) + " points of damage.")
        if players[target].get_hp() == 0:
            print(bcolors.FAIL + enemy.name +" killed " + players[target].name, bcolors.ENDC)
            del players[target]


    if len(enemies) == 0:
        print(bcolors.OKGREEN, "YOU WIN!",bcolors.ENDC)
        running = False
    elif len(players) == 0:
        print(bcolors.FAIL, "YOU LOST!", bcolors.ENDC)
        running = False
