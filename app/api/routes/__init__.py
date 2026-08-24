from fastapi import APIRouter

from .auth import routes

API_Routes = APIRouter()

API_Routes.include_router(routes, prefix="/auth", tags=["auth"])