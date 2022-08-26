import sys
sys.path.append('../')

from typing import List
from fastapi import APIRouter
from schemas.follow import Follow, FollowCreate
from schemas.user import User

router=APIRouter()

dummy_follow=Follow(follow_by=0,follow_for=1,follow_at=0)

dummy_users=[
    User(user_id=0,username="john",email="Foo@gmail.com",hashed_password="hashedpassword",created_at=0),
    User(user_id=1,username="michel",email="Bar@gmail.com",hashed_password="hashedpassword",created_at=0),
]

@router.get("/follow/{user_id}/following", response_model=List[User])
def get_following_users(user_id:int):
    return dummy_users

@router.get("/follow/{user_id}/followed")
def get_followed_users(user_id:int):
    return dummy_users

@router.post("/follow/{user_id}")
def follow_user(user_id:int, follow_body: FollowCreate):
    return Follow(follow_at="2022-08-26 16:50:00",**follow_body.dict())

@router.delete("/follow/{user_id}")
def unfollow_user(user_id:int):
    return