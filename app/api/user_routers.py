from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import EducationLevel
from ..database import SessionLocal
from ..crud.userCrud import get_user,create_user_crud
from datetime import date

router = APIRouter(prefix='userss', tags=['API'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/")
def create_user(first_name: str, last_name: str,
                middle_name:str,date_of_birth: date,
                hash_password: str, education_level: EducationLevel,
                db: Session = Depends(get_db)):
    return create_user_crud(db=db, first_name=first_name, last_name=last_name,
                       middle_name=middle_name, date_of_birth=date_of_birth,
                       hash_password=hash_password, education_level=education_level)

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user