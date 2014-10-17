import unittest

from spam_eggs import prepare_meal


class TestSpamAndEggs(unittest.TestCase):

    def test_eggs(self):
        self.assertEqual("eggs", prepare_meal(5))

    def test_spam(self):
        self.assertEqual("spam", prepare_meal(3))

    def test_more_spam(self):
        self.assertEqual("spam spam spam", prepare_meal(27))

    def test_spam_and_eggs(self):
        self.assertEqual("spam and eggs", prepare_meal(15))

    def test_more_spam_and_eggs(self):
        self.assertEqual("spam spam and eggs", prepare_meal(45))

    def test_no_meal(self):
        self.assertEqual("", prepare_meal(7))


if __name__ == '__main__':
    unittest.main()
