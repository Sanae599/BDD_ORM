import os, sys
sys.path.append(os.getcwd())
from models.course import CourseStatutEnum, Course
from sqlmodel import Session

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