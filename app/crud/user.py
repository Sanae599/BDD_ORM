from app.models.tables_user import UserBase, User, Learner
from app.enumerations.all_enumerations import Role
from sqlmodel import Session, select
from app.schemas.user_schemas import (
    UserCreate,
    UserPublic,
    UserUpdate,
    PasswordUpdate,
    PasswordReset,
)


def add_one_user(session: Session, user_data: UserCreate):
    existing_user = session.exec(
        select(User).where(User.email == user_data.email)
    ).first()
    if existing_user:
        raise ValueError(f"Un utilisateur avec l'email {user_data.email} existe déjà.")

    validated_data = user_data.model_dump()

    if validated_data["role"] == Role.LEARNER:
        # créer user
        user = Learner(
            firstname=validated_data["firstname"],
            lastname=validated_data["lastname"],
            email=validated_data["email"],
            password=validated_data["password"],
            # is_active=True,
            role=validated_data["role"],
        )
    else:
        print("il faut gérer les autres cas ...")

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
    user = session.exec(
        select(UserBase).where(UserBase.email == password_data.email)
    ).first()
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
