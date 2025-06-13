from typing import Optional, List
from datetime import datetime
from sqlmodel import Session, select
from app.models.course import CourseStatutEnum, Course
from pydantic import ValidationError

from app.schemas.course_schemas import CourseCreate, CourseRead, CourseUpdate

def add_one_course(session: Session, course_data: CourseCreate):
    existing_course = session.exec(select(Course).where(Course.title == course_data.titre)).first()
    if existing_course:
        print('le cours existe déjà dans la db')
        return None

    course = Course(
        title=course_data.titre,
        description=course_data.description,
        start_date=datetime(2025, 7, 10, 9),  # ✅ CHAMP CORRECT
        end_date=datetime(2025, 7, 14, 17),   # ✅ CHAMP CORRECT
        id_room=course_data.id_room,
        max_capacity=course_data.capacite_max,
        statut=course_data.statut,
    )
    session.add(course)
    session.commit()
    session.refresh(course)
    return CourseRead.model_validate(course)

def get_one_course_by_id(session: Session, course_id: int) -> Optional[CourseRead]:
    statement = select(Course).where(Course.id_course == course_id)
    result = session.exec(statement)
    course = result.one_or_none()
    if course:
        return CourseRead.model_validate(course)
    return None

def get_all_courses(session: Session) -> List[CourseRead]:
    statement = select(Course)
    result = session.exec(statement)
    courses = result.all()
    return [CourseRead.model_validate(course) for course in courses]

def update_course(session: Session, course_id: int, course_data: CourseUpdate) -> Optional[CourseRead]:
    course = session.get(Course, course_id)
    if not course:
        return None

    for key, value in course_data.model_dump(exclude_unset=True).items():
        setattr(course, key, value)

    session.commit()
    session.refresh(course)
    return CourseRead.model_validate(course)

def delete_course(session: Session, course_id: int) -> bool:
    course = session.get(Course, course_id)
    if not course:
        return False

    session.delete(course)
    session.commit()
    return True
