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
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.arkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.arkl, self.atkh)



    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp


    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost


    def choose_action(self):


        i = 1
        print("    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.FAIL + "    Actions: " + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + "    Magic: " + bcolors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ":", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1
    def do_magic(self, i):
        #i = int(input("    Choose a spell: ")) - 1
        #self.choose_action()
        spell = self.magic[i]
        magic_damage = spell.generate_damage()
        if self.magic[i].cost > self.mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            return
        else:
            return spell, magic_damage




    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN + "    Items: " + bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ":", item["item"].name + ": " + item["item"].description + " X" + str(item["quantity"]))
            i += 1

    def choose_enemy(self, enemies):
        i = 1
        print(bcolors.FAIL + "    Enemies: " + bcolors.ENDC)
        for enemy in enemies:
            print("    " + str(i) + ".", enemy.name)
            i += 1
        return

    def get_stats(self):
        shp = self.hp / self.maxhp * 100 / 4
        cur_hp = ""
        while len(cur_hp) < 25:
            if len(cur_hp) < shp:
                cur_hp += "#"
            else:
                cur_hp += " "

        smp = self.mp / self.maxmp * 100 / 10
        cur_mp = ""
        while len(cur_mp) < 10:
            if len(cur_mp) < smp:
                cur_mp += "#"
            else:
                cur_mp += " "
        current_hp = " " * (4 - len(str(self.hp)))
        print("                         _________________________         __________ ")
        print(
            bcolors.BOLD + self.name + "        " + current_hp + str(self.hp) + "/" + str(self.maxhp) + "|" + bcolors.OKGREEN + cur_hp + bcolors.ENDC + "|  "+ str(self.mp) + "/" + str(self.maxmp) + "|" + bcolors.OKBLUE + cur_mp + bcolors.ENDC + "|")


class Enemy(Person):
    def get_stats(self):
        shp = self.hp / self.maxhp * 100 / 4
        cur_hp = ""
        while len(cur_hp) < 25:
            if len(cur_hp) < shp:
                cur_hp += "#"
            else:
                cur_hp += " "

        smp = self.mp / self.maxmp * 100 / 10
        cur_mp = ""
        while len(cur_mp) < 10:
            if len(cur_mp) < smp:
                cur_mp += "#"
            else:
                cur_mp += " "
        current_hp = " " * (4 - len(str(self.hp)))
        print("                        _________________________         __________ ")
        print(
            bcolors.BOLD + self.name + "        " + current_hp + str(self.hp) + "/" + str(
                self.maxhp) + "|" + bcolors.FAIL + cur_hp + bcolors.ENDC + "|  " + str(self.mp) + "/" + str(
                self.maxmp) + "|" + bcolors.OKBLUE + cur_mp + bcolors.ENDC + "|")