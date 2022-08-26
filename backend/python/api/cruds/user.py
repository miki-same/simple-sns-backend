import sys
import time
sys.path.append('../')

import models.user as user_model
import schemas.user as user_schema

def create_user(db,user_create:user_schema.UserCreate) -> user_model.User:
    user=user_model.User(created_at=time.time(),**user_create.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user