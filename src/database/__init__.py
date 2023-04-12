import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

conn_str ="sqlite:///" + os.path.join(BASE_DIR, "database.db")

Base = declarative_base()
Session = sessionmaker()
engine = create_engine(conn_str, echo=True)
