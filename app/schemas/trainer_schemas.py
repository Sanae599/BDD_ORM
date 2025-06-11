from sqlmodel import SQLModel
from typing import Optional
from datetime import date
from pydantic import field_validator, ConfigDict


# Schéma de création (POST)
class TrainerCreate(SQLModel):
    speciality: str
    hire_date: date
    hourly_rate: float
    bio: Optional[str] = None
    Id_user: int

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True
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


# Schéma public (GET normal)
class TrainerPublic(SQLModel):
    Id_trainer: int
    speciality: str
    hire_date: date
    hourly_rate: float
    bio: Optional[str] = None

    model_config = ConfigDict(
        use_enum_values=True,
        str_strip_whitespace=True
    )


# Schéma de lecture pour usage interne (admin)
class TrainerAdminRead(TrainerPublic):
    Id_user: int


# Schéma de mise à jour (PATCH)
class TrainerUpdate(SQLModel):
    speciality: Optional[str] = None
    hire_date: Optional[date] = None
    hourly_rate: Optional[float] = None
    bio: Optional[str] = None
    Id_user: Optional[int] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True
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
