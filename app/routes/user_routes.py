from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql import select
from sqlalchemy.orm import selectinload
from app.database import get_session
from app.models.tables_user import UserBase
from passlib.context import CryptContext
from app.models.tables_user import Learner, Trainer, Admin, TeachingStaff

user_bp = Blueprint("user", __name__)

def find_user_by_email(email):
    """Fonction utilitaire pour chercher un utilisateur par email"""
    with get_session() as session:
        # Liste des modèles à vérifier
        models = [
            ('Learner', Learner),
            ('Trainer', Trainer), 
            ('Admin', Admin),
            ('TeachingStaff', TeachingStaff)
        ]
        
        for model_name, model_class in models:
            try:
                print(f"Recherche dans {model_name}...")
                
                # Méthode 1: Utilisation de session.query (plus compatible)
                user = session.query(model_class).filter(model_class.email == email).first()
                
                if user:
                    print(f"Utilisateur trouvé dans {model_name}: {user.email}")
                    # Vérifier que l'objet a bien tous les attributs nécessaires
                    if hasattr(user, 'password') and hasattr(user, 'email'):
                        return user
                    else:
                        print(f"Attributs manquants sur {model_name}")
                        
            except Exception as e:
                print(f"Erreur lors de la recherche dans {model_name}: {e}")
                continue
                
        return None

@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        pwd = request.form.get("password", "")
        
        if not email or not pwd:
            flash("Email et mot de passe requis", "danger")
            return render_template("login.html")
        
        print(f"Tentative de connexion pour: {email}")
        
        try:
            user_found = find_user_by_email(email)
            
            if user_found:
                print(f"Utilisateur trouvé: {user_found.email}")
                print(f"Type d'utilisateur: {type(user_found).__name__}")
                
                # Vérification du mot de passe
                if hasattr(user_found, 'password'):
                    stored_password = user_found.password
                    print(f"Mot de passe stocké: {stored_password[:5]}...")  # Affiche les 5 premiers caractères
                    
                    if pwd == stored_password:
                        print("Mot de passe correct, connexion en cours...")
                        login_user(user_found)
                        flash("Connexion réussie", "success")
                        return redirect(url_for("main.index"))
                    else:
                        print("Mot de passe incorrect")
                        flash("Mot de passe incorrect", "danger")
                else:
                    print("Erreur: pas d'attribut password")
                    flash("Erreur de configuration utilisateur", "danger")
            else:
                print("Utilisateur non trouvé")
                flash("Utilisateur non trouvé", "danger")
                
        except Exception as e:
            print(f"Erreur générale lors de la connexion: {e}")
            flash("Erreur lors de la connexion", "danger")

    return render_template("login.html")


@user_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Déconnexion réussie", "info")
    return redirect(url_for("main.index"))