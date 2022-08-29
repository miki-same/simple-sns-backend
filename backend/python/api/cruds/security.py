from db import Base, get_db
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from dotenv import load_dotenv
from models.user import User
from fastapi import Depends, FastAPI,APIRouter,HTTPException,status
from sqlalchemy.orm.session import Session
import os
from typing import Union, List
from datetime import datetime, timedelta

SECRET_KEY=os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")

#ユーザー名からユーザーを取得
def get_user(username:str) ->User:
    db=get_db()
    user=db.query(User).filter(User.username==username).one()
    return user

#パスワードをDBのハッシュと照合し、一致しているかをboolで返す
def verify_password(plain_password, hashed_password) ->bool:
    return pwd_context.verify(plain_password, hashed_password)

#平文パスワードのハッシュを返す
def get_password_hash(password) ->str:
    return pwd_context.hash(password)

#ログインしている場合のみ、Tokenから自身のユーザーを取得する
def get_current_user(token: str = Depends(oauth2_scheme)) ->User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user=get_user(username=username)
    
    if user is None:
        raise credentials_exception
    return user

#usernameとpasswordをDBと照合し、認証した場合ユーザークラスを返す 認証失敗した場合Falseを返す
def authenticate_user(db:Session, username:str, password:str) ->Union[User,bool]:
    user=db.query(User).filter(User.username==username).one_or_none()
    if not user:
        return False
    if not verify_password(password,user.hashed_password):
        return False
    return user

#usernameが入った辞書型からJWTアクセストークンを作成する
def create_access_token(data: dict, expires_delta=Union[timedelta, None]) ->str:
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.utcnow()+expires_delta
    else:
        expire=datetime.utcnow()+ timedelta(minutes=15)

    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt