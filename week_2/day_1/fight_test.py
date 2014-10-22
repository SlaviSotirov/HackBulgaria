from fight import Fight
from orc import Orc
from hero import Hero
from weapon import Weapon

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

    def test_flip_coin(self):
        coins = []
        for i in range(100):
            coins.append(self.fight_sim._flip_coin())
        self.assertIn(self.fight_sim._HERO_TURN, coins)
        self.assertIn(self.fight_sim._ORC_TURN, coins)

    def test_simulate_fight_orc_win(self):
        orc_w = Orc("Winner", 300, 2)
        hero_l = Hero("Loser", 300, "TheLoser")
        wep = Weapon("Ubiec", 15, 0.5)
        orc_w.equip_weapon(wep)
        orc_fight = Fight(hero_l, orc_w)
        self.assertEqual(orc_fight.simulate_fight(), orc_fight._ORC_WINNER)

    def test_simulate_fight_hero_win(self):
        orc_l = Orc("Loser", 300, 2)
        hero_w = Hero("Winner", 300, "TheWinner")
        wep = Weapon("Ubiec", 15, 0.5)
        hero_w.equip_weapon(wep)
        hero_fight = Fight(hero_w, orc_l)
        self.assertEqual(hero_fight.simulate_fight(), hero_fight._HERO_WINNER)


if __name__ == '__main__':
    unittest.main()
