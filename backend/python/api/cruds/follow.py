import sys
import time
from typing import List
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status,Depends
from cruds import user

sys.path.append('../')

import models.follow as follow_model
import schemas.follow as follow_schema
import models.user as user_model
import schemas.user as user_schema

def get_all_follows(db:Session) ->List[follow_model.Follow]:
    return db.query(follow_model.Follow).all()

def get_all_following_users(db:Session,user_id:int) -> List[user_model.User]:
    follows=db.query(follow_model.Follow).filter(follow_model.Follow.follow_by==user_id).all()
    following_users=list(map(lambda follow:follow.follow_for,follows))
    users=db.query(user_model.User).filter(user_model.User.user_id.in_(following_users)).all()
    return users

def get_all_followed_users(db:Session,user_id:int) -> List[user_model.User]:
    follows=db.query(follow_model.Follow).filter(follow_model.Follow.follow_for==user_id).all()
    print(follows)
    followed_users=list(map(lambda follow:follow.follow_by,follows))
    print(followed_users)
    users=db.query(user_model.User).filter(user_model.User.user_id.in_(followed_users)).all()
    print(users)
    return users

def follow_a_user(db:Session,follow_by:int, follow_for:int) ->follow_model.Follow:
    follow=follow_model.Follow(follow_by=follow_by,follow_for=follow_for,follow_at=time.time())
    db.add(follow)
    db.commit()
    db.refresh(follow)

    return follow

def unfollow_a_user(db:Session,follow_by:int, follow_for:int) ->follow_model.Follow:
    follow=db.query(follow_model.Follow)\
        .filter(follow_model.Follow.follow_by==follow_by, follow_model.Follow.follow_for==follow_for)\
            .one_or_none()
    
    if follow is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detali=f"user {follow_by} does not follow user {follow_for}")

    db.delete(follow)
    db.commit()

    return follow