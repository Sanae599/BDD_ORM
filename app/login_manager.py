# from flask_login import LoginManager
# from app.models.tables_user import (
#     Trainer,
# )  # ⚠️ Assure-toi que ce fichier ne réimporte pas `login_manager.py`

# login_manager = LoginManager()
# login_manager.login_view = "user.login"  # 👈 C’est ça qui manque


# def init_login_manager(app):
#     login_manager.init_app(app)

#     @login_manager.user_loader
#     def load_user(user_id):
#         from app.database import get_session  # ⚠️ Import local pour éviter boucle

#         with get_session() as session:
#             return session.get(User, int(user_id))
# app/auth/login_manager.py

from flask_login import LoginManager
from app.models.tables_user import Learner, Trainer, Admin, TeachingStaff

login_manager = LoginManager()
login_manager.login_view = 'user.login'  # Redirection vers la page de login
login_manager.login_message = 'Veuillez vous connecter pour accéder à cette page.'


def init_login_manager(app):
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.database import get_session
        
        # Extraire le type et l'ID depuis user_id
        # Format: "type:id" (ex: "trainer:1", "learner:2")
        try:
            user_type, actual_id = user_id.split(':')
            actual_id = int(actual_id)
            
            with get_session() as session:
                if user_type == 'trainer':
                    return session.get(Trainer, actual_id)
                elif user_type == 'learner':
                    return session.get(Learner, actual_id)
                elif user_type == 'admin':
                    return session.get(Admin, actual_id)
                elif user_type == 'teachingstaff':
                    return session.get(TeachingStaff, actual_id)
        except (ValueError, AttributeError):
            # Si le format n'est pas correct, essayer l'ancien format
            # (pour compatibilité)
            with get_session() as session:
                # Essayer chaque type d'utilisateur
                for model in [Trainer, Learner, Admin, TeachingStaff]:
                    try:
                        user = session.get(model, int(user_id))
                        if user:
                            return user
                    except:
                        continue
        
        return None