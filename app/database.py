from sqlmodel import SQLModel, create_engine, Session
from app.models.course import Course
from app.models.tables_user import User, Admin, Learner, TeachingStaff, Trainer
from app.models.room import Room

# from app.models.admin import
from app.models.equipment import Equipment

# from app.models.learner import
from app.models.register import Register

# from app.models.teaching_staff import
# from app.models.trainer import

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
