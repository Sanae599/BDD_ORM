# app/crud/admin.py
from sqlmodel import Session, select
from app.models.tables_user import Admin
from app.schemas.admin_schemas import AdminCreate
from app.enumerations.all_enumerations import Role

from typing import List

def add_one_admin(session: Session, admin_data: AdminCreate) -> Admin:
    existing_admin = session.exec(select(Admin).where(Admin.email == admin_data.email)).first()
    if existing_admin:
        print("Administrateur déjà existant dans la base de données")
        return existing_admin
    else:
        new_admin = Admin(
            firstname=admin_data.firstname,
            lastname=admin_data.lastname,
            email=admin_data.email,
            password=admin_data.password,
            role=admin_data.role, # Role.ADMIN,
            date_promotion=admin_data.date_promotion,
            level_access=admin_data.level_access,
        )
        session.add(new_admin)
        session.commit()
        session.refresh(new_admin)
        return new_admin

def get_one_admin_by_id(session: Session, id_admin: int) -> Admin:
    statement = select(Admin).where(Admin.id_admin == id_admin)
    result = session.exec(statement)
    return result.one()

def get_all_admins(session: Session) -> List[Admin]:

    statement = select(Admin)
    result = session.exec(statement)
    return result.all()

def update_admin(session: Session, id_admin: int) -> bool:
    admin = session.get(Admin, id_admin)
    if not admin:
        return False
    # Mettre à jour les champs souhaités
    session.commit()
    return True

def delete_admin(session: Session, id_admin: int) -> bool:
    admin = session.get(Admin, id_admin)
    if not admin:
        return False
    session.delete(admin)
    session.commit()
    return True
