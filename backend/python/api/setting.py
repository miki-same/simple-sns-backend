import os
from pydantic import BaseSettings

from db import DB_URL

class Settings(BaseSettings):
    DB_URL:str
    SECRET_KEY:str
    CONFIG:str