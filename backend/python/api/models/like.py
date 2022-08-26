import sys
sys.path.append('../')

from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME,Float
from sqlalchemy.orm import relationship

from db import Base

class Like(Base):
    __tablename__ = "likes"

    like_id=Column(Integer, primary_key=True,autoincrement=True)
    like_for=Column(Integer)
    like_by=Column(Integer)
    like_at=Column(Float)