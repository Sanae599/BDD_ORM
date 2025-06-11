from sqlmodel import SQLModel

#Schéma de création d’un lead (POST)
class LeadCreate(SQLModel):
    Id_trainer: int
    Id_course: int


#Schéma de lecture d’un lead (GET)
class LeadRead(LeadCreate):
    pass

#Schéma de suppression d’un lead (DELETE si besoin , cas de changement de formateur ou erreur lors de l'affectation)
class LeadDelete(SQLModel):
    Id_trainer: int
    Id_course: int
