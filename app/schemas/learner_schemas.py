from sqlmodel import SQLModel
from typing import Optional
from datetime import datetime, date
from pydantic import field_validator
from app.enumerations.all_enumerations import LearnerLevelEnum
import re

class LearnerCreate(SQLModel):
    date_birth: date
    study_level: Optional[LearnerLevelEnum]
    phone_number: Optional[str]
    platform_registration_date: datetime = datetime.now()
    certification_obtained: Optional[str]
    Id_user: int 

    @field_validator("date_birth")
    def validate_age(cls, value):
        age = (date.today() - value).days // 365
        if age < 16:
            raise ValueError("L'apprenant doit avoir au moins 16 ans")
        return value

    @field_validator("phone_number")
    def validate_phone(cls, value):
        if value:
            #Dans notre cas numéro français : 10 chiffres, commence par 0
            if not re.fullmatch(r"0\d{9}", value):
                raise ValueError("Numéro de téléphone invalide")
        return value

class LearnerRead(LearnerCreate):
    Id_learner: int

class LearnerUpdate(SQLModel):
    date_birth: Optional[date] = None
    study_level: Optional[LearnerLevelEnum] = None
    phone_number: Optional[str] = None
    platform_registration_date: Optional[datetime] = None
    certification_obtained: Optional[str] = None
    Id_user: Optional[int] = None

    @field_validator("date_birth")
    def validate_age(cls, value):
        if value:
            age = (date.today() - value).days // 365
            if age < 16:
                raise ValueError("L'apprenant doit avoir au moins 16 ans")
        return value

    @field_validator("phone_number")
    def validate_phone(cls, value):
        if value:
            if not re.fullmatch(r"0\d{9}", value):
                raise ValueError("Numéro de téléphone invalide")
        return value
