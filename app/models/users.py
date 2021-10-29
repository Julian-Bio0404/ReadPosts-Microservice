"""User models."""

# SQLalchemy
from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

# Databese
from database import Base


class User(Base):
    """User model."""

    __tablename__ = 'users_user'

    id = Column(Integer, primary_key=True, index=True)
    password = Column(String(128))
    last_login = Column(DateTime)
    is_superuser = Column(Boolean, default=False)
    username = Column(String(150), unique=True)
    first_name = Column(String(150))
    last_name = Column(String(150))
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    date_joined = Column(DateTime)
    created = Column(DateTime)
    modified = Column(DateTime)
    email = Column(String(254), unique=True, index=True)
    phone_number = Column(String(17))
    verified = Column(Boolean, default=False)
    role = Column(String(16))

    posts = relationship('Post', back_populates='author')