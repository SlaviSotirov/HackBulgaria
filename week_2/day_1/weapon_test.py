from weapon import Weapon

import unittest


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.wep = Weapon("Durvo", 25, 0.2)

    def test_weapon_init(self):
        self.assertEqual("Durvo", self.wep.type)
        self.assertEqual(25, self.wep.damage)
        self.assertEqual(0.2, self.wep.critical_strike_percent)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            weap = Weapon("Durvo", 50, 1.2)

    def test_critical_strike(self):
        is_false = False
        is_true = False
        for i in range(100):
            if self.wep.critical_hit():
                is_true = True
            else:
                is_false = True
        self.assertTrue(is_true)
        self.assertTrue(is_false)



if __name__ == '__main__':
    unittest.main()
