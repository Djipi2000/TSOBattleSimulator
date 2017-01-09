import Unit
import Adventure
import Battle
from collections import namedtuple
import itertools
from pprint import pprint
import timeit
#test_unit = Unit.ImportUnit("./Adventures/CN/units.json", abbrev="S")
#test_unit.debug()
#
#test_adventure = Adventure.ImportAdventure("./Adventures/CN/adventure_info.json")
#test_adventure.debug()
#print(" ")

class SimulationWrapper:
    def __init__(self, file):
        self.allowed_units = []
        self.file_units = file
        pass
    def add_allowed_unit(self, name=None):
        self.allowed_units.append(name)
    def get_all_iterations(self):
        all_permutations = itertools.permutations(range(0,200), len(self.allowed_units))
        return all_permutations
    def get_iteration(self, iteration):
        Side = Battle.Side()
        i = 0
        for unit in self.allowed_units:
            unit = Unit.ImportUnit(self.file_units, name=self.allowed_units[i], amount=iteration[i])
            Side.add_unit(unit)
            i += 1
        #Side.debug()

def test():
    simulation_w = SimulationWrapper("./Adventures/player_units.json")
    simulation_w.add_allowed_unit("Cavalier")
    simulation_w.add_allowed_unit("Soldat")
    ii = 0
    for a in simulation_w.get_all_iterations():
        ii += 1
        simulation_w.get_iteration(a)
    print(ii)
print(timeit.timeit('test()', globals=globals(), number=1))
print("")
#print(timeit.timeit("test()", setup="from __main__ import test"))
#pprint(list(sim_limit.get_all_iterations()))

#test = itertools.combinations(range(200), 1)
#t = 0
#for i in test:
#    print(i[0])
#    t += 1
#    pass
#print(t)