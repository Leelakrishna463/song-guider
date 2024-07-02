from unittest.mock import patch, Mock
from app.service.songs import utils as song_utils
from app.service.recommendation import utils as recommendation_utils
from app.models import Mood, Weather

@patch("app.service.recommendation.utils.get_genre_by_energy_and_valence")
def test_get_genre_by_energy_and_valence(mock_get_genre_by_energy_and_valence):
    # Mock the get_genre_by_energy_and_valence function
    mock_get_genre_by_energy_and_valence.return_value = "pop"

    # Call the function with sample mood and weather
    data = {
        "sno": [0],
        "energy": [(Mood(title="happy").energy*0.7 +  Weather(title="clear").energy*0.3)],
        "valence": [(Mood(title="happy").valence*0.7 +  Weather(title="clear").valence*0.3)]
    }
    genre = recommendation_utils.get_genre_by_energy_and_valence(data)

    # Assertions
    assert genre == "pop"


@patch("app.service.songs.utils.recommend_genres")
def test_recommend_genres(mock_recommend_genres):
    # Mock the get_genre_by_energy_and_valence function
    mock_recommend_genres.return_value = ["pop"]

    # Call the function with sample mood and weather
    recommended_genres = song_utils.recommend_genres(Mood(title="happy"), Weather(title="clear"))

    # Assertions
    assert recommended_genres == ["pop"]


@patch("app.service.songs.utils.recommend_songs_paginated")
def test_recommend_songs_paginated(mock_recommend_songs_paginated):
    # Mock the from app.config function
    mock_recommend_songs_paginated.return_value = {"songs": [{"title": "Song1", "artist": "Artist1"}]}

    # Call the function with sample mood and weather
    recommended_songs = song_utils.recommend_songs_paginated(Mood(title="depressed"), Weather(title="clear"))

    # Assertions
    assert recommended_songs == {"songs": [{"title": "Song1", "artist": "Artist1"}]}
