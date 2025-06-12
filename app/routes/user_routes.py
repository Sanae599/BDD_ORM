from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql import select
from app.database import get_session
from app.models.tables_user import UserBase
from passlib.context import CryptContext

user_bp = Blueprint("user", __name__, url_prefix="/users")
