from sqlalchemy.orm import Session
from app.api.models import User
from app.Schemas import UserCreate  # импортируем схему
from app.security.Sec_pass import secu_me




def create_user_crud(db: Session, user: UserCreate):
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name,
        date_of_birth=user.date_of_birth,
        hash_password=secu_me(user.password),
        education_level=user.education_level
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()