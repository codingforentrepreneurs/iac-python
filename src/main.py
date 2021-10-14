from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_view():
    return  {"hello": "world", "msg": "iac is amazing", "cron": "is working well"}


@app.post("/")
def home_post_view():
    return  {"hello": "world"}
