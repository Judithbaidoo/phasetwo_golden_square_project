from lib.music_library import *
from lib.tracks import *
def test_library_tracks():
    library = MusicLibrary()
    song1 = Track("lovely day","Bill Withers")
    song2 = Track("all I want for christmas","Mariah Carey")
    library.add(song1)
    library.add(song2)
    assert library.tracks == [song1,song2]