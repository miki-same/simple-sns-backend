from fastapi import APIRouter

router=APIRouter()

@router.get("/likes/{username}")
def get_likes(username:str):
    return {"liked_posts":[
        {
            "post_id":0,
            "message":"liked_tweet",
            "posted_by":"john",
            "posted_at":"2022-08-26 14:29",
            "response_for":None
        },
        {
            "post_id":1,
            "message":"liked_tweet_2",
            "posted_by":"michel",
            "posted_at":"2022-08-26 14:29",
            "response_for":None
        },
    ]}

@router.get("/likes/{username}/{post_id}")
def get_users_liked(username:str, post_id:int):
    return {"users":[
            {
                    "username":"taro",
                    "mail":"hoge@gmail.com"
            },
            {
                    "username":"jiro",
                    "mail":"hoge@gmail.com"
            },    
        ]
    }

@router.post("/likes/{username}/{post_id}")
def like_to_post(username:str,post_id:int):
    return

@router.delete("/likes/{username}/{post_id}")
def delete_like_to_post(username:str,post_id:int):
    return 