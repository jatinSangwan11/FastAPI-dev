from fastapi import FastAPI

app = FastAPI()

#------- this is the path or the url --------
@app.get("/")  # this decorator is what converts this function here into a route or in FASTAPI we say path operation
def get():    # this is a python func and here the async keyword is operation only needed if the work is asynchronous
    return {"message": "hello world and we are in disect branch with a NOTES.txt"}