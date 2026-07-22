from turtle import title
from fastapi import Body, FastAPI


app = FastAPI()

#------- this is the path or the url --------
@app.get("/")  # this decorator is what converts this function here into a route or in FASTAPI we say path operation
def get():    # this is a python func and here the async keyword is operation only needed if the work is asynchronous
    return {"message": "hello world and we are in disect branch with a NOTES.txt"}


@app.get("/posts")
def get_posts():
    # logic here

    return {"data": "here the posts will come..."}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    print(type(payload))
    data = {}
    for key in payload:
        print(f"This is the {key}: {payload[key]}")
        data[key] = payload[key]
    return {
        "message": "we received the data and the post is created",
        "title": data["title"],
        "content": data["content"]
        }