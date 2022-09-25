from sqlite3 import Timestamp
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base
import datetime

class Community(Base):
    __tablename__ = "communities"
    id = Column(Integer, primary_key=True, index=True)
    airtable_id = Column(String, index=True)
    title = Column(String, index=True)
    slug = Column(String, unique=True, index=True)
    description = Column(String)
    url = Column(String)
    submitted_by = Column(String)
    created_on = Column(DateTime,default=datetime.datetime.now)
    last_updated = Column(DateTime, onupdate=datetime.datetime.now)    

"""
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
"""

