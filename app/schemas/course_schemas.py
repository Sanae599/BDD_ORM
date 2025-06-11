from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, field_validator, ConfigDict
from app.enumerations.all_enumerations import CourseStatutEnum

#Schéma de création (POST)
class CourseCreate(BaseModel):
    titre: str
    description: Optional[str] = None
    date_debut: datetime
    date_fin: datetime
    id_salle: int
    id_formateur: int
    capacite_max: int
    statut: CourseStatutEnum = CourseStatutEnum.OPEN
    prerequis: Optional[List[str]] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("date_fin")
    def check_dates(cls, date_fin, values):
        date_debut = values.get("date_debut")
        if date_debut and date_fin <= date_debut:
            raise ValueError("La date de fin doit être après la date de début")
        return date_fin

    @field_validator("capacite_max")
    def check_capacity(cls, value):
        if value <= 0:
            raise ValueError("La capacité maximale doit être supérieure à zéro")
        return value

#Schéma complet de lecture (GET)
class CourseRead(BaseModel):
    id: int
    titre: str
    description: Optional[str] = None
    date_debut: datetime
    date_fin: datetime
    id_salle: int
    id_formateur: int
    capacite_max: int
    statut: CourseStatutEnum
    prerequis: Optional[List[str]] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        use_enum_values=True
    )

#Schéma public pour l’interface utilisateur (front)
class CoursePublic(BaseModel):
    titre: str
    description: Optional[str] = None
    date_debut: datetime
    date_fin: datetime
    statut: CourseStatutEnum

    model_config = ConfigDict(
        str_strip_whitespace=True,
        use_enum_values=True
    )

#Schéma de mise à jour (PATCH)
class CourseUpdate(BaseModel):
    titre: Optional[str] = None
    description: Optional[str] = None
    date_debut: Optional[datetime] = None
    date_fin: Optional[datetime] = None
    id_salle: Optional[int] = None
    id_formateur: Optional[int] = None
    capacite_max: Optional[int] = None
    statut: Optional[CourseStatutEnum] = None
    prerequis: Optional[List[str]] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("date_fin")
    def validate_dates(cls, date_fin, values):
        date_debut = values.get("date_debut")
        if date_debut and date_fin and date_fin <= date_debut:
            raise ValueError("La date de fin doit être après la date de début")
        return date_fin

    @field_validator("capacite_max")
    def validate_capacity(cls, value):
        if value is not None and value <= 0:
            raise ValueError("La capacité maximale doit être supérieure à zéro")
        return value
