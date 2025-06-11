from sqlmodel import Session, select
from app.models.equipment import Equipment
from app.enumerations.all_enumerations import EquipmentType
from typing import Optional

from app.schemas.equipment_schemas import EquipmentRead

def add_equipment_to_room(session: Session, description: str, equipment_type: EquipmentType,
                         quantity: int, id_room: Optional[int] = None, is_mobile: bool = True):
    equipment = Equipment(
        description=description,
        type_equipment=equipment_type,
        quantity=quantity,
        id_room=id_room,
        is_mobile=is_mobile
    )

    session.add(equipment)
    session.commit()
    session.refresh(equipment)
    return equipment

def get_one_equipment_by_id(session: Session, equipment_id: int):
    equipment = session.get(Equipment, equipment_id)
    if not equipment:
        return None
    
    return EquipmentRead.model_validate(equipment)

def get_all_equipments(session: Session):
    equipment = select(Equipment)
    result = session.exec(equipment)
    return result.all()
    
def delete_equipment(session: Session, equipment_id: int):
    equipment = session.get(Equipment, equipment_id)
    if not equipment:
        return False
    session.delete(equipment)
    session.commit()
    return True