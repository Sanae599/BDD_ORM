from sqlmodel import Session, select
from app.models.tables_user import TeachingStaff
from app.schemas.teaching_staff_schemas import TeachingStaffCreate, TeachingStaffUpdate
from sqlalchemy.exc import IntegrityError


def add_one_teaching_staff(session: Session, staff_data: TeachingStaffCreate) -> TeachingStaff:
    existing_staff = session.exec(select(TeachingStaff).where(TeachingStaff.email == staff_data.email)).first()
    if existing_staff:
        print("Membre du personnel enseignant déjà existant dans la base de données")
        return existing_staff

    new_staff = TeachingStaff(**staff_data.dict())
    session.add(new_staff)
    session.flush() 
    try:
        session.commit()
        session.refresh(new_staff)
    except IntegrityError as e:
        session.rollback()
        raise ValueError(f"Erreur lors de l'ajout : {e}")
    
    return new_staff


def get_one_teaching_staff(session: Session, staff_id: int) -> TeachingStaff:
    staff = session.get(TeachingStaff, staff_id)
    if not staff:
        raise ValueError("Personnel enseignant non trouvé.")
    return staff


def update_teaching_staff(session: Session, staff_id: int, staff_update: TeachingStaffUpdate) -> TeachingStaff:
    staff = session.get(TeachingStaff, staff_id)
    if not staff:
        raise ValueError("Personnel enseignant non trouvé.")

    staff_data = staff_update.dict(exclude_unset=True)
    for key, value in staff_data.items():
        setattr(staff, key, value)
    session.add(staff)
    session.commit()
    session.refresh(staff)
    return staff


def delete_teaching_staff(session: Session, staff_id: int) -> None:
    staff = session.get(TeachingStaff, staff_id)
    if not staff:
        raise ValueError("Personnel enseignant non trouvé.")
    session.delete(staff)
    session.commit()
