import unittest
import Adventure
import Unit

class Test_Adventure(unittest.TestCase):
    def setUp(self):
        self.expected_name = "Les Chevaliers Noirs"
        self.expected_unit_file = "./Adventures/CN/units.json"
        self.expected_number_of_camps = 2
    def test_expected_name(self):
        adventure = Adventure.ImportAdventure("./adventures/CN/adventure_info.json")
        self.assertEqual(adventure.name, self.expected_name)
    def test_expected_unit_file(self):
        adventure = Adventure.ImportAdventure("./adventures/CN/adventure_info.json")
        self.assertEqual(adventure.units_file, self.expected_unit_file)
    def test_expected_number_of_camps(self):
        adventure = Adventure.ImportAdventure("./adventures/CN/adventure_info.json")
        self.assertEqual(len(adventure.camps), 2)
        self.assertIsInstance(adventure.camps[0], Adventure.Camp)
    def test_get_camp(self):
        adventure = Adventure.ImportAdventure("./adventures/CN/adventure_info.json")
        camp = adventure.get_camp("1")
        self.assertEqual(camp.name, "1")
    def test_debug(self):
        adventure = Adventure.ImportAdventure("./adventures/CN/adventure_info.json")
        camp = adventure.get_camp("1")
        adventure.debug()

class Test_Camp(unittest.TestCase):
    def setUp(self):
        pass
    def test_import(self):
        c_file = {}
        c_file["name"] = "1" 
        c_file["file"] = "./Adventures/CN/2.json" 
        camp = Adventure.ImportCamp("./adventures/CN/units.json", c_file)
        self.assertEqual(camp.name, "1")
    def test_debug(self):
        c_file = {}
        c_file["name"] = "1" 
        c_file["file"] = "./Adventures/CN/2.json" 
        camp = Adventure.ImportCamp("./adventures/CN/units.json", c_file)
        camp.debug()
    def test_add_unit(self):
        c_file = {}
        c_file["name"] = "1" 
        c_file["file"] = "./Adventures/CN/2.json" 
        camp = Adventure.ImportCamp("./adventures/CN/units.json", c_file)
        unit = Unit.ImportUnit("./adventures/CN/units.json", name="soldat")
        previous_len = len(camp.units)
        camp.add_unit(unit)
        self.assertEqual(len(camp.units), previous_len+1)
        
if __name__ == '__main__':
    unittest.main()
