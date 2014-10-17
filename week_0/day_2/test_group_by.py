import unittest

from group_by import group_by


class TestGroupBy(unittest.TestCase):

    def test_group_by(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        output = {0: [0, 2, 4, 6], 1: [1, 3, 5, 7]}
        self.assertEqual(output, group_by(lambda x: x % 2, arr))

    def test_group_by_v2(self):
        arr = [1, 2, 3, 5, 8, 9, 10, 12]
        output = {'even': [2, 8, 10, 12], 'odd': [1, 3, 5, 9]}
        self.assertEqual(output, group_by(lambda x: 'odd' if x % 2 else 'even', arr))

    def test_group_by_v3(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        output = {0: [0, 3, 6], 1: [1, 4, 7], 2: [2, 5]}
        self.assertEqual(output, group_by(lambda x: x % 3, arr))


if __name__ == '__main__':
    unittest.main()
