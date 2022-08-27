import sys
sys.path.append('../')

from typing import List,Union
from fastapi import APIRouter, Depends, HTTPException,status

from schemas.user import User,UserCreate, UserResponse
from db import get_db
from cruds.user import create_user,get_all_users,get_one_user

router=APIRouter()

dummy_users=[
    User(user_id=0,username="john",email="Foo@gmail.com",hashed_password="hashedpassword",created_at=0),
    User(user_id=1,username="michel",email="Bar@gmail.com",hashed_password="hashedpassword",created_at=0),
]

@router.get("/users", response_model=List[UserResponse])
def list_users(db=Depends(get_db)):
    return get_all_users(db=db)

@router.post("/users", response_model=User)
def create_new_user(user_body:UserCreate, db=Depends(get_db)):
    return create_user(db=db, user_create=user_body)


@router.get("/users/{user_id}", response_model=UserResponse)
def show_user(user_id:int, db=Depends(get_db)):
    user=get_one_user(db=db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")

    return user
