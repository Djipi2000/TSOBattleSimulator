
class Battle:
    originalside =[]
    def __init__(self):
        pass
    def set_up_side(side_number: int, side):
        if side_number == 0:
            self.originalside[0] = side
        if side_number == 1:
            self.originalside[1] = side
        
    

class Side:
    def __init__(self, units=None):
        self.units = []
        if units != None:
            self.add_units(units)
        
    def add_units(self, units):
        for unit in units:
            self.units.append(unit)
    def add_unit(self, unit):
        self.units.append(unit)

    def has_lost(self):
        remaining_units = []
        for unit in self.units:
            if unit.amount > 1:
                remaining_units.append(unit)
        if len(remaining_units) > 1:
            return False
        else:
            return True
    def debug(self):
        print(str(len(self.units)) + " unites.")
        for unit in self.units:
            print(str(unit.name) + " * " + str(unit.amount))
        
    def get_unit(self, weakest=False):
        if weakest == True:
            return get_weakest_unit(self.units)
        else:
            return get_next_targetorder_unit(self.units)
    def get_unit_with_name(self, name: str):
        return get_unit_with_name(self.units, name)
    def get_unit_with_abbrev(self, abbrev: str):
        return get_unit_with_abbrev(self.units, abbrev)

def get_next_targetorder_unit(units):
    targeted_u = units[0] # need to start with some value
    for i in units:
        if i.targetorder < targeted_u.targetorder and i.amount > 0:
            targeted_u = i
    return targeted_u

def get_weakest_unit(units):
    weakest_u = units[0] # need to start with some value
    for i in units:
        if i.hp < weakest_u.hp and i.amount > 0:
            weakest_u = i
    return weakest_u

def get_unit_with_name(units, name: str):
    found_u = None
    for i in units:
        if i.name == name:
            found_u = i
    return found_u
def get_unit_with_abbrev(units, abbrev: str):
    found_u = None
    for i in units:
        if i.abbrev == abbrev:
            found_u = i
    return found_u
