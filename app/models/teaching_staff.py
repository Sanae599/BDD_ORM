from datetime import date
from typing import Dict, Optional
from sqlmodel import SQLModel, Field, Relationship
from user import UserBase
from enum import Enum

class JobStaffEnum(str, Enum):
    ResponsablePedagogique = "Responsable pédagogique"
    ChargeeProjet = "CHargée de projet"

class TeachingStaff(SQLModel, table=True):
    Id_teaching_staff: int | None = Field(default=None, primary_key=True)
    job: JobStaffEnum 
    date_takingup_office: date 
    responsabilities: Optional[Dict]
    Id_user: int = Field(foreign_key="user.Id_user")

    user: UserBase | None = Relationship(back_populates="user")
