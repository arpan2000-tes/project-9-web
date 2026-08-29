from pydantic import BaseModel ,EmailStr
from enum import Enum

class UserRoles(str, Enum):
   pelanggan = "pelanggan"
   kasir = "kasir"
   admin_gudang = "admin_gudang"
   hrd = "hrd"
   owner = "owner"
      
class Login(BaseModel):
   email : EmailStr
   password : str
   
class singnup (BaseModel):
   name : str
   email : EmailStr
   password : str
   
class email_tes(BaseModel):
   email : str