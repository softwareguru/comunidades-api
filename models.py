from sqlite3 import Timestamp
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table, PickleType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.mutable import MutableList

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
    topics = Column(MutableList.as_mutable(PickleType), default=[])
    topics_flat = Column(String)
    tags = Column(MutableList.as_mutable(PickleType), default=[])
    tags_flat = Column(String)
    submitted_by = Column(String)
    created_on = Column(DateTime,default=datetime.datetime.now)
    last_updated = Column(DateTime, onupdate=datetime.datetime.now)

