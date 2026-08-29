from sqlalchemy.orm import Session 

from app.database.db import sessionlocal
from app.core.security import hasing_pass
from app.models.schemas.users import email_tes
from app.models.user import UserBase

def get_db() :
    db = sessionlocal()
    try:
        yield db
    finally :
        db.close()

def log_IN_up (request: email_tes, db: Session ):
    user_exists = db.query(UserBase).filter(UserBase.email == request.email).first()
    return user_exists

