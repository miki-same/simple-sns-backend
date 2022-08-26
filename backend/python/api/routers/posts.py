from fastapi import APIRouter

router=APIRouter()

@router.get("/posts")
def get_posts():
    return {"posts":
        [
        {
            "post_id":0,
            "message":"hello world",
            "posted_by":"john",
            "posted_at":"2022-08-26 14:29",
            "response_for":None
        },
        {
            "post_id":1,
            "message":"Fast API is Great",
            "posted_by":"mary",
            "posted_at":"2022-08-26 14:30",
            "response_for":0
        },
        ]
    }

@router.get("/posts/following")
def get_posts_following():
    return {"posts":
        [
        {
            "post_id":0,
            "message":"tweet by following user",
            "posted_by":"john",
            "posted_at":"2022-08-26 14:29",
            "response_for":None
        },
        ]
    }

@router.get("/posts/{username}")
def get_post_by_user(username:str):
    return {"posts":
        [
        {
            "post_id":0,
            "message":"tweet by same user",
            "posted_by":username,
            "posted_at":"2022-08-26 14:29",
            "response_for":None
        },
        {
            "post_id":1,
            "message":"tweet by same user",
            "posted_by":username,
            "posted_at":"2022-08-26 14:29",
            "response_for":None
        },
        ]
    }

@router.post("/posts/{username}")
def users_post(username:str):
    return 

@router.get("/posts/{username}/{post_id}")
def get_one_post_by_user(username:str,post_id:int):
    return {"posts":
        [
        {
            "post_id":post_id,
            "message":"tweet by particular user",
            "posted_by":username,
            "posted_at":"2022-08-26 14:29",
            "response_for":None
        },
        ]
    }

@router.delete("/posts/{username}/{post_id}")
def delete_post(username:str,post_id:int):
    return