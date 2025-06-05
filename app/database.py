from sqlmodel import SQLModel, create_engine, Session
from app.models.user import UserBase  # Import nécessaire pour créer les tables

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
