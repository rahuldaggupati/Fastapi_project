
from fastapi import FastAPI
from database import engine, Base
from routers import router
import logging

logging.basicConfig(level=logging.INFO)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "running", "docs": "/docs"}
