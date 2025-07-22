from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint,VARCHAR
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    status = Column(VARCHAR, default="active")

    reviews = relationship("Review", back_populates="user")

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    author = Column(String, nullable=False)
    status = Column(VARCHAR, default="available")

    reviews = relationship("Review", back_populates="book")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    rating = Column(Integer)

    __table_args__ = (UniqueConstraint('book_id', 'user_id', name='unique_user_review'),)

    book = relationship("Book", back_populates="reviews")
    user = relationship("User", back_populates="reviews")
