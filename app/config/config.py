# app/config/config.py

from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    elasticsearch_host: str = os.getenv("ELASTICSEARCH_HOST", "https://localhost:9200")
    elasticsearch_user: str = os.getenv("ELASTICSEARCH_USER")
    elasticsearch_password: str = os.getenv("ELASTICSEARCH_PASSWORD")

    class Config:
        env_file = ".env"

settings = Settings()
