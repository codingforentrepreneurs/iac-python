from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_view():
    return  {"hello": "world", "cron": "this is working..."}


@app.post("/")
def home_post_view():
    return  {"hello": "world"}
