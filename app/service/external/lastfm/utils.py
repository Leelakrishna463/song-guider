import pylast
from app.config import settings
from typing import List
from app.logger import logger
from math import ceil
from app.models import SongList


class LastFMAPI:
    api_interface = pylast.LastFMNetwork(
        api_key=settings.LASTFM_API_KEY,
        api_secret=settings.LASTFM_API_SECRET,
        username=settings.LASTFM_USERNAME,
        password_hash=pylast.md5(settings.LASTFM_PASSWORD)
    )

    @staticmethod
    def get_tracks_for_genres_paginated(genres: List[str], page_size: int, page: int) -> SongList:
        """
        Retrieve top tracks for given genres from LastFM.

        Args:
            genres (List[str]): A list of genres to retrieve tracks for.
            page_size (int): The number of songs to recommend
            page (int): The page number from where the song listing to start
            

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing track details.
        """
        logger.info("Fetching tracks for genres")
        logger.debug(f"Genres: {genres}")

        tracks = []
        for genre in genres:
            try:
                logger.info(f"Fetching top tracks for genre: {genre}")
                genre_tracks_response = LastFMAPI.api_interface.get_tag(genre).get_top_tracks()
                max_pages = ceil(len(genre_tracks_response)/page_size)
                if page > max_pages:
                    raise IndexError("Page size is out of range. Please reduce page value")
                genre_tracks_response_paginated = genre_tracks_response[page*page_size: page_size*(page+1)]
                for track in genre_tracks_response_paginated:
                    track_info = {
                        "title": track.item.title,
                        "artist": track.item.artist.name,
                        "url": track.item.get_url(),
                        "genre": genre
                    }
                    tracks.append(track_info)
                    logger.debug(f"Track info: {track_info}")
            except IndexError as e:
                raise IndexError(e)
            except Exception as e:
                logger.error(f"Error fetching tracks for genre {genre}: {e}")

        logger.info("Completed fetching tracks")
        return tracks
