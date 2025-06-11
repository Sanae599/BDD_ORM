from sqlmodel import SQLModel
from datetime import date
from enum import Enum
from typing import Optional
from app.enumerations.all_enumerations import NiveauAccesEnum

class AdminCreate(SQLModel):
    date_promotion: date
    level_access: NiveauAccesEnum
    Id_user: int

class AdminRead(AdminCreate):
    Id_admin: int

class AdminUpdate(SQLModel):
    date_promotion: Optional[date] = None
    level_access: Optional[NiveauAccesEnum] = None
    Id_user: Optional[int] = None
