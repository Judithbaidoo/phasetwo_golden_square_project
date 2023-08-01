from lib.music_library import MusicLibrary
from lib.track import Track
"""
When we add two tracks
We get the tracks back in the track list
"""
def test_add_stracks():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.all() == [track_1,track_2] 
    assert library.all()[0].title == "Always The Hard Way"
    assert library.all()[1].title == "Higher Place"
    # => [track_1, track_2]

"""
When we add two tracks
And we search for a word in the title
We get the matching track back
"""
def test_search_word():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_2)
    library.add(track_1)
    assert library.search_by_title("Way") == ["Always The Hard Way"] # => [track_1]

"""
When we add two tracks
And we search for a small part of a word in the title
We get the matching track back
"""
def test_sub_string():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    result =  library.search_by_title("lace") 
    assert result == ["Higher Place"] 
    # => [track_2]

"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""
def test_non_existing_names():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    result = library.search_by_title("zzz") # => []
    assert result == []

"""
Given a track with a title and artist
#format returns a string like TITLE by ARTIST
"""
def test_title_artist():
    track = Track("Higher Place", "Malevolence")
    result = track.format()
    assert result ==  "Higher Place by Malevolence"