from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

# Import local des modèles liés (type hints uniquement)
from app.models.room import Room
from app.models.associate import Associate

class EquipmentType(str, Enum):
    AUDIOVISUAL = "audiovisual"
    COMPUTER = "computer"
    FURNITURE = "furniture"
    OTHER = "other"

class Equipment(SQLModel, table=True):
    Id_equipment: Optional[int] = Field(default=None, primary_key=True)
    description: str
    type_equipment: EquipmentType
    quantity: int = Field(ge=0)
    is_mobile: bool = True

    #FK vers une salle (peut être NULL si équipement mobile)
    Id_room: Optional[int] = Field(default=None, foreign_key="room.Id_room")

    room: Optional["Room"] = Relationship(back_populates="equipments")
    associated_courses: List["Associate"] = Relationship(back_populates="equipment")
