from lib.music_library import *

def test_create_library():
    libraryshelf = MusicLibrary()
    libraryshelf.add("Song1")
    expected = ["Song1"]
    result = libraryshelf.tracks
    assert result == expected

def test_search_by_title():
    libraryshelf = MusicLibrary()
    libraryshelf.add("happy days")
    libraryshelf.add("bad romance")
    search = libraryshelf.search_by_title("ys")
    expected = ["happy days"]
    assert search == expected
    search = libraryshelf.search_by_title("romance")
    expected = ["bad romance"]
    assert search == expected
