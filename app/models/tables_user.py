from datetime import date, datetime
from typing import Optional, List, Dict
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship, Column, JSON
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import Column as SAColumn, Enum as SQLEnum
from flask_login import UserMixin
from app.enumerations.all_enumerations import (
    Role,
    NiveauAccesEnum,
    JobStaffEnum,
    LearnerLevelEnum,
)


class Password(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str
    user: Optional["User"] = Relationship(back_populates="password")

    def get_id(self):
        return str(self.id)


class User(SQLModel, UserMixin, table=True):
    Id_user: Optional[int] = Field(default=None, primary_key=True)
    firstname: str
    lastname: str
    email: str
    id_password: int = Field(foreign_key="password.id")
    role: Role = Field(sa_column=SAColumn(SQLEnum(Role), default=Role.LEARNER))

    password: Optional[Password] = Relationship(back_populates="user")
    trainer: Optional["Trainer"] = Relationship(back_populates="user")
    admin: Optional["Admin"] = Relationship(back_populates="user")
    teaching_staff: Optional["TeachingStaff"] = Relationship(back_populates="user")

    def get_id(self):
        return str(self.Id_user)


class Trainer(SQLModel, table=True):
    Id_trainer: Optional[int] = Field(default=None, primary_key=True)
    speciality: str
    hire_date: date
    hourly_rate: float
    bio: Optional[str] = None
    Id_user: int = Field(foreign_key="user.Id_user")

    user: Optional[User] = Relationship(back_populates="trainer")


class Admin(SQLModel, table=True):
    Id_admin: Optional[int] = Field(default=None, primary_key=True)
    date_promotion: date
    level_access: NiveauAccesEnum
    Id_user: int = Field(foreign_key="user.Id_user")

    user: Optional[User] = Relationship(back_populates="admin")


class TeachingStaff(SQLModel, table=True):
    Id_teaching_staff: Optional[int] = Field(default=None, primary_key=True)
    job: JobStaffEnum
    date_takingup_office: date
    responsabilities: Dict = Field(
        default={}, sa_column=Column(MutableDict.as_mutable(JSON))
    )
    Id_user: int = Field(foreign_key="user.Id_user")

    user: Optional[User] = Relationship(back_populates="teaching_staff")


class Learner(SQLModel, table=True):
    Id_learner: int | None = Field(default=None, primary_key=True)
    date_birth: date
    study_level: Optional[LearnerLevelEnum]
    phone_number: Optional[str]
    platform_registration_date: datetime = Field(default=datetime.now())
    certification_obtained: Optional[str]
    # Id_user: int = Field(foreign_key="user.Id_user")

    # user: Optional["User"] | None = Relationship(back_populates="room")

    registers: list["Register"] = Relationship(back_populates="learner")
