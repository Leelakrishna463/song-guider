from app.models.weather import Weather, WeatherTitleEnum

def test_weather_model_repr():
    weather_data = {"title": WeatherTitleEnum.Clear}
    weather = Weather(**weather_data)
    assert repr(weather) == "The weather is Clear"

def test_weather_model_properties():
    weather_data = {"title": WeatherTitleEnum.Clear}
    weather = Weather(**weather_data)
    assert weather.energy == 1.0
    assert weather.valence == 1.0
