from fastapi import APIRouter

router=APIRouter()

@router.get("/search/posts")
def search_posts():
    return

@router.get("/search/users")
def search_users():
    return