from typing import Optional, List, Dict
from sqlmodel import SQLModel, Field, Relationship, Column, JSON
from sqlalchemy.ext.mutable import MutableDict
from flask_login import UserMixin


class Room(SQLModel, UserMixin, table=True):
    id_room: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)
    capacity: int = Field(gt=0)  # ≥ 1, donc > 0
    location: str
    equipments: Dict = Field(
        default={}, sa_column=Column(MutableDict.as_mutable(JSON))
    )
    is_active: bool = Field(default=True)

    courses: List["Course"] = Relationship(back_populates="room")
    equipments_rel: List["Equipment"] = Relationship(back_populates="room")

    