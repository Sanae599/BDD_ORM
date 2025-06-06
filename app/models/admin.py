from datetime import date
from sqlmodel import SQLModel, Field, Relationship
from user import UserBase
from enum import Enum

class NiveauAccesEnum(str, Enum):
    ADMIN_STANDARD = "Admin standard"
    SUPERADMIN = "Super admin"


class Admin(SQLModel, table=True):
    Id_admin: int | None = Field(default=None, primary_key=True)
    date_promotion: date
    level_access: NiveauAccesEnum
    Id_user: int = Field(foreign_key="user.Id_user")

    user: UserBase | None = Relationship(back_populates="user")
