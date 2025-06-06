from flask import Flask
import os
from app.auth.login_manager import init_login_manager
from app.database import init_db


def create_app():
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
    app = Flask(__name__, template_folder=template_dir)
    app.secret_key = "f6743107467a160afa96a573646a0d5c3e6d807d55329f65"
    # obtenu avec : os.urandom(24).hex()

    init_db()
    init_login_manager(app)

    from app.routes.user_routes import user_bp
    from app.routes.home_route import main_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(main_bp)

    return app
