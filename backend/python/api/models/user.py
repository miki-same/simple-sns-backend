import sys
sys.path.append('../')

from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME, Float
from sqlalchemy.orm import relationship

from db import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(length=20))
    email = Column(String(200))
    hashed_password = Column(String(200))
    created_at = Column(Float)
