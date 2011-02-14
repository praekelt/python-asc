import re
from urllib import urlopen

class Parser(object):
    tracks = []
    
    def __init__(self, url):
        self.url = url
        self.parse()

    def parse(self):
        data = urlopen(self.url).read()
        data = data.split('\n')

        for line in data:
            match = re.match("(.{8})(.{8})(.{7})(.{51})(.{102})(.{8})", line)
            if match:
                if match.group(3).startswith('Song'):
                    self.tracks.append(Track(title=match.group(5), artist=match.group(4), status=match.group(2), length=match.group(6)))

    def now_playing(self):
        for track in self.tracks:
            if track.status.startswith('Playing'):
                return track

class Track(object):
    def __init__(self, title, artist, status, length):
        self.title = title
        self.artist = artist
        self.status = status
        self.length = length

