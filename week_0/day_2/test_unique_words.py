import unittest

from unique_words import unique_words_count


class TestUniqueWordsCount(unittest.TestCase):

    def test_unique_words_count(self):
        input = ["apple", "banana", "apple", "pie"]
        self.assertEqual(3, unique_words_count(input))

    def test_unique_words_count_v2(self):
        input = ["python", "python", "python", "ruby"]
        self.assertEqual(2, unique_words_count(input))

    def test_unique_words_count_v3(self):
        input = ["HELLO!"] * 10
        self.assertEqual(1, unique_words_count(input))


if __name__ == '__main__':
    unittest.main()
