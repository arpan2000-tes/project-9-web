from fastapi import APIRouter , HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.schemas import singnup , Login
from app.api.dependencies import log_IN_up, get_db
from app.models.user import UserBase
from app.core.security import hasing_pass

routes = APIRouter()

@routes.post("/signin")
def signin (User_Login : Login, db: Session = Depends(get_db)) :
    if log_IN_up (User_Login, db) :
        return HTTPException (status_code=401, detail="wrong email or password")
    return User_Login
    
@routes.post("/signup")
def signup(new_users: singnup, db: Session = Depends(get_db)):
    log_IN_up(new_users, db)
    if new_users:
        return HTTPException (status_code=401, detail="alredy email")
    
    new_users_signup = UserBase(
        name=new_users.name,
        email=new_users.email,
        password=hasing_pass(new_users.password),
        is_verified=False
    )
    
    db.add(new_users_signup)
    db.commit()
    db.refresh(new_users_signup)
    
    return{"message": "newuser add"}