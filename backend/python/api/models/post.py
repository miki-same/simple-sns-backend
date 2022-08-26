import sys
sys.path.append('../')

from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME,Float
from sqlalchemy.orm import relationship

from db import Base

class Post(Base):
    __tablename__ = "posts"

    post_id=Column(Integer, primary_key=True,autoincrement=True)
    posted_by=Column(Integer)
    message=Column(String(length=100))
    reply_for=Column(Integer, nullable=True)
    posted_at=Column(Float)