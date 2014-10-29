from playlist import Playlist
from song import Song
from mutagen.mp3 import MP3

import os


class MusicCrawler:
    ARTIST = "TPE1"
    TITLE = "TIT2"
    ALBUM = "TALB"

    def __init__(self, music_dir):
        self.music_dir = music_dir

    def generate_playlist(self, name):
        files = os.listdir(self.music_dir)
        pl = Playlist(name)
        for f in files:
            if ".mp3" in f:
                music_file = MP3(self.music_dir+"/"+f)
                title = music_file.tags[self.TITLE][0]
                artist = music_file.tags[self.ARTIST][0]
                bitrate = music_file.info.bitrate
                length = music_file.info.length
                album = music_file.tags[self.ALBUM][0]
                temp_song = Song(title, artist, album, length, bitrate)
                pl.add_song(temp_song)

        return pl
