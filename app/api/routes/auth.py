from fastapi import APIRouter , HTTPException, Depends, requests
from app.models.schemas import Users , Login
from typing import Annotated
from api.dependencies import login

routes = APIRouter()

@routes.post("/signin")
def signin (Login : Annotated[dict,Depends(login)] ):
    if Login != Login :
        return HTTPException (status_code=401, detail="wrong email or password")
    
@routes.post("/signup")
def signup(new_users: Users, sess):
    for Users