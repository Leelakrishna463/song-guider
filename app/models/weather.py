from enum import Enum
from typing import Optional, ClassVar, Dict
from pydantic import BaseModel
from .mood import Mood

class WeatherTitleEnum(str, Enum):
    """
    Enumeration of possible weather titles.
    """
    Thunderstorm = 'thunderstorm'
    Drizzle = 'drizzle'
    Rain = 'rain'
    Snow = 'snow'
    Mist = 'mist'
    Smoke = 'smoke'
    Haze = 'haze'
    Dust = 'sand'
    Fog = 'fog'
    Sand = 'sand'
    Ash = 'volcanic ash'
    Squall = 'squalls'
    Tornado = 'tornado'
    Clear = 'clear'
    Clouds = 'clouds'

class Weather(BaseModel):
    """
    A model representing weather with associated energy and valence values.

    Attributes:
        title (WeatherTitleEnum): The title of the weather.
    """
    weather_energy_valence: ClassVar[Dict[WeatherTitleEnum, Dict[str, float]]] = {
        WeatherTitleEnum.Thunderstorm: {"energy": 0.75, "valence": 0.1},
        WeatherTitleEnum.Drizzle: {"energy": 0.4, "valence": 0.4},
        WeatherTitleEnum.Rain: {"energy": 0.2, "valence": 0.2},
        WeatherTitleEnum.Snow: {"energy": 0, "valence": 0.5},
        WeatherTitleEnum.Mist: {"energy": 0.3, "valence": 0.35},
        WeatherTitleEnum.Smoke: {"energy": 0.3, "valence": 0.35},
        WeatherTitleEnum.Haze: {"energy": 0.3, "valence": 0.35},
        WeatherTitleEnum.Dust: {"energy": 0.3, "valence": 0.35},
        WeatherTitleEnum.Fog: {"energy": 0.3, "valence": 0.35},
        WeatherTitleEnum.Sand: {"energy": 0.3, "valence": 0.35},
        WeatherTitleEnum.Ash: {"energy": 0.3, "valence": 0.35},
        WeatherTitleEnum.Squall: {"energy": 0.3, "valence": 0.35},
        WeatherTitleEnum.Tornado: {"energy": 0.3, "valence": 0.35},
        WeatherTitleEnum.Clear: {"energy": 1.0, "valence": 1.0},
        WeatherTitleEnum.Clouds: {"energy": 0.6, "valence": 0.5},
    }
    title: WeatherTitleEnum

    def type(self) -> WeatherTitleEnum:
        """
        Return the type of weather.

        Returns:
            WeatherTitleEnum: The title of the weather.
        """
        return self.title

    @property
    def energy(self) -> Optional[float]:
        """
        Get the energy level associated with the weather.

        Returns:
            Optional[float]: The energy level.
        """
        return Weather.weather_energy_valence[self.title]["energy"]

    @property
    def valence(self) -> Optional[float]:
        """
        Get the valence level associated with the weather.

        Returns:
            Optional[float]: The valence level.
        """
        return Weather.weather_energy_valence[self.title]["valence"]

    @property
    def mood(self) -> Optional[Mood]:
        """
        Placeholder for mood property, potentially linking weather to mood.
        """
        pass

    def __repr__(self) -> str:
        """
        Return a string representation of the weather.

        Returns:
            str: A string in the format 'The weather is title'.
        """
        return f"The weather is {self.title}"

