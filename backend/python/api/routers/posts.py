import sys
from this import d

from schemas.user import UserRequest
sys.path.append('../')

from datetime import datetime
from typing import Dict, List,Union
from fastapi import APIRouter,Depends, HTTPException, status
from schemas.post import Post, PostCreate, PostResponse, PostResponseWithName

from db import get_db
from cruds.post import delete_post, get_all_posts,get_all_posts_with_name ,get_one_post, create_post, get_posts_by_user, get_posts_by_following_user
from cruds.security import get_current_username_and_id

router=APIRouter()

dummy_post=Post(post_id=0,message="fake post", reply_for=0, posted_at=0,posted_by=3)

@router.get("/posts", response_model=List[PostResponseWithName])
def list_posts(db=Depends(get_db)):
    return get_all_posts_with_name(db=db)

@router.post("/posts", response_model=PostResponse)
def users_new_post(post_body: PostCreate, db=Depends(get_db),userdata:Dict=Depends(get_current_username_and_id)):
    post_body.posted_by=userdata.get("user_id")
    return create_post(db=db, post_create=post_body)

@router.get("/posts/following", response_model=List[PostResponse])
def list_posts_following(user_id:int,db=Depends(get_db)):
    return get_posts_by_following_user(db=db, user_id=user_id)

@router.get("/posts/{user_id}", response_model=List[PostResponse])
def list_posts_by_user(user_id:int, db=Depends(get_db)):
    return get_posts_by_user(db=db, user_id=user_id)

@router.get("/posts/{user_id}/{post_id}", response_model=PostResponse)
def show_one_post_by_user(user_id:int,post_id:int, db=Depends(get_db)):
    return get_one_post(db=db, post_id=post_id)

@router.delete("/posts/{user_id}/{post_id}", response_model=PostResponse)
def delete_one_post(user_id:int,post_id:int, db=Depends(get_db),userdata:Dict=Depends(get_current_username_and_id)):
    if user_id!=userdata.get("user_id") and userdata.get("username")!="admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="action is not authorized")

    return delete_post(db=db,user_id=user_id,post_id=post_id)