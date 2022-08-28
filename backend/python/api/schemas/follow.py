from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel, Field

class FollowBase(BaseModel):
    follow_by: int

class Follow(FollowBase):
    follow_for: int
    follow_at: float

class FollowResponse(Follow):
    class Config:
        orm_mode=True

class FollowCreate(FollowBase):
    pass