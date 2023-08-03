from lib.tracks import *

def test_track_songs():
    songs = Track("Title1","Artist1")
    assert songs.title == "Title1"
    assert songs.artist == "Artist1"
def test_title_by_artist():
    songs = Track("Title1","Artist1")
    result = songs.format()
    assert result == "Title1 by Artist1"
    
