import sys

sys.path.append('../')

from typing import List
from fastapi import APIRouter,Depends
from schemas.follow import Follow, FollowCreate, FollowResponse
from schemas.user import User, UserResponse

from db import get_db

from cruds.follow import follow_a_user, get_all_followed_users, get_all_following_users, get_all_follows, unfollow_a_user

router=APIRouter()

@router.get("/follow", response_model=List[FollowResponse])
def list_all_follows(db=Depends(get_db)):
    return get_all_follows(db=db)

@router.get("/follow/{user_id}/following", response_model=List[UserResponse])
def list_following_users(user_id:int,db=Depends(get_db)):
    return get_all_following_users(db=db,user_id=user_id)

@router.get("/follow/{user_id}/followed", response_model=List[UserResponse])
def list_followed_users(user_id:int, db=Depends(get_db)):
    return get_all_followed_users(db=db, user_id=user_id)

@router.post("/follow/{user_id}", response_model=FollowResponse)
def follow_user(user_id:int, follow_body: FollowCreate,db=Depends(get_db)):
    return follow_a_user(db=db,follow_by=follow_body.follow_by ,follow_for=user_id)

@router.delete("/follow/{user_id}", response_model=FollowResponse)
def unfollow_user(user_id:int, follow_body: FollowCreate, db=Depends(get_db)):
    return unfollow_a_user(db=db,follow_by=follow_body.follow_by ,follow_for=user_id)