from app.models.tables_user import UserBase
from app.enumerations.all_enumerations import Role
from sqlmodel import Session, select
from app.schemas.user_schemas import UserCreate, UserPublic, UserUpdate, PasswordUpdate, PasswordReset
from app.crud.password import add_one_password

def add_one_user(session: Session, user_data: UserCreate):
    validated_data = user_data.model_dump()

    pwd = add_one_password(session, validated_data['password'])

    # créer user
    user = UserBase(
    firstname=validated_data['firstname'],
    lastname=validated_data['lastname'],
    email=validated_data['email'],
    is_active=True,
    role=validated_data['role'],
    id_password=pwd.id,
    )

    session.add(user)
    session.commit()
    session.refresh(user)


    return UserPublic.model_validate(user)

def get_one_user_by_id(session: Session, user_id: int):
    user = session.get(UserBase, user_id)
    if not user:
        return None
    
    return UserPublic.model_validate(user)

def update_user(session: Session, user_id: int, user_data: UserUpdate):
    user = session.get(UserBase, user_id)
    if not user:
        return None

    update_data = user_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)

    return UserPublic.model_validate(user)

def update_user_password(session: Session, user_id: int, password_data: PasswordUpdate):
    user = session.get(UserBase, user_id)
    if not user:
        return None

    return UserPublic.model_validate(user)

def reset_user_password(session: Session, password_data: PasswordReset):
    user = session.exec(select(UserBase).where(UserBase.email == password_data.email)).first()
    if not user:
        return None

    return UserPublic.model_validate(user)

def delete_user(session: Session, user_id: int):
    user = session.get(UserBase, user_id)
    if not user:
        return False
    session.delete(user)
    session.commit()
    return True