from typing import List
from pydantic import BaseModel

# Define UserBase first
class UserBase(BaseModel):
    username: str
    Email: str
    password: str

# Article inside UserDisplay
class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: UserBase  # Now UserBase is already defined
    class Config:
         from_attributes = True

class UserDisplay(BaseModel):
    username: str
    Email: str
    items: List[ArticleDisplay] = []
    class Config:
         from_attributes = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    user_id: int  
    class Config:
        from_attributes  = True

