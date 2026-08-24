import bcrypt

def hash_any(key: str):
    hashed = bcrypt.hashpw(key,bcrypt.gensalt(14))
    return hashed

def hasing_pass(password: str):
    return hash_any(password)