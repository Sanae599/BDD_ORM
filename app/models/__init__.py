# from flask import Flask
# from app.database import init_db
# from app.auth.login_manager import login_manager
# from app.routes.user_routes import user_bp


# def create_app():
#     app = Flask(__name__)
#     app.secret_key = "super-secret-key"  # nécessaire pour Flask-Login

#     init_db()
#     login_manager.init_app(app)

#     app.register_blueprint(user_bp)
#     return app
