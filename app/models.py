<<<<<<< HEAD
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
=======
# app/models.py
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False, index=True)  # <-- ✅ FIXED
    password = Column(String(255), nullable=False)
    is_active = Column(Integer, default=1)
    otp = Column(String(10), nullable=True)
>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70
