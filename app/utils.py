from passlib.context import CryptContext
<<<<<<< HEAD
from datetime import datetime, timedelta
from jose import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
=======
import random

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70

def hash_password(password: str):
    return pwd_context.hash(password)

<<<<<<< HEAD
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict, expires_minutes: int = 30):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
=======
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def generate_otp():
    return str(random.randint(100000, 999999))
>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70
