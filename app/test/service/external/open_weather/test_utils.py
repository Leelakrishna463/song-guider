from unittest.mock import Mock, patch
from requests.exceptions import RequestException
from app.service.external.open_weather.utils import OpenWeatherAPI

@patch("app.service.external.open_weather.utils.requests.get")
def test_get_weather_from_city(mock_requests_get):
    # Mock successful response from OpenWeather API
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"weather": [{"main": "Clear"}]}
    mock_requests_get.return_value = mock_response

    # Call the method with a sample city name
    weather = OpenWeatherAPI.get_weather_from_city("London")

    # Assertions for successful response
    assert weather.title == "clear"

    # Mock unsuccessful response from OpenWeather API
    mock_response.status_code = 404
    mock_requests_get.return_value = mock_response

    # Assertions for unsuccessful response
    try:
        OpenWeatherAPI.get_weather_from_city("London")
    except Exception as e:
        assert str(e) == "Unable to get weather from OpenWeather"

    # Mock network error
    mock_requests_get.side_effect = RequestException()

    # Assertions for network error
    try:
        OpenWeatherAPI.get_weather_from_city("London")
    except Exception as e:
        assert str(e) == "Unable to get weather from OpenWeather"
