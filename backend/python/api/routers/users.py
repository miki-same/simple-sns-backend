import sys
sys.path.append('../')

from typing import List
from fastapi import APIRouter, Depends

from schemas.user import User,UserCreate
from db import get_db
from cruds.user import create_user

router=APIRouter()

dummy_users=[
    User(user_id=0,username="john",email="Foo@gmail.com",hashed_password="hashedpassword",created_at=0),
    User(user_id=1,username="michel",email="Bar@gmail.com",hashed_password="hashedpassword",created_at=0),
]

@router.get("/users", response_model=List[User])
def list_users():
    return dummy_users

@router.post("/users", response_model=User)
def create_new_user(user_body:UserCreate, db=Depends(get_db)):
    return create_user(db=db, user_create=user_body)


@router.get("/users/{user_id}", response_model=User)
def get_user(username:int):
    return dummy_users[0]