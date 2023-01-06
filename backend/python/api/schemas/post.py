from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

class PostBase(BaseModel):
    message: str = Field(..., max_length=100)
    reply_for: Optional[int]

class Post(PostBase):
    post_id: int
    posted_at: float
    posted_by: int

class PostResponse(Post):
    pass

    class Config:
        orm_mode=True

class PostWithName(Post):
    username: str

class PostResponseWithName(PostWithName):
    pass

    class Config:
        orm_mode=True

class PostCreate(PostBase):
    posted_by: Optional[int]