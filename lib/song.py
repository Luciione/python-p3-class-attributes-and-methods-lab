class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.__class__.count += 1
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_to_genres(self):
        if self.genre not in self.genres:
            self.genres.append(self.genre)

    def add_to_artists(self):
        if self.artist not in self.artists:
            self.artists.append(self.artist)

    def add_to_genre_count(self):
        if self.genre not in self.genre_count:
            self.genre_count[self.genre] = 0
        self.genre_count[self.genre] += 1

    def add_to_artist_count(self):
        if self.artist not in self.artist_count:
            self.artist_count[self.artist] = 0
        self.artist_count[self.artist] += 1
