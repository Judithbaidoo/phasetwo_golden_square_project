class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self.track = []

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Returns:
        #   Nothing
        self.track.append(track)
    def all(self):
        #Returns:
            #list of all tracks
        return self.track
    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: a string
        # Returns:
        #   a list of Track instances with titles that include the keyword
        for obj1 in self.track :
            if keyword in obj1.title:
                return [obj1.title] 
        return []

