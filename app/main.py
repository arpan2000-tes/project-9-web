from fastapi import FastAPI, APIRouter
from app.api.routes import API_Routes

app = FastAPI()

@app.get("/")
def get():
    return {"hello": "world"}

app.include_router(API_Routes, prefix="/api/v1")