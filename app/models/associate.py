from typing import Optional
from sqlmodel import Field, SQLModel, Relationship

class Associate(SQLModel, table=True):
    id_course: int = Field(foreign_key="course.id_course", primary_key=True)
    id_equipment: int = Field(foreign_key="equipment.id_equipment", primary_key=True)
    quantity: int = Field(ge=0)

    course: "Course" = Relationship(back_populates="associates")
    equipment: Optional["Equipment"] = Relationship(back_populates="associated_courses")
                               