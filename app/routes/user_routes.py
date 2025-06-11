from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql import select
from app.database import get_session
from app.models.tables_user import User, Password
from passlib.context import CryptContext

user_bp = Blueprint("user", __name__, url_prefix="/users")

# Initialisation de passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        pwd_input = request.form.get("password")

        with get_session() as session:
            statement = select(User).where(User.email == email)
            user: User = session.exec(statement).scalars().first()

            if user:
                # On récupère le mot de passe haché associé
                statement = select(Password).where(Password.id == user.id_password)
                password_obj: Password = session.exec(statement).scalars().first()

                # Vérifie le mot de passe avec passlib
                if password_obj and pwd_context.verify(
                    pwd_input, password_obj.password
                ):
                    login_user(user)
                    return redirect(url_for("user.profile"))  #  redirection inchangée

            flash("Identifiants incorrects")

    return render_template("login.html")


@user_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("user.login"))  # ✅ redirection inchangée


@user_bp.route("/profile")
@login_required
def profile():
    return f"Bienvenue {current_user.firstname} {current_user.lastname}!"
