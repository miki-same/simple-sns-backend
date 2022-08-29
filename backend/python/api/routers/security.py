from fastapi import Depends, FastAPI,APIRouter,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from db import Base, get_db
from sqlalchemy.orm.session import Session
from passlib.context import CryptContext
from jose import JWTError, jwt
from dotenv import load_dotenv
import os
from typing import Union, List
from models.user import User
from datetime import datetime, timedelta
from pydantic import BaseModel

from cruds.security import ACCESS_TOKEN_EXPIRE_MINUTES, oauth2_scheme,get_user,verify_password,get_password_hash,get_current_user,authenticate_user,create_access_token


router=APIRouter()

@router.get("/items")
def read_items(token: str = Depends(oauth2_scheme)):
    return {"token":token}

@router.post("/token")
def login(db:Session =Depends(get_db),form_data: OAuth2PasswordRequestForm= Depends()):
    user=authenticate_user(db=db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate":"Bearer"})
    
    access_token_expires=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token=create_access_token(
        data={"sub":user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}