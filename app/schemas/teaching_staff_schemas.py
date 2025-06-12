from datetime import date
from typing import Optional, Dict
from pydantic import BaseModel, EmailStr, ConfigDict, field_validator
from app.enumerations.all_enumerations import Role, JobStaffEnum


#Base commune à toutes les variantes
class TeachingStaffBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    role: Role = Role.STAFF

    job: JobStaffEnum
    date_takingup_office: date
    responsabilities: Dict = {}

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("date_takingup_office")
    def check_not_future_date(cls, v: date) -> date:
        if v > date.today():
            raise ValueError("La date de prise de fonction ne peut pas être dans le futur")
        return v


#Création (POST)
class TeachingStaffCreate(TeachingStaffBase):
    pass


#Lecture complète (GET)
class TeachingStaffRead(TeachingStaffBase):
    id: int


#Lecture publique pour l’interface utilisateur
class TeachingStaffPublic(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    job: JobStaffEnum

    model_config = ConfigDict(
        str_strip_whitespace=True,
        use_enum_values=True
    )


#Mise à jour partielle (PATCH)
class TeachingStaffUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[Role] = None

    job: Optional[JobStaffEnum] = None
    date_takingup_office: Optional[date] = None
    responsabilities: Optional[Dict] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("date_takingup_office")
    def check_not_future_update(cls, v: Optional[date]) -> Optional[date]:
        if v and v > date.today():
            raise ValueError("La date de prise de fonction ne peut pas être dans le futur")
        return v
