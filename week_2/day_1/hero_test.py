from hero import Hero

import unittest


class TestHero(unittest.TestCase):

    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual("DragonSlayer", self.bron_hero.nickname)

    def test_known_as(self):
        self.assertEqual("Bron The DragonSlayer", self.bron_hero.known_as())


if __name__ == '__main__':
    unittest.main()
