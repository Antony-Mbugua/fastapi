# FastAPI Capstone Project

**Author:** Antony Mbugua Githinji  
**Technology:** FastAPI (Python)  
**Python Version:** 3.12 (recommended)  
**Purpose:** Developer Toolkit Capstone Project

This project is a simple REST API built using FastAPI. It demonstrates routing, path parameters, JSON validation using Pydantic, and automatic API documentation via Swagger UI.

The project must always be run inside a virtual environment to isolate dependencies.

---

## Setup Instructions

Create the project folder and enter it:
mkdir fastapi-capstone  
cd fastapi-capstone  

Create a virtual environment:
python -m venv venv  

Activate the virtual environment (Windows PowerShell):
.\venv\Scripts\Activate.ps1  

If activation is blocked, run:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned  
then activate again:
.\venv\Scripts\Activate.ps1  

Upgrade pip:
python -m pip install --upgrade pip  

Install dependencies:
pip install fastapi uvicorn  

Freeze dependencies into a requirements file:
pip freeze > requirements.txt  

---

## Application Code (main.py)

Create a file named main.py and add the following code:

from fastapi import FastAPI  
from pydantic import BaseModel  

app = FastAPI(  
    title="Antony's FastAPI Capstone",  
    description="A beginner's REST API built with FastAPI",  
    version="1.0.0"  
)  

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

---

## Run the Application

Start the server with:
uvicorn main:app --reload  

Then open in browser:

http://127.0.0.1:8000/  
http://127.0.0.1:8000/greet/Antony  
http://127.0.0.1:8000/docs  

---

## API Endpoints

GET / → Welcome message  
GET /greet/{name} → Personalized greeting  
POST /items/ → Create item (JSON body)  
GET /docs → Interactive Swagger UI  

---

## Project Structure

fastapi-capstone/  
├── main.py  
├── requirements.txt  
├── README.md  
├── venv/ (NOT committed to git)  
└── .gitignore  

---

## Git Setup

Initialize repository:
git init  

Add files:
git add .  

Commit:
git commit -m "Initial commit: FastAPI capstone project"  

Set identity (first time only):
git config --global user.name "Your Name"  
git config --global user.email "you@example.com"  

---

## .gitignore

Ensure this is included:
venv/  
__pycache__/  
*.pyc  
.env  

---

## Important Notes

The virtual environment is local-only and must not be pushed to GitHub. Only requirements.txt is used to recreate dependencies elsewhere.

Always ensure:
- venv is activated before running the app
- Python version is stable (3.10–3.12 recommended; avoid unstable alpha builds)
- dependencies are installed inside the active environment

---

## Author

Antony Mbugua Githinji