from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


# dark magic initialize
toop = Spell("Toop", 800, 11, "dark")
tank = Spell("Tank", 600, 9, "dark")
feshfeshe = Spell("Feshfeshe", 700, 10, "dark")

# white magic initialize
cure = Spell("Cure", 1500, 9, "white")
cura = Spell("Cura", 3000, 14, "white")

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


player = Person(10000, 50, 480, 40, player_spells, player_items)
enemy = Person(10000, 50, 480, 40, [], [])

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
            enemy.take_dmg(dmg)
            print(bcolors.FAIL+ spell.name+ " deals " + str(dmg) + " points of damage.", bcolors.ENDC)
        else:
            player.heal(dmg)
            print(bcolors.OKBLUE + item.name + " heals for " + str(item.prop) + " HP.", bcolors.ENDC)

    elif choice == 2:
        player.choose_item()
        index = int(input("Choose item:")) - 1
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
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKBLUE + item.name + " fully restores HP/MP ", bcolors.ENDC)

        elif item.type == "attack":
            enemy.take_dmg(item.prop)
            print(bcolors.FAIL + item.name + " deals " + str(item.prop) + " points of damage.", bcolors.ENDC)

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
