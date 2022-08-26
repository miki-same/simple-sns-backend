from curses import echo
import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from db import Base

load_dotenv()

DB_URL=os.environ.get("DB_URL")
engine=create_engine(DB_URL, echo=True)

from models.user import User
from models.post import Post
from models.like import Like
from models.follow import Follow

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()