from datetime import datetime
from sqlmodel import Session, select
from app.models.course import CourseStatutEnum, Course

def create_one_course(session: Session):
    course = Course(
        titre="Maths",
        description="belle description t'as vu",
        start_date=datetime.strptime("2022-12-13", "%Y-%m-%d"),
        end_date=datetime.strptime("2022-12-15", "%Y-%m-%d"),
        is_active=True,
        statut=CourseStatutEnum.OPEN,
    )
    session.add(course)
    session.commit()
    session.refresh(course)
    return course

def get_one_course_by_id(session: Session, course_id: int):
    statement = select(Course).where(Course.Id_course == course_id)
    result = session.exec(statement)
    return result.one()

def get_all_courses(session: Session):
    statement = select(Course)
    result = session.exec(statement)
    courses = result.all()
    for course in courses:
        print(course)
    return courses

def update_course(session: Session):
    pass

def delete_course(session: Session):
    pass