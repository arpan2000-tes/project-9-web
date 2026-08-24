import uuid
from typing import Any

from sqlalchemy.orm import session
from sqlalchemy import Select

from models.schemas import Users

def crete_user(*, session: session, usercrate : Users) -> Users:
    db_obj = Users.model_validate(
        usercrate, update={"hashed_password": }
    )