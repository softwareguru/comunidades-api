from sqlalchemy.orm import Session
from slugify import slugify

import models, schemas

def get_community( db:Session, id: int):
    return db.query(models.Community).filter(models.Community.id == id).first()

def get_community_by_slug(db: Session, slug: str):
    return db.query(models.Community).filter(models.Community.slug== slug).first()

def get_communities(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Community).offset(skip).limit(limit).all()    

def create_community(db: Session, community: schemas.CommunityCreate):
    db_comm = models.Community(**community.dict(), slug=slugify(community.title))    
    db.add(db_comm)
    db.commit()
    db.refresh(db_comm)
    return db_comm

def update_community(db: Session, db_comm: models.Community, incoming: schemas.CommunityCreate):
    new_data = incoming.dict(exclude_unset=True)
    for key, value in new_data.items():
        setattr(db_comm, key, value)
    db.add(db_comm)
    db.commit()
    db.refresh(db_comm)
    return db_comm




