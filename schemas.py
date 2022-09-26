from pydantic import BaseModel

class CommunityBase(BaseModel):
    title: str
    airtable_id: str | None = None
    description: str | None = None
    url: str | None = None
    submitted_by: str | None = None
    topics_flat: str | None = None
    tags_flat: str | None = None
    

class CommunityCreate(CommunityBase):
    pass

class Community(CommunityBase):
    id: int
    slug: str
    topics: set[str] = set()
    tags: set[str] = set()

    class Config:
        orm_mode = True


