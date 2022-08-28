from fastapi import Depends, FastAPI,APIRouter
from fastapi.security import OAuth2PasswordBearer

from models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router=APIRouter()

@router.get("/items")
def read_items(token: str = Depends(oauth2_scheme)):
    return {"token":token}

def get_current_user(token: str = Depends(oauth2_scheme)):
    fake_user=User(username="taro",email="email",hashed_password="hashed",user_id=1,created_at=0)
    return fake_user