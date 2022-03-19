from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_view():
    return  {"hello": "world", "cron": "smooth-cronjob", "watchtower": "working"}


@app.post("/")
def home_post_view():
    return  {"hello": "world"}
