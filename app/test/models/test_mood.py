from app.models.mood import Mood, MoodTitleEnum

def test_mood_model_properties():
    mood_data = {"title": MoodTitleEnum.Happy}
    mood = Mood(**mood_data)
    
    assert mood.title == MoodTitleEnum.Happy
    assert mood.energy == 0.75
    assert mood.valence == 1.0
