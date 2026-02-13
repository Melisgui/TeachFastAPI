from fastapi import APIRouter, Depends, HTTPException
from pyexpat.errors import messages
from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, status
from sqlalchemy.future import select
import logging
from sqlalchemy.exc import IntegrityError

from ..Schemas import UserCreate
from ..database import get_db
from ..Schemas import UserResponse
from .models import User
from ..security.Sec_pass import secu_me

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/user", tags=['Users'])


@router.post("/create", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
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
        user_duplicate = db.query(User).filter_by(email=db_user.email).first()
        if user_duplicate:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Пользователь с таким email уже существует"
            )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь с таким email уже существует"
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Ошибка при создании пользователя: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Не удалось создать пользователя"
        )

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    res = db.execute(select(User).where(User.id == user_id))
    user = res.scalar()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user

@router.delete("/delete{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    res = db.execute(select(User).where(User.id == user_id))
    user = res.scalar()
    db.delete(user)
    db.commit()
    return "Пользователь удален"


