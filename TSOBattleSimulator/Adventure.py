import json
import Unit

def ImportAdventure(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return Adventure(data[0]["adventure_name"], data[0]["adventure_units"], data[0]["adventure_camps"])

def ImportCamp(units_file: str, camp_file: str):
    units = []
    camp = Camp(camp_file["name"])
    with open(camp_file["file"]) as f:
        f_json = json.load(f)
        for unit in f_json:
            camp.add_unit(Unit.ImportUnit(units_file, name=unit["name"], amount=unit["amount"]))
    return camp

def ImportCamps(camps_files, units_files):
    camps = []
    for camp_file in camps_files:
        camps.append(ImportCamp(units_files, camp_file))
    return camps

class Camp():
    def __init__(self, name: str):
        self.name = name
        self.units = []
    def debug(self):
        print(self.units)
    def add_unit(self, unit):
        self.units.append(unit)

class Adventure():
    def __init__(self, name: str, units_file: str, camps_f: str):
        self.name = name
        self.units_file = units_file
        self.camps_f = camps_f
        self.camps = ImportCamps(self.camps_f, self.units_file)

    def debug(self):
        print(self.name)
        print(self.units_file)
        print(str(len(self.camps)) + " camps.")
        for camp in self.camps:
            print(" ----- ")
            print("Camp " + camp.name)
            for unit in camp.units:
                print(str(unit.name) + " * " + str(unit.amount))
    def get_camp(self, camp_name):
        for camp in self.camps:
            if camp.name == camp_name:
                return camp
        print("Camp introuvable")
        return None