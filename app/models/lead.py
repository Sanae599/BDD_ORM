from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship

if TYPE_CHECKING:
    from app.models.tables_user import Trainer
    from app.models.course import Course

class Lead(SQLModel, table=True):
    id_trainer: int = Field(foreign_key="trainer.id_trainer", primary_key=True)
    id_course: int = Field(foreign_key="course.id_course", primary_key=True)

    trainer: "Trainer" = Relationship(back_populates="leads")
    course: Optional["Course"] = Relationship(back_populates="leads")
