from unittest.mock import Mock, patch
from app.service.external.lastfm.utils import LastFMAPI

@patch("app.service.external.lastfm.utils.LastFMAPI.api_interface")
def test_get_tracks_for_genres_paginated(mock_lastfm_api):
    # Mock the LastFM API response
    mock_tracks = [
        Mock(item=Mock(title="Track1", artist=Mock(name="Artist1"), get_url=Mock(return_value="http://track1.com"))),
        Mock(item=Mock(title="Track2", artist=Mock(name="Artist2"), get_url=Mock(return_value="http://track2.com"))),
        Mock(item=Mock(title="Track3", artist=Mock(name="Artist3"), get_url=Mock(return_value="http://track3.com"))),
        Mock(item=Mock(title="Track4", artist=Mock(name="Artist4"), get_url=Mock(return_value="http://track4.com"))),
        Mock(item=Mock(title="Track5", artist=Mock(name="Artist5"), get_url=Mock(return_value="http://track5.com"))),
    ]

    # Mock the get_tag and get_top_tracks methods
    mock_tag = Mock()
    mock_tag.get_top_tracks.return_value = mock_tracks
    mock_lastfm_api.get_tag.return_value = mock_tag

    # Call the function with sample data
    genres = ["genre1"]
    tracks = LastFMAPI.get_tracks_for_genres_paginated(genres, page_size=5, page=0)

    # Assertions
    assert len(tracks) == 5
    for track in tracks:
        assert isinstance(track, dict)
        assert "title" in track
        assert "artist" in track
        assert "url" in track
        assert "genre" in track

        assert track["title"] is not None
        assert track["artist"] is not None
        assert track["url"] is not None
        assert track["genre"] == "genre1"