import unittest
from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Title", "Gosho ot pochivka", "Album", 100, 128)

    def test_init(self):
        self.assertEqual(self.song.title, "Title")
        self.assertEqual(self.song.artist, "Gosho ot pochivka")
        self.assertEqual(self.song.length, 100)
        self.assertEqual(self.song.bitrate, 128)

    def test_rate(self):
        self.song.rate(3)
        self.assertEqual(3, self.song.rating)

    def test_invalid_rating(self):
        with self.assertRaises(ValueError):
            self.song.rate(10)


if __name__ == '__main__':
    unittest.main()
