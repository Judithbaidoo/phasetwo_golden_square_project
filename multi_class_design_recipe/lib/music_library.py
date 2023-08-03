class MusicLibrary():
    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)
    def search_by_title(self,title):
        outcome = [ x for x in self.tracks if title in x ]
        return outcome