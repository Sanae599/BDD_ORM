from datetime import date, datetime
from typing import Optional
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship

class LearnerLevelEnum(str, Enum):
    BAC = "Bac"
    BAC2 = "Bac+2"
    BAC5 = "Bac+5"

class Learner(SQLModel, table=True):
    Id_learner: int | None = Field(default=None, primary_key=True)
    date_birth: date 
    study_level: Optional[LearnerLevelEnum] 
    phone_number: Optional[str]
    platform_registration_date: datetime = Field(default=datetime.now())
    certification_obtained: Optional[str]
    Id_user: int = Field(foreign_key="user.Id_user")

    user: Optional["User"] | None = Relationship(back_populates="room")
