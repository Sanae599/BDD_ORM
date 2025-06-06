import os, sys
sys.path.append(os.getcwd())
from models.course import CourseStatutEnum, Course
from sqlmodel import Session, select

def add_one_course(session: Session):
    course = Course(
        titre="Maths",
        description="belle description t'as vu",
        start_date="13-13-2022",
        end_date="15-13-2022",
        is_active=True,
        role=CourseStatutEnum.OPEN,
        )
    session.add(course)
    session.commit()
    session.refresh(course)
    return course

def get_one_course_by_id(session: Session, course_id: int):
    statement = select(Course).where(Course.Id_course == course_id)
    result = session.exec(statement)
    return result.scalar_one_or_none()