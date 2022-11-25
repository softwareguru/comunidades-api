from pydantic import BaseModel

class Community(BaseModel):
    title: str
    slug: str | None = None
    airtable_id: str | None = None
    description: str | None = None
    url: str | None = None
    submitted_by: str | None = None
    topics_flat: str = ""
    tags_flat: str = ""
    topics: set[str] = set()
    tags: set[str] = set()
    

