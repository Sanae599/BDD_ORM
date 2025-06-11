from datetime import date, datetime
from typing import Optional, List, Dict
from enum import Enum
from sqlmodel import SQLModel, Field, Relationship, Column, JSON
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import Column as SAColumn, Enum as SQLEnum
from flask_login import UserMixin
from app.enumerations.all_enumerations import (
    Role,
    NiveauAccesEnum,
    JobStaffEnum,
    LearnerLevelEnum,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:                                     
    from app.models.lead import Lead                  
                                                      
                                                      
class UserBase(UserMixin):                            
    firstname: str                                    
    lastname: str                                     
    email: str                                        
    password: str                                     
    role: Role = Field(sa_column=SAColumn(SQLEnum(Role), default=Role.LEARNER))

class Trainer(SQLModel, UserBase, table=True):        
    id_trainer: Optional[int] = Field(default=None, primary_key=True)
    speciality: str                                   
    hire_date: date                                   
    hourly_rate: float                                
    bio: Optional[str] = None                         
                                                      
    def get_id(self):                                 
        return self.id_trainer                                
                                                      
                     
class Admin(SQLModel, UserBase, table=True):
    id_admin: Optional[int] = Field(default=None, primary_key=True)
    date_promotion: date
    level_access: NiveauAccesEnum
                     
    def get_id(self):
        return self.id_admin
    
class TeachingStaff(SQLModel, UserBase, table=True):
    id_techingstaff: Optional[int] = Field(default=None, primary_key=True)
    job: JobStaffEnum
    date_takingup_office: date
    responsabilities: Dict = Field(
        default={}, sa_column=Column(MutableDict.as_mutable(JSON))
    )                
                     
    def get_id(self):
        return self.id_techingstaff
                 
                 
class Learner(SQLModel, UserBase, table=True):
    id_learner: Optional[int] = Field(default=None, primary_key=True)
    date_birth: date                
    study_level: Optional[LearnerLevelEnum]
    phone_number: Optional[str]     
    platform_registration_date: datetime = Field(default_factory=datetime.now)
    certification_obtained: Optional[str]
                                    
    def get_id(self):               
        return str(self.id_learner)         
                                    
    registers: List["Register"] = Relationship(back_populates="learner")