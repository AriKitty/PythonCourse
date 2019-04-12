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


class Album:
    """Class to represent an album, using it's track list

    :param name (str): The name of the album
    :param year (int): The year the album was released
    :param artist (Artist): The artist responsible for the album
        If not specified, the artist will default to an artist with the name
        "Various Artists".
    :param tracks (List[Song]): A list of the songs on the album

    Methods:
        add_song: Used to add a new song to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        self.tracks = []
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

    def add_song(self, song, position=None):
        """Adds a song to the track list

        :param song (Song): A song to add
        :param position (Optional[int]): If specified, the song will be added to that position
            in the track list - inserting it between other songs if necessary.
            Otherwise, the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details

    :param name (Str): The name of the artist
    :param albums (List[Album]): A list of albums by this artist.
        The list includes only those albums in this collection, it is
        not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist's albums list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list

        :param album (Album): Album object to add to the list.
            If the album is already present, it will not be added again (Not yet implemented)
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(f"{artist_field}:{album_field}:{year_field}:{song_field}")

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # New artist
                # Store the current album int he current artists collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # New album
                # Store the current album in the artist's collection then create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # Create a new Song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After reading the last line of the file, there will be an extra album and artist. Processing now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)

    return artist_list


def create_check_file(artist_list):
    """Create a check file from the object data for comparison with the original file"""
    with open ("checkfile.txt", "w") as check_file:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(f"{new_artist.name}\t{new_album.name}\t{new_album.year}\t{new_song.title}", file=check_file)


if __name__ == '__main__':
    artists = load_data()
    print(f"There are {len(artists)} artists")

    create_check_file(artists)
