from typing import Optional
from datetime import date
from pydantic import BaseModel, ConfigDict, field_validator
from app.enumerations.all_enumerations import EquipmentCategoryEnum, EquipmentStatusEnum


#Création d’un équipement (POST)
class EquipmentCreate(BaseModel):
    name: str
    category: EquipmentCategoryEnum
    status: EquipmentStatusEnum
    purchase_date: date
    quantity: int

    model_config = ConfigDict(
        use_enum_values=True,
        str_strip_whitespace=True,
        validate_assignment=True
    )

    @field_validator("quantity")
    def check_quantity(cls, value: int) -> int:
        if value < 0:
            raise ValueError("La quantité ne peut pas être négative.")
        return value


#Lecture complète (GET)
class EquipmentRead(BaseModel):
    id: int
    name: str
    category: EquipmentCategoryEnum
    status: EquipmentStatusEnum
    purchase_date: date
    quantity: int

    model_config = ConfigDict(
        use_enum_values=True
    )

#Lecture publique
class EquipmentPublic(BaseModel):
    name: str
    status: EquipmentStatusEnum
    quantity: int

    model_config = ConfigDict(
        use_enum_values=True
    )


#Mise à jour partielle (PATCH)
class EquipmentUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[EquipmentCategoryEnum] = None
    status: Optional[EquipmentStatusEnum] = None
    purchase_date: Optional[date] = None
    quantity: Optional[int] = None

    model_config = ConfigDict(
        use_enum_values=True,
        validate_assignment=True,
        str_strip_whitespace=True
    )

    @field_validator("quantity")
    def check_quantity(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value < 0:
            raise ValueError("La quantité ne peut pas être négative.")
        return value
