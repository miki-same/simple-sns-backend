from operator import or_
import sys
import time
from typing import List
from sqlalchemy.orm.session import Session
from sqlalchemy import or_
from fastapi import HTTPException, status
import re
sys.path.append('../')

import models.user as user_model
import schemas.user as user_schema

from cruds.security import get_password_hash

username_pattern=re.compile(r'[\w_]+')
email_pattern=re.compile(r'[\w\-._]+@[\w\-._]+\.[A-Za-z]+')

def is_valid_name(name:str) ->bool:
    return True if (len(name)<=20 and username_pattern.fullmatch(name)) else False

def is_valid_email(email:str) ->bool:
    return email_pattern.fullmatch(email) is not None

def create_user(db:Session,user_create:user_schema.UserCreate) -> user_model.User:
    
    #20文字以内&アルファベット・数字・ハイフンのみの名前か確認
    if not is_valid_name(user_create.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"username {user_create.username} is not valid")

    #同名ユーザーが存在するか確認
    same_name_user =db.query(user_model.User).filter(user_model.User.username==user_create.username).one_or_none()
    if same_name_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"user {user_create.username} already exists")
    
    #メールアドレスが有効か確認
    if not is_valid_email(user_create.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"email {user_create.email} is not valid")

    #同じメールアドレスのユーザーが存在するか確認
    same_email_user = db.query(user_model.User).filter(user_model.User.email==user_create.email).all()
    if same_email_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"a same email user already exists")


    user_create_dict={
        "username":user_create.username,
        "nickname":user_create.nickname,
        "email":user_create.email,
        "hashed_password": get_password_hash(user_create.password)
    }

    user=user_model.User(created_at=time.time(),**user_create_dict)
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