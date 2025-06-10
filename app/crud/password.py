from app.models.tables_user import Password
from sqlmodel import Session


def add_one_password(session: Session, password: str):
    pwd = Password(
        password=password,
    )
    session.add(pwd)
    session.commit()
    session.refresh(pwd)
    return pwd
