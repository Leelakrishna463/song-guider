from typing import Optional, List
from pydantic import BaseModel

class Song(BaseModel):
    """
    A model representing a song with various attributes.

    Attributes:
        title (str): The title of the song.
        artist (str): The artist of the song.
        energy (Optional[float]): The energy level of the song, if available.
        valence (Optional[float]): The valence level of the song, if available.
        genre (Optional[str]): The genre of the song, if available.
        url (Optional[str]): The URL link to the song, if available.
    """
    title: str
    artist: str
    energy: Optional[float] = None
    valence: Optional[float] = None
    genre: str
    url: Optional[str] = None

    def __repr__(self) -> str:
        """
        Return a string representation of the song.

        Returns:
            str: A string in the format 'title by artist from album'.
        """
        return f"{self.title} by {self.artist}"

class SongList(BaseModel):
    """
    A model representing a list of songs.

    Attributes:
        songs (List[Song]): A list of Song objects.
    """
    songs: List[Song]
