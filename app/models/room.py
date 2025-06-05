from typing import Dict, Optional
from sqlmodel import Field, SQLModel, Column, JSON

class Room(SQLModel, table=True):
    Id_room: Optional[int] = Field(default=None, primary_key=True)
    nom: str = Field(unique=True)
    capacite: int
    localisation: str
    equipements: Dict = Field(default=None, sa_column=Column(JSON))
    is_active: bool = Field(default=True)
