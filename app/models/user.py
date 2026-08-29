from sqlalchemy import Column, Integer , String , Boolean

from app.database.base import Base
from app.models.schemas import UserRoles

class UserBase(Base):
   __tablename__ = "users"
   
   id = Column(Integer,primary_key=True, index=True) 
   name = Column(String)
   email = Column(String, unique=True, index=True)
   password = Column(String)
   is_verified = Column(Boolean, default=False)
   roles = UserRoles = UserRoles.pelanggan