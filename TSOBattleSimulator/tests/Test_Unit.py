import unittest
import Unit
class Test_Unit(unittest.TestCase):
    def setUp(self):
        self.file_path = "./Adventures/CN/units.json"
        self.name = "soldat"
        self.abbrev = "S"
        self.expected_damage_single = [20, 40]
        self.expected_hp = 90
        self.expected_accuracy = 65
        self.expected_strike_order = 2
        self.expected_targetweakest = False
        self.expected_splash_damage = False
        self.expected_target_order = 3
    def test_import_with_name(self):
        unit = Unit.ImportUnit(self.file_path, name=self.name)
        self.assertEqual(unit.name, self.name)
        self.assertEqual(unit.abbrev, self.abbrev)

    def test_import_with_abbrev(self):
        unit = Unit.ImportUnit(self.file_path, abbrev=self.abbrev)
        self.assertEqual(unit.name, self.name)
        self.assertEqual(unit.abbrev, self.abbrev)

    def test_import_with_abbrev_fail(self):
        unit = Unit.ImportUnit(self.file_path, abbrev="aaa")
        self.assertNotIsInstance(unit, Unit.Unit)
    def test_import_with_both(self):
        unit = Unit.ImportUnit(self.file_path, abbrev="aaa", name="ll")
        self.assertNotIsInstance(unit, Unit.Unit)
    def test_import_with_none(self):
        unit = Unit.ImportUnit(self.file_path)
        self.assertNotIsInstance(unit, Unit.Unit)

    def test_damage_single(self):
        unit = Unit.ImportUnit(self.file_path, name=self.abbrev)
        damage = unit.get_damage(single=True)
        print("Damage : " + str(damage))
        self.assertIn(damage, self.expected_damage_single)

    def test_damage_multi(self):
        unit = Unit.ImportUnit(self.file_path, name=self.abbrev)
        expected = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
        unit.set_amount(5)
        damage = unit.get_damage(total=True)
        print("Damage : " + str(damage))
        self.assertIn(damage, expected)

    def test_damage_single_repeat(self):
        unit = Unit.ImportUnit(self.file_path, name=self.abbrev)
        for i in range(0, 1000):
            damage = unit.get_damage(single=True)
            print("Damage : " + str(damage))
            self.assertIn(damage, self.expected_damage_single)

    def test_damage_multi_repeat(self):
        unit = Unit.ImportUnit(self.file_path, name=self.abbrev)
        expected = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
        unit.set_amount(5)
        for i in range(0,1000):
            damage = unit.get_damage(total=True)
            print("Damage : " + str(damage))
            self.assertIn(damage, expected)
    def test_import_correct_hp(self):
        unit = Unit.ImportUnit(self.file_path, name=self.name)
        self.assertEqual(unit.get_hp(), self.expected_hp)
    def test_import_correct_accuracy(self):
        unit = Unit.ImportUnit(self.file_path, name=self.name)
        self.assertEqual(unit.accuracy, self.expected_accuracy)
    def test_import_correct_strike_order(self):
        unit = Unit.ImportUnit(self.file_path, name=self.name)
        self.assertEqual(unit.strike_order, self.expected_strike_order)
    def test_import_correct_splashdamage(self):
        unit = Unit.ImportUnit(self.file_path, name=self.name)
        self.assertEqual(unit.get_splashdamage(), self.expected_splash_damage)
    def test_import_correct_target_order(self):
        unit = Unit.ImportUnit(self.file_path, name=self.name)
        self.assertEqual(unit.targetorder, self.expected_target_order)
    def test_set_amount(self):
        unit = Unit.ImportUnit(self.file_path, name=self.name)
        initial = unit.get_amount()
        unit.set_amount(initial + 5)
        self.assertEqual(initial + 5, unit.get_amount())
    def test_debug(self):
        unit = Unit.ImportUnit(self.file_path, name=self.name)
        unit.debug()

if __name__ == '__main__':
    unittest.main()
