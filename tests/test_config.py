# Import application settings
from backend.config import settings


# Test whether Gemini API key is loaded
def test_gemini_api_key():

    assert settings.GEMINI_API_KEY is not None
    assert settings.GEMINI_API_KEY != ""