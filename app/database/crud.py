import uuid
from typing import Any

from sqlalchemy.orm import Session
from sqlalchemy import Select

from app.core.security import hasing_pass
from models.schemas import Users

def crete_user(*, session: Session, usercrate : Users) -> Users:
    db_obj = Users.model_validate(
        usercrate, update={"hashed_password": hasing_pass(usercrate.password)}
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj

def get_email(*,session : Session, email: str) -> User | None :
    statament = Select(User)