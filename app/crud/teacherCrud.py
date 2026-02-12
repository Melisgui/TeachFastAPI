from ..api.models import Teacher, EducationLevel
from sqlalchemy.orm import Session


def create_teacher(db: Session, teach_lesson: str, teacher_experience: int,
                   experience_description: str):
    new_teacher = Teacher(teach_lesson=teach_lesson, teacher_experience=teacher_experience,
                          experience_description=experience_description, )
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher



def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()


def delete_teacher(db: Session, teacher_id: int):
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher:
        db.delete(teacher)
        db.commit()
