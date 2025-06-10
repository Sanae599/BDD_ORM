from app.models.tables_user import User
from app.enumerations.all_enumerations import Role
from sqlmodel import Session


def add_one_user(
    session: Session,
    firstname: str,
    lastname: str,
    email: str,
    role: Role,
    id_password: str,
):
    user = User(
        firstname=firstname,
        lastname=lastname,
        email=email,
        is_active=True,
        role=role,
        id_password=id_password,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
