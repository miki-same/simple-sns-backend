from typing import Optional

from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    username: str
    email: Optional[str]
    hashed_password: str