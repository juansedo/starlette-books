from src.database import Base, engine
from src.database.models.books import Book

Book.__table__.drop(engine)
