from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
<<<<<<< HEAD
from dotenv import load_dotenv
import os
=======
import os
from dotenv import load_dotenv
>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

<<<<<<< HEAD
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

=======
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=False, future=True)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to be used in FastAPI routes
>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
<<<<<<< HEAD
=======

>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70
