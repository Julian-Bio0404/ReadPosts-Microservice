"""Users schemas."""

# Pydantic
from pydantic.main import BaseModel


class User(BaseModel):
    """User schema."""

    username: str

    class Config:
        """Config options."""
        orm_mode = True