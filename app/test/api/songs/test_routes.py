from fastapi.testclient import TestClient
from app.service.external.open_weather.utils import OpenWeatherAPI
from app.models import SongList
from app.main import app
from app.config import settings

client = TestClient(app)


def test_recommend_endpoint():
    # Mocking the weather API response
    app.dependency_overrides[OpenWeatherAPI.get_weather_from_city] = lambda city_name: {"title": "Sunny"}

    # Sending a test request to the endpoint
    response = client.get("/songs/recommend/?user_mood=happy&city_name=Bengaluru&page=0&page_size=1", headers={"Authorization": settings.API_KEY})

    # Checking if the response status code is 200
    assert response.status_code == 200

    # Checking if the response contains the SongList
    assert isinstance(SongList.model_validate(response.json()), SongList)

    # You can add more specific assertions based on your requirements
