from sqlmodel import Session, select
from app.models.tables_user import Trainer
from app.schemas.trainer_schemas import TrainerCreate, TrainerUpdate
from sqlalchemy.exc import IntegrityError


def add_one_trainer(session: Session, trainer_data: TrainerCreate) -> Trainer:
    existing_trainer = session.exec(select(Trainer).where(Trainer.email == trainer_data.email)).first()
    if existing_trainer:
        print("Formateur déjà existant dans la base de données")
        return existing_trainer

    new_trainer = Trainer(**trainer_data.dict())
    session.add(new_trainer)
    try:
        session.commit()
        session.refresh(new_trainer)
    except IntegrityError as e:
        session.rollback()
        raise ValueError(f"Erreur lors de l'ajout du formateur : {e}")
    
    return new_trainer


def get_one_trainer(session: Session, trainer_id: int) -> Trainer:
    trainer = session.get(Trainer, trainer_id)
    if not trainer:
        raise ValueError("Formateur non trouvé.")
    return trainer


def update_trainer(session: Session, trainer_id: int, trainer_update: TrainerUpdate) -> Trainer:
    trainer = session.get(Trainer, trainer_id)
    if not trainer:
        raise ValueError("Formateur non trouvé.")

    update_data = trainer_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(trainer, key, value)

    session.add(trainer)
    session.commit()
    session.refresh(trainer)
    return trainer


def delete_trainer(session: Session, trainer_id: int) -> None:
    trainer = session.get(Trainer, trainer_id)
    if not trainer:
        raise ValueError("Formateur non trouvé.")
    session.delete(trainer)
    session.commit()
