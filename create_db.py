from src.database import Base, engine
from src.database.models import Book

Base.metadata.create_all(bind=engine)
