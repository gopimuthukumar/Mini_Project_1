from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database,utils
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    try:
        payload = jwt.decode(token, utils.SECRET_KEY, algorithms=[utils.ALGORITHM])
        user_id = int(payload.get("sub"))
        return db.query(models.User).filter(models.User.id == user_id).first()
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/review")
def review_book(review: schemas.ReviewCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    existing = db.query(models.Review).filter_by(book_id=review.book_id, user_id=current_user.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="You have already reviewed this book.")
    new_review = models.Review(book_id=review.book_id, user_id=current_user.id, rating=review.rating)
    db.add(new_review)
    db.commit()
    return {"message": "Review submitted"}
