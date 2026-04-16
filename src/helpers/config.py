from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # ← explicitly load .env before Settings() is called


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    FILE_ALLOWED_EXTENSIONS: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    model_config = {"env_file": ".env"}


def get_settings():
    return Settings()
