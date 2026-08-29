from fastapi import FastAPI, APIRouter
from app.api.routes import API_Routes
from app.database.base import Base
from app.database.db import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def get():
    return {"hello": "world"}

app.include_router(API_Routes, prefix="/api/v1")