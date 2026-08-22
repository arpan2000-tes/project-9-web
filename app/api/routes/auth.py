from fastapi import APIRouter , HTTPException, Depends
from schemas import user
from typing import Annotated
from dependencies import login

routes = APIRouter()

@routes.post("/signin")
def signin (users: Annotated[Depends(login)] ):
    if users != user :
        return HTTPException (status_code=401, detail="wrong email or password")