from datetime import date
from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict, field_validator
from app.enumerations.all_enumerations import Role, NiveauAccesEnum


#Schéma de base hérité de UserBase
class AdminBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    role: Role = Role.ADMIN

    date_promotion: date
    level_access: NiveauAccesEnum

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("date_promotion")
    def validate_promotion_date(cls, value: date) -> date:
        if value > date.today():
            raise ValueError("La date de promotion ne peut pas être dans le futur")
        return value


#Création (POST)
class AdminCreate(AdminBase):
    pass


#Lecture complète (GET)
class AdminRead(AdminBase):
    id: int


#Lecture publique (interface utilisateur)
class AdminPublic(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    level_access: NiveauAccesEnum
    role : Role
    
    model_config = ConfigDict(
        str_strip_whitespace=True,
        use_enum_values=True
    )


#Mise à jour (PATCH)
class AdminUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[Role] = None

    date_promotion: Optional[date] = None
    level_access: Optional[NiveauAccesEnum] = None

    model_config = ConfigDict(
        str_strip_whitespace=True,
        validate_assignment=True,
        use_enum_values=True
    )

    @field_validator("date_promotion")
    def validate_promotion_date(cls, value: Optional[date]) -> Optional[date]:
        if value and value > date.today():
            raise ValueError("La date de promotion ne peut pas être dans le futur")
        return value
