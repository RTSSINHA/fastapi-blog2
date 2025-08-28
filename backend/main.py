from fastapi import FastAPI
from core.config import config

app = FastAPI(title=config.PROJECT_TITLE, version=config.PROJECT_VERSION)

@app.get("/")
def sayHello():
    return "Hello world!"

