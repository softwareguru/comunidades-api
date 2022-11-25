from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key: str = "SetAnEnvironmentVar"
    github_token: str = "SetAnEnvironmentVar"
    repo_name: str = "owner/repo"

    class Config:
        env_file = ".env"

