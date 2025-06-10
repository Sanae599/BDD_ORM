# from typing import Optional
# from sqlmodel import Field, SQLModel, Relationship
# from app.models.course import Course
# from app.models.tables_user import Trainer


# class Lead(SQLModel, table=True):
#     Id_trainer: int = Field(foreign_key="trainer.Id_trainer", primary_key=True)
#     Id_course: int = Field(foreign_key="course.Id_course", primary_key=True)

#     course: "Course" = Relationship(back_populates="lead")
#     trainer: "Trainer" = Relationship(back_populates="lead")


from typing import Optional
from sqlmodel import Field, SQLModel, Relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.course import Course
    from app.models.tables_user import Trainer

class Lead(SQLModel, table=True):
    Id_trainer: int = Field(foreign_key="trainer.Id_trainer", primary_key=True)
    Id_course: int = Field(foreign_key="course.Id_course", primary_key=True)

    course: "Course" = Relationship(back_populates="lead")
    trainer: "Trainer" = Relationship(back_populates="lead")
