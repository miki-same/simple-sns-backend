import sys
from this import d

from schemas.user import UserRequest
sys.path.append('../')

from datetime import datetime
from typing import List,Union
from fastapi import APIRouter,Depends, HTTPException, status
from schemas.post import Post, PostCreate, PostResponse

from db import get_db
from cruds.post import delete_post, get_all_posts, get_one_post, create_post, get_posts_by_user, get_posts_by_following_user

router=APIRouter()

dummy_post=Post(post_id=0,message="fake post", reply_for=0, posted_at=0,posted_by=3)

@router.get("/posts", response_model=List[PostResponse])
def list_posts(db=Depends(get_db)):
    return get_all_posts(db=db)

#TODO:フォローしているユーザーの投稿を抽出する機能を作る
@router.get("/posts/following", response_model=List[PostResponse])
def list_posts_following(user_id:int,db=Depends(get_db)):
    return get_posts_by_following_user(db=db, user_id=user_id)

@router.get("/posts/{user_id}", response_model=List[PostResponse])
def list_posts_by_user(user_id:int, db=Depends(get_db)):
    return get_posts_by_user(db=db, user_id=user_id)

@router.post("/posts/{user_id}", response_model=PostResponse)
def users_new_post(user_id:int, post_body: PostCreate, db=Depends(get_db)):
    post_body.posted_by=user_id
    return create_post(db=db, post_create=post_body)

@router.get("/posts/{user_id}/{post_id}", response_model=PostResponse)
def show_one_post_by_user(user_id:int,post_id:int, db=Depends(get_db)):
    return get_one_post(db=db, post_id=post_id)

@router.delete("/posts/{user_id}/{post_id}", response_model=PostResponse)
def delete_one_post(user_id:str,post_id:int, db=Depends(get_db)):
    return delete_post(db=db,user_id=user_id,post_id=post_id)