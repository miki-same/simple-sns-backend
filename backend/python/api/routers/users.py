import sys
sys.path.append('../')

from typing import List
from fastapi import APIRouter

from schemas.user import User

router=APIRouter()

@router.get("/users", response_model=List[User])
def list_users():
    return [
        User(id=0,username="john",email="Foo@gmail.com",hashed_password="hashedpassword"),
        User(id=1,username="michel",email="Bar@gmail.com",hashed_password="hashedpassword"),
    ]

@router.get("/users/{username}", response_model=User)
def get_user(username:str):
    return User(id=0,username="john",email="Foo@gmail.com",hashed_password="hashedpassword")