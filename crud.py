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
    db_comm = models.Community(**community.dict(), slug=slugify(community.title), topics=make_array(community.topics_flat), tags=make_array(community.tags_flat))
    db.add(db_comm)
    db.commit()
    db.refresh(db_comm)
    return db_comm

def update_community(db: Session, db_comm: models.Community, incoming: schemas.CommunityCreate):
    new_data = incoming.dict(exclude_unset=True)
    for key, value in new_data.items():
        setattr(db_comm, key, value)
    tag_list = [x.strip() for x in incoming.tags_flat.split(',')]
    setattr(db_comm, "tags", tag_list)
    topic_list = [x.strip() for x in incoming.topics_flat.split(',')]
    setattr(db_comm, "topics", topic_list)
    db.add(db_comm)
    db.commit()
    db.refresh(db_comm)
    return db_comm


def make_array(flat_list: str):
    results = []
    if flat_list != "":
        results = [translate_term(x.strip()) for x in flat_list.split(',')]
    return results

def translate_term(term: str): 
    """In the creation form we want to put terms with special characters like & or / that are not picked up 
    as taxonomy terms by Hugo. So, we add this utility function to translate them to something friendlier to Hugo. 
    TODO: Provide a more elegant solution instead of matching with ifs. I suppose something with dicts, 
    but the issue is keys may not be exact matches. Will think about it."""
    
    if "Infraestructura" in term:
        return "infra"

    return term    

