from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, utils

router = APIRouter()

@router.post("/get-otp")
def get_otp(email: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    otp = utils.generate_otp()
    user.otp = otp
    db.commit()
    return {"otp": otp}  # Replace this with email sending logic in production

@router.post("/reset-password")
def reset_password(email: str, otp: str, new_password: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == email, models.User.otp == otp).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid OTP or email")
    user.password = utils.hash_password(new_password)
    user.otp = None
    db.commit()
    return {"message": "Password reset successful"}
