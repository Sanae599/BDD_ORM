from typing import Optional
from sqlmodel import SQLModel, Field
from enum import Enum
from sqlalchemy import Column, Enum as SQLEnum
from flask_login import UserMixin


class Role(Enum):
    APPRENANT = 0
    FORMATEUR = 1
    STAFF = 2
    ADMIN = 3


class UserBase(SQLModel, UserMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firstname: str
    lastname: str
    email: str
    password: str
    is_active: bool = True
    role: Role = Field(sa_column=Column(SQLEnum(Role), default=Role.APPRENANT))

    def get_id(self):
        return str(self.id)
