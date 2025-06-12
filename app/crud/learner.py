from sqlmodel import Session, select
from app.models.tables_user import Learner
from datetime import date, datetime
from app.schemas.learner_schemas import LearnerCreate


# def add_one_learner(session: Session, date_birth: date, study_level: str,
#                     phone_number: str, platform_registration_date: datetime, certification_obtained: str):
def add_one_learner(session: Session, cl: LearnerCreate):
    existing_learner = session.exec(
        select(Learner).where(Learner.email == cl.email)
    ).first()
    if existing_learner:
        print("learner déjà existante dans la db")
        return existing_learner

    else:
        learner = Learner(
            firstname=cl.firstname,
            lastname=cl.lastname,
            email=cl.email,
            role=cl.role,
            password=cl.password,
            date_birth=cl.date_birth,
            study_level=cl.study_level,
            phone_number=cl.phone_number,
            platform_registration_date=cl.platform_registration_date,
            certification_obtained=cl.certification_obtained,
        )
    session.add(learner)
    session.commit()
    session.refresh(learner)
    return learner


def get_one_learner_by_id(session: Session, id_learner: int):
    statement = select(Learner).where(Learner.id_learner == id_learner)
    result = session.exec(statement)
    return result.one()


def get_all_learner(session: Session):
    statement = select(Learner)
    result = session.exec(statement)
    return result.all()


def update_learner(session: Session):
    pass


def delete_learner(session: Session, id_learner: int):
    learner = session.get(Learner, id_learner)
    if not learner:
        return False

    session.delete(learner)
    session.commit()
    return True
