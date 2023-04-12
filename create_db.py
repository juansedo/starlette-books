from src.database import Base, engine
from src.database.models.books import Book

Base.metadata.create_all(bind=engine)
