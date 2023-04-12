from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.database import conn_str

Base = declarative_base()
Session = sessionmaker()
engine = create_engine(conn_str, echo=True)
Session.configure(bind=engine)