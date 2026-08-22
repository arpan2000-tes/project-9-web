from fastapi import FastAPI, APIRouter
from api import routes

app = FastAPI()

app.include_router(routes)