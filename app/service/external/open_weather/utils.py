from app.models import Weather
from app.config import settings
import requests
from app.logger import logger




class OpenWeatherAPI:
    """
    A class to interact with the OpenWeather API to fetch weather data.

    Attributes:
        API_BASE (str): The base URL for the OpenWeather API.
    """
    API_BASE = settings.OPEN_WEATHER_API_BASE
    API_KEY = settings.OPEN_WEATHER_API_KEY

    @staticmethod
    def get_weather_from_city(city_name: str) -> Weather:
        """
        Get the current weather for a given city.

        Args:
            city_name (str): The name of the city to get the weather for.

        Returns:
            Weather: An instance of the Weather model with the fetched data.

        Raises:
            Exception: If unable to get weather data from OpenWeather.
        """
        api_url = f"{OpenWeatherAPI.API_BASE}/weather?q={city_name}&appid={OpenWeatherAPI.API_KEY}&units=metric"
        logger.info(f"Fetching weather data for city: {city_name}")
        logger.debug(f"API URL: {api_url}")

        try:
            response = requests.get(api_url)
            data = response.json()

            if response.status_code == 200:
                logger.info(f"Weather data fetched successfully for city: {city_name}")
                weather_data = {
                    "title": data['weather'][0]['main'].lower()
                }
                logger.debug(f"Weather data: {weather_data}")
                return Weather.model_validate(weather_data)
            else:
                error_message = f"Failed to get weather data for city: {city_name}, status code: {response.status_code}, response: {data}"
                logger.error(error_message)
                raise Exception("Unable to get weather from OpenWeather")
        except requests.RequestException as ex:
            logger.error(f"RequestException occurred: {ex}")
            raise Exception("Unable to get weather from OpenWeather")
