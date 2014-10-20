from orc import Orc

import unittest


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.orc = Orc("Bron", 100, 2)

    def test_orc_init(self):
        self.assertEqual(2, self.orc.berserk_factor)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            badass_orc = Orc("Hanko", 200, 3)


if __name__ == '__main__':
    unittest.main()
