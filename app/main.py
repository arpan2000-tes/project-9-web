from fastapi import FastAPI, APIRouter
from app.api.routes import API_Routes

app = FastAPI()

app.include_router(API_Routes, prefix="api/v1")