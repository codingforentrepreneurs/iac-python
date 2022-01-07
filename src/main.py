from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_view():
    return  {"hello": "world", "cron": "welcome-home"}


@app.post("/")
def home_post_view():
    return  {"hello": "world"}
