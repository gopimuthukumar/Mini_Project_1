from fastapi import FastAPI
<<<<<<< HEAD
from app import models, database, auth, books, reviews
=======
from app import models, database, auth, otp
>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(auth.router)
<<<<<<< HEAD
app.include_router(books.router)
app.include_router(reviews.router)
=======
app.include_router(otp.router)

>>>>>>> 47107c79f7b4d4bc179df40632b66393ba51bb70
