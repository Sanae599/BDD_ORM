from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, field_validator
from app.enumerations.all_enumerations import Role


# Base partagée (hérite implicitement de UserBase)
class TrainerBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    role: Role = Role.LEARNER  # ou Role.TRAINER si spécifique

    speciality: str
    hire_date: date
    hourly_rate: float
    bio: Optional[str] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("hire_date")
    def check_hire_date_not_future(cls, value: date) -> date:
        if value > date.today():
            raise ValueError("La date d'embauche ne peut pas être dans le futur")
        return value

    @field_validator("hourly_rate")
    def check_positive_rate(cls, value: float) -> float:
        if value < 0:
            raise ValueError("Le taux horaire doit être positif ou nul")
        return value


#Création (POST)
class TrainerCreate(TrainerBase):
    pass


#Lecture complète (GET)
class TrainerRead(TrainerBase):
    id: int


#Lecture publique (interface utilisateur)
class TrainerPublic(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    speciality: str
    hire_date: date
    hourly_rate: float

    model_config = ConfigDict(
        str_strip_whitespace=True,
        use_enum_values=True
    )


#Mise à jour (PATCH)
class TrainerUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[Role] = None

    speciality: Optional[str] = None
    hire_date: Optional[date] = None
    hourly_rate: Optional[float] = None
    bio: Optional[str] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("hire_date")
    def check_hire_date_not_future(cls, value: Optional[date]) -> Optional[date]:
        if value and value > date.today():
            raise ValueError("La date d'embauche ne peut pas être dans le futur")
        return value

    @field_validator("hourly_rate")
    def check_positive_rate(cls, value: Optional[float]) -> Optional[float]:
        if value is not None and value < 0:
            raise ValueError("Le taux horaire doit être positif ou nul")
        return value
