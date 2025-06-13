from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, field_validator
from app.enumerations.all_enumerations import RegistrationStatusEnum


#Base commune
class RegisterBase(BaseModel):
    id_learner: int
    id_session: int
    registration_date: Optional[datetime] = None
    registration_status: RegistrationStatusEnum = RegistrationStatusEnum.EN_ATTENTE
    presence: Optional[bool] = None

    model_config = ConfigDict(
        validate_assignment=True,
        use_enum_values=True
    )


#Création (POST)
class RegisterCreate(RegisterBase):
    pass


#Lecture complète (GET)
class RegisterRead(RegisterBase):
    id: int


#Lecture côté utilisateur
class RegisterPublic(BaseModel):
    registration_date: datetime
    registration_status: RegistrationStatusEnum
    presence: Optional[bool] = None

    model_config = ConfigDict(use_enum_values=True)


#Mise à jour (PATCH)
class RegisterUpdate(BaseModel):
    registration_status: Optional[RegistrationStatusEnum] = None
    presence: Optional[bool] = None

    model_config = ConfigDict(validate_assignment=True, use_enum_values=True)
