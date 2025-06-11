from typing import Optional
from pydantic import BaseModel, field_validator, ConfigDict
from app.enumerations.all_enumerations import EquipmentType


#Création (POST)
class EquipmentCreate(BaseModel):
    description: str
    type_equipment: EquipmentType
    quantity: int
    is_mobile: Optional[bool] = True

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("quantity")
    def validate_quantity(cls, value: int) -> int:
        if value < 0:
            raise ValueError("La quantité doit être supérieure ou égale à 0")
        return value


#Lecture complète (GET)
class EquipmentRead(BaseModel):
    id: int
    description: str
    type_equipment: EquipmentType
    quantity: int
    is_mobile: bool

    model_config = ConfigDict(use_enum_values=True)


#Lecture publique pour affichage 
class EquipmentPublic(BaseModel):
    description: str
    type_equipment: EquipmentType
    is_mobile: bool

    model_config = ConfigDict(use_enum_values=True)


#Mise à jour (PATCH)
class EquipmentUpdate(BaseModel):
    description: Optional[str] = None
    type_equipment: Optional[EquipmentType] = None
    quantity: Optional[int] = None
    is_mobile: Optional[bool] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("quantity")
    def validate_quantity(cls, value: Optional[int]) -> Optional[int]:
        if value is not None and value < 0:
            raise ValueError("La quantité doit être supérieure ou égale à 0")
        return value
