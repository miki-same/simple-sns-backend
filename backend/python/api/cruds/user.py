import sys
import time
from typing import List
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
sys.path.append('../')

import models.user as user_model
import schemas.user as user_schema

def create_user(db:Session,user_create:user_schema.UserCreate) -> user_model.User:
    same_name_user =db.query(user_model.User).filter(user_model.User.username==user_create.username).one()
    if same_name_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"user {user_create.username} is already exist")
    user=user_model.User(created_at=time.time(),**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_all_users(db:Session) -> List[user_model.User]:
    users=db.query(user_model.User).all()

    return users

def get_one_user(db:Session, user_id: int) -> user_model.User:
    user=db.query(user_model.User).filter(user_model.User.user_id==user_id).one_or_none()

    return user