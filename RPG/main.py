from RPG.classes.game import  Person, bcolors
from RPG.classes.magic import Spell
from RPG.classes.inventory import Item

#Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

#Create whit magic
cure = Spell("Cure", 14, 140, "white")
cura = Spell("Cura", 18, 200, "white")

#Crete items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hipotion", "potion", "Heals 100 HP", 100)
superpotion = Item("Superpotion", "potion", "Heals 500 HP", 500)
elexir = Item("Exlixir", "elixir", "Fully restore HP/MP for one person", 9999)
superelexir = Item("SuperExlixir", "elixir", "Fully restore HP/MP for team", 9999)

grenade = Item("Grenade", "attack", "Deals 500 HP", 500)

player_magic = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 5},  {"item": hipotion, "quantity": 5}, {"item": superpotion, "quantity": 5},
                {"item": elexir, "quantity": 5}, {"item": superelexir, "quantity": 5}, {"item": grenade, "quantity": 5}]
#Initiate People
player = Person(460, 65, 60, 34, player_magic, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print('************************************')
    player.choose_action()
    choice = input("Eneter action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")

    if index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose a spell: ")) - 1
        if magic_choice == -1:
            continue
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()


        current_mp = player.get_mp()

        if current_mp < spell.cost:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        if spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage")

        elif spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals", str(magic_dmg), "points of HP")

    if index == 2:
        player.choose_item()
        item_choice = int(input("Choose a item: ")) - 1
        if item_choice == -1:
            continue
        item = player.items[item_choice]["item"]
        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
            continue
        player.items[item_choice]["quantity"] -= 1

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals " + str(item.prop) + " points of HP")
        elif item.type == "elixir":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + " restore HP and MP" + bcolors.ENDC )
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.FAIL + "\n" + item.name + " deal " + str(item.prop) + " of HP" + bcolors.ENDC )



    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("***************************")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC + "\n")

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You lose..." + bcolors.ENDC)
        running = False
