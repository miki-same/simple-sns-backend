import sys
from this import d
sys.path.append('../')

from datetime import datetime
from typing import List
from fastapi import APIRouter
from schemas.post import Post, PostCreate

router=APIRouter()

dummy_post=Post(post_id=0,message="fake post", reply_for=0, posted_at="2022-03-16 20:13:15",posted_by=3)

@router.get("/posts", response_model=List[Post])
def get_posts():
    return [
        dummy_post
        ]

@router.get("/posts/following", response_model=List[Post])
def get_posts_following():
    return [dummy_post]

@router.get("/posts/{user_id}", response_model=List[Post])
def get_post_by_user(user_id:int):
    return [dummy_post]

@router.post("/posts/{user_id}")
def users_post(user_id:int, post_body: PostCreate):
    return Post(post_id=1, posted_at="2022-08-26 16:29:30", **post_body.dict())

@router.get("/posts/{user_id}/{post_id}", response_model=Post)
def get_one_post_by_user(user_id:int,post_id:int):
    return dummy_post

@router.delete("/posts/{user_id}/{post_id}")
def delete_post(user_id:str,post_id:int):
    return