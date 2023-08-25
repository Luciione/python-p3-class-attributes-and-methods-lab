import pytest
from song import Song

class TestSong:

    def test_genres_attribute(self):
        initial_genres = Song.genres.copy()
        song = Song("Test Song", "Test Artist", "Test Genre")
        assert song.genre in Song.genres
        assert Song.genres == initial_genres + [song.genre]

    def test_artists_attribute(self):
        song = Song("Test Song", "Test Artist", "Test Genre")
        assert song.artist in Song.artists

    def test_genre_count_attribute(self):
        initial_genre_count = Song.genre_count.copy()
        song1 = Song("Song 1", "Artist 1", "Genre 1")
        song2 = Song("Song 2", "Artist 2", "Genre 2")
        song3 = Song("Song 3", "Artist 1", "Genre 1")
        assert Song.genre_count == {'Genre 1': 2, 'Genre 2': 1, 'Test Genre': 2}

    def test_artist_count_attribute(self):
        initial_artist_count = Song.artist_count.copy()
        song1 = Song("Song 1", "Artist 1", "Genre 1")
        song2 = Song("Song 2", "Artist 2", "Genre 2")
        song3 = Song("Song 3", "Artist 1", "Genre 1")
        assert Song.artist_count == {'Artist 1': 2, 'Artist 2': 1, 'Test Artist': 2}
