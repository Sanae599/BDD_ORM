from sqlmodel import SQLModel
from pydantic import EmailStr, field_validator
import re

#Schéma de création d’un mot de passe (ex: lors de la création de compte)
class PasswordCreate(SQLModel):
    password: str
    user_id: int

    @field_validator("password")
    def validate_password_strength(cls, value: str) -> str:
        if len(value) < 10:
            raise ValueError("Le mot de passe doit contenir au moins 10 caractères")
        if not any(c.isupper() for c in value):
            raise ValueError("Le mot de passe doit contenir au moins une majuscule")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Le mot de passe doit contenir au moins un caractère spécial")
        return value


#Schéma pour authentification (pendant le formulaire de connexion)
class LoginInput(SQLModel):
    email: EmailStr
    password: str

#Schéma pour mise à jour du mot de passe (sur le profil utilisateur)
class PasswordUpdate(SQLModel):
    old_password: str
    new_password: str

    @field_validator("new_password")
    def validate_new_password(cls, value: str) -> str:
        if len(value) < 10:
            raise ValueError("Le mot de passe doit contenir au moins 10 caractères")
        if not any(c.isupper() for c in value):
            raise ValueError("Le mot de passe doit contenir au moins une majuscule")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Le mot de passe doit contenir au moins un caractère spécial")
        return value
