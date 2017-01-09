import random
import json

def ImportUnit(file: str, name=None, abbrev=None, amount=None):
    if name != None:
        to_search = name
    elif name == None and abbrev != None:
        to_search = abbrev
    elif name == None and abbrev == None:
        print("Erreur : abbrev et name == Null")
        return None
    with open(file, "r") as json_file:
        data = json.load(json_file)
        for unit in data:
            if unit["name"] == to_search or unit["abbrev"] == to_search:
                return Unit(unit["name"], unit["abbrev"], unit["hp"], unit["min_dmg"], unit["max_dmg"], unit["accuracy"], unit["strike_order"], unit["targetweakest"], unit["splashdamage"], unit["targetorder"], amount=amount)


class Unit:
    def __init__(self, name: str, abbrev: str, hp: int, min_dmg: int, max_dmg: int, accuracy: int, strike_order, targetweakest: int, splashdamage: int, targetorder: int, amount=None):
        self.name = name
        self.abbrev = abbrev
        self.hp = int(hp)
        self.min_dmg = int(min_dmg)
        self.max_dmg = int(max_dmg)
        self.accuracy = int(accuracy)
        self.strike_order = int(strike_order)
        if int(targetweakest) == 1:
            self.targetweakest = True
        else:
            self.targetweakest = False
        self.splashdamage = bool(int(splashdamage))

        if amount == None:
            self.amount = 1
        else:
            self.amount = amount
        self.targetorder = int(targetorder)

    def debug(self):
        print("name : " + self.name)
        print("abbrev : " + self.abbrev)
        print("hp : " + str(self.hp))
        print("min_dmg : " + str(self.min_dmg))
        print("max_dmg : " + str(self.max_dmg))
        print("accuracy : " + str(self.accuracy))
        print("strike_order : " + str(self.strike_order))
        print("targetweakest : " + str(self.targetweakest))
        print("splashdamage : " + str(self.splashdamage))
        print("amount : " + str(self.amount))
        print("targetorder : " + str(self.targetorder))

    def set_amount(self, amount):
        self.amount = amount
    def get_amount(self):
        return self.amount
    def get_strikeorder(self):
        return self.strike_order
    def get_hp(self):
        return self.hp
    def get_total_hp(self):
        return self.hp * self.number
    def get_splashdamage(self):
        if self.splashdamage == 0:
            return False
        else:
            return True
    def get_damage(self, total=True, single=False):
        if total == True:
            total = 0
            for x in range(0, self.amount):
                acc = random.randint(0, 100)
                if acc >= self.accuracy:
                    total += self.min_dmg
                else:
                    total += self.max_dmg
            return total
        if single == True:
            acc = random.randint(0, 100)
            damage = 0
            if acc >= self.accuracy:
                damage = self.min_dmg
            else:
                damage = self.max_dmg
            return damage
        
