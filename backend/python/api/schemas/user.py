from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str

class User(UserBase):
    email: Optional[str]
    hashed_password: str
    user_id: int
    created_at: float

    class Config:
        orm_mode=True

class UserInDB(User):
    pass

class UserResponse(UserBase):
    user_id: int
    
    class Config:
        orm_mode=True

class UserCreate(UserBase):
    email: Optional[str]
    hashed_password: str