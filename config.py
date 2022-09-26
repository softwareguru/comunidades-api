from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./sample.db"
    api_key: str = "SetAnEnvironmentVar"

    class Config:
        env_file = ".env"

