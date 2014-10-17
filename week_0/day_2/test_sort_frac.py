import unittest

from sort_frac import *


class TestSortFraction(unittest.TestCase):

    def test_sort_fraction(self):
        lst = [(2, 3), (1, 2)]
        self.assertEqual([(1, 2), (2, 3)], sort_fractions(lst))

    def test_sort_fraction_v2(self):
        lst = [(2, 3), (1, 2), (1, 3)]
        self.assertEqual([(1, 3), (1, 2), (2, 3)], sort_fractions(lst))

    def test_sort_fraction_v3(self):
        lst = [(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]
        res = [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
        self.assertEqual(res, sort_fractions(lst))


if __name__ == '__main__':
    unittest.main()
