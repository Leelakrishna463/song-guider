from fastapi import APIRouter, HTTPException, status
from app.models import Mood, SongList
from app.service.songs.utils import recommend_songs_paginated
from app.service.external.open_weather.utils import OpenWeatherAPI
from app.logger import logger

router = APIRouter()


@router.get("/recommend/", response_model=SongList, response_model_exclude_none=True)
def recommend(user_mood: str, city_name: str, page_size: int, page: int) -> SongList:
    """
    Recommend songs based on the user's mood and the weather of a specified city.

    Args:
        user_mood (str): The mood of the user.
        city_name (str): The name of the city to get the weather information from.
        page_size (int): The count of songs to recommend
        page (int): The page number from where the songs should be listed

    Returns:
        SongList: A list of recommended songs tailored to the user's mood and current weather conditions.
    """
    logger.info("Received request for song recommendation")
    logger.debug(f"user_mood: {user_mood}, city_name: {city_name}")

    try:
        weather = OpenWeatherAPI.get_weather_from_city(city_name)
        logger.info(f"Weather data fetched for city: {city_name}")
    except Exception as e:
        logger.error(f"Error fetching weather data for city {city_name}: {e}")
        raise HTTPException(status_code=500, detail="Error fetching weather data")

    try:
        mood = Mood.model_validate({"title": user_mood})
        logger.info(f"Mood validated: {user_mood}")
    except Exception as e:
        logger.error(f"Error validating mood: {user_mood}: {e}")
        raise HTTPException(status_code=400, detail="Invalid mood provided")

    try:
        recommended_songs = recommend_songs_paginated(mood, weather, page_size, page)
        logger.info(f"Songs recommended successfully")
        return recommended_songs
    except IndexError:
        raise HTTPException(status_code=416, detail="Page size is out of range. Please reduce page value")
    except Exception as e:
        logger.error(f"Error recommending songs: {e}")
        raise HTTPException(status_code=500, detail="Error recommending songs")