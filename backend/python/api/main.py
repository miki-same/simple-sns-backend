from fastapi import FastAPI
from routers import users,posts,likes,follow,search
app=FastAPI()

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(likes.router)
app.include_router(follow.router)
app.include_router(search.router)

@app.get("/hello")
def hello():
    return {"message": "hello world!"}