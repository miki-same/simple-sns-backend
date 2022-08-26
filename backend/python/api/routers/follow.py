from fastapi import APIRouter

router=APIRouter()

@router.get("/follow/{username}/following")
def get_following_users(username:str):
    return

@router.get("/follow/{username}/followed")
def get_followed_users(username:str):
    return

@router.post("/follow/{username}")
def follow_user(username:str):
    return

@router.delete("/follow/{username}")
def unfollow_user(username:str):
    return