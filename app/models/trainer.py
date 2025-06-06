from datetime import date
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Trainer(SQLModel, table=True):
    Id_trainer: int | None = Field(default=None, primary_key=True)
    speciality: str
    hire_date: date 
    hourly_rate: float
    bio: Optional[str]
    Id_user: int = Field(foreign_key="user.Id_user")

    user: ["User"] = Relationship(back_populates="user")
