from RPG.classes.game import  Person, bcolors, Enemy
from RPG.classes.magic import Spell
from RPG.classes.inventory import Item
import random


print('\n\n')
print("NAME                   HP                            MP")
print("                       _____________________         ____________ ")
print(bcolors.BOLD + "RALF:          460/460|" + bcolors.OKGREEN + "██████            " + bcolors.ENDC +"|  65/65|" + bcolors.OKBLUE +"███████" + bcolors.ENDC + "|")


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
enemy_magic = [fire, thunder, cure]
player_items = [{"item": potion, "quantity": 5},  {"item": hipotion, "quantity": 5}, {"item": superpotion, "quantity": 5},
                {"item": elexir, "quantity": 5}, {"item": superelexir, "quantity": 5}, {"item": grenade, "quantity": 5}]
#Initiate People
player1 = Person("Ralf  :", 3460, 65, 60, 34, player_magic, player_items)
player2 = Person("Bob   :", 4100, 65, 60, 34, player_magic, player_items)
player3 = Person("Jhon  :", 4460, 65, 60, 34, player_magic, player_items)

players = [player1, player2, player3]
enemy1 = Enemy("Magus:", 1200, 65, 450, 25, enemy_magic, [])
enemy2 = Enemy("Imp  :", 1200, 65, 450, 25, enemy_magic, [])
enemy3 = Enemy("Imp  :", 1200, 65, 450, 25, enemy_magic, [])

enemies = [enemy1, enemy2, enemy3]
running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("\n\n")
    print("NAME                    HP                             MP       ")
    for player in players:
        player.get_stats()
    print("\n\n")
    for enemy in enemies:
        enemy.get_stats()

    for player in players:
        if len(enemies) == 0:
            break
        print('************************************')
        player.choose_action()
        choice = input("    Eneter action: ")
        index = int(choice) - 1

        if index == 0:
            player.choose_enemy(enemies)
            enemy = int(input("Choose enemy: ")) - 1
            dmg = player.generate_damage()
            enemies[enemy].take_damage(dmg)
            print(player.name + " attacked for", dmg, "points of damage to " + enemies[enemy].name)
            if enemies[enemy].hp == 0:
                enemies.pop(enemy)
        if index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose a spell: ")) - 1
            if magic_choice == -1:
                continue
            if player.do_magic(magic_choice) is None:
                break
            spell, magic_dmg = player.do_magic(magic_choice)
            #spell = player.magic[magic_choice]
            #magic_dmg = spell.generate_damage()


            #current_mp = player.get_mp()



            player.reduce_mp(spell.cost)
            if spell.type == "black":
                player.choose_enemy(enemies)
                enemy = int(input("Choose enemy: ")) - 1
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " +
                      enemies[enemy].name + bcolors.ENDC)
                if enemies[enemy].hp == 0:
                    enemies.pop(enemy)

            elif spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals", str(magic_dmg), "points of HP"+ bcolors.ENDC)

        if index == 2:
            player.choose_item()
            item_choice = int(input("    Choose a item: ")) - 1
            if item_choice == -1:
                continue
            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals " + str(item.prop) + " points of HP"+ bcolors.ENDC)
            elif item.type == "elixir":
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + " restore HP and MP" + bcolors.ENDC )
            elif item.type == "attack":
                player.choose_enemy(enemies)
                enemy = int(input("Choose enemy: ")) - 1
                enemies[enemy].take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item.name + " deal " + str(item.prop) + " of HP" + bcolors.ENDC )
                if enemies[enemy].hp == 0:
                    enemies.pop(enemy)
    for enemy in enemies:
        if len(players) == 0:
            break
        action = random.randrange(0, 2)
        if action == 0:
            target = random.randrange(0,len(players))
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print("Enemy attacks for " + str(enemy_dmg) + "to " + players[target].name)
            if players[target].hp == 0:
                players.pop(target)
        elif action == 1:
            magic_choice = random.randrange(0,3)
            if enemy.do_magic(magic_choice) is None:
                break
            spell, magic_dmg = player.do_magic(magic_choice)
            # spell = player.magic[magic_choice]
            # magic_dmg = spell.generate_damage()


            # current_mp = player.get_mp()



            enemy.reduce_mp(spell.cost)
            if spell.type == "black":
                target = random.randrange(0, len(players))
                players[target].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " +
                      players[target].name + bcolors.ENDC)
                if players[target].hp == 0:
                    players.pop(target)

            elif spell.type == "white":
                enemy.heal(magic_dmg)
    print("***************************")


    if len(enemies) == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif len(players) == 0:
        print(bcolors.FAIL + "You lose..." + bcolors.ENDC)
        running = False