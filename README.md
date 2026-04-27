# FastAPI Capstone Project

**Author:** Antony Mbugua Githinji  
**Technology:** FastAPI (Python)  
**Purpose:** Developer Toolkit Capstone Project

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | / | Welcome message |
| GET | /greet/{name} | Returns a greeting |
| POST | /items/ | Create an item (JSON body) |
| GET | /docs | Interactive Swagger UI |

## Project Structure

```
fastapi-capstone/
├── main.py           # API code
├── requirements.txt  # Dependencies
├── README.md         # This file
└── .gitignore        # Git exclusions
```