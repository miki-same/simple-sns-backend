import sys
sys.path.append('../')

from typing import List
from fastapi import APIRouter

from schemas.user import User

router=APIRouter()

dummy_users=[
    User(user_id=0,username="john",email="Foo@gmail.com",hashed_password="hashedpassword",created_at="2022-08-26 16:26:30"),
    User(user_id=1,username="michel",email="Bar@gmail.com",hashed_password="hashedpassword",created_at="2022-08-26 16:26:30"),
]

@router.get("/users", response_model=List[User])
def list_users():
    return dummy_users

@router.get("/users/{user_id}", response_model=User)
def get_user(username:int):
    return dummy_users[0]