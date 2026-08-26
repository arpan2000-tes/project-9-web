from fastapi import APIRouter , HTTPException, Depends, requests
from app.models.schemas import Users , Login
from typing import Annotated
from app.api.dependencies import login

routes = APIRouter()

@routes.post("/signin")
def signin (User_Login : Annotated[dict,Depends(login)] ):
    if User_Login != Login :
        return HTTPException (status_code=401, detail="wrong email or password")
    
@routes.post("/signup")
def signup(new_users: Users, sess):
    pass