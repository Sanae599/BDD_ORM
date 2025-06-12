from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime, timezone
from sqlalchemy import UniqueConstraint
from app.enumerations.all_enumerations import RegistrationStatusEnum


class Register(SQLModel, table=True):
    id_register: Optional[int] = Field(default=None, primary_key=True)
    id_learner: int = Field(foreign_key="tables_users.learner.id_learner") 
    id_course: int = Field(foreign_key="course.id_course")  #
    registration_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    registration_status: RegistrationStatusEnum = Field(default=RegistrationStatusEnum.en_attente)
    presence: Optional[bool] = None

    __table_args__ = (
        UniqueConstraint("id_learner", "id_session"),
    )