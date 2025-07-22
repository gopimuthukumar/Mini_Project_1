from fastapi import FastAPI
from app import models, database, auth, otp

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(auth.router)
app.include_router(otp.router)

