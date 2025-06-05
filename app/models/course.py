from datetime import datetime
from typing import Dict, Optional
from sqlmodel import Field, SQLModel, create_engine, Column, JSON, Relationship
from enum import Enum
from room import Room

class CourseStatutEnum(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    ARCHIVED = "ARCHIVED"

class Course(SQLModel, table=True):
    Id_course: Optional[int] = Field(default=None, primary_key=True)
    titre: str = Field(max_length=100)
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    Id_room: int = Field(foreign_key="room.Id_room")
    max_capacity: int
    statut: CourseStatutEnum = Field(default=CourseStatutEnum.OPEN)
    prerequisites: Optional[Dict] = Field(default=None, sa_column=Column(JSON))

    room: Room | None = Relationship(back_populates="room")

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)
