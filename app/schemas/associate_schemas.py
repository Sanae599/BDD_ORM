from typing import Optional
from sqlmodel import SQLModel, Field

#Schéma de création (POST) : ajouter un lien équipement ↔ cours
class AssociateCreate(SQLModel):
    Id_course: int
    Id_equipment: int
    quantity: int = Field(ge=0)


#Schéma de lecture (GET) : lecture d’une association existante
class AssociateRead(AssociateCreate):
    pass  # Id_course et Id_equipment sont déjà dans le schéma parent


#Schéma de mise à jour (PATCH) : on ne modifie que la quantité
class AssociateUpdate(SQLModel):
    quantity: Optional[int] = Field(default=None, ge=0)
