from sqlalchemy.sql import select
from app.database import get_session, init_db
from app.models.user import UserBase
from app.crud.user import add_one_user
from app.crud.course import add_one_course

# Initialise la base
init_db()

# Ajoute un utilisateur
with get_session() as session:
    user = add_one_user(session)
    course = add_one_course(session)
    print(f"Utilisateur ajouté : {user.firstname} {user.lastname}")

# Recherche d'un utilisateur
with get_session() as session:
    statement = select(UserBase).where(UserBase.firstname == "Rémi")
    result = session.exec(statement).first()

print(f"Résultat : {result}")
