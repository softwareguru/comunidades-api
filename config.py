from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./sample.db"
    api_key: str = ""

    class Config:
        env_file = ".env"

