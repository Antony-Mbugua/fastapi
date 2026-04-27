# main.py — FastAPI Capstone Project
# Author: Antony Mbugua Githinji

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

# ✅ DEFINE APP FIRST
app = FastAPI(
    title="TechRealm's FastAPI Capstone",
    description="A beginner's REST API built with FastAPI",
    version="1.0.0"
)

# ✅ NOW it's safe to use @app
@app.get('/ui', response_class=HTMLResponse)
def ui():
    return '''
    <html>
    <head><title>Antony's FastAPI Capstone</title></head>
    <body style="font-family:Arial;max-width:600px;margin:60px auto;padding:20px">
      <h1 style="color:#1F3864">FastAPI Capstone API</h1>
      <p>Author: Antony Mbugua Githinji</p>
      <ul>
        <li><a href="/">GET /</a> — Welcome message</li>
        <li><a href="/greet/Antony">GET /greet/Antony</a> — Greeting</li>
        <li><a href="/docs">GET /docs</a> — Interactive API docs</li>
      </ul>
    </body></html>
    '''

# Data model
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.get("/")
def read_root():
    return {"message": "Hello! This is Antony Mbugua Githinji's FastAPI Capstone."}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": f"Hello, {name}! Welcome to my capstone API."}

@app.post("/items/")
def create_item(item: Item):
    return {"status": "Item created successfully", "item": item}