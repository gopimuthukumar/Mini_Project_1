from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
<<<<<<< HEAD
from app import models, schemas, utils, database
from fastapi.security import OAuth2PasswordRequestForm
=======
from app.database import get_db
from app import models, schemas, utils
>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70

router = APIRouter()

@router.post("/register")
<<<<<<< HEAD
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
=======
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    user_model = models.User(email=user.email, password=utils.hash_password(user.password))
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return {"message": "User registered"}

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not utils.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Logged in successfully"}

@router.post("/logout")
def logout():
    return {"message": "User logged out"}
>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70
