from enum import auto
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from functools import lru_cache
from config import Settings

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()

engine = create_engine(settings.database_url, connect_args= {"check_same_thread": False} )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
