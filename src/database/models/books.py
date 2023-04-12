from typing import Any, List

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Query

from src.database import Base, Session

local_session=Session()

class Book(Base):
    __tablename__ = 'books'
    id=Column(Integer(), primary_key=True)
    title=Column(String(255))
    year=Column(Integer())

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
        }

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, year={self.year})"

class BookRepository:
    def getAll() -> List[Book]:
        books = local_session.query(Book).all()
        return [x.as_dict() for x in books]

    def getOne(id: int) -> Book:
        book = local_session.query(Book).get(id)
        return book.as_dict()

    def filterBy(*args: Any) -> Query[Book]:
        return local_session.query(Book).filter_by(*args)

    def createOne(payload) -> None:
        try:
            book = Book(
                title = payload['title'],
                year = payload['year'],
            )
            local_session.add(book)
            local_session.commit()
            return
        except KeyError as e:
            raise KeyError(str(e)[1:-1])
        except Exception as e:
            raise e