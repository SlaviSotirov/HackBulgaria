from playlist import Playlist
from song import Song
import unittest


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.my_playlist = Playlist("Qki pesni 2011")
        self.song = Song("Title", "Gosho ot pochivka", "Album", 100, 128)
        self.song1 = Song("Title2", "Gosho ot pochivka2", "Album", 200, 256)
        self.song2 = Song("Title3", "Gosho ot pochivka2", "Album", 200, 128)

    def test_init(self):
        self.assertEqual("Qki pesni 2011", self.my_playlist.name)

    def test_add_song(self):
        self.my_playlist.add_song(self.song)
        self.assertIn(self.song, self.my_playlist.playlist)

    def test_remove_song(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.remove_song("Title")
        self.assertNotIn(self.song, self.my_playlist.playlist)

    def test_total_length(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song1)
        self.assertEqual(300, self.my_playlist.total_length())

    def test_remove_disrated(self):
        self.song.rate(2)
        self.my_playlist.add_song(self.song)
        self.song1.rate(4)
        self.my_playlist.add_song(self.song1)
        self.song2.rate(3)
        self.my_playlist.add_song(self.song2)
        self.my_playlist.remove_disrated(3)
        self.assertNotIn(self.song, self.my_playlist.playlist)
        self.assertNotIn(self.song2, self.my_playlist.playlist)

    def test_remove_bad_quality(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song1)
        self.my_playlist.remove_bad_quality()
        self.assertNotIn(self.song, self.my_playlist.playlist)

    def test_show_artists(self):
        self.my_playlist.add_song(self.song)
        self.my_playlist.add_song(self.song1)
        song2 = Song("Title5", "Gosho ot pochivka", "Album", 100, 128)
        self.my_playlist.add_song(song2)
        artists = ["Gosho ot pochivka", "Gosho ot pochivka2"]
        self.assertEqual(artists, self.my_playlist.show_artists())

if __name__ == '__main__':
    unittest.main()
