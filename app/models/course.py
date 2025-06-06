from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from enum import Enum

class CourseStatutEnum(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    ARCHIVED = "ARCHIVED"

class Course(SQLModel, table=True):
    Id_course: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    Id_room: Optional[int] = Field(foreign_key="room.Id_room")
    max_capacity: int
    statut: CourseStatutEnum = Field(default=CourseStatutEnum.OPEN)

    room: Optional["Room"] = Relationship(back_populates="courses")
    associates: List["Associate"] = Relationship(back_populates="course")
