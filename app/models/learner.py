from sqlmodel import SQLModel, Field
from enum import Enum


class UserBase(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    firstname: str
    lastname: str
    email: str
    is_active: bool = True
    role: Role
