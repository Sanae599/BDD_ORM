from typing import Dict, Optional, List
from sqlmodel import Field, SQLModel, Column, JSON, Relationship
from flask_login import UserMixin
from sqlalchemy.ext.mutable import MutableDict

class Room(SQLModel, UserMixin, table=True):
    Id_room: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    capacity: int
    location: str
    equipments: Dict = Field(default={}, sa_column=Column(MutableDict.as_mutable(JSON)))
    is_active: bool = Field(default=True)

    courses: List["Course"] = Relationship(back_populates="room")
    equipments: List["Equipment"] = Relationship(back_populates="room")
    
