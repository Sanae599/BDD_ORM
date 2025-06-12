from webapp.flask_manager import create_app
from app.database import get_session, init_db
from app.crud.learner import add_one_learner
from app.crud.admin import add_one_admin
from app.crud.teaching_staff import add_one_teaching_staff
from app.crud.trainer import add_one_trainer

from app.schemas.trainer_schemas import TrainerCreate
from app.schemas.learner_schemas import LearnerCreate
from app.schemas.teaching_staff_schemas import TeachingStaffCreate
from app.schemas.admin_schemas import AdminCreate
from app.enumerations.all_enumerations import *
from datetime import date




app = create_app()


def startup_tasks():
    init_db()

    with get_session() as session:
        # Création d’un apprenant
        user_data = LearnerCreate(
            firstname="remiiiiiiiiiiiiiiiii",
            lastname="labonne",
            email="remi@labonne3.com",
            password="Caaaaaaaaaaaaaaaaazerty&",
            role=Role.LEARNER,
            date_birth=date(1980, 12, 5),
            study_level=LearnerLevelEnum.BAC,
            phone_number="0782966581",
            certification_obtained="CAPES",
        )
        try:
            user = add_one_learner(session, user_data)
            print("Utilisateur ajouté :", user.email)
        except ValueError as e:
            print("Info :", e)

        # Premier administrateur
        admin_data_1 = AdminCreate(
            firstname="Administrateur",
            lastname="Principal",
            email="admin@universite.fr",
            password="motdepasse123",
            role=Role.ADMIN,
            date_promotion=date(2023, 1, 1),
            level_access=NiveauAccesEnum.ADMIN_STANDARD
        )
        try:
            admin = add_one_admin(session, admin_data_1)
            if admin.email == admin_data_1.email and admin.id_admin is not None:
                print(f"Administrateur ajouté ou déjà présent : {admin.email}")
        except ValueError as e:
            print(f"Erreur : {e}")

        # Deuxième administrateur
        admin_data_2 = AdminCreate(
            firstname="Benjamin",
            lastname="Quinet",
            email="benji@thebest.fr",
            password="motdepasse123",
            role=Role.ADMIN,
            date_promotion=date(2023, 1, 1),
            level_access=NiveauAccesEnum.SUPERADMIN
        )
        try:
            admin = add_one_admin(session, admin_data_2)
            if admin.email == admin_data_2.email and admin.id_admin is not None:
                print(f"Administrateur ajouté ou déjà présent : {admin.email}")
        except ValueError as e:
            print(f"Erreur : {e}")

        staff_data = TeachingStaffCreate(
            firstname="Jean",
            lastname="Professeur",
            email="jean.prof@universite.fr",
            password="strongpassword123",
            role=Role.STAFF,
            job=JobStaffEnum.ResponsablePedagogique,
            date_takingup_office=date(2022, 9, 1),
            responsabilities={"matière": "Mathématiques", "niveau": "Licence"}
        )

        try:
            staff = add_one_teaching_staff(session, staff_data)
            print(f"Personnel enseignant ajouté ou déjà présent : {staff.email}")
        except ValueError as e:
            print(f"Erreur TeachingStaff : {e}")



        # Exemple de formateur
        trainer_data = TrainerCreate(
            firstname="Claire",
            lastname="Durand",
            email="claire.durand@formations.fr",
            password="MotDePasseSecurise123",
            role=Role.TRAINER,
            speciality="Développement Web",
            hire_date=date(2021, 10, 15),
            hourly_rate=45.0,
            bio="Claire est une formatrice passionnée spécialisée en Python et JavaScript."
        )

        try:
            trainer = add_one_trainer(session, trainer_data)
            print(f"Formateur ajouté ou déjà présent : {trainer.email}")
        except ValueError as e:
            print(f"Erreur Trainer : {e}")


if __name__ == "__main__":
    startup_tasks()
    app.run(debug=True)
