"""Main."""

# FastApi
from fastapi import FastAPI

# Starlette
from starlette import status

# Database
from .database import SessionLocal, engine


app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get(path='/', status_code=status.HTTP_200_OK)
def home():
    return {'Saludo': 'Hello World!'}