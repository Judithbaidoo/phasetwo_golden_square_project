Copy this into a recipe.md in your project and fill it out.

1. Describe the Problem
Put or write the user story here. Add any clarifying notes you might have.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE
```py

class MusicLibrary:
    # User-facing properties:
    #   tracks: list of instances of Track

    def __init__(self):
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        pass # No code here yet

    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A list of the Track objects that have titles that include the keyword
        pass # No code here yet
#----------------------------------------------------------------------------------------------
    class Track:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self, title, artist):
        # Parameters:
        #   title: string
        #   artist: string
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        pass # No code here yet

3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

""" 
"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]"

"""
4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.