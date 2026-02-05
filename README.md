#  FastAPI CRUD Application

A simple FastAPI backend project demonstrating CRUD operations with a modular structure using:

- FastAPI  
- SQLAlchemy  
- Pydantic  
- SQLite (default DB)

---

##  Project Structure

main.py # App entry point
database.py # DB connection & session
models.py # SQLAlchemy models
schemas.py # Pydantic schemas
crud.py # Database logic
routers.py # API routes
requirements.txt
.gitignore
README.md


---

## Prerequisites

- Python 3.9+
- pip

---

##  Setup (Local)

### 1. Create virtual environment (recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
2. Install dependencies
pip install -r requirements.txt
Run the Application
From the folder containing main.py:

uvicorn main:app --reload
Server will start at:

http://127.0.0.1:8000
API Docs
Swagger UI:

http://127.0.0.1:8000/docs
ReDoc:

http://127.0.0.1:8000/redoc
Database
Uses SQLite by default
DB file is auto-created on first run

Change DB URL in database.py to use PostgreSQL/MySQL if needed

Usage
Start server

Open /docs

Use POST to create data

GET to fetch

PUT to update

DELETE to remove

All routes are defined in routers.py.

