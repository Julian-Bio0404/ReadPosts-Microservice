# Database
import database
from app.database import SessionLocal, engine


def create_database():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()