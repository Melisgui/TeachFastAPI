from datetime import date

from sqlalchemy import Date

from ..api.models import User, EducationLevel
from ..security.Sec_pass import secu_me
from sqlalchemy.orm import Session


def create_user_crud(db: Session, first_name: str, last_name: str,
                middle_name:str,date_of_birth: date,
                hash_password: str, education_level: EducationLevel):
    new_user = User(first_name=first_name, last_name=last_name,middle_name=middle_name,
                    date_of_birth=date_of_birth,
                    hash_password=secu_me(hash_password), education_level=education_level)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg": "Пользователь успешно зарегистрирован"}


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()