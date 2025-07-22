from fastapi import FastAPI
from app import models, database, auth, books, reviews

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(books.router)
app.include_router(reviews.router)
