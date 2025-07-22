<<<<<<< HEAD
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class BookCreate(BaseModel):
    name: str
    author: str

class BookOut(BookCreate):
    id: int
    class Config:
        from_attributes = True

class ReviewCreate(BaseModel):
    book_id: int
    rating: int
=======
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ShowUser(BaseModel):
    email: EmailStr
    class Config:
       from_attributes = True
>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70
