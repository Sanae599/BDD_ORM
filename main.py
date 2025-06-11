from webapp.flask_manager import create_app
from app.database import get_session, init_db
from app.crud.user import add_one_user
from app.crud.password import add_one_password
from app.crud.room import add_one_room
from app.crud.equipment import add_equipment_to_room
from app.models.equipment import EquipmentType
from app.models.tables_user import User, Password

from sqlalchemy.sql import select

from app.enumerations.all_enumerations import Role

app = create_app()


def startup_tasks():
    init_db()

    with get_session() as session:
        # Ajouter un utilisateur de test
        # pwd: Password = add_one_password(session, "azerty")
        user: User = add_one_user(
            session, "remi", "labonne", "remi@labonne.com", Role.LEARNER, "azerty"
        )
        print(f"Utilisateur ajouté : {user.firstname} {user.lastname}")

        # # Rechercher un utilisateur
        # statement = select(UserBase).where(UserBase.firstname == "Rémi")
        # select_user = session.exec(statement).first()
        # print(f"Résultat : {select_user}")

        # Ajout d'une salle
        room = add_one_room(
            session=session,
            name="Salle test",
            capacity=20,
            location="Lille, Centre-ville"
        )
        print(f"Salle créée : {room.name} (ID: {room.id_room})")

        # Ajout équipements 
        equipments = [
            ("Projecteur", EquipmentType.AUDIOVISUAL, 1),
            ("Tableau blanc", EquipmentType.FURNITURE, 1),
            ("Ordinateurs", EquipmentType.COMPUTER, 5),
            ("Chaises", EquipmentType.FURNITURE, 20)
        ]

        for desc, equip_type, quantity in equipments:
            add_equipment_to_room(
                session=session,
                description=desc,
                equipment_type=equip_type,
                quantity=quantity,
                id_room=room.id_room,
                is_mobile=False
            )

        print(f"Équipements ajoutés à la salle {room.name}")


if __name__ == "__main__":
    startup_tasks()
    app.run(debug=True)

# from webapp.flask_manager import create_app
# from app.database import get_session, init_db
# from app.crud.user import add_one_user
# from app.crud.course import create_one_course, get_all_courses
# from app.crud.room import create_one_room
# from sqlalchemy.sql import select
# from app.models.user import User

# app = create_app()

# def startup_tasks():
#     init_db()

#     with get_session() as session:
#         # Ajouter un utilisateur de test
#         user = add_one_user(session)
#         print(f"Utilisateur ajouté : {user.firstname} {user.lastname}")

#         # Rechercher un utilisateur
#         statement = select(User).where(User.firstname == "Rémi")
#         result = session.exec(statement).first()
#         print(f"Résultat : {result}")

#         #get all courses test
#         #all_courses = get_all_courses(session)
#         #print(all_courses)

#         #Add room test
#         room = create_one_room(session)
#         print(room)

#         #Add course test
#         course = create_one_course(session, 1)


# if __name__ == "__main__":
#     startup_tasks()
#     app.run(debug=True)
