import os
from dotenv import load_dotenv, find_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv(find_dotenv())
URL_DATABASE_NEON = os.getenv("DATABASE_URL")

engine = create_engine(URL_DATABASE_NEON)
sessionlocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)

base = declarative_base()