import bcrypt

def hash_any(key: str):
    bytes_key = key.encode('utf-8')
    hashed = bcrypt.hashpw(bytes_key,bcrypt.gensalt(14))
    return hashed

def hasing_pass(password: str):
    return hash_any(password)