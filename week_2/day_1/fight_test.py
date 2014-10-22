from fight import Fight
from orc import Orc
from hero import Hero

import unittest


class TestFight(unittest.TestCase):

    def setUp(self):
        self.orc = Orc("Bron", 300, 1.3)
        self.hero = Hero("Brom", 300, "DragonSlayer")
        self.fight_sim = Fight(self.hero, self.orc)

    def test_hero_in_fight(self):
        self.assertEqual("Brom", self.fight_sim.hero.name)
        self.assertEqual(300, self.fight_sim.hero.health)
        self.assertEqual("DragonSlayer", self.fight_sim.hero.nickname)

    def test_orc_in_fight(self):
        self.assertEqual("Bron", self.fight_sim.orc.name)
        self.assertEqual(300, self.fight_sim.orc.health)
        self.assertEqual(1.3, self.fight_sim.orc.berserk_factor)


if __name__ == '__main__':
    unittest.main()
