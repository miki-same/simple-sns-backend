import sys
sys.path.append('../')

from typing import List
from fastapi import APIRouter

from schemas.like import Like,LikeCreate
from schemas.user import User

router=APIRouter()

@router.get("/likes/{user_id}", response_model=List[Like])
def get_likes(user_id:int):
    return [
        Like(like_id=0,like_for=1,like_by=3,like_at="2022-08-26 12:15:30")
    ]

@router.get("/likes/{user_id}/{post_id}")
def get_users_liked(user_id:int, post_id:int):
    return [
        User(user_id=0,username="john",email="Foo@gmail.com",hashed_password="hashedpassword"),
        ]

@router.post("/likes/{user_id}/{post_id}")
def like_to_post(user_id:int,post_id:int, like_body:LikeCreate):
    return

@router.delete("/likes/{user_id}/{post_id}")
def delete_like_to_post(user_id:int,post_id:int):
    return 