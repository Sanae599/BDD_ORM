from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, field_validator, ConfigDict, constr
from app.enumerations.all_enumerations import CourseStatutEnum

#Schéma de création (POST)
class CourseCreate(BaseModel):
    titre: constr(max_length=100)
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    id_room: int
    id_trainer: int
    max_capacity: int
    status: CourseStatutEnum = CourseStatutEnum.OPEN
    prerequisites: Optional[List[str]] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("end_date")
    def check_dates(end_date, values):
        start_date = values.get("start_date")
        if start_date and end_date <= start_date:
            raise ValueError("La date de fin doit être après la date de début")
        return end_date

    @field_validator("max_capacity")
    def check_capacity(value):
        if value <= 0:
            raise ValueError("La capacité maximale doit être supérieure à zéro")
        return value


#Schéma de lecture complet (GET)
class CourseRead(BaseModel):
    id: int
    title: constr(max_length=100)
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    id_room: int
    id_trainer: int
    max_capacity: int
    status: CourseStatutEnum
    prerequisites: Optional[List[str]] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        use_enum_values=True
    )


#Schéma public pour l’interface utilisateur
class CoursePublic(BaseModel):
    title: constr(max_length=100)
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    status: CourseStatutEnum

    model_config = ConfigDict(
        str_strip_whitespace=True,
        use_enum_values=True
    )


#Schéma de mise à jour partielle (PATCH)
class CourseUpdate(BaseModel):
    title: Optional[constr(max_length=100)] = None
    description: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    id_room: Optional[int] = None
    id_trainer: Optional[int] = None
    max_capacity: Optional[int] = None
    status: Optional[CourseStatutEnum] = None
    prerequisites: Optional[List[str]] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("end_date")
    def check_dates(end_date, values):
        start_date = values.get("start_date")
        if start_date and end_date <= start_date:
            raise ValueError("La date de fin doit être après la date de début")
        return end_date

    @field_validator("max_capacity")
    def check_capacity(value):
        if value <= 0:
            raise ValueError("La capacité maximale doit être supérieure à zéro")
        return value
