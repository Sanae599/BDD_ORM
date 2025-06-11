import re
from typing import Optional
from sqlmodel import SQLModel
from pydantic import EmailStr, ConfigDict, field_validator
from app.enumerations.all_enumerations import Role


#Création d'un utilisateur (POST)
class UserCreate(SQLModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    role: Role

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("new_password")
    def validate_new_password(cls, value: str) -> str:
        if len(value) < 10:
            raise ValueError("Le mot de passe doit contenir au moins 10 caractères")
        if not any(c.isupper() for c in value):
            raise ValueError("Le mot de passe doit contenir au moins une majuscule")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Le mot de passe doit contenir au moins un caractère spécial")
        return value

# Lecture publique d’un utilisateur (GET)
class UserPublic(SQLModel):
    Id_user: int
    firstname: str
    lastname: str
    email: EmailStr
    role: Role

    model_config = ConfigDict(use_enum_values=True)


#Mise à jour d’un utilisateur (PATCH)
class UserUpdate(SQLModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[Role] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )


#Mise à jour du mot de passe
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

# Réinitialisation de mot de passe (mot de passe oublié)
class PasswordReset(SQLModel):
    email: EmailStr
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