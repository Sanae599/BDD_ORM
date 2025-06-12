from sqlmodel import Session, select
from app.models.room import Room
from app.schemas.room_schemas import RoomCreate

def add_one_room(session: Session, rc: RoomCreate):
    existing_room = session.exec(select(Room).where(Room.name == rc.nom)).first()
    if existing_room:
        print('room déjà existante dans la db')
        return existing_room

    room = Room(
        name = rc.nom,
        capacity = rc.capacite,
        location = rc.localisation,
        is_active= rc.is_active
    )
    session.add(room)
    session.commit()
    session.refresh(room)
    return room

def get_one_room_by_id(session: Session, room_id: int):
    statement = select(Room).where(Room.id_room == room_id)
    result = session.exec(statement)
    return result.one()

def get_all_rooms(session: Session):
    statement = select(Room)
    result = session.exec(statement)
    return result.all()

def update_room(session: Session):
    pass

def delete_room(session: Session, room_id: int):
    room = session.get(Room, room_id)
    if not room:
        return False

    session.delete(room)
    session.commit()
    return True