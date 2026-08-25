import bcrypt

def hasing_pass(password: str):
    bytes_key = password.encode('utf-8')
    hashed = bcrypt.hashpw(bytes_key,bcrypt.gensalt(14))
    return hashed