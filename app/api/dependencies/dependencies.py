from sqlalchemy.orm import Session
from app.database.db import sessionlocal

def get_db() :
    db = sessionlocal()
    try:
        yield db
    finally :
        db.close()

def login (name : str , email : str , password : str ):
    return name, email , password_hash