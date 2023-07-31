from lib.music_library import *

def test_create_music_library():
    library_songs = MusicLibrary([])
    result = library_songs.all_songs()
    assert result == []

def test_add_music_library():
    library_songs = MusicLibrary([])
    library_songs.add_track("All I want for christmas")
    result = library_songs.all_songs()
    assert result == ["All I want for christmas"]

def test_error_song():
    library_songs = MusicLibrary([])
    library_songs.add_track(12334) 

def test_allsongs():
    library_songs = MusicLibrary([])
    library_songs.add_track("All I want for christmas")
    assert library_songs.all_songs() == ['All I want for christmas']
    library_songs.add_track("break my stride") 
    assert library_songs.all_songs() == (["All I want for christmas","break my stride"])


