import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):

    def test_init(self):
        a = Fraction(1, 2)
        self.assertEqual(a.nominator, 1)
        self.assertEqual(a.denominator, 2)

    def test_is_euqal(self):
        a = Fraction(1, 2)
        b = Fraction(2, 4)
        self.assertTrue(a == b)

    def test_is_not_equal(self):
        a = Fraction(3, 5)
        b = Fraction(13, 12)
        self.assertFalse(a == b)

    def test_is_greater_than(self):
        a = Fraction(1, 2)
        b = Fraction(1, 10)
        self. assertTrue(a > b)

    def test_is_less_than(self):
        a = Fraction(1, 2)
        b = Fraction(1, 10)
        self. assertTrue(b < a)

    def test_simplify(self):
        a = Fraction(5, 10)
        self.assertEqual(a.nominator, 1)
        self.assertEqual(a.denominator, 2)

    def test_cant_simplify(self):
        a = Fraction(7, 23)
        a.simplify()
        self.assertEqual(a.nominator, 7)
        self.assertEqual(a.denominator, 23)

    def test_add_fractions(self):
        a = Fraction(1, 2)
        b = Fraction(1, 2)
        a = a + b
        self.assertEqual(a.nominator, 1)
        self.assertEqual(a.denominator, 1)

    def test_add_harder_fraction(self):
        a = Fraction(1, 10)
        b = Fraction(2, 17)
        a = a + b
        self.assertEqual(a.nominator, 37)
        self.assertEqual(a.denominator, 170)

    def test_sub_fraction(self):
        a = Fraction(5, 10)
        b = Fraction(1, 5)
        a = a - b
        self.assertEqual(a.nominator, 3)
        self.assertEqual(a.denominator, 10)

if __name__ == '__main__':
    unittest.main()
