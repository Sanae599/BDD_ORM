from app.models.tables_user import User
from app.enumerations.all_enumerations import Role
from sqlmodel import Session
from enum import Enum
from random import choice
import faker
from app.crud.password import add_one_password


def add_one_user(
    session: Session,
    firstname: str,
    lastname: str,
    email: str,
    role: Role,
    password: str,
):

    pwd = add_one_password(session, password)
    user = User(
        firstname=firstname,
        lastname=lastname,
        email=email,
        is_active=True,
        role=role,
        id_password=pwd.id,
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def add_one_user_fake(
    session: Session,
):

    f = faker.Faker("fr_FR")
    pwd = add_one_password(session, f.password())
    l_roles = [r.value for r in Role]

    user = User(
        firstname=f.first_name(),
        lastname=f.last_name(),
        email=f.email(),
        is_active=True,
        role=choice(l_roles),
        id_password=pwd.id,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def add_n_user_fake(session: Session, n: int):
    for _ in range(n):
        add_one_user_fake(session)
