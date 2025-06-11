from typing import Optional, List, Dict
from datetime import datetime, date, timezone
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
from sqlalchemy.sql import func

class UserBase(SQLModel, table=False):
    firstname: str
    lastname: str
    email: str = Field(unique=True)
    password: str
    date_creation: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))    
    role: Role = Field(sa_column=SAColumn(SQLEnum(Role), default=Role.LEARNER))
    is_active: Optional[bool] = True
    
class Trainer(UserBase, table=True):
    # https://docs.sqlalchemy.org/en/20/orm/inheritance.html
    # mapper args pour créer les tables enfants avec les champs de la table parent
    __mapper_args__ = {'concrete': True}
    id_trainer: Optional[int] = Field(default=None, primary_key=True)
    role: Role = Field(sa_column=SAColumn(SQLEnum(Role), default=Role.TRAINER))
    speciality: str
    hire_date: date
    hourly_rate: float
    bio: Optional[str] = None

    def get_id(self):
        return self.id_trainer

class Admin(UserBase, table=True):
    __mapper_args__ = {'concrete': True}
    id_admin: Optional[int] = Field(default=None, primary_key=True)
    role: Role = Field(sa_column=SAColumn(SQLEnum(Role), default=Role.ADMIN))
    date_promotion: date
    level_access: NiveauAccesEnum

    def get_id(self):
        return self.id_admin

class TeachingStaff(UserBase, table=True):
    __mapper_args__ = {'concrete': True}
    id_staff: Optional[int] = Field(default=None, primary_key=True)
    role: Role = Field(sa_column=SAColumn(SQLEnum(Role), default=Role.STAFF))
    job: JobStaffEnum
    date_takingup_office: date
    responsabilities: Dict = Field(
        default={}, sa_column=Column(MutableDict.as_mutable(JSON))
    )

    def get_id(self):
        return self.id_staff

class Learner(UserBase, SQLModel, table=True):
    __mapper_args__ = {'concrete': True}
    id_learner: Optional[int] = Field(default=None, primary_key=True)
    role: Role = Field(sa_column=SAColumn(SQLEnum(Role), default=Role.LEARNER))
    date_birth: date
    study_level: Optional[LearnerLevelEnum]
    phone_number: Optional[str]
    platform_registration_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    certification_obtained: Optional[str]

    def get_id(self):
        return str(self.id_learner)

    registers: List["Register"] = Relationship(back_populates="learner")
