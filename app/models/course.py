from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship, Column, JSON
from sqlalchemy import Column as SAColumn, Enum as SAEnum
from sqlalchemy.ext.mutable import MutableDict
from app.enumerations.all_enumerations import CourseStatutEnum

class Course(SQLModel, table=True):
    id_course: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    description: Optional[str] = None

    start_date: datetime
    end_date: datetime

    id_room: Optional[int] = Field(foreign_key="room.id_room")
    id_trainer: Optional[int] = Field(foreign_key="tables_users.trainer.id_trainer")

    max_capacity: int

    status: CourseStatutEnum = Field(
        sa_column=SAColumn(SAEnum(CourseStatutEnum)), default=CourseStatutEnum.OPEN
    )

    prerequisites: Optional[List[str]] = Field(
        default=None,
        sa_column=Column(MutableDict.as_mutable(JSON))
    )

    room: Optional["Room"] = Relationship(back_populates="courses")
    trainer: Optional["Trainer"] = Relationship(back_populates="courses")
    associates: List["Associate"] = Relationship(back_populates="course")
    lead: List["Lead"] = Relationship(back_populates="course")
    registers: List["Register"] = Relationship(back_populates="course")
