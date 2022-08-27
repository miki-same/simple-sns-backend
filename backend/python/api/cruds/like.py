import sys
import time
from typing import List
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status,Depends

from db import get_db

sys.path.append('../')

import models.like as like_model
import schemas.like as like_schema

def get_all_likes(db:Session) -> List[like_model.Like]:
    likes=db.query(like_model.Like).all()

    return likes

def get_all_likes_by_user(db:Session, user_id:int) -> List[like_model.Like]:
    likes=db.query(like_model.Like).filter(like_model.Like.like_by==user_id).all()

    return likes

def get_all_likes_for_post(db:Session,user_id:int,post_id:int)-> List[like_model.Like]:
    likes=db.query(like_model.Like).filter(like_model.Like.like_for==post_id).all()
    return likes

def post_like(db:Session,like_by:int, like_for:int) -> like_model.Like:
    #TODO:likeの存在判定

    like=like_model.Like(like_by=like_by, like_for=like_for, like_at=time.time())

    db.add(like)
    db.commit()
    db.refresh(like)

    return like

def delete_like(db:Session,like_by:int, like_for:int) -> like_model.Like:
    like=db.query(like_model.Like).filter(like_model.Like.like_by==like_by, like_model.Like.like_for==like_for).one_or_none()
    if like is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"the post is not liked yet")
    
    db.delete(like)
    db.commit()
    
    return like