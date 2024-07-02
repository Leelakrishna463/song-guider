from enum import Enum
from typing import Optional, ClassVar, Dict

from pydantic import BaseModel

class MoodTitleEnum(str, Enum):
    """Enumeration of possible mood titles."""
    Excited = "excited"
    Delighted = "delighted"
    Happy = "happy"
    Content = "content"
    Relaxed = "relaxed"
    Calm = "calm"
    Tired = "tired"
    Bored = "bored"
    Depressed = "depressed"
    Frustrated = "frustrated"
    Angry = "angry"
    Tense = "tense"

class Mood(BaseModel):
    """
    A model representing a mood with associated energy and valence values.

    Attributes:
        title (MoodTitleEnum): The title of the mood.
    """
    mood_energy_valence_map: ClassVar[Dict[MoodTitleEnum, Dict[str, float]]] = {
        MoodTitleEnum.Excited: {"energy": 1.0, "valence": 0.75},
        MoodTitleEnum.Delighted: {"energy": 0.875, "valence": 0.875},
        MoodTitleEnum.Happy: {"energy": 0.75, "valence": 1.0},
        MoodTitleEnum.Content: {"energy": 0.375, "valence": 1.0},
        MoodTitleEnum.Relaxed: {"energy": 0.25, "valence": 0.875},
        MoodTitleEnum.Calm: {"energy": 0.125, "valence": 0.75},
        MoodTitleEnum.Tired: {"energy": 0.125, "valence": 0.375},
        MoodTitleEnum.Bored: {"energy": 0.25, "valence": 0.25},
        MoodTitleEnum.Depressed: {"energy": 0.375, "valence": 0.125},
        MoodTitleEnum.Frustrated: {"energy": 0.75, "valence": 0.125},
        MoodTitleEnum.Angry: {"energy": 0.875, "valence": 0.25},
        MoodTitleEnum.Tense: {"energy": 1.0, "valence": 0.375},
    }
    title: MoodTitleEnum

    @property
    def energy(self) -> Optional[float]:
        """
        Get the energy level associated with the mood.

        Returns:
            Optional[float]: The energy level.
        """
        return Mood.mood_energy_valence_map[self.title]["energy"]

    @property
    def valence(self) -> Optional[float]:
        """
        Get the valence level associated with the mood.

        Returns:
            Optional[float]: The valence level.
        """
        return Mood.mood_energy_valence_map[self.title]["valence"]
