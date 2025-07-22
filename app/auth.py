from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, utils, database
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = models.User(name=user.name, password=utils.hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered"}

@router.post("/login", response_model=schemas.Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.name == form.username).first()
    if not user or not utils.verify_password(form.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = utils.create_access_token(data={"sub": str(user.id)})
    return {"access_token": token, "token_type": "bearer"}
