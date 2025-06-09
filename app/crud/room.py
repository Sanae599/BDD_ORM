from sqlmodel import Session, select
from app.models.room import Room

def create_one_room(session: Session):
    # if not existe
    existing_room = session.exec(select(Room).where(Room.name == "room1")).first()
    if existing_room:
        print('room déjà existante dans la db')
        
    else:
        room = Room(
            name = "room1",
            capacity = 2,
            location = "lille city",
            equipments = {
                "projector": 1,
                "whiteboard": 1,
                "chairs": 10,
                "tables": 2,
                "microphone": 1
            },
            is_active= True

        )
        session.add(room)
        session.commit()
        session.refresh(room)
        return room

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