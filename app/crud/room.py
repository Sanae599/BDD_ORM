from sqlmodel import Session, select
from models.room import Room

def create_one_room(session: Session):
    #pas sur de l'utilité
    pass

def get_one_room_by_id(session: Session, room_id: int):
    statement = select(Room).where(Room.Id_room == room_id)
    result = session.exec(statement)
    return result.one()

def get_all_rooms(session: Session):
    statement = select(Room)
    result = session.exec(statement)
    rooms = result.all()
    for room in rooms:
        print(room)
    return rooms

def update_course(session: Session):
    pass

def delete_course(session: Session):
    pass