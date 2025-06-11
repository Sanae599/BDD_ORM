from sqlmodel import SQLModel
from typing import Optional
from pydantic import field_validator
from app.enumerations.all_enumerations import EquipmentType


#Création d’un équipement (POST)
class EquipmentCreate(SQLModel):
    description: str
    type_equipment: EquipmentType
    quantity: int
    is_mobile: bool = True
    id_room: Optional[int] = None  # Peut être None si équipement mobile

    @field_validator("quantity")
    def validate_quantity(cls, value):
        if value < 0:
            raise ValueError("La quantité doit être un entier positif")
        return value


#Lecture d’un équipement (GET)
class EquipmentRead(EquipmentCreate):
    id_equipment: int


#Mise à jour d’un équipement (PATCH)
class EquipmentUpdate(SQLModel):
    description: Optional[str] = None
    type_equipment: Optional[EquipmentType] = None
    quantity: Optional[int] = None
    is_mobile: Optional[bool] = None
    id_room: Optional[int] = None

    @field_validator("quantity")
    def validate_quantity(cls, value):
        if value is not None and value < 0:
            raise ValueError("La quantité doit être un entier positif")
        return value
