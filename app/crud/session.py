from app.database import init_db, get_session
from models.user import UserBase, Role
from sqlalchemy.sql import select

# Initialise la base et les tables
init_db()

# Ajoute un utilisateur
with get_session() as session:
    user = UserBase(
        firstname="Rémi",
        lastname="LABONNE",
        email="remilabonne@yahoo.fr",
        is_active=True,
        role=Role.APPRENANT,
    )
    session.add(user)
    session.commit()


def manage_base():
    user = UserBase(
        firstname="Rémi",
        lastname="LABONNE",
        email="remilabonne@yahoo.fr",
        is_active=True,
        role=Role.APPRENANT,
    )



# Recherche d'un utilisateur
with get_session() as session:
    statement = select(UserBase).where(UserBase.firstname == "Rémi")
    result = session.execute(statement).scalar_one_or_none()

print(f"Résultat : {result}")
