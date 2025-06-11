from sqlmodel import Session
from app.models.equipment import Equipment, EquipmentType
from typing import Optional

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

