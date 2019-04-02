class Song:
    """Class to represent a song

    :param title (str): The title of the song
    :param artist (Artist): An artist object representing the song's creator
    :param duration (int): The duration of the song in seconds. May be 0
    """

    def __init__(self, title, artist, duration=0):
        """Song init method

        :param title (str): Initialize the title attribute
        :param artist (Artist): An Artist object representing the song's creator
        :param duration (Optional[int]): Initial value for the 'duration' attribute.
            Will default to 0;
        """
        self.title = title
        self.artist = artist
        self.duration = duration
