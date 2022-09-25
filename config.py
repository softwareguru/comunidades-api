from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./sample.db"

    class Config:
        env_file = ".env"

settings = Settings()