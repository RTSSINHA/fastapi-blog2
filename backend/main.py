from fastapi import FastAPI
from core.config import config
from db.session import engine
from db.base_class import Base

def create_table():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=config.PROJECT_TITLE, version=config.PROJECT_VERSION)
    create_table()
    return app

app = start_application()

@app.get("/")
def sayHello():
    return "Hello world!"

