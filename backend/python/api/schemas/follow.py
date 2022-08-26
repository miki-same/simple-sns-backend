from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel, Field

class FollowBase(BaseModel):
    follow_by: int
    follow_for: int

class Follow(FollowBase):
    follow_at: float

class FollowCreate(FollowBase):
    pass