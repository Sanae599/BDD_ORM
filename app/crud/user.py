from app.models.user import UserBase, Role
from sqlmodel import Session


def add_one_user(session: Session):
    user = UserBase(
        firstname="Rémi",
        lastname="LABONNE",
        email="remilabonne@yahoo.fr",
        password="azerty",
        is_active=True,
        role=Role.APPRENANT,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
