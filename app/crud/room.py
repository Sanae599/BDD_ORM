from sqlmodel import Session, select
from app.models.room import Room

def add_one_room(session: Session, name: str, capacity: int, location: str, is_active:bool = True):
    # if not existe
    existing_room = session.exec(select(Room).where(Room.name == name)).first()
    if existing_room:
        print('room déjà existante dans la db')
        return existing_room

    room = Room(
        name = name,
        capacity = capacity,
        location = location,
        is_active= is_active
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

def update_course(session: Session):
    pass

def delete_course(session: Session):
    pass