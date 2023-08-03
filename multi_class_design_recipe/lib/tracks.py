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
        self.title = title
        self.artist = artist

    def format(self):
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        return f"{self.title} by {self.artist}"