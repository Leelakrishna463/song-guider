from app.models.song import Song, SongList

def test_song_model_repr():
    song_data = {
        "title": "Title",
        "artist": "Artist",
        "genre": "Acoustic"
    }
    song = Song(**song_data)
    assert repr(song) == "Title by Artist"

def test_songlist_model():
    songs_data = [
        {"title": "Title1", "artist": "Artist1", "genre": "Alternative"},
        {"title": "Title2", "artist": "Artist2", "genre": "Acoustic"}
    ]
    song_list = SongList(songs=[Song(**song_data) for song_data in songs_data])

    assert len(song_list.songs) == 2
    assert isinstance(song_list.songs[0], Song)
    assert isinstance(song_list.songs[1], Song)
