from typing import Optional
from sqlmodel import SQLModel
from pydantic import EmailStr
#Champs communs
class UserBase(SQLModel):
    firstname: str
    lastname: str
    email: EmailStr  #Validation automatique du format email
    role: Role


#Création d'un utilisateur (POST)
class UserCreate(UserBase):
    password: str  #Le mot de passe sera stocké dans une table séparée, mais ici transmis en clair pour insertion


#Lecture d’un utilisateur (GET)
class UserRead(UserBase):
    Id_user: int


#Mise à jour partielle d’un utilisateur (PATCH)
class UserUpdate(SQLModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[Role] = None
