from sqlalchemy import Column, Integer, String

from src.database import Base, Session


class Book(Base):
    __tablename__ = 'books'
    id=Column(Integer(), primary_key=True)
    title=Column(String(255))
    year=Column(Integer())

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, year={self.year})"

class BookRepository:
    local_session=Session()

    def getAll():
        return BookRepository.local_session.query(Book).all()