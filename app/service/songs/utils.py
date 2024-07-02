from app.models import Weather, Mood, Song
from app.service.external.lastfm.utils import LastFMAPI
from app.service.recommendation.utils import get_genre_by_energy_and_valence
from app.logger import logger




def recommend_genres(mood: Mood, weather: Weather) -> list[str]:
    """
    Recommends genres based on the given mood and weather.

    Args:
        mood (Mood): The mood object.
        weather (Weather): The weather object.

    Returns:
        list[str]: A list of recommended genres.
    """
    logger.info("Recommending genres based on mood and weather")
    logger.debug(f"Mood: {mood}, Weather: {weather}")

    # Find K closest genres
    try:
        data = {
            "sno": [0],
            "energy": [(mood.energy * 0.7 + weather.energy * 0.3)],
            "valence": [(mood.valence * 0.7 + weather.valence * 0.3)]
        }
        logger.debug(f"Data for genre recommendation: {data}")
        genre = get_genre_by_energy_and_valence(data)
        logger.info(f"Recommended genre: {genre}")
        return [genre]
    except Exception as e:
        logger.error(f"Error recommending genres: {e}")
        return []

def recommend_songs_paginated(mood: Mood, weather: Weather, page_size: int, page: int) -> Song:
    """
    Recommends songs based on the given mood and weather.

    Args:
        mood (Mood): The mood object.
        weather (Weather): The weather object.
        page_size (int): The number of songs to recommend
        page (int): The page number from where the song listing to start

    Returns:
        Song: A dictionary containing recommended songs.
    """
    logger.info("Recommending songs based on mood and weather")
    logger.debug(f"Mood: {mood}, Weather: {weather}")

    try:
        recommended_song_genres = recommend_genres(mood, weather)
        logger.debug(f"Recommended genres: {recommended_song_genres}")
        tracks = LastFMAPI.get_tracks_for_genres_paginated(recommended_song_genres, page_size, page)
        logger.info("Songs recommended successfully")
        return {"songs": tracks}
    except IndexError as ie:
        raise IndexError(ie)
    except Exception as e:
        logger.error(f"Error recommending songs: {e}")
        return {"songs": []}