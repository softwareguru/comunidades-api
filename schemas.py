from pydantic import BaseModel

class Community(BaseModel):
    title: str
    slug: str | None = None
    source_id: str | None = None
    description: str | None = None
    date: str | None = None
    url_main: str | None = None
    submitted_by: str | None = None
    strlist_links: str = ""
    strlist_topics: str = ""
    strlist_tags: str = ""
    

