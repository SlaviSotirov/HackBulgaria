import unittest

from count_words import count_words


class TestCountWords(unittest.TestCase):

    def test_count_words(self):
        input = ["apple", "banana", "apple", "pie"]
        output = {'apple': 2, 'pie': 1, 'banana': 1}
        self.assertEqual(output, count_words(input))

    def test_count_words_v2(self):
        input = ["python", "python", "python", "ruby"]
        output = {'ruby': 1, 'python': 3}
        self.assertEqual(output, count_words(input))


if __name__ == '__main__':
    unittest.main()
