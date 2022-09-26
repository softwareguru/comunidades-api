from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./sample.db"
    api_key: str = "SetAnEnvironmentVar"
    github_token: str = "SetAnEnvironmentVar"
    repo_name: str = "owner/repo"

    class Config:
        env_file = ".env"

