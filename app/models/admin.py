from datetime import date
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from enum import Enum

class NiveauAccesEnum(str, Enum):
    ADMIN_STANDARD = "Admin standard"
    SUPERADMIN = "Super admin"

class Admin(SQLModel, table=True):
    Id_admin: int | None = Field(default=None, primary_key=True)
    date_promotion: date
    level_access: NiveauAccesEnum
    Id_user: int = Field(foreign_key="user.Id_user")

    user: Optional["User"] = Relationship(back_populates="admin")
