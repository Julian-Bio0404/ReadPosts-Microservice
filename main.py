"""Main."""

# Utilities
from typing import List

# FastApi
from fastapi import FastAPI
from fastapi.params import Depends

# SQLalchemy
from sqlalchemy.orm.session import Session

# Starlette
from starlette import status

# Database
from app import services

# Models
from app.models import Post

# Schemas
from app.schemas import PostSchema


app = FastAPI()

services.create_database()


@app.get(path='/', status_code=status.HTTP_200_OK)
def home():
    return {'Saludo': 'Hello World!'}


@app.get(
    path='/posts/',
    response_model=List[PostSchema],
    status_code=status.HTTP_200_OK
)
def list_posts(db: Session=Depends(services.get_db)):
    """List all posts."""
    posts = db.query(Post).all()
    return posts

@app.get(
    path='/posts/{id}',
    response_model=PostSchema,
    status_code=status.HTTP_200_OK
)
def get_post(id: int, db: Session=Depends(services.get_db)):
    """Retrive a post."""
    post = db.query(Post).filter(Post.id==id)