import sys
import time
from typing import List
from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status

sys.path.append('../')

import models.post as post_model
import schemas.post as post_schema

import models.follow as follow_model
import schemas.follow as follow_schema

def get_all_posts(db: Session) -> List[post_model.Post]:
    posts=db.query(post_model.Post).all()

    return posts

def get_one_post(db: Session, post_id: int) ->post_model.Post:
    post=db.query(post_model.Post).filter(post_model.Post.post_id==post_id).one_or_none()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="post doesn't exist")
    return post

def get_posts_by_following_user(db: Session, user_id: int) ->List[post_model.Post]:
    follows=db.query(follow_model.Follow)\
        .filter(follow_model.Follow.follow_by==user_id)\
            .all()
    following_users=list(map(lambda follow:follow.follow_for, follows))
    posts=db.query(post_model.Post)\
        .filter(post_model.Post.posted_by.in_(following_users))\
            .all()
    
    return posts

def get_posts_by_user(db:Session, user_id: int) ->List[post_model.Post]:
    posts=db.query(post_model.Post).filter(post_model.Post.posted_by==user_id).all()

    return posts

def create_post(db: Session, post_create: post_schema.PostCreate) -> post_model.Post:
    post=post_model.Post(posted_at=time.time(), **post_create.dict())
    db.add(post)
    db.commit()
    db.refresh(post)

    return post

def delete_post(db: Session,user_id: int, post_id: int) ->post_model.Post:
    post=db.query(post_model.Post).filter(post_model.Post.post_id==post_id).one_or_none()
    if post:
        if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post {post_id} is not found")
        if post.posted_by!=user_id:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post {post_id} is not posted by user {user_id}")
        db.delete(post)
        db.commit()

    return post