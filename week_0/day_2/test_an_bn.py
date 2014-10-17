import unittest

from an_bn import is_an_bn


class TestAnBn(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(is_an_bn(""))

    def test_an_bn(self):
        self.assertTrue(is_an_bn("aaabbb"))

    def test_an_bn_v2(self):
        self.assertTrue(is_an_bn("aaaaabbbbb"))

    def test_not_an_bn(self):
        self.assertFalse(is_an_bn("rado"))

    def test_close_to_an_bn(self):
        self.assertFalse(is_an_bn("aaabb"))

    def test_close_to_an_bn_v2(self):
        self.assertFalse(is_an_bn("aabbaabb"))

    def test_close_to_an_bn_v3(self):
        self.assertFalse(is_an_bn("bbbaaa"))


if __name__ == '__main__':
    unittest.main()
