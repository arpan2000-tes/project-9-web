from pydantic import BaseModel
from enum import Enum

class userroles(str, Enum):
   pelanggan = "pelanggan"
   kasir = "kasir"
   admin_gudang = "admin_gudang"
   hrd = "hrd"
   owner = "owner"

class user(BaseModel):
   name : str
   email : str
   password : str
   roles : userroles = userroles.pelanggan
      