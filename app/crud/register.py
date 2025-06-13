from sqlmodel import Session, select
from app.models.register import Register
from app.schemas.register_schemas import RegisterCreate, RegisterRead
from typing import List


def create_register(session: Session, register_data: RegisterCreate) -> Register:
    register = Register(**register_data.dict())
    session.add(register)
    session.commit()
    session.refresh(register)
    return register


def get_all_registers(session: Session) -> List[Register]:
    statement = select(Register)
    return session.exec(statement).all()
