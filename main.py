from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message" : "Hello world"}

@app.post("/communities/", response_model=schemas.Community)
def create_community(community: schemas.CommunityCreate, db: Session = Depends(get_db)):
    return crud.create_community(db=db, community=community)

@app.get("/communities/", response_model=list[schemas.Community])
def read_communities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = crud.get_communities(db, skip=skip, limit=limit)
    return results

@app.get("/communities/{community_id}", response_model=schemas.Community)
def read_community(community_id: int, db: Session = Depends(get_db)):
    db_comm = crud.get_community(db, id=community_id)
    if db_comm is None:
        raise HTTPException(status_code=404, detail="Not found")
    return db_comm
