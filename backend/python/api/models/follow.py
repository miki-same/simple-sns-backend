import sys
sys.path.append('../')

from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME,Float
from sqlalchemy.orm import relationship

from db import Base

class Follow(Base):
    __tablename__ = "follows"

    follow_id=Column(Integer, primary_key=True,autoincrement=True)
    follow_by=Column(Integer)
    follow_for=Column(Integer)
    follow_at=Column(Float)