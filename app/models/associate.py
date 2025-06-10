from typing import Optional
from sqlmodel import Field, SQLModel, Relationship

class Associate(SQLModel, table=True):
    Id_course: int = Field(foreign_key="course.Id_course", primary_key=True)
    Id_equipment: int = Field(foreign_key="equipment.Id_equipment", primary_key=True)
    quantity: int = Field(ge=0)

    course: "Course" = Relationship(back_populates="associates")
    equipment: Optional["Equipment"] = Relationship(back_populates="associated_courses")
                               