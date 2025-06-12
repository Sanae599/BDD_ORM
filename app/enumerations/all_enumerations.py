from enum import Enum


# class Role(str, Enum):
#     APPRENANT = "learner"
#     FORMATEUR = "trainer"
#     STAFF = "admin"
#     ADMIN = "staff"

class CourseStatutEnum(str, Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    ARCHIVED = "ARCHIVED"
    
class Role(str, Enum):
    LEARNER = "learner"
    TRAINER = "trainer"
    ADMIN = "admin"
    STAFF = "staff"


class NiveauAccesEnum(str, Enum):
    ADMIN_STANDARD = "Admin standard"
    SUPERADMIN = "Super admin"


class JobStaffEnum(str, Enum):
    ResponsablePedagogique = "Responsable pédagogique"
    ChargeeProjet = "Chargée de projet"


class LearnerLevelEnum(str, Enum):
    BAC = "Bac"
    BAC2 = "Bac+2"
    BAC5 = "Bac+5"

class EquipmentType(str, Enum):
    AUDIOVISUAL = "audiovisual"
    COMPUTER = "computer"
    FURNITURE = "furniture"
    OTHER = "other"


class RegisterStatutEnum(str, Enum):
    ENREGISTRE = "enregistre"
    DESINSCRIT = "desinscrit"
    EN_ATTENTE = "en_attente"
