"""Main."""

# FastApi
from fastapi import FastAPI

# Starlette
from starlette import status


app = FastAPI()


@app.get(path='/', status_code=status.HTTP_200_OK)
def home():
    return {'Saludo': 'Hello World!'}