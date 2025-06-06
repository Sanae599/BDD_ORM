from sqlmodel import SQLModel, create_engine, Session
from app.models.course import Course
from app.models.user import User  # Import nécessaire pour créer les tables
from app.models.room import Room
from app.models.admin import Admin
from app.models.equipment import Equipment
from app.models.learner import Learner
from app.models.register import Register
from app.models.teaching_staff import TeachingStaff
from app.models.trainer import Trainer

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
