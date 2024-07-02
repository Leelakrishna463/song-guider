from app.main import app
from fastapi.testclient import TestClient
import pytest
from app.config import settings


client = TestClient(app)

# Test valid API key
def test_valid_api_key():
    response = client.get("/health", headers={"Authorization": settings.API_KEY})
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }

# Test invalid API key
def test_invalid_api_key():
    response = client.get("/health", headers={"Authorization": "invalid_api_key"})
    assert response.status_code == 401
    assert response.json() == {"detail": "You're not authorized to access this resource"}

# Test missing API key
def test_missing_api_key():
    response = client.get("/health")
    assert response.status_code == 403
    assert response.json() == {"detail": "Not authenticated"}

