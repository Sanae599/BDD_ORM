from sqlmodel import SQLModel
from typing import Optional, Dict
from datetime import date
from pydantic import field_validator
from app.enumerations.all_enumerations import JobStaffEnum


#Création (POST)
class TeachingStaffCreate(SQLModel):
    job: JobStaffEnum
    date_takingup_office: date
    responsabilities: Optional[Dict] = {}
    Id_user: int  # Clé étrangère vers la table user

    @field_validator("date_takingup_office")
    def validate_date(cls, value):
        if value > date.today():
            raise ValueError("La date de prise de fonction ne peut pas être dans le futur")
        return value


#Lecture (GET)
class TeachingStaffRead(TeachingStaffCreate):
    Id_teaching_staff: int


#Mise à jour (PATCH)
class TeachingStaffUpdate(SQLModel):
    job: Optional[JobStaffEnum] = None
    date_takingup_office: Optional[date] = None
    responsabilities: Optional[Dict] = None
    Id_user: Optional[int] = None

    @field_validator("date_takingup_office")
    def validate_date(cls, value):
        if value and value > date.today():
            raise ValueError("La date de prise de fonction ne peut pas être dans le futur")
        return value
