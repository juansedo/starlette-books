from sqlalchemy import Column, Integer, String

from . import Base


class Book(Base):
    __tablename__ = 'books'
    id=Column(Integer(), primary_key=True)
    title=Column(String(255))
    year=Column(Integer())

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, year={self.year})"