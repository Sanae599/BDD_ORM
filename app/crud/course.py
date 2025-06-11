from datetime import datetime
from sqlmodel import Session, select
from app.models.course import CourseStatutEnum, Course

def add_one_course(session: Session, title:str, description: str, start_date: str,
                       end_date: str, id_room: int, max_capacity: int):
    # if not existe
    existing_course = session.exec(select(Course).where(Course.title == title)).first()
    if existing_course:
        print('room déjà existante dans la db')
        return None

    else:
        course = Course(
            title=title,
            description=description,
            start_date=datetime.strptime(start_date, "%Y-%m-%d"),
            end_date=datetime.strptime(end_date, "%Y-%m-%d"),
            id_room=id_room,
            max_capacity=max_capacity,
            statut=CourseStatutEnum.OPEN,
        )
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

def get_one_course_by_id(session: Session, course_id: int):
    statement = select(Course).where(Course.id_course == course_id)
    result = session.exec(statement)
    return result.one()

def get_all_courses(session: Session):
    statement = select(Course)
    result = session.exec(statement)
    return result.all()


def update_course(session: Session):
    pass

def delete_course(session: Session, course_id: int):
    course = session.get(Course, course_id)
    if not course:
        return False

    session.delete(course)
    session.commit()
    return True