from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List, Dict, Optional
from db import users
from pydantic import BaseModel

class Notification(BaseModel):
    author: str
    description: str

class User(BaseModel):
    name: str
    username: str
    email: str
    birthday: str
    friends: List[str]
    notifications: List[Notification]

class UserDB(User):
    hashed_password: str

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name= "static")

@app.get("/")
def root():
    return {"set": "up!"}