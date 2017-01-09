import unittest
import Battle
import Unit
class Test_Battle(unittest.TestCase):
    pass
class Test_Side_simple(unittest.TestCase):
    def setUp(self):
        self.Side = Battle.Side()
        self.file_path = "./Adventures/CN/units.json"
        self.name = "soldat"
        self.abbrev = "S"

    def test_create(self):
        self.assertIsInstance(self.Side, Battle.Side)
    def test_has_lost_true(self):
        unit = Unit.ImportUnit(self.file_path, abbrev=self.abbrev, amount=0)
        self.Side.add_unit(unit)
        self.assertTrue(self.Side.has_lost())
    def test_has_lost_false(self):
        unit = Unit.ImportUnit(self.file_path, abbrev=self.abbrev, amount=200)
        self.Side.add_unit(unit)
        self.assertTrue(self.Side.has_lost())
    def test_add_unit(self):
        unit = Unit.ImportUnit(self.file_path, abbrev=self.abbrev, amount=200)
        self.Side.add_unit(unit)
        self.Side.add_unit(unit)
        self.assertEqual(len(self.Side.units), 2)
    def test_add_units(self):
        unit = Unit.ImportUnit(self.file_path, abbrev=self.abbrev, amount=200)
        units = []
        units.append(unit)
        units.append(unit)
        self.Side.add_units(units)
        self.assertEqual(len(self.Side.units), 2)
    def test_get_unit(self):
        unit = Unit.ImportUnit(self.file_path, abbrev=self.abbrev, amount=200)
        units = []
        units.append(unit)
        self.Side.add_units(units)
        self.assertIsInstance(self.Side.get_unit(), Unit.Unit)
    def test_get_unit_with_name(self):
        unit = Unit.ImportUnit(self.file_path, abbrev=self.abbrev, amount=200)
        units = []
        units.append(unit)
        self.Side.add_units(units)
        self.assertEqual(self.Side.get_unit_with_name("soldat").name, "soldat")
    def test_get_unit_with_abbrev(self):
        unit = Unit.ImportUnit(self.file_path, abbrev=self.abbrev, amount=200)
        units = []
        units.append(unit)
        self.Side.add_units(units)
        self.assertEqual(self.Side.get_unit_with_abbrev("S").name, "soldat")
    def test_get_weakest_unit(self):
        unit = Unit.ImportUnit(self.file_path, abbrev=self.abbrev, amount=200)
        units = []
        units.append(unit)
        self.Side.add_units(units)
        self.assertIsInstance(self.Side.get_unit(weakest=True), Unit.Unit)

class Test_Side_complex(unittest.TestCase):
    def setUp(self):
        self.Side = Battle.Side()
        self.file_path = "./Adventures/CN/units.json"
        self.unit_cav = Unit.ImportUnit(self.file_path, abbrev="Cava", amount=100)
        self.unit_sol = Unit.ImportUnit(self.file_path, abbrev="S", amount=100)
        self.unit_arc = Unit.ImportUnit(self.file_path, abbrev="Arc", amount=100)
        self.Side.add_unit(self.unit_arc)
        self.Side.add_unit(self.unit_sol)
        self.Side.add_unit(self.unit_cav)

    def test_get_weakest_unit(self):
        returned_u = self.Side.get_unit(weakest=True)
        self.assertEqual(returned_u.abbrev, "Cava")
    def test_get_weakest_unit_2(self):
        self.Side.get_unit_with_abbrev("Cava").set_amount(0)
        returned_u = self.Side.get_unit(weakest=True)
        self.assertEqual(returned_u.abbrev, "Arc")
    def test_get_next_unit(self):
        returned_u = self.Side.get_unit()
        self.assertEqual(returned_u.abbrev, "Cava")
    def test_get_next_unit_2(self):
        self.Side.get_unit_with_abbrev("Cava").set_amount(0)
        returned_u = self.Side.get_unit()
        self.assertEqual(returned_u.abbrev, "S")
    def test_get_next_unit_3(self):
        self.Side.get_unit_with_abbrev("Cava").set_amount(0)
        self.Side.get_unit_with_abbrev("S").set_amount(0)
        returned_u = self.Side.get_unit()
        self.assertEqual(returned_u.abbrev, "Arc")

if __name__ == '__main__':
    unittest.main()
