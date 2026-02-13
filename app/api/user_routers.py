from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, status
from sqlalchemy.future import select
import logging

from ..Schemas import UserCreate
from ..database import get_db
from ..Schemas import UserResponse
from .models import User
from ..security.Sec_pass import secu_me

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/user",tags=['Users'])


@router.post("/create", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = secu_me(user.password)
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        middle_name=user.middle_name,
        date_of_birth=user.date_of_birth,
        hash_password=hashed_password,
        education_level=user.education_level,
        email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # чтобы получить id и другие поля от БД
    return db_user


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    res = db.execute(select(User).where(User.id == user_id))
    user = res.scalar()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user