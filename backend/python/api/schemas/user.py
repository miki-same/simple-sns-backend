from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str
    email: Optional[str]
    hashed_password: str

class User(UserBase):
    user_id: int
    created_at: float

    class Config:
        orm_mode=True

class UserCreate(UserBase):
    pass