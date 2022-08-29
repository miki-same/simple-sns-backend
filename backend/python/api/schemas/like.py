from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class LikeBase(BaseModel):
    like_by: int

class Like(LikeBase):
    like_for: int
    like_id: int
    like_at: float

class LikeResponse(Like):
    class Config:
        orm_mode=True

class LikeCreate(BaseModel):
    like_by: Optional[int]