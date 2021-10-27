"""Database configuration."""

from decouple import config

# SQLalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine(config('POSTGRES_URL'), echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)