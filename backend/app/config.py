
import os

class Settings:
    # Basic application information
    APP_NAME = "DevMate"
    APP_VERSION = "1.0.0"
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

    # AI model configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    # Database configuration
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./devmate.db"
    )


# Create a settings object
settings = Settings()
