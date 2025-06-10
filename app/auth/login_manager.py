# app/auth/login_manager.py

from flask_login import LoginManager
from app.models.tables_user import User
# from app.enumerations.all_enumerations import User

login_manager = LoginManager()


def init_login_manager(app):
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.database import get_session  # ✅ Import local pour éviter boucle

        with get_session() as session:
            return session.get(User, int(user_id))
