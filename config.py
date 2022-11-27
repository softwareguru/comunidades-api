from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key: str = "SetAnEnvironmentVar"
    github_token: str = "SetAnEnvironmentVar"
    repo_name: str = "owner/repo"
    file_dir: str = "content/items/"
    
    # Uncomment if you want to read environment variables from a .env file
    # class Config:
    #    env_file = ".env"

