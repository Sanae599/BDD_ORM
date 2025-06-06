from typing import Optional, List, Dict
from datetime import datetime
from sqlmodel import SQLModel
from pydantic import model_validator  #pydantic v2
from app.models.course import CourseStatutEnum

#Créer un cours
class CourseCreate(SQLModel): #POST
    titre: str
    description: Optional[str] = None
    date_debut: datetime
    date_fin: datetime
    id_salle: int
    id_formateur: int
    capacite_max: int
    statut: CourseStatutEnum = CourseStatutEnum.OPEN
    prerequis: Optional[List[str]] = None

    @model_validator(mode="after") #Empêcher qu’une session finisse avant d’avoir commencé
    def check_dates(self) -> "courseCreate":
        if self.date_fin <= self.date_debut:
            raise ValueError("La date de fin doit être après la date de début")
        return self

#Afficher un cours
class CourseRead(CourseCreate): #GET
    id_course: int

#Modifier un cours
class CourseUpdate(SQLModel): #PATCH
    titre: Optional[str] = None
    description: Optional[str] = None
    date_debut: Optional[datetime] = None
    date_fin: Optional[datetime] = None
    id_salle: Optional[int] = None
    id_formateur: Optional[int] = None
    capacite_max: Optional[int] = None
    statut: Optional[CourseStatutEnum] = None
    prerequis: Optional[List[str]] = None

    @model_validator(mode="after") #Verifier que les 2 dates soients présentes et empêcher qu’une session finisse avant d’avoir commencé
    def check_dates(self) -> "courseUpdate":
        if self.date_debut and self.date_fin and self.date_fin <= self.date_debut:
            raise ValueError("La date de fin doit être après la date de début")
        return self
