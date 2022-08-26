from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

class PostBase(BaseModel):
    message: str = Field(..., max_length=100)
    reply_for: Optional[int]
    posted_by: int

class Post(PostBase):
    post_id: int
    posted_at: datetime

class PostCreate(PostBase):
    pass