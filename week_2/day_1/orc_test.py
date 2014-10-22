from orc import Orc
from weapon import Weapon

import unittest


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.orc = Orc("Bron", 100, 2)

    def test_orc_init(self):
        self.assertEqual(2, self.orc.berserk_factor)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            badass_orc = Orc("Hanko", 200, 3)

    def test_orc_attack(self):
        wep = Weapon("Durvo", 50, 0)
        drug_orc = Orc("Drug orc", 50, 1.7)
        drug_orc.equip_weapon(wep)
        self.assertEqual((1.7 * 50), drug_orc.attack())


if __name__ == '__main__':
    unittest.main()
