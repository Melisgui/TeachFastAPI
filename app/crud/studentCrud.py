from sqlalchemy.orm import Session
from ..api.models import Student


def create_student(db: Session,student_id: int, education_class: int):
    new_student = Student(
        id=student_id,
        education_class=education_class
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
