from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

@router.post("/books")
def add_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    return db_book

@router.get("/books", response_model=list[schemas.BookOut])
def get_books(db: Session = Depends(database.get_db)):
    return db.query(models.Book).all()
