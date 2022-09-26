from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

from fastapi.security.api_key import APIKey
import auth

models.Base.metadata.create_all(bind=engine)


description = """
Obten via API información de comunidades técnicas. 

Tenemos contemplado soportar las siguientes entidades:
 * Comunidades (listo)
 * Temas de interés (pronto)
 * Ciudades (pronto)
 * Eventos (pronto)

[Ver código en GitHub](https://github.com/softwareguru/comunidades-api)
"""

app = FastAPI(
    title="Comunidades.dev API",
    description=description,
    version="0.1.0",
    license_info={
        "name": "MIT License",
        "url": "https://choosealicense.com/licenses/mit/",
    },
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", include_in_schema=False)
def root():
    return {"message" : "It would be nice to config your web server to show an html file instead of this."}

@app.get("/communities/", response_model=list[schemas.Community])
def get_communities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = crud.get_communities(db, skip=skip, limit=limit)
    return results

@app.get("/communities/{community_id}", response_model=schemas.Community)
def get_community(community_id: int, db: Session = Depends(get_db)):
    db_comm = crud.get_community(db, id=community_id)
    if db_comm is None:
        raise HTTPException(status_code=404, detail="Not found")
    return db_comm

@app.post("/communities/", response_model=schemas.Community)
def create_community(community: schemas.CommunityCreate, db: Session = Depends(get_db), api_key: APIKey = Depends(auth.get_api_key)):
    return crud.create_community(db=db, community=community)
