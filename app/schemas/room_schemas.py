from sqlmodel import SQLModel
from typing import Optional, Dict
from pydantic import field_validator
from datetime import datetime

#Créer la salle
class RoomCreate(SQLModel): #POST
    nom: str
    capacite: int
    localisation: str
    equipements: Optional[Dict[str, str | bool | int]] = None  # JSON libre
    is_active: bool = True

    @field_validator("capacite")
    def check_capacity(cls, value: int) -> int:
        if value < 1:
            raise ValueError("La capacité doit être au moins de 1")
        return value

#Schéma de lecture de salle (GET)
class RoomRead(RoomCreate):
    id_room: int 

#Mise à jour de salle #PATCH
class RoomUpdate(SQLModel):
    nom: Optional[str] = None
    capacite: Optional[int] = None
    localisation: Optional[str] = None
    equipements: Optional[Dict[str, str | bool | int]] = None
    is_active: Optional[bool] = None

    @field_validator("capacite")
    def check_capacity(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value < 1:
            raise ValueError("La capacité doit être au moins de 1")
        return value
