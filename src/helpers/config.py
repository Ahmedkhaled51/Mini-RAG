from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # ← explicitly load .env before Settings() is called

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    model_config = {"env_file": ".env"}


def get_settings():
    return Settings()
    