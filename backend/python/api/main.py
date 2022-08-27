from fastapi import FastAPI, File, UploadFile
from routers import users,posts,likes,follow,search
import shutil
import os
app=FastAPI()

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(likes.router)
app.include_router(follow.router)
app.include_router(search.router)

@app.get("/hello")
def hello():
    return {"message": "hello world!"}

UPLOAD_DIR = "./static/img"

@app.post("/file_upload")
def file_upload(file: UploadFile = File(None)):
    if file:
        filename=file.filename
        fileobj=file.file
        
        with open(UPLOAD_DIR+f'/{filename}', 'w+b') as upload_dir:
            shutil.copyfileobj(fileobj,upload_dir)

        return {
            "filename":file.filename
        }
    
    return {"Detail": "File not uploaded"}