import datetime

from pydantic import BaseModel, EmailStr, BaseConfig
from enum import Enum


class UserRoles(str, Enum):
   pelanggan = "pelanggan"
   kasir = "kasir"
   admin_gudang = "admin_gudang"
   hrd = "hrd"
   owner = "owner"

class Users(BaseModel):
   name : str
   email : EmailStr
   password : str
   is_verified: bool = False
   roles : UserRoles = UserRoles.pelanggan
      
class Login(BaseModel):
   name : str
   password : str
   