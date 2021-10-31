"""Posts Schemas."""

# Utilities
import datetime

# Pydantic
from pydantic.main import BaseModel


class PostSchema(BaseModel):
    """Post schema."""

    id: int
    author_id: int
    about: str
    privacy: str
    location: str
    feeling: str
    post_id: int
    reactions: int
    comments: int
    shares: int
    created: datetime
    modified: datetime

    class Config:
        """Config options."""
        orm_mode = True