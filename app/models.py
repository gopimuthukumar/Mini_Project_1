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
