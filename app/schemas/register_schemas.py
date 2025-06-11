from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime
from enum import Enum
from pydantic import field_validator
from app.enumerations.all_enumerations import RegisterStatus

#Schéma de création d’une inscription (POST)
class RegisterCreate(SQLModel):
    id_learner: int
    id_course: int
    registration_date: Optional[datetime] = None  # auto si non fourni
    status: RegisterStatus = RegisterStatus.ENREGISTRE
    presence: Optional[bool] = None

    @field_validator("registration_date")
    def default_registration_date(cls, v):
        return v or datetime.now()


#Schéma de lecture d’une inscription (GET)
class RegisterRead(RegisterCreate):
    id_register: int  


#Schéma de mise à jour partielle d’une inscription (PATCH)
class RegisterUpdate(SQLModel):
    id_learner: Optional[int] = None
    id_course: Optional[int] = None
    registration_date: Optional[datetime] = None
    status: Optional[RegisterStatus] = None
    presence: Optional[bool] = None
