from webapp.flask_manager import create_app
from app.database import get_session, init_db
from app.crud.user import add_one_user
from app.crud.course import create_one_course, get_all_courses
from app.crud.room import create_one_room
from sqlalchemy.sql import select
from app.models.user import User

app = create_app()

def startup_tasks():
    init_db()

    with get_session() as session:
        # Ajouter un utilisateur de test
        user = add_one_user(session)
        print(f"Utilisateur ajouté : {user.firstname} {user.lastname}")

        # Rechercher un utilisateur
        statement = select(User).where(User.firstname == "Rémi")
        result = session.exec(statement).first()
        print(f"Résultat : {result}")

        #get all courses test
        #all_courses = get_all_courses(session)
        #print(all_courses)

        #Add room test
        room = create_one_room(session)
        print(room)

        #Add course test
        course = create_one_course(session, 1)



if __name__ == "__main__":
    startup_tasks()
    app.run(debug=True)
