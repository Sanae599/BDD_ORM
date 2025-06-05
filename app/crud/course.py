from app.models.course import Course
from sqlmodel import Session


def add_one_course(session: Session):
    course = Course(
        titre="Maths",
        description="belle description",
        start_date="13-13-2022",
        end_date="15-13-2022"
        is_active=True,
        role=Role.APPRENANT
        )
    session.add(course)
    session.commit()
    session.refresh(course)
    return course