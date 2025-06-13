import re
from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, field_validator
from app.enumerations.all_enumerations import Role, LearnerLevelEnum


#Base commune (non utilisée directement)
class LearnerBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    role: Role = Role.LEARNER

    date_birth: date
    study_level: Optional[LearnerLevelEnum] = None
    phone_number: Optional[str] = None
    certification_obtained: Optional[str] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("date_birth")
    def validate_age(cls, value: date) -> date:
        age = (date.today() - value).days // 365
        if age < 16:
            raise ValueError("L'apprenant doit avoir au moins 16 ans")
        return value

    @field_validator("phone_number")
    def validate_phone(cls, value: Optional[str]) -> Optional[str]:
        if value and not re.fullmatch(r"0\d{9}", value):
            raise ValueError("Numéro de téléphone invalide")
        return value


#Création (POST)
class LearnerCreate(LearnerBase):
    platform_registration_date: datetime = datetime.now()


#Lecture complète (GET)
class LearnerRead(LearnerBase):
    id: int
    platform_registration_date: datetime


#Lecture publique pour le front
class LearnerPublic(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    study_level: Optional[LearnerLevelEnum] = None
    certification_obtained: Optional[str] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        use_enum_values=True
    )


#Mise à jour partielle (PATCH)
class LearnerUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[Role] = None

    date_birth: Optional[date] = None
    study_level: Optional[LearnerLevelEnum] = None
    phone_number: Optional[str] = None
    platform_registration_date: Optional[datetime] = None
    certification_obtained: Optional[str] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("date_birth")
    def validate_age(cls, value: Optional[date]) -> Optional[date]:
        if value:
            age = (date.today() - value).days // 365
            if age < 16:
                raise ValueError("L'apprenant doit avoir au moins 16 ans")
        return value

    @field_validator("phone_number")
    def validate_phone(cls, value: Optional[str]) -> Optional[str]:
        if value and not re.fullmatch(r"0\d{9}", value):
            raise ValueError("Numéro de téléphone invalide (format attendu : 0XXXXXXXXX)")
        return value
