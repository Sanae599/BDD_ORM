from app.schemas.user_schemas import PasswordUpdate
from pydantic import ValidationError


from datetime import date, timedelta
from app.schemas.trainer_schemas import TrainerCreate, TrainerUpdate, TrainerPublic

print(" Test TrainerCreate")

try:
    trainer = TrainerCreate(
        speciality="Python",
        hire_date=date.today() - timedelta(days=30),
        hourly_rate=50.0,
        bio="Formateur expert Python",
        Id_user=1
    )
    print(" TrainerCreate valide :", trainer)
except Exception as e:
    print(" Erreur TrainerCreate :", e)


print("\n Test TrainerUpdate avec valeurs valides")

try:
    update = TrainerUpdate(
        hourly_rate=45.5
    )
    print(" TrainerUpdate valide :", update)
except Exception as e:
    print(" Erreur TrainerUpdate :", e)


print("\n Test TrainerUpdate avec taux négatif (doit échouer)")

try:
    update_invalid = TrainerUpdate(hourly_rate=-10)
except Exception as e:
    print(" Erreur attendue :", e)


print("\n Test TrainerPublic")

try:
    public = TrainerPublic(
        Id_trainer=1,
        speciality="Data Science",
        hire_date=date.today(),
        hourly_rate=60.0,
        bio="Enseigne depuis 5 ans"
    )
    print(" TrainerPublic valide :", public)
except Exception as e:
    print(" Erreur TrainerPublic :", e)
