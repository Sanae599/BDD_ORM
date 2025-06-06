from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql import select
from app.database import get_session
from app.models.user import UserBase

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        with get_session() as session:
            statement = select(UserBase).where(UserBase.email == email)
            user = (
                session.exec(statement).scalars().first()
            )  # Bien récupérer l'instance UserBase

            if user and user.password == password:
                login_user(user)
                return redirect(url_for("user.profile"))

            flash("Identifiants incorrects")
    return render_template("login.html")


@user_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("user.login"))


@user_bp.route("/profile")
@login_required
def profile():
    return f"Bienvenue {current_user.firstname} {current_user.lastname}!"
