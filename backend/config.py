# Load environment variables
from dotenv import load_dotenv

# Read environment variables
import os


# Load .env
load_dotenv()


# Application settings
class Settings:

    # Gemini API Key
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Single settings object
settings = Settings()