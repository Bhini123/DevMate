import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "DevMate"
    APP_VERSION = "1.0.0"
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    # AI model configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    # Database configuration
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./devmate.db"
    )

settings = Settings()