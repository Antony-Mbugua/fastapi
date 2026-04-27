# main.py — FastAPI Capstone Project
# Author: Antony Mbugua Githinji

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="TechRealm's FastAPI Capstone",
    description="A beginner's REST API built with FastAPI",
    version="1.0.0"
)

# Data model — FastAPI validates incoming data automatically
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

# GET / — Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello! This is Antony Mbugua Githinji's FastAPI Capstone."}

# GET /greet/{name} — Greeting with a path parameter
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": f"Hello, {name}! Welcome to my capstone API."}

# POST /items/ — Accepts JSON body, validates it, returns it
@app.post("/items/")
def create_item(item: Item):
    return {"status": "Item created successfully", "item": item}