import unittest

from simp_frac import simplify_fraction


class TestSimplifyFraction(unittest.TestCase):

    def test_simplify_fraction(self):
        self.assertEqual((1, 3), simplify_fraction((3, 9)))

    def test_simplify_fraction_v2(self):
        self.assertEqual((1, 7), simplify_fraction((1, 7)))

    def test_simplify_fraction_v3(self):
        self.assertEqual((2, 5), simplify_fraction((4, 10)))

    def test_simplify_fraction_v4(self):
        self.assertEqual((3, 22), simplify_fraction((63, 462)))


if __name__ == '__main__':
    unittest.main()
