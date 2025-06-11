from app.models.tables_user import Password
from sqlmodel import Session
from passlib.context import CryptContext
#faire un pip install 'passlib[bcrypt]'

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def add_one_password(session: Session, password: str):
    hashed_password = pwd_context.hash(password)
    pwd = Password(password=hashed_password)
    session.add(pwd)
    session.commit()
    session.refresh(pwd)
    return pwd
