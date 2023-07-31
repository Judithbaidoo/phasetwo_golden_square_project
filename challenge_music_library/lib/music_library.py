# design a music library where you can add music and see a list of the tracks listened to

class MusicLibrary():
    def __init__(self,library):
        #creates empty library which we can access to make changes
        #Paramenters:
        #library : array
        #returns : nothing
        self.library = library
    def add_track(self,song):
        #Task : adds a song to music library
        #song : string 
        #returns nothing
        #side-effects : is no song is added return "Please add a song" or if type is wrong return "please enter a string"
        try:
            if type(song) == str:
                self.library.append(song)
        except:
            raise Exception("please enter a string")
    def all_songs(self):
        #returns a list of all the songs 
        #Parameters : none
        #returns list of music
        return self.library

#EXAMPLES

#1. creates empty array
# library = MusicLibrary([])
# library.all_songs() => []

#2. given a song, it adds it to the library
# library = MusicLibrary([])
#library.add_track("merry christmas")
# library == ["merry chritmas"]
#library.add_track("break my stride")
# library == ["merry chritmas", "break my stride"]

#3.if no songs are added, returns a message 
# library = MusicLibrary([])
#library.add_track() => "Please add a song"

#4 if wrong type is added give error message "Please enter string type music"
# library = MusicLibrary([])
#library.add_track(123) => "Please enter string type music"

#5 returns list of all the songs
# library = MusicLibrary([])
# library.all_songs() => ["merry chritmas", "break my stride"]


