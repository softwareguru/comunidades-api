from pydantic import BaseModel

class CommunityBase(BaseModel):
    title: str
    airtable_id: str | None = None
    description: str | None = None
    url: str | None = None
    submitted_by: str | None = None

class CommunityCreate(CommunityBase):
    pass

class Community(CommunityBase):
    id: int
    slug: str

    class Config:
        orm_mode = True


"""
class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass 

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
"""

