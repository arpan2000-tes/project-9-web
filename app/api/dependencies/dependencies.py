from sqlalchemy.orm import Session
from database import see

def get_db() :
    with Session()

def login (name : str , email : str , password : str ):
    return name, email , password_hash