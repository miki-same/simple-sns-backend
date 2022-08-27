import sys

from cruds.like import delete_like, get_all_likes_for_post, post_like, get_all_likes_by_user
sys.path.append('../')

from typing import List
from fastapi import APIRouter,Depends

from db import get_db

from schemas.like import Like,LikeCreate, LikeResponse
from schemas.user import User

router=APIRouter()

@router.get("/likes/{user_id}", response_model=List[LikeResponse])
def list_likes(user_id:int, db=Depends(get_db)):
    return get_all_likes_by_user(db=db, user_id=user_id)

@router.get("/likes/{user_id}/{post_id}", response_model=List[LikeResponse])
def list_likes_for_post(user_id:int, post_id:int, db=Depends(get_db)):
    return get_all_likes_for_post(db=db, user_id=user_id,post_id=post_id)


@router.post("/likes/{user_id}/{post_id}", response_model=LikeResponse)
def create_like_to_post(user_id:int,post_id:int, like_body:LikeCreate,db=Depends(get_db)):
    return post_like(db=db, like_by=like_body.like_by, like_for=post_id)

@router.delete("/likes/{user_id}/{post_id}", response_model=LikeResponse)
def delete_like_to_post(user_id:int,post_id:int,like_body:LikeCreate, db=Depends(get_db)):
    return delete_like(db=db, like_by=like_body.like_by,like_for=post_id)