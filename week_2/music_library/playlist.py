import json
from song import Song


def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    return '%02d:%02d' % (mins, secs)


def load(filename):
        read_file = open(filename, "r")
        temp = json.load(read_file)
        playlist = Playlist(temp['name'])
        for song in temp["songs"]:
            title = song["title"]
            artist = song["artist"]
            bitrate = song["bitrate"]
            rate = song["rating"]
            album = song["album"]
            length = song["length"]
            temp_song = Song(title, artist, album, length, bitrate)
            if rate is not None:
                temp_song.rate(rate)
            playlist.add_song(temp_song)

        return playlist


class Playlist:
    BAD_QUALITY_BITRATE = 128

    def __init__(self, name):
        self.name = name
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song_name):
        for s in self.playlist:
            if s.title == song_name:
                self.playlist.remove(s)

    def total_length(self):
        total = 0
        for song in self.playlist:
            total += song.length
        return total

    def remove_disrated(self, rating):
        for song in self.playlist:
            if song.rating <= rating:
                self.playlist.remove(song)

    def remove_bad_quality(self):
        for song in self.playlist:
            if song.bitrate <= self.BAD_QUALITY_BITRATE:
                self.playlist.remove(song)

    def show_artists(self):
        artists = []
        for song in self.playlist:
            if song.artist not in artists:
                artists.append(song.artist)

        return artists

    def __str__(self):
        result = ""
        for song in self.playlist:
            result += "{} {} - {}\n".format(song.artist, song.title, humanize_time(song.length))

        return result

    def save(self):
        songs = []
        for song in self.playlist:
            songs.append(song.__dict__)

        with open("test", "w") as file:
            json.dump({"name": self.name, "songs": songs}, file)
            file.close()
