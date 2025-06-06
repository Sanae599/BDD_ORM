from datetime import date
from typing import Dict, Optional
from sqlmodel import SQLModel, Field, Relationship, Column, JSON
from enum import Enum
from sqlalchemy.ext.mutable import MutableDict

class JobStaffEnum(str, Enum):
    ResponsablePedagogique = "Responsable pédagogique"
    ChargeeProjet = "CHargée de projet"

class TeachingStaff(SQLModel, table=True):
    Id_teaching_staff: int | None = Field(default=None, primary_key=True)
    job: JobStaffEnum 
    date_takingup_office: date 
    responsabilities: Dict = Field(default={}, sa_column=Column(MutableDict.as_mutable(JSON)))
    Id_user: int = Field(foreign_key="user.Id_user")

    user: ["User"] = Relationship(back_populates="user")
