from sqlalchemy.orm import Session

def get_db() :
    with Session()

def login (name : str , email : str , password : str ):
    return name, email , password_hash