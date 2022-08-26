from curses import echo
import os
from os.path import join, dirname
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DB_URL=os.environ.get("DB_URL")

engine=create_engine(DB_URL, echo=True)

sessionClass = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base=declarative_base()

def get_db():
    return sessionClass()