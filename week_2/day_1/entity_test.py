import unittest

from entity import Entity

from weapon import Weapon


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.test_entity = Entity("Bron", 100)

    def test_entity_init(self):
        self.assertEqual("Bron", self.test_entity.name)
        self.assertEqual(100, self.test_entity.health)

    def test_get_health(self):
        self.assertEqual(100, self.test_entity.get_health())

    def test_is_alive(self):
        self.assertTrue(self.test_entity.is_alive())

    def test_is_dead(self):
        self.test_entity.health = 0
        self.assertFalse(self.test_entity.is_alive())

    def test_take_dmg_still_alive(self):
        self.test_entity.take_damage(30)
        self.assertEqual(70, self.test_entity.get_health())

    def test_take_dmg_until_zero_health(self):
        self.test_entity.take_damage(100)
        self.assertEqual(0, self.test_entity.get_health())
        self.assertFalse(self.test_entity.is_alive())

    def test_take_dmg_more_than_health(self):
        self.test_entity.take_damage(200)
        self.assertEqual(0, self.test_entity.get_health())
        self.assertFalse(self.test_entity.is_alive())

    def test_take_healing(self):
        self.test_entity.take_damage(50)
        self.test_entity.take_healing(20)
        self.assertEqual(70, self.test_entity.get_health())

    def test_healing_dead_hero(self):
        self.test_entity.take_damage(100)
        self.assertFalse(self.test_entity.take_healing(50))
        self.assertEqual(0, self.test_entity.get_health())

    def test_over_healing_not_allowed(self):
        self.test_entity.take_damage(30)
        self.assertTrue(self.test_entity.take_healing(50))
        self.assertEqual(self.test_entity.get_health(), 100)

    def test_equip_weapon(self):
        wep = Weapon("Durvo", 50, 0.5)
        self.test_entity.equip_weapon(wep)
        self.assertTrue(self.test_entity.has_weapon())

    def test_attack_with_no_weapon(self):
        self.assertEqual(self.test_entity.attack(), 0)

    def test_attack(self):
        wep = Weapon("Durvo", 50, 0)
        self.test_entity.equip_weapon(wep)
        self.assertEqual(self.test_entity.attack(), 50)

    def test_attack_crit(self):
        wep = Weapon("Durvo", 50, 0.9)
        self.test_entity.equip_weapon(wep)
        dmg_taken = []
        for i in range(100):
            dmg_taken.append(self.test_entity.attack())
        self.assertIn(50, dmg_taken)
        self.assertIn(100, dmg_taken)

if __name__ == '__main__':
    unittest.main()
