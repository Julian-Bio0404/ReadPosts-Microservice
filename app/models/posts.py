"""Post models."""

# Utilities
import datetime

# SQLalchemy
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

# Database
from app.database import Base


class Post(Base):
    """Post model."""

    __tablename__ = 'posts_post'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey('users_user.id'))
    about = Column(String)
    privacy = Column(String(7))
    location = Column(String(60))
    feeling = Column(String(9))
    post_id = Column(Integer)
    reactions = Column(Integer)
    comments = Column(Integer)
    shares = Column(Integer)
    created = Column(DateTime, default=datetime.timezone)
    modified = Column(DateTime, default=datetime.timezone)

    author = relationship('User', back_populates='posts')