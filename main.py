from signal import pause
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None    # If something is optional then provide a default value

#------- this is the path or the url --------
@app.get("/")  # this decorator is what converts this function here into a route or in FASTAPI we say path operation
def get():    # this is a python func and here the async keyword is operation only needed if the work is asynchronous
    return {"message": "hello world and we are in disect branch with a NOTES.txt"}


@app.get("/posts")
def get_posts():
    # logic here

    return {"data": "here the posts will come..."}


@app.post("/createposts")
def create_posts(payload: Post): # pydantic will automatically validate the data it receives
    print(payload)
    print(type(payload))
    print(payload.published)
    return {
        "message": "we received the data and the post is created",
        "title": payload.title,
        "content": payload.content,
        "published": payload.published,
        "rating": payload.rating
        }