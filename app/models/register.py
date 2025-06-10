from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Relationship
from enum import Enum
from app.models.course import Course
from app.models.tables_user import Learner


class RegisterStatutEnum(str, Enum):
    ENREGISTRE = "ENREGISTRE"
    DESINSCRIT = "DESINSCRIT"
    EN_ATTENTE = "EN_ATTENTE"


class Register(SQLModel, table=True):
    id_course: int = Field(foreign_key="course.id_course", primary_key=True)
    id_learner: int = Field(foreign_key="learner.id_learner", primary_key=True)
    registration_date: datetime = Field(default=datetime.now)
    registration_status: RegisterStatutEnum
    presence: Optional[bool]

    # course: Course | None = Relationship(back_populates="course")
    # learner: Learner | None = Relationship(back_populate="learner")
    course: Course | None = Relationship(back_populates="registers")
    learner: Learner | None = Relationship(back_populates="registers")


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)
