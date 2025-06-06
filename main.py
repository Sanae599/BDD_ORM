from webapp.flask_manager import create_app
from app.database import get_session, init_db
from app.crud.user import add_one_user
from sqlalchemy.sql import select
from app.models.user import UserBase

app = create_app()


def startup_tasks():
    init_db()

    with get_session() as session:
        # Ajouter un utilisateur de test
        user = add_one_user(session)
        print(f"Utilisateur ajouté : {user.firstname} {user.lastname}")

        # Rechercher un utilisateur
        statement = select(UserBase).where(UserBase.firstname == "Rémi")
        result = session.exec(statement).first()
        print(f"Résultat : {result}")


if __name__ == "__main__":
    startup_tasks()
    app.run(debug=True)
