"""Posts Schemas."""

# Utilities
from typing import Optional

# Pydantic
from pydantic.main import BaseModel

# Schemas
from .users import User


class PostBase(BaseModel):
    """Post Base schema."""

    author_id: int
    about: str
    privacy: str
    location: str
    feeling: str
    created: str

    class Config:
        """Config options."""
        orm_mode = True


class Post(PostBase):
    """Post schema."""

    id: int
    post: Optional[PostBase]

    class Config:
        """Config options."""
        orm_mode = True